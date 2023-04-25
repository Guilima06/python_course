# procura uma loja no maps pelo seu nome e endereço, obtendo o endereço completo com CEP
# e latitude e longitude

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pandas as pd
from utils import utilsFunctions

# Lê o arquivo Excel e armazena os dados em um DataFrame
store_list = utilsFunctions.read_excel()
browser = utilsFunctions.open_chrome()
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

utilsFunctions.save_excel(addresses)
