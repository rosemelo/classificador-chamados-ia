import random
import re
import nltk

nltk.download('rslp')  # Stemmer para português
stemmer = nltk.stem.RSLPStemmer()

# Perguntas rimadas da IA
perguntas_rimadas = [
    "Olá, meu amigo, que bom te encontrar!\nMe diga uma coisa: o que te faz sonhar?",
    "Me conta aí, nessa rima bonita,\nQual é a lembrança que nunca se evita?",
    "Chegue mais perto, me diga sem medo,\nO que te acalma nos dias de enredo?",
    "Se a vida rimasse igual poesia,\nQual verso seria sua melodia?",
    "O que te faz sorrir em um dia cinza?\nO que ilumina quando a alma balança?"
]

def gerar_pergunta():
    return random.choice(perguntas_rimadas)

# Função simples para verificar rima pelo sufixo da última palavra
def verifica_rima(p1, p2):
    # Extrai a última palavra de cada frase
    ultima1 = re.findall(r'\b\w+\b', p1.lower())[-1]
    ultima2 = re.findall(r'\b\w+\b', p2.lower())[-1]
    
    # Usa stemmer pra tentar normalizar
    return ultima1[-3:] == ultima2[-3:] or stemmer.stem(ultima1) == stemmer.stem(ultima2)

def gerar_resposta_rimada(pergunta, resposta_usuario):
    # IA avalia se há rima com a pergunta
    ultima_ia = pergunta.strip().split("\n")[-1]
    if verifica_rima(ultima_ia, resposta_usuario):
        respostas_bonitas = [
            "Boa rima, parceiro, mandou bem demais!\nPrepare seu verso, quero ouvir mais!",
            "Sua rima brilhou feito o sol do sertão,\nContinue esse ritmo no coração!",
            "Rapaz, que talento, quase um trovador!\nManda mais uma com todo o amor!",
        ]
        return random.choice(respostas_bonitas)
    else:
        return "Eu gostei da ideia, mas vou te alertar:\nSua rima fugiu, bora tentar alinhar!"




