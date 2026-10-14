import pandas as pd

# 1. Extração dos dados brutos do e-commerce
dados_brutos = [
    {'id': 101, 'tipo': 'Eletrônicos ', 'valor': 1500.0, 'status': 'Concluída'},
    {'id': 102, 'tipo': 'Vestuário', 'valor': None, 'status': 'Concluída'},          # Opa, valor nulo!
    {'id': 103, 'tipo': ' Eletrônicos', 'valor': 800.0, 'status': 'Cancelada'},     # Espaço extra no texto!
    {'id': 104, 'tipo': 'Vestuário', 'valor': 300.0, 'status': None},               # Status nulo!
    {'id': 105, 'tipo': 'Eletrônicos', 'valor': 1200.0, 'status': 'Concluída'}
]

df = pd.DataFrame(dados_brutos)

# 2. Limpeza dos dados
df_limpo = df.copy()

# Remove os espaços extras da coluna tipo
df_limpo['tipo'] = df_limpo['tipo'].str.strip()

# Remove as linhas com valor ou status nulos
df_limpo = df_limpo.dropna(subset=['valor', 'status'])

# Adiciona a coluna com o imposto
df_limpo['valor_com_imposto'] = df_limpo['valor'] * 1.10

# Filtra por apenas as concluídas
vendas_concluidas = df_limpo[df_limpo['status'] == 'Concluída']

# Agrupa pelo tipo e soma os impostos desse tipo
relatorio = vendas_concluidas.groupby('tipo')['valor_com_imposto'].sum()

print("Dados Tratados:")
print(relatorio)