import os

import chardet  # Você pode precisar instalar o pacote chardet: pip install chardet
from utils import utilsFunctions

def convert_utf8_to_iso8859(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as utf8_file:
        utf8_content = utf8_file.read()

    iso8859_content = utf8_content.encode('iso-8859-1', 'ignore')

    with open(output_path, 'wb') as iso8859_file:
        iso8859_file.write(iso8859_content)

# Substitua 'caminho_entrada' e 'caminho_saida' pelos caminhos de entrada e saída desejados
caminho_entrada = utilsFunctions.open_file()
caminho_saida = os.path.join(os.getcwd(), 'teste convert')

convert_utf8_to_iso8859(caminho_entrada, caminho_saida)