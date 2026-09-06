# 🐍 Jogo da Cobra (Snake Game) em Python

Um clássico jogo da cobra desenvolvido em Python utilizando a biblioteca gráfica **Turtle**. Este projeto foi construído do zero focando em conceitos fundamentais de lógica de programação, controle de eventos e manipulação de estruturas de dados.

---

## 🎮 Como Funciona o Jogo

* **Objetivo:** Controle a cobra para comer a comida vermelha, aumentar sua pontuação e fazer o corpo crescer.
* **Game Over:** Se a cabeça da cobra atingir qualquer uma das 4 paredes, o jogo é reiniciado, os segmentos do corpo são removidos e a pontuação volta a zero.

---

## 🕹️ Controles

Utilize as seguintes teclas do teclado para movimentar a cobra:

* **`W`** : Mover para Cima
* **`S`** : Mover para Baixo
* **`A`** : Mover para a Esquerda
* **`D`** : Mover para a Direita

---

## 🧠 Conceitos e Aprendizados Aplicados

Durante o desenvolvimento deste projeto, foram aplicados diversos conceitos essenciais de programação:

- **Interface Gráfica Nativa:** Uso da biblioteca `turtle` para desenhar elementos visuais, lidar com coordenadas $X$ e $Y$ e animação em tempo real (`tracer` e `update`).
- **Mapeamento de Teclado:** Captura de eventos assíncronos do usuário (`onkeypress`).
- **Estrutura de Dados (Listas):** Gerenciamento dinâmico dos segmentos do corpo da cobra com `append()` e `clear()`.
- **Lógica de Movimentação em Fila:** Algoritmo usando loops regressivos (`range(len-1, 0, -1)`) para fazer cada pedaço do corpo seguir a posição do pedaço anterior.
- **Detecção de Colisão:** Cálculo de distâncias entre objetos e verificação de limites da tela.
- **Placar Dinâmico:** Manipulação e atualização de variáveis de pontuação em tempo real na tela.

---