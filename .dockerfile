FROM python:3.11

# Copiar e instalar dependências
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copiar e executar o script de instalação
COPY setup.sh /app/setup.sh
RUN chmod +x /app/setup.sh
RUN /app/setup.sh

# Copiar código da aplicação
COPY . /app

# Executar o aplicativo
CMD ["streamlit", "run", "/app/app.py"]
