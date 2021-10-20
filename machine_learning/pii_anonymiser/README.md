# PII (Personal Identifiable Information) Anonymiser

version 1.1.1

#NLP #NaturalLanguageProcessing #NER #NamedEntityRecognition

![pii_screen](https://user-images.githubusercontent.com/84317349/138094429-6c38fc60-cbad-4a21-aae5-6936775f9d6f.jpg)

## Concept

This Flask application is a deployment-ready PII Anonymiser using Named Entity Recognition POS tagging to identify and replace Proper Nouns and Numerical values by emojis.

## Work in progress :

+ v1.2
    - options between replacing with emojis and proper POS tags ::)
    - differentiate between person/organisation

+ v1.3
    - differentiate between date/address/phone number

## Librairies

To run the notebooks, follow those steps:

1. Create a virtual environment :

        python -m venv virtual
        
2. Activate the virtual environment :

    on Linux:

        source virtual/Scripts/activate
        
    on Windows:
        
        .\virtual\Scripts\activate
        
3. Install the necessary librairies :

        pip install flask
        pip install spacy
