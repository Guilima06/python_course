import pandas as pd
from bs4 import BeautifulSoup
# import tkinter as tk
# from tkinter import filedialog
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl
import requests
import json
# from win10toast import ToastNotifier


def open_folder():
    # Abre a janela do explorer para escolher um arquivo
    root = tk.Tk()
    root.withdraw()
    path_folder = filedialog.askdirectory()
    return path_folder


def open_file():
    # Abre a janela do explorer para escolher um arquivo
    root = tk.Tk()
    root.withdraw()
    path_file = filedialog.askopenfilename()
    return path_file


def read_excel(header=None):
    file_path = open_file()
    # Lê o arquivo Excel e armazena os dados em um DataFrame
    return pd.read_excel(file_path, header=header) \
        if header is not None else pd.read_excel(file_path)


# def write_excel(data):
#     df = pd.DataFrame(data)
#     file_name = save_excel()
#     # Salvando o dataframe em um arquivo Excel
#     df.to_excel(file_name)


def write_txt(data):
    df = pd.DataFrame(data)
    file_name = save_txt()


def read_html():
    file_path = open_file()
    # Abrindo o arquivo e lendo o conteúdo
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def save_excel(database):
    # abre a caixa de diálogo para seleção do local de salvamento do arquivo Excel
    filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo Excel', filetypes=[('Excel files', '*.xlsx')])
    if not filename.endswith('.xlsx'):
        filename += '.xlsx'
    database.to_excel(filename, index=False)


def save_txt():
    # abre a caixa de diálogo para seleção do local de salvamento do arquivo TXT
    filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo txt', filetypes=[('Text Documents', '*.txt')])
    if not filename.endswith('.txt'):
        filename += '.txt'
    return filename


#funções Selenium
def open_chrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    return browser


def click_btn_wait(location):
    button = location
    button.click()
    time.sleep(2)


def click_btn(location,browser):
    button = location
    button.click()
    browser.implicitly_wait(2)


def open_firefox():
    driver = webdriver.Firefox
    return driver


def insert_site(browser, site):
    open_site = str(site)
    browser.get(open_site)
    # Aguardando o carregamento completo da página
    print(browser.title)
    time.sleep(5)
    input('Aguarde o carregamento da página....')


def open_console():
    options = webdriver.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")
    return webdriver.Chrome(options=options)


def get_token_dysrup():
    # employer_code = input(str('Insira o código do Empregador: '))
    # user = input(str('Insira o usuário: '))
    # password = input(str('Insira a senha: '))
    employer_code = '5YTD7'
    user = 'suporte@dysrup.com.br'
    password = 'Dysrup@2023'

    response = requests.post('https://app.dysrup.com.br/api/v1/login', json={
        "username": user,
        "password": password,
        "type": "web",
        "employer_code": employer_code,
    })

    headers = {'Authorization': f'Bearer {token}'}
    return headers



def win10_notification(title, msg):
    # Inicializa #
    toaster = ToastNotifier()

    title = title
    msg = msg

    toaster.show_toast(
        title,
        msg,
        threaded=True,
        icon_path=None,
        duration=5  # 5 segundos
    )


def find_loja(lista, nome_parametro, nome_buscado):
    for item in lista:
        if item[nome_parametro] == nome_buscado:
            return item
    return None
