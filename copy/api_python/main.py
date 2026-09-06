import requests
import pprint

api_key = "" #coloque sua chave api do site weatherapi

link_api = "http://api.weatherapi.com/v1/current.json"

parametros = {
    "key": api_key,
    "q": "São Paulo",
    "lang": "pt"
}

resposta = requests.get(link_api, params=parametros)

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    pprint.pprint(dados_requisicao)