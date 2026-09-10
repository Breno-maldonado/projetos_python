saldo = 500.0

def depositar(saldo_atual):
    print("Digite o valor de deposito: ")
    deposito = float(input("R$ "))
    if deposito <= 0:
        print("Valor invalido!")
    else:
        saldo_atual += deposito
        print()
        print(f'Valor de R$ {deposito} reais, depositado com sucesso!','\n')
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
        print("Em construção")
    elif usuario == 4:
        break
    else:
        print("Número digitado não correspondido")