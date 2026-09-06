# 📅 Validador de Data de Vencimento (Python)

Este projeto é um **validador simples de datas de vencimento** feito em Python.  
Ele recebe uma data informada pelo usuário e verifica se essa data **já expirou ou ainda é válida**, comparando com a data atual do sistema.

---

## 📂 Estrutura do Projeto

/
├── validade.py
└── functions.py

## 📄 Descrição dos Arquivos

validade.py
Arquivo principal, responsável pela interação com o usuário.

functions.py
Contém as funções de validação e comparação de datas.

## ⚙️ Como Funciona

O programa solicita ao usuário uma data de vencimento.

A data deve ser informada no formato:
DIA-MES-ANO
Exemplo: 01-01-2025

## O sistema:

Valida se o formato está correto

Converte a data para o tipo datetime

Compara com a data atual

## Retorna uma mensagem informando se:

✅ A data ainda é válida

❌ A data já expirou
