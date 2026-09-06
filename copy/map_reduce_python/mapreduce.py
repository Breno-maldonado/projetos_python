import json
from functools import reduce

f = open("aquario.json", encoding="utf8")
dados_aquario = json.load(f)
animais = dados_aquario["data"]

def pegar_animal_tipo(animal):
    return animal["type"], 1

def reducer(acc, val):
    if val[0] not in acc.keys():
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = acc[val[0]] + val[1]
    return acc

tipo_animais = list(map(pegar_animal_tipo, animais))
print(tipo_animais)
count_tipo_animais = reduce(reducer, tipo_animais, {})
print(count_tipo_animais)