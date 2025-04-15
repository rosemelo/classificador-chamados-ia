import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixar os recursos necessários
nltk.download('stopwords')
nltk.download('punkt')

# Testar stopwords
stop_words = set(stopwords.words('portuguese'))
print("Stopwords:", stop_words)

# Testar tokenização
texto = "Olá, como vai você? Vamos conversar?"
tokens = word_tokenize(texto, language='portuguese')
print("Tokens:", tokens)