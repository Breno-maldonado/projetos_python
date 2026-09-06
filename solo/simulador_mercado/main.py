estoque = {
    'macarrao': {"preco": 5.00, "quantidade": 0},
    'arroz': {"preco": 6.00, "quantidade": 6},
    'feijao': {"preco": 3.00, "quantidade": 12}
}

carrinho = []

while True:
    print("\n---------------------------")
    cliente_opcao = input("Escolha uma das opções:\n(1) Comprar Produto\n(2) Ver Carrinho\n(3) Sair e Pagar\nDigite a opção: ")

    if cliente_opcao == "1":
        cliente_estoque = input("\nDigite o nome do produto: ")
        produto_digitado = cliente_estoque.lower()

        if produto_digitado not in estoque:
            print("Desculpe, não temos esse produto no mercado.")

        elif estoque[produto_digitado]['quantidade'] == 0:
            print(f"O produto {produto_digitado} está esgotado!")

        else:
            preco = estoque[produto_digitado]['preco']
            qtd = estoque[produto_digitado]['quantidade']
            
            print(f"Produto encontrado! O valor do {produto_digitado} é R$ {preco:.2f} e temos {qtd} unidades.")
            
            compra = input(f"Quer levar o {produto_digitado}? (sim/nao): ")
            
            if compra.lower() == 'sim':
                estoque[produto_digitado]['quantidade'] -= 1
                carrinho.append(produto_digitado)
                print(f"-> {produto_digitado} adicionado ao carrinho com sucesso!")
            else:
                print("Produto não adicionado.")

    elif cliente_opcao == "2":
        print("\n--- ITENS NO SEU CARRINHO ---")
        if len(carrinho) == 0:
            print("Seu carrinho está vazio!")
        else:
            for item in carrinho:
                print(f"- {item}")

    elif cliente_opcao == "3":
        print("\nSaindo do sistema e indo para o caixa...")
        break

    else:
        print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.")