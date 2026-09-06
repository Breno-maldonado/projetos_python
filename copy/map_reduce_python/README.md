# 🐠 MapReduce em Python – Contagem de Animais por Tipo

Este projeto demonstra o conceito de **MapReduce** utilizando **Python puro**, aplicando as funções `map()` e `reduce()` para contar a quantidade de animais por tipo a partir de um arquivo **JSON**.

O objetivo é praticar **programação funcional**, transformação de dados e redução de coleções.

---

## 📁 Estrutura do Projeto

📦 map_reduce
┣ 📜 aquario.json
┣ 📜 mapreduce.py
┗ 📜 README.md

---

## 📄 aquario.json

Arquivo responsável por armazenar os dados do aquário.

### Campos dos objetos:
- **name** → Nome do animal  
- **species** → Espécie  
- **tank number** → Número do tanque  
- **type** → Tipo do animal (fish, shellfish, turtle, etc.)

### Exemplo de estrutura:
```json
{
  "data": [
    {
      "name": "sammy",
      "species": "shark",
      "tank number": 11,
      "type": "fish"
    }
  ]
}
```

## 🐍 mapreduce.py

Script responsável por aplicar o padrão MapReduce para contar os animais por tipo.

# ⚙️ Funcionamento do Código
🔹 Leitura do JSON

Os dados são carregados a partir do arquivo aquario.json utilizando a biblioteca padrão json.

🔹 Fase Map

Cada animal é transformado em uma tupla no formato:

```(tipo_do_animal, 1)```

Função utilizada:
```
def pegar_animal_tipo(animal):
    return animal["type"], 1
```

🔹 Fase Reduce

As tuplas são reduzidas para um dicionário que soma a quantidade de cada tipo.
```
def reducer(acc, val):
    if val[0] not in acc.keys():
        acc[val[0]] = val[1]
    else:
        acc[val[0]] += val[1]
    return acc
```
