import os

# Pega automaticamente a pasta onde o próprio main.py está salvo
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# 1. Define o caminho completo até a pasta 'bagunca'
caminho_da_pasta = os.path.join(diretorio_atual, 'bagunca')

# 2. Acessa a pasta e lista os arquivos que estão lá dentro
arquivos_na_pasta = os.listdir(caminho_da_pasta)
print("Arquivos encontrados na pasta:", arquivos_na_pasta)

# 3. Monta o caminho exato até o arquivo e abre para ler o conteúdo
caminho_do_arquivo = os.path.join(caminho_da_pasta, 'arquivo.txt')

with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print("\n--- Conteúdo do arquivo.txt ---")
    print(texto)