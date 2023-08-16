import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import filedialog

url = input('Insira a url para baixar os produtos ')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todos os elementos com a classe "box-lista-produto"
produtos = soup.find_all(class_='box-lista-produto')

lista_produtos = []

# Iterar sobre os elementos encontrados e extrair as informações desejadas
for produto in produtos:
    # Extrair o nome do produto
    nome_produto = produto.find(class_='titulo-produto').text.strip()

    # Extrair o código do produto
    codigo_produto = produto.find(class_='btn-vermelho')['data-produto_codigo']

    # Extrair a URL da imagem do produto
    url_imagem = produto.find('img')['src']

    # Imprimir as informações

    dados_produtos = {'Nome do produto:': nome_produto,
    'Código do produto:': codigo_produto,
    'URL da imagem:': url_imagem}
    lista_produtos.append(dados_produtos)
print(lista_produtos)
data = pd.DataFrame(lista_produtos)
# abre a caixa de diálogo para seleção do local de salvamento do arquivo Excel
filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo Excel', filetypes=[('Excel files', '*.xlsx')])
if not filename.endswith('.xlsx'):
    filename += '.xlsx'
data.to_excel(filename, index=False)