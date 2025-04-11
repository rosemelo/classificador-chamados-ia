import streamlit as st
from classify import classificar
from respostas import gerar_resposta

st.set_page_config(page_title="Classificador de Chamados", layout="centered")

st.title("🤖 Classificador de Chamados com IA")
st.write("Digite abaixo o texto de um chamado e veja a mágica acontecer!")

texto_usuario = st.text_area("Texto do chamado:")

if st.button("Classificar"):
    if texto_usuario.strip() == "":
        st.warning("Por favor, digite algo antes de classificar!")
    else:
        categoria = classificar(texto_usuario)
        resposta = gerar_resposta(categoria)

        st.success(f"**Categoria:** {categoria}")
        st.info(f"**Resposta do sistema:** {resposta}")


