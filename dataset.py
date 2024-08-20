# Este script tem como função criar o dataset que será utlizado como banco de imagens para a rede YOLOV8 

# A API utilizada é da Unsplash, uma vez que a biblioteca DuckDuckGoImages parece apresentar mal funcionamento em versões mais recentes do Python ,
# para usar o script, digitar o seguinte comando no Prompt de Comando
# pip install requests
# Feito por Bruno Gabriel Mainardes Vieira, estudante de Análise e Desenvolvimento de Sistemas ,

import requests
import os
from urllib.parse import urlparse

# Unsplash API key
# Registre-se em https://unsplash.com, pegue sua API key e insira ela aqui
access_key = " " 

# Definindo o filtro de busca e o diretório de destino
filtro = 'gun'
destino = 'C:\\Users\\Bruno\\Desktop\\GuardButton alpha0.0.1\\dataset'

# Criar o diretório de destino se não existir
if not os.path.exists(destino):
    os.makedirs(destino)

# Filtro e download das imagens
def download_image(url, folder, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder, file_name), 'wb') as file:
            file.write(response.content)
    else:
        print(f"Falha ao baixar a imagem: {url}")

print("Iniciando downloads...")

try:
    # URL da API de busca de imagens do Unsplash
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": filtro,
        "per_page": 10,  # Editar este parâmetro para que o número de imagens seja maior
        "client_id": access_key
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    # Baixar imagens
    for i, image in enumerate(data['results']):
        image_url = image['urls']['regular']
        file_name = f"image_{i+1}.jpg"
        download_image(image_url, destino, file_name)

except Exception as e:
    # Depuração
    print("Erro:", str(e))

print('Downloads Concluídos :D')
