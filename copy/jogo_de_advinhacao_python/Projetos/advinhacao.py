import random

print("Bem vindo(a) o jogo de adivinhação!")
numero_teto = input("Digite o número teto do desafio: ")

if numero_teto.isdigit():
    numero_teto = int(numero_teto)
else:
    print("Erro: valor informado não é númerico. Digite novamente!")
    quit()

numero_aleatorio = random.randint(0, numero_teto)

while True:
    tentativa_usuario = input("Advinhe o número: ")

    if tentativa_usuario.isdigit():
        tentativa_usuario = int(tentativa_usuario)
    else:
        print("Erro: valor informado não é númerico. Digite novamente!")
        continue
    
    if tentativa_usuario == numero_aleatorio:
        print("Acertou!")
        break
    elif tentativa_usuario > numero_aleatorio:
        print("O número é menor!")
    else:
        print("O número é maior!")