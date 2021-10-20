# Sentiment Analysis on @peta's Twitter interactions

#SentimentAnalysis #Wordcloud #DataCleaning #ModelTraining #ModelScoring

## Concept

This project attempts to do a sentiment analysis on @peta's Twitter account interactions (mentions, retweets and replies) using specific relevant librairies such as *TextBlob* and *sklearn*.

Here are the followed steps: 

1. Fetching Twitter API after authentification
2. Sanitising data using Regular Expressions
3. Getting **Polarity** and **Subjectivity** coefficients using *TextBlob*
4. Clustering the dataset with KMeans algorithm from *Sklearn*
5. Classifying the dataset using KNN algorithm from *Sklearn*
6. Plotting Decision Boundaries
7. Displaying performance indicators and a Confusion Matrix

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

        pip install pandas numpy matplotlib seaborn
        pip install sklearn
        pip install tweepy
        pip install wordcloud textblob

PS: All the librairies can be found in **requirements.txt**.

## Nota Bene

Those notebooks were used as initial overview on the dataset. The exported csv file has then been uploaded on Dataiku. There, the same steps were repeated, in addition to comparison between multiple classification models such as Random Forest Tree Classifier or XGBoost Classifier.
