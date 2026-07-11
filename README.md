# Sentiment Analyzer from python

## Working of the project:
A web application that analyzes the sentiment of any text and tells 
you if it is Positive, Negative or Neutral using Natural Language 
Processing.

## Features of the project
- Classifies text as Positive, Negative or Neutral
- Shows polarity score (-1 to +1)
- Shows subjectivity score (0 = factual, 1 = opinion)
- Shows word count and character count
- Clean and simple web interface

## What I learned
- Natural Language Processing basics
- Sentiment analysis using TextBlob
- Building web apps with Streamlit
- Polarity and subjectivity scoring

## How to run
1. Make sure Python is installed
2. Install required libraries:
pip install streamlit textblob
python -m textblob.download_corpora
3. Run this command:
streamlit run app.py
4. App will open automatically in your browser

## Tech used
- Python
- TextBlob
- Streamlit
