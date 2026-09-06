import random

pontos_usuario = 0
pontos_pc = 0

opcoes = ["R", "T", "P"]

while True:
    opcao_usuario = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").upper()

    if opcao_usuario == "Q":
        break

    opcao_pc = random.randint(0, 2)
    # 0 : R, 1 : T, 2 : P
    escolha_pc = opcoes[opcao_pc]

    print("O computador escolher " + escolha_pc)

    if opcao_usuario == escolha_pc:
        print("Empate!")
    elif opcao_usuario == "R" and escolha_pc == "T":
        print("Você perdeu!")
        pontos_pc = pontos_pc + 1
    elif opcao_usuario == "R" and escolha_pc == "P":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1
    elif opcao_usuario == "T" and escolha_pc == "R":
        print("Você perdeu!")
        pontos_pc = pontos_pc + 1
    elif opcao_usuario == "T" and escolha_pc == "P":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1
    elif opcao_usuario == "P" and escolha_pc == "R":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1
    else:
        print("Você perdeu!")
        pontos_pc = pontos_pc + 1

print(f"Sua pontuação: {pontos_usuario}")
print(f"Pontuação do computador: {pontos_pc}")

if pontos_pc > pontos_usuario:
    print("Você perdeu pra um computador kkkk")
elif pontos_pc == pontos_usuario:
    print("Empate!")
else:
    print("Você ganhou!")

print("Tchau!")