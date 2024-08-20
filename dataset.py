# Este script tem como função adicionar imagens de alta qualidade 
# para a criação do dataset que será utilizado no YOLOV8 

# Para o funcionamento da biblioteca de imagens do bing, usar o seguinte comando no Prompt de Comando
# pip install bing-image-downloader

# encoding: utf-8
# Python ver 3.8.0
# Criado por Bruno Gabriel Mainardes Vieira

from bing_image_downloader import downloader
import os

# Definição dos parâmetros e indicação do diretório do dataset
keyword = 'gun'
output_dir = 'C:/Users/Bruno/Desktop/GuardButton-YOLOV8/dataset/images'
limit = 100  # Numero de imagens a ser baixada

# Criação do diretório de imagens caso o mesmo não exista
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download das imagens e filtros
def safe_download():
    try:
        downloader.download(
            keyword,
            limit=limit,            # Limite de imagens
            output_dir=output_dir,  # Diretório de download
            adult_filter_off=True,  # Usado para evitar conteúdo explícito
            force_replace=False,    
            timeout=60              # Limite tempo de operação
        )
        print(f'Images downloaded to {output_dir}')

        #Depuração Adicionada para erros
    except Exception as e:
        print(f'An error occurred: {e}')

safe_download()
