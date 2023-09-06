from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from utils import utilsFunctions
import time


def open_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    return browser


def search_store_adressess(store_address, store_name):
    # Limpando o campo de pesquisa
    elem = browser.find_element(By.NAME, 'q')
    elem.clear()

    # Preenchendo o campo de pesquisa com o endereço da loja
    elem.send_keys(store_address + Keys.RETURN)

    # Aguardando o carregamento completo da página
    time.sleep(2)

    soup = get_formated_html_content()
    address = search_adress_in_html(soup, store_name)
    return address


def get_formated_html_content():
    html_content = browser.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup


def search_adress_in_html(soup, store_name):
    icon = soup.find("img", {"src": "//www.gstatic.com/images/icons/material/system_gm/2x/place_gm_blue_24dp.png"})
    if not icon:
        icon = soup.find("img", {"src": "//www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png"})
    if icon:
        endereco_element = div_find(icon)
    else:
        endereco_element = 'Não encontrado'

    return format_address(endereco_element, store_name)

def div_find(icon_location):
    icon_div = icon_location.find_parent("div")
    parent_div = icon_div.find_parent("div")
    endereco_element = parent_div.get('aria-label')
    return endereco_element


def format_address(store_address, store_name):
    loja_endereco = {
        'Loja:': store_name,
        'Endereço': store_address.replace('Endereço, ', '')
        }
    return loja_endereco


# Lê o arquivo Excel e armazena os dados em um DataFrame
store_list = utilsFunctions.read_excel()

#Cria lista para receber endereços
address_list = []
address_list_not_found = []

browser = open_browser()
site = str('https://www.google.com/maps')
browser.get(site)
time.sleep(3)

for index, row in store_list.iterrows():
    store_name = row['Loja']
    store_address_search = row['Endereço']
    validated_store_address = search_store_adressess(store_address_search, store_name)
    if validated_store_address['Endereço'] == 'Não encontrado':
        address_list_not_found.append(validated_store_address)
    else:
        address_list.append(validated_store_address)



# Criando um dataframe do pandas com as informações coletadas
addresses = pd.DataFrame(address_list)
addresses_not_found = pd.DataFrame(address_list_not_found)

utilsFunctions.save_excel(addresses)
utilsFunctions.save_excel(addresses_not_found)