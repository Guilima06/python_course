import os
import chardet  # Você pode precisar instalar o pacote chardet: pip install chardet
from utils import utilsFunctions


def get_file_type_and_charset(file_path):
    with open(file_path, 'rb') as file:
        header = file.read(8)  # Lê os primeiros 8 bytes do arquivo

    if header.startswith(b'\x50\x4B\x03\x04'):
        file_type = 'Zip'  # Arquivo no formato ZIP
    elif header.startswith(b'\x25\x50\x44\x46'):
        file_type = 'PDF'  # Arquivo no formato PDF
    elif header.startswith(b'\x49\x49\x2A\x00') or header.startswith(b'\x4D\x4D\x00\x2A'):
        file_type = 'TIFF'  # Arquivo no formato TIFF (Little-endian ou Big-endian)
    elif header.startswith(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'):
        file_type = 'PNG'  # Arquivo no formato PNG
    elif header.startswith(b'\xFF\xD8\xFF'):
        file_type = 'JPEG'  # Arquivo no formato JPEG
    elif header.startswith(b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1'):
        file_type = 'XLS'  # Arquivo no formato XLS (BIFF)
    elif header.startswith(b'\x50\x4B\x05\x06'):
        file_type = 'XLSX'  # Arquivo no formato XLSX (OpenXML)
    elif header.startswith(b'\x49\x44\x3D\x22'):
        file_type = 'CSV'  # Arquivo no formato CSV (primeiros bytes de uma URL de exportação do Excel)
    else:
        file_type = 'Tipo de arquivo não reconhecido'

    # Detecta o conjunto de caracteres da codificação do arquivo
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        charset = result['encoding']

    return file_type, charset


# Substitua 'caminho_do_arquivo' pelo caminho do arquivo que você deseja verificar
file_path = utilsFunctions.open_file()
file_type, charset = get_file_type_and_charset(file_path)
print(f'Tipo do arquivo: {file_type}')
print(f'Charset: {charset}')