# ❌⭕ Tic-Tac-Toe Engine (Jogo da Velha em Python)

Um jogo de terminal interativo em **Python** que aplica manipulação de matrizes bidimensionais, controle de fluxo de turnos em tempo real e verificação de condições de vitória.

---

## 🛠️ Tecnologias e Conceitos Aplicados

* **Python 3**
* **Matrizes 3x3 (Listas Aninhadas):** Mapeamento do tabuleiro através de índices estáticos e dinâmicos `[linha][coluna]`.
* **Funções com Retorno Booleano (`return True / False`):** Módulo desacoplado para verificação de padrões de vitória (horizontais, verticais e diagonais).
* **Game Loop Assíncrono/Alternado (`while True`):** Controle contínuo de turnos entre Jogador X e Jogador O com interrupção por `break`.
* **Indexação Dinâmica com `int()`:** Captura de entrada do usuário mapeada diretamente para as coordenadas da matriz sem redundância de condicionais.

---

## 🎮 Como Funciona o Jogo

O tabuleiro é representado por uma matriz $3 \times 3$ inicializada com hífens `'-'`:

$$\begin{pmatrix}  - & - & - \\  - & - & - \\  - & - & -  \end{pmatrix}$$

### Fluxo da Partida

1. O **Jogador X** escolhe as coordenadas de linha (0 a 2) e coluna (0 a 2).
2. O tabuleiro é atualizado e exibido no terminal.
3. A função `validacao_campo()` é chamada imediatamente para verificar se houve vitória do Jogador X.
4. O **Jogador O** realiza sua jogada.
5. O tabuleiro é atualizado e o sistema valida novamente se houve vitória do Jogador O.
6. A partida é encerrada no momento exato em que uma trinca (linha, coluna ou diagonal) é formada.

---