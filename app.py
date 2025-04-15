import streamlit as st
import pandas as pd
import os

from classify import classificar
from respostas import gerar_resposta

st.set_page_config(page_title="Classificador de Chamados", layout="centered")

st.title("🤖 Classificador de Chamados com IA")

st.markdown("""
Bem-vindo(a)! Este aplicativo utiliza **inteligência artificial** para ajudar a classificar automaticamente os chamados que você digitar.

### Como usar:
- Escreva abaixo uma descrição de chamado técnico, como por exemplo:
  - *“Não consigo acessar o sistema desde ontem”*
  - *“Erro 403 ao tentar acessar a intranet”*
- O sistema irá prever a **categoria do chamado** e gerar uma **resposta automática**.
""")

# === Função para registrar a interação ===
def registrar_interacao(rodada, tipo, texto, caminho_csv='data/rodadas.csv'):
    novo_registro = pd.DataFrame([{
        'rodada': rodada,
        'tipo': tipo,
        'texto': texto
    }])

    if os.path.exists(caminho_csv):
        novo_registro.to_csv(caminho_csv, mode='a', header=False, index=False)
    else:
        novo_registro.to_csv(caminho_csv, mode='w', header=True, index=False)

# Entrada do usuário
texto_usuario = st.text_area(
    "📨 Digite a descrição do chamado:",
    placeholder="Ex: Preciso de acesso ao sistema XYZ para realizar meus relatórios."
)

# Simples controle de rodada
rodada = 1  # futuramente você pode usar uma variável de estado ou data/hora

# Botão de ação
if st.button("Classificar"):
    if texto_usuario.strip() == "":
        st.warning("⚠️ Por favor, digite algo antes de classificar!")
    else:
        categoria = classificar(texto_usuario)
        resposta = gerar_resposta(categoria)

        st.success(f"✅ **Categoria prevista:** {categoria}")
        st.info(f"💡 **Resposta automática:** {resposta}")

        # Registrar interações
        registrar_interacao(rodada, "usuário", texto_usuario)
        registrar_interacao(rodada, "IA", resposta)
        registrar_interacao(rodada, "feedback", f"Classificado como '{categoria}'")




