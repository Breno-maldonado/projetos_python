saldo = 500.0

def depositar(saldo_atual):

    print("Digite o valor de deposito: ")

    try:
        deposito = float(input("R$ "))
    except ValueError:
        print()
        print("Opção inválida! Por favor, digite apenas números!\n")
        return saldo_atual
    
    if deposito <= 0:
        print("Valor invalido!")
    else:
        saldo_atual += deposito
        print()
        print(f'Valor de R$ {deposito} reais, depositado com sucesso!','\n')
    return saldo_atual

def sacar(saldo_atual):

    print("Qual o valor do saque?")

    try:
        saque = float(input("R$ "))
    except ValueError:
        print()
        print("Opção inválida! Por favor, digite apenas números!\n")
        return saldo_atual

    if saque <= 0 or saque > saldo_atual:
        print("\nValor inválido ou saldo insuficiente!")
    else:
        saldo_atual = saldo_atual - saque
        print()
        print(f"Valor de R$ {saque} reais, sacado com sucesso!", '\n')
        
    return saldo_atual

while True:
    print('Caixa Eletronico\n',
        '[1] Ver Saldo \n',
        '[2] Depositar \n',
        '[3] Sacar \n',
        '[4] Sair')
    
    try:
        usuario = int(input('Digite o número da sua opção: '))
    except ValueError:
        print("Opção inválida! Por favor, digite apenas números inteiros.\n")
        continue

    print()

    if usuario == 1:
        print(f'Seu saldo é de R$',saldo,'reais','\n')
    elif usuario == 2:
       saldo = depositar(saldo)
    elif usuario == 3:
        saldo = sacar(saldo)
    elif usuario == 4:
        break
    else:
        print("Número digitado não correspondido")