import os

def titulo():
    print("""
    ░██████╗░██╗░░░██╗██╗███████╗
    ██╔═══██╗██║░░░██║██║╚════██║
    ██║██╗██║██║░░░██║██║░░███╔═╝
    ╚██████╔╝██║░░░██║██║██╔══╝░░
    ░╚═██╔═╝░╚██████╔╝██║███████╗
    ░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝\n""")

titulo()

def primeira_rodada():
    print("1. Atlantico")
    print("2. Indico")
    print("3. Pacífico")
    print("4. Ártico")

def segunda_rodada():
    print("1. 15")
    print("2. 26")
    print("3. 12")
    print("4. 32")

print("Bem vindo(a) ao quiz, aqui você tera um jogo de respostas\n")
print("Rodada 1:\n")

resposta_oceano = 3
resposta_usuario = ""

while resposta_usuario != resposta_oceano:
    print("Qual o maior oceano do mundo❓")
    primeira_rodada()
    resposta_usuario = int(input("Resposta: "))

    if resposta_usuario != resposta_oceano:
        print("Resposta errada, tente novamente.")

    os.system("cls")
    titulo()

print("Parabéns! Você acertou.")

print("Vamos para a proxima rodada?")
proximo = str(input("s/n: "))

if proximo == "n":
    exit()

os.system("cls")

titulo()

print("Rodada 2:\n")

resposta_estados = 2
resposta_usuario = ""

while resposta_usuario != resposta_estados:
    print("Quantos estados tem o Brasil❓")
    segunda_rodada()
    resposta_usuario = int(input("Resposta: "))

    if resposta_usuario != resposta_estados:
        print("Resposta errada, tente novamente.")

print("Parabéns! Você acertou.")