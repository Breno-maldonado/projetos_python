labirinto = [
    ["S",0,1,0],
    [1,0,1,0],
    [0,0,0,"E"]
]

for linha in labirinto:
    for celula in linha:
        print(celula, end=' ')
    print()