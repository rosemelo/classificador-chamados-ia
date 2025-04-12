import streamlit as st
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

# Campo de entrada com placeholder explicativo
texto_usuario = st.text_area(
    "📨 Digite a descrição do chamado:",
    placeholder="Ex: Preciso de acesso ao sistema XYZ para realizar meus relatórios."
)

# Botão com validação
if st.button("Classificar"):
    if texto_usuario.strip() == "":
        st.warning("⚠️ Por favor, digite algo antes de classificar!")
    else:
        categoria = classificar(texto_usuario)
        resposta = gerar_resposta(categoria)

        st.success(f"✅ **Categoria prevista:** {categoria}")
        st.info(f"💡 **Resposta automática:** {resposta}")



