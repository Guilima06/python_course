from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time


def open_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True, )
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    return browser


def search_store_adressess(store_search, store_name):
    try:
        # Limpando o campo de pesquisa
        elem = browser.find_element(By.NAME, 'q')
        elem.clear()

        # Preenchendo o campo de pesquisa com o endereço da loja
        elem.send_keys(store_search + Keys.RETURN)

        # Aguardando o carregamento completo da página
        time.sleep(4)

        url = browser.current_url
    except Exception as ErroFindTextfield:
        browser.get(site)
        time.sleep(2)

        # Limpando o campo de pesquisa
        elem = browser.find_element(By.NAME, 'q')
        elem.clear()

        # Preenchendo o campo de pesquisa com o endereço da loja
        elem.send_keys(store_search + Keys.RETURN)

        # Aguardando o carregamento completo da página
        time.sleep(4)

        url = browser.current_url

    try:
        soup = get_formated_html_content()
    except Exception as erroSoup:
        print('Erro ao gerar o html.parser')
        store_address = 'Erro na busca'
        address = format_address(store_address, store_name, url)
    else:
        address = search_adress_in_html(soup, store_name, url)
        return address


def get_formated_html_content():
    try:
        html_content = browser.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
    except Exception as erroGetHtml:
        print('Erro ao obter o HTML da página')
    else:
        return soup


def search_adress_in_html(soup, store_name, url):
    try:
        icon = soup.find("img", {"src": "//www.gstatic.com/images/icons/material/system_gm/2x/place_gm_blue_24dp.png"})

        if icon:
            endereco_element = div_find(icon)
        elif not icon:
            icon = soup.find("img", {"src": "//www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png"})
            endereco_element = div_find(icon)
        else:
            endereco_element = 'Não encontrado'
    except Exception as ErroSearchDiv:
        print('Erro ao buscar os dados no arquivo HTML')
        endereco_element = 'não encontrado'
        return format_address(endereco_element, store_name, url)
    else:
        return format_address(endereco_element, store_name, url)


def div_find(icon_location):
    try:
        icon_div = icon_location.find_parent("div")
        parent_div_icon = icon_div.find_parent("div")
        next_div = parent_div_icon.find_next_sibling("div")
        endereco_element = next_div.find("div")
    except Exception as ErroFindDiv:
        print('Erro ao buscar a div com o endereço')
        endereco_element = 'Não encontrado'
        return endereco_element
    else:
        return endereco_element.text


def format_address(store_address, store_name, url):
    coordenates = format_coordenates(url)
    loja_endereco = {
        'Loja:': store_name,
        'Endereço': store_address,
        'Latitude': coordenates['Latitude'],
        'Longitude': coordenates['Longitude']
    }
    return loja_endereco


def format_coordenates(url):
    try:
        lat_init = url.find('@') + 1
        end_lat = url[lat_init:].find(',')
        latitude = url[lat_init:(lat_init + end_lat)]

        lon_init = url.find(latitude) + len(latitude) + 1
        end_lon = url[lon_init:].find(',')
        longitude = url[lon_init:(lon_init + end_lon)]
        coordenates = {
            'Latitude': latitude,
            'Longitude': longitude
        }
        return coordenates
    except Exception as ErroLatLong:
        print('Erro ao buscar a latitude e Longitude')
        coordenates = {
            'Latitude': 'Não encontrado',
            'Longitude': 'Não encontrado'
        }
        return coordenates


element = '/home/felipe/Downloads/busca endereço atacadão.xlsx'
# df = pd.read_excel(element)
# Lê o arquivo Excel e armazena os dados em um DataFrame
store_list = pd.read_excel(element)

stores = []
for index, row in store_list.iterrows():
    store_name = row['Loja']
    store_address = row['Endereço']
    store_data_to_search = {
        "Loja": store_name,
        'Endereço': store_address
    }
    stores.append(store_data_to_search)


#Cria lista para receber resultados endereços
address_list = []
address_list_not_found = []
except_list = []

browser = open_browser()
site = str('https://www.google.com/maps')
browser.get(site)
time.sleep(3)

for store in stores:
    search = store['Loja'] + ' - ' + store['Endereço']
    print(f'Buscando a loja {store}')

    try:
        validated_store_address = search_store_adressess(search, store['Loja'])
        print(validated_store_address)
        address_list.append(validated_store_address)
    except Exception as erroSearchStore:
        print('Erro ao tentar buscar a loja')

        loja_endereco = {
            'Loja:': store['Loja'],
            'Endereço': 'Não encontrado',
            'Latitude': 'Não encontrado',
            'Longitude': 'Não encontrado'
        }
        address_list.append(loja_endereco)
        print(loja_endereco)


adresses = pd.DataFrame(address_list)
adresses.to_excel('Lista de lojas pesquisadas atacadão.xlsx')