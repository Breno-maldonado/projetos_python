print("""
█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄ █▀█\n""")
print("Operações:\n")

print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

entrada_op = int(input("Qual a operação que você deseja?"))

if entrada_op < 1 or entrada_op > 4:
    print("Opção inválida.")
    exit()

p_num = int(input("Digite o primeiro número: "))
s_num = int(input("Digite o segundo número: "))

if entrada_op == 1:
    print(p_num + s_num)
elif entrada_op == 2:
    print(p_num - s_num)
elif entrada_op == 3:
    print(p_num * s_num)
else: 
    print(p_num / s_num)