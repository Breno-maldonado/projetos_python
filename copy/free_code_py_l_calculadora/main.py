print("""
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝\n""")


primeiro_numero = int(input("Digite o primeiro número: \n"))

segundo_numero = int(input("Digite o segundo número: \n"))
print()

def exibirlista():
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print()
print("Digite o número de qual operação você deseja: ")
exibirlista()

operacao = int(input(": "))

soma = primeiro_numero + segundo_numero
subtrair = primeiro_numero - segundo_numero
multiplicar = primeiro_numero * segundo_numero
dividir = primeiro_numero / segundo_numero

if operacao == 1:
    print(f"A soma de {primeiro_numero} + {segundo_numero} é =", soma)
elif operacao == 2:
    print(f"A subtração de {primeiro_numero} - {segundo_numero} é =", subtrair)
elif operacao == 3:
    print(f"A multiplicação de {primeiro_numero} * {segundo_numero} é =", multiplicar)
else:
    print(f"A divisão de {primeiro_numero} / {segundo_numero} é =", dividir)