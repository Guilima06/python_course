# import requests
# from bs4 import BeautifulSoup
# import tkinter as tk
# from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
site = str('https://online.g4educacao.com/')
browser.get(site)
assert 'G4' in browser.title
# Aguardando o carregamento completo da página
time.sleep(5)
input('Faça a ação necessária no site')

browser.get('https://online.g4educacao.com/path-player?courseid=fundamentos-contratacao&unit=621fe85fd41f8c75410cb3e6Unit')
time.sleep(10)

# simula a ação do usuário para abrir o console
browser.execute_script("console.log('Console aberto via Selenium!')")
input('aguarde..')

# seleciona todo o código HTML
body_element = browser.find_element(By.TAG_NAME, 'body')
body_element.send_keys(Keys.CONTROL, 'a')
input('aguarde')

# copia o conteúdo selecionado
body_element.send_keys(Keys.CONTROL, 'c')
input('aguarde')


# response = requests.get(
#     'https://online.g4educacao.com/path-player?courseid=fundamentos-contratacao&unit=621fe85fd41f8c75410cb3e6Unit')
# html_content = response.content
#
# soup = BeautifulSoup(html_content, 'html.parser')
# video_element = soup.find('videoIframe')
# # video = video_element["content"]
# print(video_element)
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
# print(html)
