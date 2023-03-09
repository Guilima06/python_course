from tkinter.filedialog import asksaveasfilename

import pandas as pd
from bs4 import BeautifulSoup
import os
import tkinter as tk
from tkinter import filedialog
import openpyxl
import re


# Selecionando o arquivo com o código HTML
# Cria uma janela de diálogo para selecionar o arquivo de entrada
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Abrindo o arquivo e lendo o conteúdo
with open(file_path, 'r', encoding='utf-8') as file:
    html = file.read()

# Criando o objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
for br in soup.find_all('br'):
    br.replace_with(', ')

# Encontrando todas as lojas
stores = soup.find_all('div', {'class': 'box_loja'})
# print(stores)

# Criando uma lista para armazenar as informações
store_list = []
#
# # Iterando sobre todas as lojas encontradas
for store in stores:
    # Verificando se a tag com a classe desejada existe
    name_element = store.find('h3', {'class': 'title_loja'})
    if name_element is not None:
        # Extraindo as informações
        name = name_element.text.strip().title()
        address = store.find('li').text.strip().replace('\n                  ','')
        dados_loja = {
            'Nome': name,
            'Endereço': address
        }
        store_list.append(dados_loja)
print(store_list)
# Criando um dataframe do pandas com as informações coletadas
df = pd.DataFrame(store_list, columns=['Nome', 'Endereço'])

# abre a caixa de diálogo para seleção do local de salvamento do arquivo Excel
filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo Excel', filetypes=[('Excel files', '*.xlsx')])
if not filename.endswith('.xlsx'):
    filename += '.xlsx'

# Salvando o dataframe em um arquivo Excel
df.to_excel(filename)
