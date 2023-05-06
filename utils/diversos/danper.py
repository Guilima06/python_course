import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'http://www.danpercalcados.com.br/tradicional/'
# driver = webdriver.Chrome()
# driver.get(url)
# html_content = driver.page_source

response = requests.get(url)
cookies = response.cookies

# Envie a permissão dos cookies na próxima solicitação
headers = {
    'Cookie': '; '.join([f'{name}={value}' for name, value in cookies.items()])
}
response = requests.get(url, headers=headers)

html_content = response.content

# input('Aguarde o carregamento da página')
soup = BeautifulSoup(html_content, 'html.parser')
html = soup.prettify()
# print(html)
with open('arquivo.html', 'w', encoding='utf-8') as arquivo:
    arquivo.write(html)