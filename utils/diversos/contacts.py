import pandas as pd
import tkinter as tk
from tkinter import filedialog
import openpyxl


# Cria uma janela de diálogo para selecionar o arquivo de entrada
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Lê o arquivo Excel e armazena os dados em um DataFrame
clients = pd.read_excel(file_path)

#Lista que armazenará os dados das lojas
clients_list = []
print(clients.columns)

# Iterando sobre todas as lojas encontradas
for index, row in clients.iterrows():
    try:
        client_name = row['Nome Fantasia']
        tel_geral = row['Telefone Geral']
        if tel_geral is None:
            tel_geral = 'Não cadastrado.'
        dados_cliente = {
            'Nome': client_name,
            'Telefone': tel_geral
        }
        clients_list.append(dados_cliente)
    except IndexError as erro1:
        print('erro na conversão')
        # dados_lojas = {
        #     'Rua': endereco,
        #     'Número': '',
        #     'Bairro': '',
        #     'Cidade - UF': '',
        #     'Cep:': ''
        # }
        # store_list.append(dados_lojas)

print(clients_list)

#
# # Criando um dataframe do pandas com as informações coletadas
# addresses = pd.DataFrame(store_list)
#
# # abre a caixa de diálogo para seleção do local de salvamento do arquivo Excel
# filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo Excel', filetypes=[('Excel files', '*.xlsx')])
# if not filename.endswith('.xlsx'):
#     filename += '.xlsx'
#
# # Salvando o dataframe em um arquivo Excel
# addresses.to_excel(filename)