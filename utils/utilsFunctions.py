import pandas as pd
from bs4 import BeautifulSoup
import os
import tkinter as tk
from tkinter import filedialog
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl


def open_folder():
    # Abre a janela do explorer para escolher um arquivo
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()


def open_file():
    # Abre a janela do explorer para escolher um arquivo
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

# path = open_folder()
# print(path)

def read_excel(header = None):
    file_path = open_file()
    # Lê o arquivo Excel e armazena os dados em um DataFrame
    return pd.read_excel(file_path, header=header) \
        if header is not None else pd.read_excel(file_path)


def write_excel(data):
    df = pd.DataFrame(data)
    file_name = save_excel()
    # Salvando o dataframe em um arquivo Excel
    df.to_excel(file_name)


def write_txt(data):
    df = pd.DataFrame(data)
    file_name = save_txt()

def read_html():
    file_path = open_file()
    # Abrindo o arquivo e lendo o conteúdo
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def save_excel():
    # abre a caixa de diálogo para seleção do local de salvamento do arquivo Excel
    filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo Excel', filetypes=[('Excel files', '*.xlsx')])
    if not filename.endswith('.xlsx'):
        filename += '.xlsx'
    return filename


def save_txt():
    # abre a caixa de diálogo para seleção do local de salvamento do arquivo TXT
    filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo txt', filetypes=[('Text Documents', '*.txt')])
    if not filename.endswith('.txt'):
        filename += '.txt'
    return filename


def open_chrome():
    return webdriver.Chrome()


def insert_site(browser, site):
    open_site = str(site)
    browser.get(open_site)
    # assert 'Google' in browser.title
    # Aguardando o carregamento completo da página
    print(browser.title)
    time.sleep(5)
    input('Insira algo para seguir....')


def open_console():
    options = webdriver.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")
    return webdriver.Chrome(options=options)

def input_int(texto):
    return int(input(texto))