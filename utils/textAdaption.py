import pandas as pd
import tkinter as tk
from tkinter import filedialog
import openpyxl
import utilsFunctions

excel_data = utilsFunctions.read_excel()
print(excel_data.columns)
user_list = []

print(excel_data.columns)

with open('Assinaturas.txt', 'a') as file:
# Iterando sobre todas as lojas encontradas
    for index, row in excel_data.iterrows():
        users_name = row['Nome']
        users_setor = row['Setor']
        users_mail = row['E-mail']
        users_tel = row['Telefone']
        user = {
            'Nome: ': users_name,
            'Setor: ': users_setor,
            'E-mail: ': users_mail,
            'Telefone: ': users_tel
        }
        user_list.append(user)

        # escreve cada valor do dicionário no arquivo de texto
        for key, value in user.items():
            file.write(key + str(value) + '\n')

        # adiciona uma linha em branco após o dicionário
        file.write('\n')

        # imprime cada valor do dicionário na tela
        for key, value in user.items():
            print(key, value)

    # salva o arquivo de texto
    utilsFunctions.save_txt()


