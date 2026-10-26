import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_da_pasta = os.path.join(diretorio_atual, 'bagunca')

arquivos_na_pasta = os.listdir(caminho_da_pasta)
print("Arquivos encontrados na pasta:", arquivos_na_pasta)