import os

import chardet  # Você pode precisar instalar o pacote chardet: pip install chardet
from utils import utilsFunctions

def read_file_with_charset(file_path, charset):
    try:
        with open(file_path, 'r', encoding=charset) as file:
            content = file.read()
            print(f'Charset: {charset}')
            print('Conteúdo do arquivo:')
            print(content)
    except FileNotFoundError:
        print('Arquivo não encontrado.')
    except UnicodeDecodeError:
        print(f'Erro ao decodificar usando o charset: {charset}')

# Substitua 'caminho_do_arquivo' pelo caminho do arquivo que você deseja ler
# Substitua 'utf-8' pelo charset desejado
caminho_do_arquivo = 'teste convert'
charset_desejado = 'ISO-8859-1'

read_file_with_charset(caminho_do_arquivo, charset_desejado)
