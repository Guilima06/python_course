from tkinter import filedialog
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
import openpyxl
import utilsFunctions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome()
site = str('https://app.tangerino.com.br/Tangerino/pages/LoginPage/wicket:pageMapName/wicket-0')
browser.get(site)
# input('Aguardando login....')
email = 'guilherme.lima@solucoesabc.com.br'
password = 'Gui@300696'
input_email = browser.find_element(By.NAME, 'login')
input_email.send_keys(email)
input_password = browser.find_element(By.NAME, 'password')
input_password.send_keys(password)
login = browser.find_element(By.NAME, 'btnLogin')
login.click()

time.sleep(2)
menu_colaboradores = browser.find_element(By.XPATH, "//span[text()='Colaboradores']")
menu_colaboradores.click()
painel = browser.find_element(By.XPATH, "//span[text()='Colaboradores']")
painel.click()

search_colaborador = browser.find_element(By.CSS_SELECTOR, 'id418')
search_colaborador.send_keys('Alcione')

search = browser.find_element(By.NAME, 'buscarInformacoes')
search.click()

# email = str(input('insira o email de acesso: '))
# password = str(input('Insira sua senha: '))

# elem = browser.find_element(By.ID, 'id79')
# elem = browser.find_element(By.ID, 'cabecalho')
# elem.click()
time.sleep(20)