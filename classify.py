import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

def preprocess(texto):
    return ' '.join([palavra for palavra in texto.lower().split() if palavra not in stopwords])

def classificar(texto):
    modelo, vetor = joblib.load("model/classificador.pkl")
    texto_limpo = preprocess(texto)
    X = vetor.transform([texto_limpo])
    return modelo.predict(X)[0]

