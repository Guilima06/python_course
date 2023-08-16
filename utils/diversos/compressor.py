#reduzir o tamanho de imagens
from PIL import Image
import os
#
# def reduzir_imagem(nome_arquivo, largura_max, altura_max):
#     imagem = Image.open(nome_arquivo)
#     largura_original, altura_original = imagem.size
#     proporcao = min(largura_max / largura_original, altura_max / altura_original)
#     nova_largura = int(largura_original * proporcao)
#     nova_altura = int(altura_original * proporcao)
#     imagem_redimensionada = imagem.resize((nova_largura, nova_altura), Image.ANTIALIAS)
#     destiny_dir = 'C:\\Users\\guilherme.lima\Desktop\\Mockups Selmi - Atualizado Março 2023\\Mockups Selmi - Atualizado Março 2023\\novos'
#     imagem_redimensionada.save(destiny_dir, "{nome_arquivo}_redimensionada.jpg")
#
#
# pasta = 'C:\\Users\\guilherme.lima\Desktop\\Mockups Selmi - Atualizado Março 2023\\Mockups Selmi - Atualizado Março 2023'
# products_list = []
# for nome_arquivo in os.listdir(pasta):
#     caminho_arquivo = os.path.join(pasta, nome_arquivo.replace('.png', ''))
#     # products = {
#     #     'Nome arquivo': nome_arquivo.replace('.png', ''),
#     #     'Caminho': caminho_arquivo
#     # }
#     if os.path.isfile(caminho_arquivo):
#         print("Nome do arquivo: ", nome_arquivo)
#         print("Caminho do arquivo:", caminho_arquivo)
#         reduzir_imagem(nome_arquivo, 800, 800)
#         # products_list.append(products)
#
#

def reduzir_imagem(nome_arquivo, largura_maxima, altura_maxima, diretorio_destino):
    # Abrir a imagem
    imagem = Image.open(nome_arquivo)

    # Obter as dimensões atuais da imagem
    largura_original, altura_original = imagem.size

    # Calcular as novas dimensões mantendo a proporção original
    proporcao = min(largura_maxima / largura_original, altura_maxima / altura_original)
    nova_largura = int(largura_original * proporcao)
    nova_altura = int(altura_original * proporcao)

    # Redimensionar a imagem
    imagem_redimensionada = imagem.resize((nova_largura, nova_altura), Image.LANCZOS)

    # Obter apenas o nome do arquivo (sem o caminho)
    nome_arquivo = os.path.basename(nome_arquivo)

    # Construir o caminho completo para o arquivo redimensionado
    caminho_arquivo_redimensionado = os.path.join(diretorio_destino, nome_arquivo)

    # Salvar a imagem redimensionada
    imagem_redimensionada.save(caminho_arquivo_redimensionado)


# Exemplo de uso
pasta_origem = "C:\\Users\\guilherme.lima\Desktop\\Mockups Selmi - Atualizado Março 2023\\Mockups Selmi - Atualizado Março 2023"  # Substitua pelo caminho da pasta de origem
pasta_destino = "C:\\Users\\guilherme.lima\Desktop\\Mockups Selmi - Atualizado Março 2023\\Mockups Selmi - Atualizado Março 2023\\novos"  # Substitua pelo caminho da pasta de destino

for nome_arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)

    if os.path.isfile(caminho_arquivo):
        reduzir_imagem(caminho_arquivo, 800, 800, pasta_destino)