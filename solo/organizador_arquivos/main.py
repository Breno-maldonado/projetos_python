import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_da_pasta = os.path.join(diretorio_atual, 'bagunca')

arquivos_na_pasta = os.listdir(caminho_da_pasta)

for arquivo in arquivos_na_pasta:
    nome, extensao = os.path.splitext(arquivo)
    print(f'Arquivo encontrado: {nome} | Extensão: {extensao}.')