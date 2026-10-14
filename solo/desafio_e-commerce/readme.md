# 🛒 ShopData Pipeline: E-commerce Data Cleaning & Transformation

Pipeline de Dados de ponta a ponta desenvolvido em **Python** e **Pandas** para simular o tratamento, limpeza e agregação de dados transacionais brutos de um e-commerce.

---

## 📋 Contexto do Projeto
No cenário real de Engenharia de Dados, os arquivos brutos extraídos de sistemas legados ou storages (como o AWS S3) frequentemente chegam sujos e corrompidos: com valores nulos, espaços em branco invisíveis e inconsistências de status. 

Este projeto simula a ingestão e o processamento desses dados brutos para entregá-los limpos, estruturados e prontos para consumo da diretoria ou para consultas analíticas (em ferramentas como AWS Athena / Data Warehouses).

---

## ⚙️ Etapas do Pipeline de Dados

1. **Extract (Extração):** Simulação da leitura de dados brutos transacionais contendo imperfeições.
2. **Data Cleaning (Limpeza):** 
   * Criação de cópia de segurança dos dados originais (`df.copy()`).
   * Remoção de espaços extras em strings usando `.str.strip()`.
   * Eliminação de linhas com valores nulos críticos nas colunas de `valor` e `status` com `.dropna()`.
3. **Transformation (Transformação e Engenharia de Recursos):** 
   * Aplicação de cálculo de impostos por meio de operações vetorizadas (`valor_com_imposto`).
   * Filtragem avançada com condições múltiplas (`&`).
4. **Aggregation (Agregação para Negócio):** 
   * Agrupamento por tipo de produto e soma do faturamento utilizando `.groupby()` e `.sum()`.

---