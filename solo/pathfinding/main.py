labirinto = [
    ["S",0,1,0],
    [1,0,1,0],
    [0,0,0,"E"]
]

def movimento_valido(linha, coluna):
    if linha < 0 or linha >= len(labirinto):
        return False
    elif coluna < 0 or coluna >= len(labirinto[0]):
        return False  
    elif labirinto[linha][coluna] == 1:
        return False
    else:
        return True

pos_linha = 0
pos_coluna = 0

while labirinto[pos_linha][pos_coluna] != "E":
    for linha in labirinto:
        for celula in linha:
            print(celula, end=' ')
        print()

    nova_linha = pos_linha
    nova_coluna = pos_coluna

    jogador_movimento = input("Escolha um movimento ('cima', 'baixo', 'esquerda', 'direita'): ")

    if jogador_movimento.lower() == 'cima':
        nova_linha -= 1
    elif jogador_movimento.lower() == 'baixo':
        nova_linha += 1
    elif jogador_movimento.lower() == 'esquerda':
        nova_coluna -= 1
    elif jogador_movimento.lower() == 'direita':
        nova_coluna += 1

    if movimento_valido(nova_linha, nova_coluna):
        pos_linha = nova_linha
        pos_coluna = nova_coluna
    else:
        print("Movimento inválido! Tem uma parede ou é o fim do mapa.")

print("Você conseguiu!")