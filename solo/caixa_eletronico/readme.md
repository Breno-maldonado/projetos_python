# 🏦 Caixa Eletrônico CLI em Python

Um sistema interativo de **Caixa Eletrônico** para linha de comando (CLI) desenvolvido em Python. O projeto simula operações bancárias essenciais, com foco em **programação defensiva**, **isolamento de funções** e **controle de estado**.

---

## 🚀 Funcionalidades

- 💰 **Consultar Saldo:** Exibe o saldo atualizado da conta em tempo real.
- 💵 **Depositar:** Permite realizar depósitos em dinheiro (valores decimais/float).
- 💸 **Sacar:** Permite realizar saques com validação automática de saldo disponível.
- 🛡️ **Programação Defensiva:** O sistema não quebra se o usuário digitar letras, caracteres especiais ou opções inválidas no menu.
- 🔒 **Validação de Regras de Negócio:**
  - Impede saques superiores ao saldo disponível.
  - Impede saques e depósitos de valores nulos ou negativos ($\le 0$).

---

## 🛠️ Conceitos Praticados

Neste projeto foram aplicados conceitos fundamentais da programação:

- **Controle de Estado:** Preservação dos dados da conta durante a execução do loop principal (`while True`).
- **Funções Desacopladas (`def`):** Uso de parâmetros e instruções de retorno (`return`) para manter a independência do código.
- **Tratamento de Exceções (`try / except`):** Captura de `ValueError` para evitar crashes por entradas inválidas.
- **Condicionais Compostas:** Aplicação de operadores lógicos (`if/elif/else`, `or`) para validações.

---

## 💻 Como Executar

### Pré-requisitos
- Ter o **Python 3.x** instalado em sua máquina.

### Passo a passo
1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)