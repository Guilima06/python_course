import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
import time


# browser = webdriver.Chrome()
# site = str('https://www.google.com/maps')
# browser.get(site)
# assert 'Google' in browser.title
# # Aguardando o carregamento completo da página
# time.sleep(5)
# elem = browser.find_element(By.NAME, 'q')
# elem.send_keys(endereco_pesquisa + Keys.RETURN)
# time.sleep(4)
#
# url_atual = browser.current_url
response = requests.get('https://www.supermercadosnegreiros.com.br/institucional/paginas/nossas-lojas')
html_content = response.content
# response = requests.get(url_atual)
# html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
# endereco_element = soup.find("meta", {"property": "og:title"})
# endereco = endereco_element["content"].split('·')
# print(endereco)
html = soup.prettify()

# abre a caixa de diálogo para seleção do local de salvamento do arquivo Excel
filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo txt', filetypes=[('Text Documents', '*.txt')])
if not filename.endswith('.txt'):
    filename += '.txt'

with open(filename, 'w', encoding='utf-8') as file:
    file.write(html)


print(html)
