# 🛒 Simulador de Gerenciamento de Estoque e Mercado em Python

Este projeto é um simulador de terminal interativo para gerenciamento de estoque e compras em um supermercado. Foi desenvolvido em Python puro como parte do meu aprendizado em lógica de programação e estruturas de dados.

O sistema permite que o usuário navegue por um menu, consulte produtos no estoque, verifique disponibilidade de quantidades, adicione itens ao carrinho e navegue de forma contínua até encerrar a sessão.

---

## 🚀 Funcionalidades

- **Consulta Dinâmica de Estoque:** Busca por produtos utilizando verificação de chaves em dicionários.
- **Tratamento de Entradas:** Uso de manipulação de strings (`.lower()`) para aceitar digitações em maiúsculas ou minúsculas sem quebrar o sistema.
- **Validação de Regras de Negócio:**
  - Checagem se o produto existe no catálogo.
  - Verificação de estoque disponível (impede a compra de itens esgotados e impede estoque negativo).
- **Carrinho de Compras:** Adição de itens dinamicamente utilizando listas.
- **Visualização de Carrinho:** Listagem organizada dos itens selecionados pelo cliente usando loops de repetição (`for`).
- **Menu Interativo Contínuo:** Estruturação em loop `while` com tratamento de opções e encerramento com `break`.

---

## 🧠 Conceitos e Estruturas de Python Utilizados

- **Dicionários Aninhados (`dict`):** Armazenamento de produtos com múltiplos atributos (preço e quantidade).
- **Listas (`list`):** Armazenamento dinâmico dos itens selecionados no carrinho (`.append()`).
- **Estruturas Condicionais (`if`, `elif`, `else`):** Controle de fluxo e validação de regras do mercado.
- **Estruturas de Repetição (`while` e `for`):** Criação do menu contínuo e iteração sobre coleções.
- **Operador `in`:** Busca performática e direta de chaves dentro de dicionários.
- **Formatação de Strings (f-strings):** Apresentação limpa de dados e valores monetários.

---