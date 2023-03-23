import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import pandas as pd
# pesquisar endereço no google maps, retornando endereço pelo request

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Lê o arquivo Excel e armazena os dados em um DataFrame
store_list = pd.read_excel(file_path)
print(store_list.columns)
browser = webdriver.Chrome()
site = str('https://www.google.com/maps')
browser.get(site)
assert 'Google' in browser.title
# Aguardando o carregamento completo da página
time.sleep(5)
address_list = []

# Iterando sobre todas as lojas encontradas
for index, row in store_list.iterrows():
    endereco_pesquisa = row['Endereço']
    # Limpando o campo de pesquisa
    elem = browser.find_element(By.NAME, 'q')
    elem.clear()
    # Preenchendo o campo de pesquisa com o endereço da loja
    elem.send_keys(endereco_pesquisa + Keys.RETURN)
    # Aguardando o carregamento completo da página
    time.sleep(4)
    # Obtendo a URL atual
    url_atual = browser.current_url
    response = requests.get(url_atual)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    endereco_element = soup.find("meta", {"property": "og:title"})
    endereco = endereco_element["content"].split('·')
    print(endereco)
    address_list.append(endereco)

# Criando um dataframe do pandas com as informações coletadas
addresses = pd.DataFrame(address_list)

# abre a caixa de diálogo para seleção do local de salvamento do arquivo Excel
filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo Excel', filetypes=[('Excel files', '*.xlsx')])
if not filename.endswith('.xlsx'):
    filename += '.xlsx'

# Salvando o dataframe em um arquivo Excel
addresses.to_excel(filename)


# response = requests.get(url_atual)
# html_content = response.content
#
# soup = BeautifulSoup(html_content, 'html.parser')
# endereco_element = soup.find("meta", {"property": "og:title"})
# endereco = endereco_element["content"].split('·')
# print(endereco)
# html = soup.prettify()
#
# # abre a caixa de diálogo para seleção do local de salvamento do arquivo Excel
# filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo txt', filetypes=[('Text Documents', '*.txt')])
# if not filename.endswith('.txt'):
#     filename += '.txt'
#
# with open(filename, 'w', encoding='utf-8') as file:
#     file.write(html)
#
#
# print(html)
#
