from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Abre o Google Maps
driver.get("https://www.google.com/maps")

# Insere o endereço na barra de pesquisa
endereco = input("Insira o endereço: ")
campo_pesquisa = driver.find_element(By.NAME, "q")
campo_pesquisa.send_keys(endereco)
campo_pesquisa.submit()

# Aguarda a página carregar completamente
driver.implicitly_wait(10)

# Clica na primeira opção de resultado
resultado = driver.find_element(By.CSS_SELECTOR, "div.section-result-content")
resultado.click()

# Coleta o endereço completo e o cep
endereco_completo = driver.find_element(By.CSS_SELECTOR, "div[data-section-id='ad']")
cep = driver.find_element(By.CSS_SELECTOR, "span[data-item-id='mo']")
print("Endereço completo:", endereco_completo.text)
print("CEP:", cep.text)

# Fecha o navegador
driver.quit()

