# PII (Personal Identifiable Information) Anonymiser

version 1.1.1

## Concept

This first version is a basic PII Anonymiser using NER (Named Entity Recognition) POS tagging to identify and replace Proper Nouns and Numerical values by emojis.

Work in progress :

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
