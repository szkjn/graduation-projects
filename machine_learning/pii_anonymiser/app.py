from flask import Flask, render_template, url_for, request
import spacy
import random

app = Flask(__name__)

app.secret_key = 'password777'

@app.route("/")
def home():
  return render_template('index.html')

@app.route("/", methods=['POST'])
def anonymised_PII():

  original_text = request.form.get('original_text')

  ner = spacy.load("en_core_web_sm")
  doc = ner(original_text)

  anonymised_string = ""

  for token in doc:

    person = ['&#127877;', '&#128125;', '&#128584;']
    numbers = ['&#128286;', '&#127921;', '&#128290;']

    if token.pos_ == 'PROPN' and token.ent_type_ != '':
      new_token = " {}".format(random.choice(person) * 3)
    elif token.pos_ == 'NUM' and token.ent_type_ != '':
      new_token = " {}".format(random.choice(numbers) * 3)
    elif token.pos_ == 'PUNCT':
      new_token = token.text
    else:
      new_token = " {}".format(token.text)

    anonymised_string += new_token

  anonymised_string = anonymised_string.strip()

  return render_template(
    'index.html', 
    original_text=original_text, 
    anonymised_text=anonymised_string,
  )


@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == "__main__":
  app.run(debug=True)