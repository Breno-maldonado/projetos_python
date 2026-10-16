import pandas as pd

# Tabela 1: Pedidos dos clientes
dados_pedidos = [
    {'id_pedido': 1, 'cliente': 'Ana', 'cidade': 'São Paulo'},
    {'id_pedido': 2, 'cliente': 'Carlos', 'cidade': 'Rio de Janeiro'},
    {'id_pedido': 3, 'cliente': 'Beatriz', 'cidade': 'São Paulo'},
    {'id_pedido': 4, 'cliente': 'Daniel', 'cidade': 'Curitiba'}
]

# Tabela 2: Tabela de Fretes (Custo por cidade)
dados_fretes = [
    {'cidade': 'São Paulo', 'custo_frete': 25.0},
    {'cidade': 'Rio de Janeiro', 'custo_frete': 40.0},
    {'cidade': 'Curitiba', 'custo_frete': 30.0}
]

df_pedidos = pd.DataFrame(dados_pedidos)
df_fretes = pd.DataFrame(dados_fretes)

df_unificado = pd.merge(df_pedidos, df_fretes, on='cidade', how='inner')

print(df_unificado)