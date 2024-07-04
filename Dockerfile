FROM python:3.11

# Copiar e instalar dependências
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copiar o script de configuração e o código da aplicação
COPY setup.sh /app/setup.sh
COPY . /app

# Dar permissão de execução ao script
RUN chmod +x /app/setup.sh

# Executar o script de configuração
CMD ["/bin/bash", "/app/setup.sh"]
