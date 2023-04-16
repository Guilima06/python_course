import pandas as pd
from bs4 import BeautifulSoup
import os
import tkinter as tk
from tkinter import filedialog
import openpyxl


# Selecionando o arquivo com o código HTML
file_path = '/home/guilherme/Dropbox/HTML/Lojas/tenda.html'

# Abrindo o arquivo e lendo o conteúdo
with open(file_path, 'r', encoding='utf-8') as file:
    html = file.read()

# Criando o objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
for br in soup.find_all('br'):
    br.replace_with(', ')

# Encontrando todas as lojas
stores = soup.find_all('div', {'class': 'BranchComponent'})
print(len(stores))

# # Criando uma lista para armazenar as informações
store_list = []
#
# Iterando sobre todas as lojas encontradas
for store in stores:
    # Verificando se a tag com a classe desejada existe
    name_element = store.find('h5')
    if name_element is not None:
        # Extraindo as informações
        name = name_element.text.strip().title()
        address = store.find('p').text.strip()
        dados_loja = {
            'Nome': name,
            'Endereço': address,
        }
        store_list.append(dados_loja)
print(store_list)
# Criando um dataframe do pandas com as informações coletadas
df = pd.DataFrame(store_list, columns=['Nome', 'Endereço'])

# Salvando o dataframe em um arquivo Excel
df.to_excel('/home/guilherme/Dropbox/HTML/Lojas/Storestenda.xlsx', index=False)
