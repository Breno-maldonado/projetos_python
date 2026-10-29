import os
import shutil

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_da_pasta = os.path.join(diretorio_atual, 'bagunca')

pasta_destino_img = os.path.join(caminho_da_pasta, 'Imagens')
os.makedirs(pasta_destino_img, exist_ok=True)

pasta_destino_doc = os.path.join(caminho_da_pasta, 'Documentos')
os.makedirs(pasta_destino_doc, exist_ok=True)

arquivos_na_pasta = os.listdir(caminho_da_pasta)

for arquivo in arquivos_na_pasta:
    nome, extensao = os.path.splitext(arquivo)
    print(f'Processando: {nome} | Extensão: {extensao}.')

    caminho_origem = os.path.join(caminho_da_pasta, arquivo)

    if extensao == '.png' or extensao == '.jpg':
        caminho_destino = os.path.join(pasta_destino_img, arquivo)
        shutil.move(caminho_origem, caminho_destino)
        print(f'-> Movido para Imagens!')
    elif extensao == '.txt':
        caminho_destino = os.path.join(pasta_destino_doc, arquivo)
        shutil.move(caminho_origem, caminho_destino)
        print(f'-> Movido para Documentos!')