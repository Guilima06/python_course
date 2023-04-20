import utilsFunctions
import pandas as pd
from bs4 import BeautifulSoup

arquivo = utilsFunctions.read_excel()
print(arquivo.columns)
login = []

# abre o arquivo de texto para escrita em modo de anexo
with open('login.txt', 'a') as file:
    for index, row in arquivo.iterrows():
        store = row['Nome da loja']
        email = row['E-mail']
        password = row['Senha']
        login_data = {
            'Loja: ': store,
            'Cód. Empregador: ': 'SMBH',
            'E-mail: ': email,
            'Senha: ': password,
            ' ': ' '
        }
        login.append(login_data)

        # escreve cada valor do dicionário no arquivo de texto
        for key, value in login_data.items():
            file.write(key + str(value) + '\n')

        # adiciona uma linha em branco após o dicionário
        file.write('\n')

        # imprime cada valor do dicionário na tela
        for key, value in login_data.items():
            print(key, value)

    # salva o arquivo de texto
    utilsFunctions.save_txt()
