# Crie o Dockerfile
echo 'FROM python:3.11

# Copiar e instalar dependências
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copiar o script de configuração e o código da aplicação
COPY setup.sh /app/setup.sh
COPY . /app

# Dar permissão de execução ao script
RUN chmod +x /app/setup.sh

# Executar o script de configuração
CMD ["/bin/bash", "/app/setup.sh"]' > Dockerfile

# Crie o setup.sh
echo '#!/bin/bash

# Atualizar o repositório e instalar o Xvfb
apt-get update
apt-get install -y xvfb

# Iniciar o Xvfb
Xvfb :99 -screen 0 1024x768x16 &
export DISPLAY=:99

# Executar o script do Streamlit
streamlit run /mount/src/empresa_automacao/app.py' > setup.sh

# Crie o requirements.txt
echo 'streamlit
pandas
pywhatkit
pyautogui
xvfbwrapper' > requirements.txt

# Construa a imagem Docker
docker build -t empresa_automacao:latest .

# Execute a imagem Docker
docker run -p 8501:8501 empresa_automacao:latest
