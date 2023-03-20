import pandas as pd
import tkinter as tk
from tkinter import filedialog


# Cria uma janela de diálogo para selecionar o arquivo de entrada
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Lê o arquivo Excel e armazena os dados em um DataFrame
store_data = pd.read_excel(file_path)

#Lista que armazenará os dados das lojas
store_list = []

# Iterando sobre todas as lojas encontradas
for index, row in store_data.iterrows():
    try:
        endereco = row['Endereço'].split(",")
        rua = endereco[0].strip()
        num_bairro = endereco[1].strip().split('-')
        numero = num_bairro[0].strip()
        bairro = num_bairro[1].strip()
        cidade_uf = endereco[len(endereco)-2].strip()
        cep = endereco[-1].strip()
        dados_lojas = {
            'Rua': rua,
            'Número': numero,
            'Bairro': bairro,
            'Cidade - UF': cidade_uf,
            'Cep:': cep
        }
        store_list.append(dados_lojas)
    except IndexError as erro1:
        print('erro na conversão')
        dados_lojas = {
            'Rua': endereco,
            'Número': '',
            'Bairro': '',
            'Cidade - UF': '',
            'Cep:': ''
        }
        store_list.append(dados_lojas)

print(store_list)


# Criando um dataframe do pandas com as informações coletadas
addresses = pd.DataFrame(store_list)

# abre a caixa de diálogo para seleção do local de salvamento do arquivo Excel
filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo Excel', filetypes=[('Excel files', '*.xlsx')])
if not filename.endswith('.xlsx'):
    filename += '.xlsx'

# Salvando o dataframe em um arquivo Excel
addresses.to_excel(filename)
