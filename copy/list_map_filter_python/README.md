# 🐠 Gerenciamento de Aquário em Python

Este projeto demonstra como manipular dados em **Python** utilizando arquivos **JSON**, aplicando funções como `filter`, `map` e funções personalizadas para gerenciar informações de animais em um aquário.

O sistema realiza:
- Leitura de dados a partir de um arquivo JSON
- Filtragem de animais do tipo **peixe**
- Extração dos nomes desses peixes
- Atualização do número do tanque de animais selecionados

---

## 📁 Estrutura do Projeto

📦 projeto-aquario
┣ 📜 aquario.json
┣ 📜 gerencia_aquario.py
┗ 📜 README.md


---

## 📄 aquario.json

Arquivo responsável por armazenar os dados do aquário.

### Campos utilizados:
- **name**: nome do animal  
- **species**: espécie  
- **tank number**: número do tanque  
- **type**: tipo do animal (fish, shellfish, turtle, etc.)

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
```

## 🐍 gerencia_aquario.py

Script principal responsável por processar e manipular os dados do aquário.
