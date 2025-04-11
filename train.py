import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import nltk
import joblib

# Baixa as stopwords (só na primeira vez)
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

# Função para limpar o texto
def preprocess(texto):
    return ' '.join([
        palavra for palavra in texto.lower().split()
        if palavra not in stopwords
    ])

# 📥 Carrega os dados do CSV
df = pd.read_csv("data/chamados.csv")

# 🧼 Limpa os textos
df['limpo'] = df['mensagem'].apply(preprocess)

# 🔢 Vetoriza os textos
vetor = TfidfVectorizer()
X = vetor.fit_transform(df['limpo'])
y = df['categoria']

# 🧠 Treina o modelo
modelo = MultinomialNB()
modelo.fit(X, y)

# 💾 Salva modelo + vetor
joblib.dump((modelo, vetor), "model/classificador.pkl")

print("✅ Modelo treinado e salvo com sucesso!")