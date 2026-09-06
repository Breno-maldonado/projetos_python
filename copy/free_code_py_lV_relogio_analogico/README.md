# 🕒 Relógio Analógico Python (Tkinter + Math)

Este projeto é uma implementação de um relógio analógico funcional que utiliza a interface gráfica nativa do Python para renderizar tempo real de forma visual.

## 🚀 Destaques Técnicos

O projeto vai além de um simples script, abordando conceitos fundamentais de engenharia de software e computação gráfica:

- **Matemática Avançada**: Uso de funções trigonométricas ($\sin$ e $\cos$) para converter o tempo (segundos, minutos e horas) em coordenadas cartesianas ($x, y$) no Canvas.
- **Programação Orientada a Objetos (POO)**: O código é estruturado em uma classe (`relogio`), facilitando a organização de estados e métodos de desenho.
- **Renderização Dinâmica**: Implementação de um loop de atualização assíncrono com `root.after()`, permitindo que a interface seja redesenhada a cada segundo sem travar a execução do sistema.
- **Interface Gráfica (GUI)**: Uso do componente `Canvas` do Tkinter para desenho vetorial de formas geométricas.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter**: Para a construção da interface e desenhos.
- **Math**: Para conversão de graus em radianos e cálculos de posicionamento.
- **Time**: Para sincronização com o relógio do sistema operacional.

## 📐 Como funciona a lógica?

Para cada segundo que passa, o script realiza os seguintes passos:
1. Limpa o desenho anterior.
2. Obtém a hora atual do sistema.
3. Calcula o ângulo de cada ponteiro ($360^\circ / 60$ unidades).
4. Aplica a fórmula:
   - $x = \text{centro}_x + \text{raio} \times \sin(\text{angulo})$
   - $y = \text{centro}_y - \text{raio} \times \cos(\text{angulo})$
5. Desenha as novas linhas no Canvas.
