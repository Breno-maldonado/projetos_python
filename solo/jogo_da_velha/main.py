tabuleiro = [ 
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def validacao_campo(linha, coluna): 
    if tabuleiro[0][0] == 'X' and tabuleiro[1][1] == 'X'  and tabuleiro[2][2] == 'X':
        print(f'O jogador X venceu!')
        return True
    elif tabuleiro[0][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][2] == 'O':
        print(f'O jogador O venceu!')
        return True

    elif tabuleiro[0][2] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][0] == 'X':
        print(f'O jogador X venceu!')
        return True
    elif tabuleiro[0][2] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][0] == 'O':
        print(f'O jogador O venceu!')
        return True

    elif tabuleiro[0][0] == 'X' and tabuleiro[0][1] == 'X' and tabuleiro[0][2] == 'X':
        print(f'O jogador X venceu!')
        return True
    elif tabuleiro[0][0] == 'O' and tabuleiro[0][1] == 'O' and tabuleiro[0][2] == 'O':
        print(f'O jogador O venceu!')
        return True

    elif tabuleiro[1][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[1][2] == 'X':
        print(f'O jogador X venceu!')
        return True
    elif tabuleiro[1][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[1][2] == 'O':
        print(f'O jogador O venceu!')
        return True

    elif tabuleiro[2][0] == 'X' and tabuleiro[2][1] == 'X' and tabuleiro[2][2] == 'X':
        print(f'O jogador X venceu!')
        return True
    elif tabuleiro[2][0] == 'O' and tabuleiro[2][1] == 'O' and tabuleiro[2][2] == 'O':
        print(f'O jogador O venceu!')
        return True

    elif tabuleiro[0][0] == 'X' and tabuleiro[1][0] == 'X' and tabuleiro[2][0] == 'X':
        print(f'O jogador X venceu!')
        return True
    elif tabuleiro[0][0] == 'O' and tabuleiro[1][0] == 'O' and tabuleiro[2][0] == 'O':
        print(f'O jogador O venceu!')
        return True

    elif tabuleiro[0][1] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][1] == 'X':
        print(f'O jogador X venceu!')
        return True
    elif tabuleiro[0][1] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][1] == 'O':
        print(f'O jogador O venceu!')
        return True

    elif tabuleiro[0][2] == 'X' and tabuleiro[1][2] == 'X' and tabuleiro[2][2] == 'X':
        print(f'O jogador X venceu!')
        return True
    elif tabuleiro[0][2] == 'O' and tabuleiro[1][2] == 'O' and tabuleiro[2][2] == 'O':
        print(f'O jogador O venceu!')
        return True
    return False

while True: 
    for linha in tabuleiro: 
        for coluna in linha: 
            print(coluna, end=' ')
        print()

    linha = int(input("Jogador X escolha a linha (0, 1, 2): "))
    coluna = int(input("Jogador X escolha a coluna (0, 1, 2): "))

    tabuleiro[linha][coluna] = 'X'

    if validacao_campo(linha, coluna):
        print("Fim de jogo!")
        break

    for linha in tabuleiro:
        for coluna in linha: 
            print(coluna, end=' ')
        print()

    print()

    linha = int(input("Jogador O escolha a linha (0, 1, 2): "))
    coluna = int(input("Jogador O escolha a coluna (0, 1, 2): "))

    tabuleiro[linha][coluna] = 'O'

    if validacao_campo(linha, coluna):
        print("Fim de jogo!")
        break