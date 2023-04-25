# Converte dados do usuário para um formato adequado.

import pandas as pd
from utils import utilsFunctions

# Lê o arquivo Excel e armazena os dados em um DataFrame
user_data = utilsFunctions.read_excel()

# Lista que armazenará os dados dos usuários
user_list = []

# Iterando sobre todas as lojas encontradas
for index, row in user_data.iterrows():
    name = row['Nome'].title().strip()
    email = row['E-mail'].lower().strip()
    code = 'L2OT3'
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
utilsFunctions.save_excel(access)
