from flask import Flask, render_template, request, redirect, url_for, flash
import cv2, easyocr
import os
from PIL import Image
from werkzeug.utils import secure_filename
# from werkzeug.debug import DebuggedApplication
# import logging

ORIGINAL_FOLDER = 'static/original/'
FOCUS_FOLDER = 'static/focus/'
TIPPEX_FOLDER = 'static/tippex/'
COLLAGE_FOLDER = 'static/collage/'
SEARCH_FOLDER = 'static/search/'

app = Flask(__name__)
# app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

app.secret_key = 'text_detection_app'
app.config['ORIGINAL_FOLDER'] = ORIGINAL_FOLDER
app.config['FOCUS_FOLDER'] = FOCUS_FOLDER
app.config['TIPPEX_FOLDER'] = TIPPEX_FOLDER
app.config['COLLAGE_FOLDER'] = COLLAGE_FOLDER
app.config['SEARCH_FOLDER'] = SEARCH_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
  return render_template('index.html')

''' README
    - extractor() extracts text from image.
      It first checks if image is wider than 1080px, if so calls resizer().
      Its inner readtext() method is the most time consuming part of the code.
      It calls both tippexMode() and focusMode() methods.

    - resizer() resizes image at max-width 1080px

    - tippexMode() gets text boxes coordinates and returns 2 images.
      tippex and collage its negative.

    - focusMode() returns blank image on which
      it writes extracted text at +/- same coordinates
      >>>>>>>>> TO DO : proportional text size
'''
def extractor(ORIGINAL_FOLDER, filename, resize=True):
    
    global base
    base = cv2.imread(ORIGINAL_FOLDER + filename)
    img = cv2.imread(ORIGINAL_FOLDER + filename)

    if resize:
        if img.shape[1] > 1080:
            base = resizer(base)
            img = resizer(img)
    else:
        print("Resizing deactivated.")
    
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(img, width_ths=.01)

    global foundKeyword
    foundKeyword = False

    keyword = request.form.get('keyword')
    if keyword != '':
      search = searchKeyword(result, img, keyword)
      if search:
        foundKeyword = True
        search.save(os.path.join(app.config['SEARCH_FOLDER'], filename))

    tippex = tippexMode(result, img)[0]
    tippex.save(os.path.join(app.config['TIPPEX_FOLDER'], filename))
    collage = tippexMode(result, img)[1]
    collage.save(os.path.join(app.config['COLLAGE_FOLDER'], filename))
    focus = focusMode(result, img)
    focus.save(os.path.join(app.config['FOCUS_FOLDER'], filename))




def resizer(img):       
    max_width = 1080
    aspect_ratio = max_width / img.shape[1]
    new_height = int(img.shape[0] * aspect_ratio)
    dim = (max_width, new_height)
    
    resized = cv2.resize(img, dsize = dim, interpolation = cv2.INTER_AREA)
    return resized

def tippexMode(result, img):

  imgTippex = img.copy()

  for line in result:
    top_left = tuple([int(val) for val in line[0][0]])
    bottom_right = tuple([int(val) for val in line[0][2]])
    imgTippex = cv2.rectangle(imgTippex, top_left, bottom_right, (255, 255, 255), -1)
    mask = cv2.rectangle(imgTippex, top_left, bottom_right, (255,255,255), -1)

  image = cv2.cvtColor(imgTippex, cv2.COLOR_BGR2RGB)
  tippex = Image.fromarray(image)

  retval, mask = cv2.threshold(mask, 245.9, 255, cv2.THRESH_BINARY)
  reversed = cv2.bitwise_not(mask)  # Fully transparent
  reversed = cv2.add(base, reversed)
  reversed = cv2.cvtColor(reversed, cv2.COLOR_BGR2RGB)
  collage = Image.fromarray(reversed)

  return tippex, collage

def focusMode(result, img, font_size = .5, font_weight = 1):

  imgFocus = img.copy()

  font = cv2.FONT_HERSHEY_SIMPLEX
  img_fullsize = (imgFocus.shape[1], imgFocus.shape[0])
  imgFocus = cv2.rectangle(imgFocus, (0,0), img_fullsize, (255, 255, 255), -1)

  for line in result:
    bottom_left = tuple([int(val) for val in line[0][3]])
    imgFocus = cv2.putText(imgFocus, line[1], bottom_left, font, font_size, (0,0,0), font_weight, cv2.LINE_AA)

  final = cv2.cvtColor(imgFocus, cv2.COLOR_BGR2RGB)
  image = Image.fromarray(final)
  return image

def searchKeyword(result, img, keyword):
  
  global count
  count = 0
  imgSearch = img.copy()
  for line in result:
  
    top_left = tuple([int(val) for val in line[0][0]])
    bottom_right = tuple([int(val) for val in line[0][2]])

    if keyword.lower() in line[1].lower():
      imgSearch = cv2.rectangle(imgSearch, top_left, bottom_right, (0, 255, 0), 3)
      count += 1

  if count > 0:
    imgSearch = cv2.cvtColor(imgSearch, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(imgSearch)
    return image
  else:
    return None

  

@app.route('/', methods=['POST'])

def upload_image():

  if 'file' not in request.files:
    flash('No file part')
    return redirect(request.url)
  file = request.files['file']
  if file.filename == '':
    flash('No image selected for uploading')
    return redirect(request.url)
    
  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['ORIGINAL_FOLDER'], filename))
    # flash('Image successfully uploaded and displayed below')

    extractor(ORIGINAL_FOLDER, filename)

    keyword = request.form.get('keyword')
    if keyword != '':
      return render_template('index.html', filename=filename, keyword=keyword, foundKeyword=foundKeyword, count=count)
    else:
      return render_template('index.html', filename=filename)

  else: 
    flash('Allowed image types are : png, jpg, jpeg')
    return redirect(request.url)
  
@app.route('/original/<filename>')
def display_image(filename):
  return redirect(url_for('static', filename='original/' + filename), code=301)

@app.route('/focus/<filename>')
def display_focus(filename):
  return redirect(url_for('static', filename='focus/' + filename), code=301)

@app.route('/tippex/<filename>')
def display_tippex(filename):
  return redirect(url_for('static', filename='tippex/' + filename), code=301)

@app.route('/collage/<filename>')
def display_collage(filename):
  return redirect(url_for('static', filename='collage/' + filename), code=301)

@app.route('/search/<filename>')
def display_search(filename):
  return redirect(url_for('static', filename='search/' + filename), code=301)

# -------------------------------

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == "__main__":
  app.run(debug=True)
