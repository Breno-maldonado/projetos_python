# 🧩 2D Grid Maze Game & Pathfinding Engine

Um jogo de labirinto interativo executado no terminal, desenvolvido em **Python**. O projeto aplica conceitos fundamentais de matrizes bidimensionais, controle de fluxo e algoritmos de validação de movimento e colisão.

---

## 🛠️ Tecnologias e Conceitos Utilizados

* **Python 3**
* **Matrizes Bidimensionais (Listas Aninhadas):** Representação do mapa via coordenadas $(X, Y)$ ou $[linha][coluna]$.
* **Algoritmo de Validação de Fronteiras:** Prevenção de exceções `IndexError` e verificação de colisões antes da atualização de estado.
* **Variáveis Temporárias e Controle de Estado:** Mecanismo de "teste preventivo" de coordenadas antes do commit de movimento.
* **Game Loop Dinâmico (`while`):** Execução contínua orientada a estado de vitória (Exit Condition).

---

## 🎮 Como Funciona o Jogo

O mapa é estruturado a partir de uma matriz $3 \times 4$:

* `S` — Posição Inicial (*Start*)
* `0` — Caminho Livre
* `1` — Parede / Obstáculo (Movimento Bloqueado)
* `E` — Saída / Objetivo (*Exit*)

### Regras de Movimentação

1. O jogador escolhe uma direção: `cima`, `baixo`, `esquerda` ou `direita`.
2. O sistema calcula a **coordenada temporária** (`nova_linha`, `nova_coluna`).
3. A função `movimento_valido()` é acionada para garantir que:
   * A coordenada esteja dentro dos limites da matriz (`0 <= linha < len(labirinto)`).
   * A célula alvo não seja uma parede (`1`).
4. Se a posição for válida, o jogador se move. Caso contrário, o movimento é bloqueado.

---