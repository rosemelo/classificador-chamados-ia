import random
import nltk
import re

# Baixar dados necessários do NLTK
nltk.download('cmudict')
nltk.download('stopwords')

# Função para verificar se duas palavras rimam
def rimar(palavra1, palavra2):
    dicionario = nltk.corpus.cmudict.dict()
    try:
        # Obtendo as últimas sílabas
        ultimas_silabas1 = [pronunciacao[-2:] for pronunciacao in dicionario[palavra1.lower()]]
        ultimas_silabas2 = [pronunciacao[-2:] for pronunciacao in dicionario[palavra2.lower()]]
        
        # Verificando se as últimas sílabas das palavras são iguais
        return ultimas_silabas1 == ultimas_silabas2
    except KeyError:
        return False

# Função para gerar um verso da IA
def gerar_verso_ia():
    versos = [
        "Olá, meu amigo, que bom te encontrar! Me diga uma coisa: o que te faz sonhar?",
        "Fala aí, meu chapa, o que te faz vibrar? Me conta uma coisa, o que você quer cantar?",
        "Ei, companheiro, pronto pra rimar? Me diga logo, o que te
