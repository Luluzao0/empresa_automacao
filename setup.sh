#!/bin/bash

# Atualizar o repositório e instalar o Xvfb
apt-get update
apt-get install -y xvfb

# Iniciar o Xvfb
Xvfb :99 -screen 0 1024x768x16 &
export DISPLAY=:99

# Executar o script do Streamlit
streamlit run /mount/src/empresa_automacao/app.py
