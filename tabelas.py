import pandas as pd

# Criação de um DataFrame com exemplos de números de telefone
data = {
    "Telefone": ["+", "+", "+"]
}

df = pd.DataFrame(data)

# Salvando o DataFrame em um arquivo Excel
file_path = "seu_caminho"
df.to_excel(file_path, index=False)

file_path
