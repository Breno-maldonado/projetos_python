import os

print("""
██╗░░░░░██╗░██████╗████████╗░█████╗░░██████╗
██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝
██║░░░░░██║╚█████╗░░░░██║░░░███████║╚█████╗░
██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║░╚═══██╗
███████╗██║██████╔╝░░░██║░░░██║░░██║██████╔╝
╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░\n""")

def menu():
    print("1. Preencher lista")
    print("2. Mostrar lista")

def apagar():
    os.system("cls")

lista = str([])
entrada_lista = ""

while True:
    print("---------- Lista ----------\n")
    menu()

    entrada_opcao = int(input("\nDigite o número da sua opção: "))

    apagar()

    if entrada_opcao == 1:
        entrada_lista = input("Digite oque você quer listar: ")
        lista = str([entrada_lista])
        apagar()
        print("Informação armazenada com sucesso!\n")
    else:
        print(lista)
        input("\nPressione Enter para voltar ao menu...")
        apagar()
