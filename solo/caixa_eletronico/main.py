saldo = 500.0

while True:
    print('Caixa Eletronico\n',
        '[1] Ver Saldo \n',
        '[2] Depositar \n',
        '[3] Sacar \n',
        '[4] Sair')

    usuario = int(input('Digite o número da sua opção: '))
    print()

    if usuario == 1:
        print(f'Seu saldo é de R$',saldo,'reais','\n')
    elif usuario == 2:
        print("Em construção")
    elif usuario == 3:
        print("Em construção")
    elif usuario == 4:
        break
    else:
        print("Número digitado não correspondido")