import pandas as pd
from transformers import pipeline

# Carregar o modelo de análise de sentimentos
sentiment_model = pipeline("sentiment-analysis", model="neuralmind/bert-base-portuguese-cased")

# Função para extrair o sentimento de uma mensagem
def extrair_sentimento(texto):
    resultado = sentiment_model(texto)
    label = resultado[0]['label']
    
    # Mapeando os rótulos para os sentimentos em português
    if label == 'LABEL_0':
        return 'NEGATIVO'
    elif label == 'LABEL_1':
        return 'POSITIVO'
    else:
        return 'NEUTRO'  # Caso apareça algum outro label


# Ler o arquivo CSV (corrigido com o caminho correto)
df = pd.read_csv('data/chamados.csv')

# Exibir as primeiras linhas do arquivo para garantir que tudo foi lido corretamente
print(df.head())

# Aplicar a função de análise de sentimentos na coluna 'mensagem'
df['sentimento'] = df['mensagem'].apply(extrair_sentimento)

# Exibir as primeiras linhas com os sentimentos
print(df[['mensagem', 'sentimento']].head())

# Salvar o resultado em um novo arquivo CSV
df.to_csv('data/chamados_com_sentimentos.csv', index=False)

