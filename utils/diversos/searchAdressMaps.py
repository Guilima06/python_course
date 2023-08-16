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
input()
assert 'Google' in browser.title
# Aguardando o carregamento completo da página
time.sleep(5)
address_list = []
# icon = '//www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png'

# Iterando sobre todas as lojas encontradas
for index, row in store_list.iterrows():
    endereco_pesquisa = row['Endereço']
    loja_pesquisa = row['Loja']
    # Limpando o campo de pesquisa
    elem = browser.find_element(By.NAME, 'q')
    elem.clear()
    # Preenchendo o campo de pesquisa com o endereço da loja
    elem.send_keys(endereco_pesquisa + Keys.RETURN)
    # Aguardando o carregamento completo da página
    time.sleep(10)
    # Obtendo a URL atual
    url_atual = browser.current_url
    # print(url_atual)
    # response = requests.get(url_atual)
    # print('response ok')
    html_content = browser.page_source
    # print(html_content)
    #
    # print(html_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    # endereco_element = soup.find("meta", {"property": "og:title"})
    #  print('teste' + endereco_element)
    # endereco = endereco_element["content"]
    # print(endereco)
    # address_list.append(endereco)
    # time.sleep(1)

    icon = soup.find("img", {"src": "//www.gstatic.com/images/icons/material/system_gm/2x/place_gm_blue_24dp.png"})

    if icon:
        # Pegar a div pai do ícone e depois a div irmã da div pai que possui o endereço
        icon_div = icon.find_parent("div")
        parent_div = icon_div.find_parent("div")
        endereco_element = parent_div.find_next_sibling("div")
        # print(parent_div)
        # print(endereco_element)
        if endereco_element:
            endereco = endereco_element.text.strip()
            print('Endereço:', endereco)
            loja_endereco = {
                'Loja:': loja_pesquisa,
                'Endereço:': endereco
            }
            address_list.append(loja_endereco)
            # print(loja_endereco)
        else:
            print('Endereço não encontrado')
            loja_endereco = {
                'Loja:': loja_pesquisa,
                'Endereço:': url_atual
            }
            address_list.append(loja_endereco)
            # print(loja_endereco)
    else:
        print('Ícone não encontrado')
        loja_endereco = {
            'Loja:': loja_pesquisa,
            'Endereço:': url_atual
        }
        address_list.append(loja_endereco)
        # print(loja_endereco)

    time.sleep(1)

# Criando um dataframe do pandas com as informações coletadas
addresses = pd.DataFrame(address_list)

utilsFunctions.save_excel(addresses)