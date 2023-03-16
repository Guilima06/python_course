from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

# Selecionando o arquivo excel
# Cria uma janela de diálogo para selecionar o arquivo de entrada
root = tk.Tk()
root.withdraw()
# file_path = filedialog.askopenfilename(initialdir='/home/guilherme/Dropbox/HTML/Lojas/scpt_atacadao.xlsx')
file_path = '/home/guilherme/Dropbox/HTML/Lojas/scpt_atacadao.xlsx'
# Lê o arquivo Excel e armazena os dados em um DataFrame
store_list = pd.read_excel(file_path)

# print(valor)

browser = webdriver.Chrome()
site = str('https://www.google.com/maps')
browser.get(site)
assert 'Google' in browser.title

# Iterando sobre todas as lojas encontradas
for index, row in store_list.iterrows():
    elem = browser.find_element(By.NAME, 'q')  # Find the search box
    endereco_pesquisa = row['Endereço']
    elem.send_keys(endereco_pesquisa + Keys.RETURN)
    # Aguarda 10 segundos
    time.sleep(10)
    url_atual = browser.current_url
    time.sleep(2)
    url = { str(url_atual)}
# if 'place/' in url_atual:
#     url = str(url_atual)
#     print(url)
#     address = url[url.find('place/') + len('place/'):url.find('/@')].strip().title().replace('+', ' ').replace('-', ',',-1)
#     print(address)
#
#     data = address.split(',')
#     print(data)
#     street = data[0]
#     number = data[1]
#     district = data[2]
#     city = data[3]
#     state = data[4].upper()
#     cep = data[len(data)-2] + '-' + data[len(data)-1]
#
#
# else:
#     print('não foi possivel extrair os dados ')
#     print(url_atual)
# input('pressione qualquer tecla para fechar o navegador...')
#
# browser.quit()
#
