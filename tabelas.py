import pandas as pd

# Criação de um DataFrame com exemplos de números de telefone
data = {
    "Telefone": ["+559885231008", "+559889103365", "+559886081557"]
}

df = pd.DataFrame(data)

# Definindo o caminho e nome do arquivo
file_path = "C:\\Users\\luisg\\Documents\\empresa_automacao\\empresa_automacao\\numeros_telefone.xlsx"

# Salvando o DataFrame em um arquivo Excel
df.to_excel(file_path, index=False)

file_path
