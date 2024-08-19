# Este script tem como função criar o dataset que será utlizado como banco de imagens para a rede YOLOV8 

# Para o funcionamento da biblioteca de imagens do DuckDuckgo, usar o seguinte comando no Prompt de Comando
# pip install DuckDuckGoImages

#encoding: utf-8

# Importação da biblioteca e definindo-a como "ddg"
import DuckDuckGoImages as ddg 

# Definição do filtro de busca e do diretório de destino
#filtro = "lampada"
destino = "C:\\Users\\Bruno\\Desktop\\tcc\\dataset"


print("Iniciando downloads...")
 # Tenta baixar imagens usando DuckDuckGoImages
try:
    
   ddg.download('kittens')
     #ddg.search_and_download(filtro, folder=destino, remove_folder=False, parallel=True)
     # `filtro`: termo de busca para as imagens.
    # `folder`: diretório onde as imagens serão salvas.
    # `remove_folder=False`: não remove a pasta de destino se já existir.
    # `parallel=True`: permite o download paralelo para acelerar o processo.

except Exception as e:
     # Se ocorrer um erro, captura e imprime o tipo de erro
     print("Erro:", str(e))
     # Mensagem indicando que o processo de download terminou
     print("Downloads Concluídos :D")



