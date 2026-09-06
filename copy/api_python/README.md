# 🌦️ Weather API - Consulta de Clima com Python
Este é um script simples em Python que consome a WeatherAPI para obter dados meteorológicos em tempo real de uma localização específica. O script utiliza a biblioteca requests para chamadas HTTP e a pprint para exibir os dados de forma organizada no terminal.

## 🚀 Funcionalidades
Consulta dados climáticos atuais (temperatura, condição, umidade, etc.).

Suporte para localização personalizada (padrão: São Paulo).

Resposta em formato JSON traduzida para o português.

## 🛠️ Tecnologias Utilizadas
Python 3.x

Biblioteca Requests: Para lidar com as requisições à API.

WeatherAPI: Provedora dos dados climáticos.

## 📋 Pré-requisitos
Antes de começar, você precisará ter o Python instalado em sua máquina e uma chave de API válida.

1. Crie uma conta gratuita em weatherapi.com.

2. Copie sua API Key no painel de controle.

3. Instale a biblioteca requests caso ainda não a tenha:

``` pip install requests ```

## 🔧 Configuração e Uso

1. Configure sua chave: Abra o arquivo main.py e insira sua chave na variável api_key:

``` api_key = "SUA_CHAVE_AQUI" ```

2. Execute o script:

``` python main.py ```
