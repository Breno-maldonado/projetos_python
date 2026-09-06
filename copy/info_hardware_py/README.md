# 📊 Hardware Performance Monitor

Este é um utilitário em Python desenvolvido para monitorar e registrar a telemetria de hardware (CPU, RAM e GPU) em tempo real. O script é ideal para identificar gargalos de performance (bottlenecks) durante sessões de jogos ou processamento de cargas de trabalho pesadas.

## 🚀 Funcionalidades

- **Monitoramento de CPU:** Captura a carga total de processamento.
- **Métricas de RAM:** Acompanha o consumo de memória do sistema em GB.
- **Telemetria de GPU (NVIDIA):** Utiliza a API oficial da NVIDIA para monitorar o uso do núcleo e o consumo de VRAM.
- **Exportação de Dados:** Salva automaticamente todos os logs em um arquivo `.csv` para análise posterior.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **psutil:** Para coleta de dados do processador e memória RAM.
- **pynvml:** Interface Python para o NVIDIA Management Library.
- **CSV:** Para persistência de dados estruturados.
