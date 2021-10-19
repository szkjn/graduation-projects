# Book Recommendation with Gutenberg Project Corpus

## Concept

Those notebooks apply data pre-processing on Gutenberg Project dataset in order to achieve topic modeling and book recommendation.

Here are the followed steps: 

1. Creating bag of words
    + Pre-processing data :
        + Stemming
        + Lemmatization
        + Punctuation, stopwords
    + Wordcloud visualisation
2. Latent Semantic Analysis
    + Document-Term Matrix :
        + vectorizing the corpus in a TF-IDF weighted Document-Term Matrix
    + Singular Value Decomposition :
        + modeling matrix in 3 topics (n_components) using TruncatedSVD from sklearn
3. Metrics
    + Top 10 words by topics
    + Books by topics
    + Cosine similarity
4. Book recommendation :
    + Implementation of a recommendation function taking as parameters:
        + the name of a book from the corpus
        + the number of recommendations expected

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

        pip install pandas matplotlib
        pip install sklearn nltk wordcloud
        pip install os-sys

