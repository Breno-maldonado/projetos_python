# 🚚 LogiFast Pipeline: Data Enrichment & Relational Merges (Pandas)

Pipeline de Dados desenvolvido em **Python** e **Pandas** focado em enriquecimento de dados e junção de múltiplas tabelas relacionais (`JOINs` / `Merges`) para análise de custos de frete por região.

---

## 📋 Contexto do Projeto
No ecossistema de Engenharia de Dados, as informações de negócio raramente residem em um único arquivo ou tabela. Sistemas transacionais costumam separar dados de pedidos e tabelas parametrizadas (como tabelas de preços, cadastros de clientes ou fretes).

Este projeto simula a integração entre a **tabela de pedidos de clientes** e a **tabela de tarifas operacionais de frete**, permitindo calcular o custo total de logística distribuído por cidade.

---

## ⚙️ Etapas do Pipeline de Dados

1. **Ingestão de Múltiplas Fontes (Data Ingestion):** 
   * Leitura e conversão de dados relacionais em DataFrames distintos (`df_pedidos` e `df_fretes`).
2. **Enriquecimento de Dados / Cruzamento (Data Enrichment):**
   * Realização de `INNER JOIN` entre as tabelas através do operador `pd.merge()`, utilizando a coluna `cidade` como chave relacional.
3. **Agregação Analítica (Data Aggregation):** 
   * Agrupamento por localização geográfica (`cidade`) e cálculo da soma total de frete acumulado usando `.groupby()` e `.sum()`.

---