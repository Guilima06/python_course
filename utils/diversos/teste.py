from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
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
    time.sleep(3)



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


def get_options_in_cidades(estado):
    dropdown_cidades = Select(browser.find_element(By.CLASS_NAME, 'cidade'))
    cidades = []
    for cidade in dropdown_cidades.options:
        if cidade.text != 'Selecione a cidade':
            cidades.append(cidade.text)
    return cidades


def select_cidade(cidade):
    dropdown_cidades = Select(browser.find_element(By.CLASS_NAME, 'cidade'))
    dropdown_cidades.select_by_visible_text(cidade)


def get_options_in_lojas():
    dropdown_lojas = Select(browser.find_element(By.CLASS_NAME, 'loja'))
    lojas = []
    for loja in dropdown_lojas.options:
        if loja.text != 'Selecione sua loja':
            lojas.append(loja.text)
    return lojas


def selec_loja(loja):
    dropdown_lojas = Select(browser.find_element(By.CLASS_NAME, 'loja'))
    dropdown_lojas.select_by_visible_text(loja)


def get_address(location):
    address = location
    address_text = address.text
    return address_text



browser = open_browser()
site = 'https://ri.assai.com.br/o-assai/nossas-lojas/'
browser.get(site)
time.sleep(3)

#aceita os cookies da página
click_btn_wait(browser.find_element(By.ID, 'cookiescript_accept'))

#abre o modal para selecionar outra loja
click_btn(browser.find_element(By.CLASS_NAME, 'seletor-loja.trocar-loja-title'))

#busca a lista de estados da opção estado
estados = get_options_in_estado()

for estado in estados:
    select_estado(estado)
    cidades = get_options_in_cidades(estado)
    for cidade in cidades:
        select_cidade(cidade)
        lojas = get_options_in_lojas()
        for loja in lojas:
            selec_loja(loja)
            click_btn_wait(browser.find_element(By.CLASS_NAME, 'confirmar.btn-laranja'))

            endereco_result = get_address(browser.find_element(By.CLASS_NAME, 'info.endereco'))
            browser.get(site)



# for option in dropdown_estado.options:
#     if option.text != 'Selecione o seu Estado':
#         estado = option.text
#         print(estado)
#
#         # Seleciona o estado
#         dropdown_estado.select_by_visible_text(estado)
#
#         dropdown_cidades = Select(browser.find_element(By.CLASS_NAME, 'cidade'))
#         time.sleep(1)
#         for cidade_option in dropdown_cidades.options:
#             if cidade_option.text != 'Selecione a cidade':
#                 cidade = cidade_option.text
#                 print(cidade)
#                 dropdown_cidades.select_by_visible_text(cidade)
#
#                 dropdown_lojas = Select(browser.find_element(By.CLASS_NAME, 'loja'))
#                 time.sleep(1)
#                 for loja_option in dropdown_lojas.options:
#                     if loja_option.text != 'Selecione sua loja':
#                         loja = loja_option.text
#
#                         dropdown_lojas.select_by_visible_text(loja)
#                         print(loja)
#
#                         btn_confirmar_loja = browser.find_element(By.CLASS_NAME, 'confirmar.btn-laranja')
#                         btn_confirmar_loja.click()
#                         time.sleep(2)
#                         endereco_result = browser.find_element(By.CLASS_NAME, 'info.endereco')
#                         endereco = endereco_result.text
#                         print(endereco)
#                         browser.get(site)
#                         time.sleep(2)
#
#                         btn_trocar_loja = browser.find_element(By.CLASS_NAME, 'seletor-loja.trocar-loja-title')
#                         btn_trocar_loja.click()
#
#                         time.sleep(3)
#



