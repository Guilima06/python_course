from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from utils import utilsFunctions
import time
from selenium.webdriver.support.ui import Select


def open_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    return browser


def click_btn_wait(location):
    button = location
    button.click()
    time.sleep(2)


def click_btn(location):
    button = location
    button.click()


def click_btn_accept_cookie():
    btn_accept_cookie = browser.find_element(By.ID, 'cookiescript_accept')
    btn_accept_cookie.click()
    time.sleep(3)


def click_btn_trocar_loja():
    btn_trocar_loja = browser.find_element(By.CLASS_NAME, 'seletor-loja.trocar-loja-title')
    btn_trocar_loja.click()
    time.sleep(1)


def get_options_in_estado():
    dropdown_estado = Select(browser.find_element(By.CLASS_NAME, "estado"))
    estados = []
    for estado in dropdown_estado.options:
        if estado.text != 'Selecione o seu Estado':
            estados.append(estado.text)
    return estados


def select_estado(estado):
    dropdown_estado = Select(browser.find_element(By.CLASS_NAME, "estado"))
    dropdown_estado.select_by_visible_text(estado)


def get_options_in_cidades():
    dropdown_cidades = Select(browser.find_element(By.CLASS_NAME, 'cidade'))
    cidades = []
    for cidade in dropdown_cidades.options:
        if cidade.text != 'Selecione a cidade':
            cidades.append(cidade.text)
    return cidades


def select_cidade(cidade,estado):
    select_estado(estado)
    dropdown_cidades = Select(browser.find_element(By.CLASS_NAME, 'cidade'))
    dropdown_cidades.select_by_visible_text(cidade)


def get_options_in_lojas():
    dropdown_lojas = Select(browser.find_element(By.CLASS_NAME, 'loja'))
    lojas = []
    for loja in dropdown_lojas.options:
        if loja.text != 'Selecione sua loja':
            lojas.append(loja.text)
    return lojas


def select_loja(loja,cidade,estado):
    select_cidade(cidade,estado)
    dropdown_lojas = Select(browser.find_element(By.CLASS_NAME, 'loja'))
    dropdown_lojas.select_by_visible_text(loja)


def get_address(location):
    address = location
    address_text = address.text
    return address_text


def get_store_info():
    click_btn(browser.find_element(By.CLASS_NAME, 'confirmar.btn-laranja'))
    address_location = browser.find_element(By.CLASS_NAME, 'info.endereco')
    address = get_address(address_location)
    return address


def format_store_info(estado, cidade, loja, endereco):
    store_info = {
        'Estado': estado,
        'Cidade': cidade,
        'Loja': loja,
        'Endereço': endereco
    }
    # abre o modal para selecionar outra loja
    click_btn(browser.find_element(By.CLASS_NAME, 'seletor-loja.trocar-loja-title'))
    browser.implicitly_wait(2)
    return store_info


browser = open_browser()
site = 'https://ri.assai.com.br/o-assai/nossas-lojas/'
browser.get(site)
time.sleep(2)

#aceita os cookies da página
click_btn_wait(browser.find_element(By.ID, 'cookiescript_accept'))

#abre o modal para selecionar outra loja
click_btn_wait(browser.find_element(By.CLASS_NAME, 'seletor-loja.trocar-loja-title'))

#busca a lista de estados da opção estado
estados = get_options_in_estado()

stores_info = []

for estado in estados:
    select_estado(estado)
    cidades = get_options_in_cidades()
    for cidade in cidades:
        try:
            select_cidade(cidade,estado)
            lojas = get_options_in_lojas()
            for loja in lojas:
                select_loja(loja,cidade,estado)

                store_address = get_store_info()
                store_info = format_store_info(estado, cidade, loja, store_address)
                stores_info.append(store_info)
        except Exception as erro:
            continue


else:
    store_list = pd.DataFrame(stores_info)
    utilsFunctions.save_excel(store_list)
