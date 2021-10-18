Epitech Coding Academy / Data & Machine Learning 2021 End Of Course Project

## Text Extraction App

current version: v1.2.1

![app](https://user-images.githubusercontent.com/84317349/137354928-7af0a955-b56b-41c1-9458-38dafb8a4eff.jpg)

### Concept :
This application detects text from an uploaded image using OCR (Optical Character Recognition) algorithms.

It displays 4 outputs :
  + Original image
  + Focus Mode : extracted text displayed black on white at detected coordinates
  + Zen Mode : detected text erased from original image (currently looks more like a Tippex Mode)
  + Collage Mode : displays a collage of detected text boxes

An optional keyword search has also been implemented. If the keyword has been found one or several times, green boxes are drawn around the found words.

Finally, the extracted text is returned in a textarea below the 4 images. This allows further searching or copy/cut actions.

### Python librairies : 
  + *openCV*
  + *easyOCR*
  + *pytesseract*
  + *Flask*

### Methodology :
The application was built in 10 days as part of the end-of-course project and followed those 5 steps :
1. **Knowledge gathering** : I first investigate on what CV technologies are used for extracting text out of images. 

2. **Manipulation** : I then manipulated different OCR algorithms and fine-tuned them in order to find the most suitable ones for the application. It turned out *pytesseract* is more efficient when it comes to detecting groups of text (paragraphs, blocks). On the other hand, *easyOCR* has a granular detection mechanism that allows it to detect more words. 

3. **Logic implementation** : I then decided to use *easyOCR* to create the three processed 'modes' and *pytesseract* to extract and print text in the textarea.

4. **Structuring** : Once all the logic was built in my Jupyter Notebook cells, I translated everything into a Python file and designed a basic UI/UX with POST requests allowing the users to upload their own images. 

5. **Deployment-ready** : The last part consisted of creating a Flask Application with a requirements.txt file for a potential deployment on a Heroku server.

### Improvements :
The current repository is a v1 proof-of-concept that has been thought of, developed and presented as a final project after within a 10 days time period. Below are the improvements that I'd like to implement in the future to bring this app to the level of a first decent personal project :)

+ v2 :
  + delete every created image before next method call
  + display proportional font size text on Focus Mode
  + create and implement a save images button
  + add optional parameters (image resizing, font size, font weight, search box color)
  + deploy on Heroku
+ v3 :
  + optimize Zen Mode to better 'erase' text using adjacent pixel colours
  + mobile app version with a 'Take a picture' option

### Additional Screenshots :

![app2b](https://user-images.githubusercontent.com/84317349/137797595-fee4a57e-13d9-43ec-a519-bff863af72b0.jpg)

Upon click, the full-size image is popping in a modal as displayed below.
![app2](https://user-images.githubusercontent.com/84317349/137797581-cdc32c62-4d7a-4dae-b3e1-a0100069a11c.jpg)
