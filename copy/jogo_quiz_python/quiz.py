print("Seja bem vindo(a) ao Quiz!")
comecar = input("Quer começar? (s/n) ").lower()

if comecar != "s":
    quit()

print("Começando...")
print("1) Quem descobriu o Brasil?")

resposta = input("Resposta: ").upper()

if resposta == "PEDRO ALVARES CABRAL":
    print("Parabéns, é isso ai!")
else:
    print("Errou! Uma dica: espelhos")
    certeza = input("Quer tentar novamente? (s/n) ").lower()

    if certeza == "s":
        chance = input("1) Quem descobriu o Brasil? ").upper()
        if chance == "DEUS":
            print("Parabéns, agora acertou!")
        else:
            print("Deixa quieto 😅")
    else:
        print("Encerrando o quiz.")
        quit()

segunda_p = input("Pronto para a próxima pergunta? (s/n) ").lower()

if segunda_p != "s":
    print("Então tchau.")
    quit()

print("Próxima pergunta...")
print("2) Quanto é √5 dividido por 2? (aprox)")

resposta_d = float(input("Resposta: "))

if abs(resposta_d - 1.118) < 0.01:
    print("Usou o GPT, não vale!.")
else:
    print("Errado, mas boa tentativa.")
