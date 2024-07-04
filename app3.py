import streamlit as st
import pandas as pd
import pywhatkit as pwk
import os

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

# Função para enviar imagem via WhatsApp usando pywhatkit
def enviar_imagem(telefone, imagem_path):
    try:
        # Envia a imagem pelo WhatsApp Web
        pwk.sendwhats_image(telefone, imagem_path, wait_time=10, tab_close=True)
        return "Imagem enviada com sucesso!"
    except Exception as e:
        return f"Erro ao enviar a imagem: {e}"

# Upload de tabela Excel com números de telefone
uploaded_file = st.file_uploader("Insira a tabela Excel que contenha os números de telefone", type=["xlsx"])

# Inserir número de telefone individual
telefone_individual = st.text_input("Insira o telefone individual (com código do país, ex: +55XXXXXXXXXXX)")

# Inserir mensagem desejada
mensagem = st.text_area("Insira a mensagem desejada para o compartilhamento", "Bem vindo à Empresa A, o que gostaria de saber?")

# Upload de imagem
imagem = st.file_uploader("Insira uma imagem para enviar junto com a mensagem", type=["jpg", "jpeg", "png"])

# Botão para enviar mensagem
if st.button("Enviar Mensagem"):
    if telefone_individual:
        # Garantir que o número de telefone comece com "+"
        if not telefone_individual.startswith("+"):
            telefone_individual = "+" + telefone_individual
        # Enviar mensagem para telefone individual
        resultado_mensagem = enviar_mensagem(telefone_individual, mensagem)
        st.write(resultado_mensagem)
    elif uploaded_file is not None:
        # Enviar mensagem para lista de telefones no Excel
        df = pd.read_excel(uploaded_file)
        for index, row in df.iterrows():
            telefone = str(row.iloc[0])  # Assume que os números de telefone estão na primeira coluna
            # Garantir que o número de telefone comece com "+"
            if not telefone.startswith("+"):
                telefone = "+" + telefone
            # Enviar mensagem para telefone individual
            resultado_mensagem = enviar_mensagem(telefone, mensagem)
            st.write(f"{telefone}: {resultado_mensagem}")
    else:
        st.write("Por favor, insira um telefone individual ou faça o upload de uma tabela Excel.")

# Botão para enviar imagem
if st.button("Enviar Imagem"):
    imagem_path = None
    if imagem:
        # Cria o diretório se não existir
        os.makedirs('uploaded_images', exist_ok=True)
        imagem_path = os.path.join('uploaded_images', imagem.name)
        with open(imagem_path, 'wb') as f:
            f.write(imagem.getbuffer())
    
    if telefone_individual:
        # Garantir que o número de telefone comece com "+"
        if not telefone_individual.startswith("+"):
            telefone_individual = "+" + telefone_individual
        # Enviar imagem para telefone individual
        if imagem_path:
            resultado_imagem = enviar_imagem(telefone_individual, imagem_path)
            st.write(resultado_imagem)
    elif uploaded_file is not None:
        # Enviar imagem para lista de telefones no Excel
        df = pd.read_excel(uploaded_file)
        for index, row in df.iterrows():
            telefone = str(row.iloc[0])  # Assume que os números de telefone estão na primeira coluna
            # Garantir que o número de telefone comece com "+"
            if not telefone.startswith("+"):
                telefone = "+" + telefone
            # Enviar imagem para telefone individual
            if imagem_path:
                resultado_imagem = enviar_imagem(telefone, imagem_path)
                st.write(f"{telefone}: {resultado_imagem}")
    else:
        st.write("Por favor, insira um telefone individual ou faça o upload de uma tabela Excel.")
