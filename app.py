import streamlit as st
import pandas as pd
import os

from repente_ia import gerar_pergunta, gerar_resposta_rimada

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

# === Inicialização de sessão ===
if 'rodada' not in st.session_state:
    st.session_state.rodada = 1
if 'pergunta_ia' not in st.session_state:
    st.session_state.pergunta_ia = gerar_pergunta()

# === Layout da página ===
st.set_page_config(page_title="Repente com IA", layout="centered")
st.title("🎤 Repente com IA")

st.markdown("""
Bem-vindo(a)! Esse é o jogo de **repente com IA**. Vamos rimar e criar versos juntos!

### Como funciona:
- A IA começa com uma pergunta rimada, e você responde **rimando também**!
- Se você acertar a rima, a IA continua a conversa no mesmo ritmo!
- Se não rimar, a IA avisa e te convida a tentar novamente.

Vamos ver o que sai dessa interação criativa?
""")

# Exibir a pergunta atual da IA
st.markdown(f"**IA ({st.session_state.rodada}ª rodada):**\n> {st.session_state.pergunta_ia}")

# Entrada do usuário
resposta_usuario = st.text_area("🎤 Sua resposta rimada:")

# Botão para responder
if st.button("Responder"):
    if resposta_usuario.strip() == "":
        st.warning("⚠️ Por favor, digite sua resposta rimada!")
    else:
        # Gerar resposta da IA baseada na rima
        resposta_ia = gerar_resposta_rimada(st.session_state.pergunta_ia, resposta_usuario)

        # Mostrar resposta da IA
        st.markdown(f"**IA:**\n> {resposta_ia}")

        # Registrar interações
        registrar_interacao(st.session_state.rodada, "IA", st.session_state.pergunta_ia)
        registrar_interacao(st.session_state.rodada, "usuário", resposta_usuario)
        registrar_interacao(st.session_state.rodada, "IA", resposta_ia)

        # Avança para próxima rodada e nova pergunta
        st.session_state.rodada += 1
        st.session_state.pergunta_ia = gerar_pergunta()

# Botão para reiniciar
if st.button("🔄 Reiniciar Conversa"):
    st.session_state.rodada = 1
    st.session_state.pergunta_ia = gerar_pergunta()
    st.success("A conversa foi reiniciada!")




