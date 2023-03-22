import pandas as pd
import tkinter as tk
from tkinter import filedialog
import openpyxl


# Cria uma janela de diálogo para selecionar o arquivo de entrada
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Lê o arquivo Excel e armazena os dados em um DataFrame
user_data = pd.read_excel(file_path)

#Lista que armazenará os dados dos usuários
user_list = []

# Iterando sobre todas as lojas encontradas
for index, row in user_data.iterrows():
    name = row['Nome'].title().strip()
    email = row['E-mail'].lower().strip()
    # name = ('ADRIEL VITOR DE JESUS SILVA').title().strip()
    code = 'L2OT3'
    # email = ('vitoradriel616@gmail.com').title().strip()
    password = '123456'
    access_data = {
        'Nome': name,
        'Código do empregador': code,
        'E-mail': email,
        'Senha': password
    }
    user_list.append(access_data)
    print(access_data)

# Criando um dataframe do pandas com as informações coletadas
access = pd.DataFrame(user_list)

# abre a caixa de diálogo para seleção do local de salvamento do arquivo Excel
filename = tk.filedialog.asksaveasfilename(title='Salvar arquivo Excel', filetypes=[('Excel files', '*.xlsx')])
if not filename.endswith('.xlsx'):
    filename += '.xlsx'

# Salvando o dataframe em um arquivo Excel
access.to_excel(filename)
