# ⏲️ Python CLI Countdown Timer

Um cronômetro de contagem regressiva elegante e funcional para o terminal. Este script permite que o usuário defina um tempo em segundos e acompanhe a regressão em uma interface que se atualiza na mesma linha, evitando a poluição visual do console.

## 🚀 Funcionalidades

- **Atualização Dinâmica**: Utiliza o caractere `\r` (Carriage Return) para sobrescrever a linha atual, simulando um display digital.
- **Formatação HH:MM:SS**: Converte automaticamente o total de segundos para o formato padrão de horas, minutos e segundos.
- **Encerramento Seguro**: Implementa um bloco `try-except` para capturar o `KeyboardInterrupt` (CTRL+C), garantindo que o programa feche de forma limpa.
- **Feedback Visual**: Indica claramente o início da contagem e o encerramento do tempo.

## 🛠️ Conceitos Técnicos Aplicados

- **Manipulação de Buffer**: Uso de `flush=True` para garantir que o terminal exiba cada segundo imediatamente.
- **Aritmética de Tempo**:
  - `segundos = i % 60` (Módulo para resto de segundos).
  - `minutos = int(i / 60) % 60` (Divisão inteira para minutos).
  - `horas = int(i / 3600)` (Cálculo de horas totais).
- **Escape Characters**: O uso estratégico de `\r` e `end=""` para controle do cursor no terminal.
