# 🕒 Relógio Digital CLI

Um script simples e eficiente que transforma o seu terminal em um relógio digital dinâmico. Este projeto foi desenvolvido para praticar a manipulação de bibliotecas nativas do Python e o gerenciamento de processos contínuos.

## ✨ Funcionalidades

- **Atualização em Tempo Real**: O relógio atualiza os segundos instantaneamente sem "sujar" o histórico do terminal, utilizando o caractere de escape `\r`.
- **Formatação de Horas**: Exibição no formato de 12 horas (AM/PM).
- **Encerramento Seguro**: Implementação de tratamento de erro para capturar o comando `CTRL + C`, permitindo que o programa pare sem exibir mensagens de erro genéricas do sistema.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem base.
- **Biblioteca `time`**: Para captura do tempo do sistema e controle do intervalo de atualização (`sleep`).
- **Tratamento de Exceções (`try/except`)**: Utilizado especificamente para lidar com o `KeyboardInterrupt`.
