import streamlit as st
import pandas as pd
import pywhatkit as pwk
import time

st.title("EMPRESA X mensagens para compartilhar")
st.subheader('Developed by LuisaoDev')

# Função para enviar mensagem via WhatsApp usando pywhatkit
def enviar_mensagem(telefone, mensagem):
    try:
        # Envia a mensagem pelo WhatsApp Web
        pwk.sendwhatmsg_instantly(telefone, mensagem, wait_time=10, tab_close=True)
        return "Mensagem enviada com sucesso!"
    except Exception as e:
        return f"Erro ao enviar a mensagem: {e}"

# Upload de tabela Excel com números de telefone
uploaded_file = st.file_uploader("Insira a tabela Excel que contenha os números de telefone", type=["xlsx"])

# Inserir número de telefone individual
telefone_individual = st.text_input("Insira o telefone individual (com código do país, ex: +55XXXXXXXXXXX)")

# Inserir mensagem desejada
mensagem = st.text_area("Insira a mensagem desejada para o compartilhamento", "Bem vindo à Empresa A, o que gostaria de saber?")

# Botão para enviar mensagem
if st.button("Enviar Mensagem"):
    if telefone_individual:
        # Enviar mensagem para telefone individual
        resultado = enviar_mensagem(telefone_individual, mensagem)
        st.write(resultado)
    elif uploaded_file is not None:
        # Enviar mensagem para lista de telefones no Excel
        df = pd.read_excel(uploaded_file)
        for index, row in df.iterrows():
            telefone = str(row.iloc[0])  # Assume que os números de telefone estão na primeira coluna
            resultado = enviar_mensagem(telefone, mensagem)
            st.write(f"{telefone}: {resultado}")
    else:
        st.write("Por favor, insira um telefone individual ou faça o upload de uma tabela Excel.")
