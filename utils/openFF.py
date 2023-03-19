import tkinter as tk
from tkinter import filedialog
import pandas as pd
from bs4 import BeautifulSoup

# root = tk.Tk()
# root.withdraw()
# file_path = filedialog.askopenfilename()
#
# # Lê o arquivo Excel e armazena os dados em um DataFrame
# store_list = pd.read_excel(file_path)
# print(store_list.columns)
# print(store_list['Endereço'])
# for index, row in store_list.iterrows():
#     endereco_pesquisa = row['Endereço']
#     print(endereco_pesquisa)
address_store = ('Rod. Dr. João Miranda, 252 - Cristo Redentor, Abaetetuba - PA, 68440-000').split(',')
address = address_store[0]
print(address)
# dados_loja = {
#     'Endereço': address,
#     'Numero': num,
#     'Bairro': district,
#     'Cidade': city,
#     'CEP': cep
#     }
# store_list.append(dados_loja)