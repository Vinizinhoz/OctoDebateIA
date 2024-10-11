import Peter      
import Kevin
import time
import random
import streamlit as st
import json
import os

peter = Peter.Peter()
kevin = Kevin.Kevin()

def salvar_debate_json():
    if st.session_state.conversa:
        debate_salvo = {"tema": st.session_state.tema, "conversa": st.session_state.conversa.copy()}
        st.session_state.debates_salvos.append(debate_salvo)
        with open("debates.json", "w") as f:
            json.dump(st.session_state.debates_salvos, f)
        st.session_state.conversa = []

def carregar_debates_json():
    if os.path.exists("debates.json"):
        with open("debates.json", "r") as f:
            st.session_state.debates_salvos = json.load(f)

def exibir_debates_salvos():
    st.sidebar.header("Debates Salvos")
    if st.session_state.debates_salvos:
        debate_escolhido = st.sidebar.selectbox("Escolha um debate salvo", [debate["tema"] for debate in st.session_state.debates_salvos])
        if debate_escolhido:
            debate = next((debate for debate in st.session_state.debates_salvos if debate["tema"] == debate_escolhido), None)
            if debate:
                st.sidebar.write(f"**Tema:** {debate['tema']}")
                for mensagem in debate['conversa']:
                    st.sidebar.write(mensagem)
    else:
        st.sidebar.write("Nenhum debate salvo.")

def falapeter(fala):
    resposta = peter.Debate(fala)
    st.session_state.conversa.append(f"Peter: {resposta}")
    exibir_conversa()
    time.sleep(12)
    falakevin(resposta)

def falakevin(fala):
    resposta = kevin.Debate(fala)
    st.session_state.conversa.append(f"Kevin: {resposta}")
    exibir_conversa()
    time.sleep(12)
    falapeter(resposta)

def iniciatema(tema):
    numero = random.choice([1, 2])
    st.session_state.tema = tema
    st.session_state.conversa.append(f"Tema: {tema}")
    if numero == 1:
        falapeter(f"Tema: {tema}")
    else:
        falakevin(f"Tema: {tema}")

def exibir_conversa():
    container = st.empty()
    with container:
        for mensagem in st.session_state.conversa:
            if mensagem.startswith("Peter:"):
                st.markdown(
                    f"<div style='background-color: #444; color: #fff; padding: 10px; border: 1px solid #fff; border-radius: 5px; margin-bottom: 10px;'>{mensagem}</div>", 
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"<div style='background-color: #666; color: #fff; padding: 10px; border: 1px solid #fff; border-radius: 5px; margin-bottom: 10px;'>{mensagem}</div>", 
                    unsafe_allow_html=True
                )

st.set_page_config(page_title="Debate entre IAs", page_icon="logo.png")
col1,col2 = st.columns([1,2])

st.title("""
Debate entre IAs - Octo🐙
@octo_academy""")

if "conversa" not in st.session_state:
    st.session_state.conversa = []

if "debates_salvos" not in st.session_state:
    st.session_state.debates_salvos = []

carregar_debates_json()

tema = st.text_input("Digite o tema do Debate")

if st.button("Iniciar Debate"):
    if tema and len(st.session_state.conversa) == 0:
        iniciatema(tema)
    elif len(st.session_state.conversa) > 0:
        st.write("O debate já tá rolando.")
    else:
        st.write("Insira um tema")

if st.button("Salvar Debate"):
    salvar_debate_json()

exibir_conversa()
exibir_debates_salvos()