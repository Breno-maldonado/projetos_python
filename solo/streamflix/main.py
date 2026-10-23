import pandas as pd

# Tabela 1: Clientes cadastrados
dados_clientes = [
    {'id_cliente': 1, 'nome': 'Alice', 'plano': 'Premium'},
    {'id_cliente': 2, 'nome': 'Bruno', 'plano': 'Basic'},
    {'id_cliente': 3, 'nome': 'Carla', 'plano': 'Premium'},
    {'id_cliente': 4, 'nome': 'Diego', 'plano': 'Basic'}
]

# Tabela 2: Histórico de consumo (Horas assistidas)
dados_consumo = [
    {'id_cliente': 1, 'horas_assistidas': 45.5},
    {'id_cliente': 2, 'horas_assistidas': 12.0},
    {'id_cliente': 3, 'horas_assistidas': 60.0},
    {'id_cliente': 1, 'horas_assistidas': 10.0} # Alice assistiu em outro dispositivo também!
]

df_clientes = pd.DataFrame(dados_clientes)
df_consumo = pd.DataFrame(dados_consumo)

df_tabela = pd.merge(df_clientes, df_consumo, on='id_cliente', how='inner')

df_agg = df_tabela.groupby(['id_cliente', 'nome', 'plano'])['horas_assistidas'].sum().reset_index()

df_ordenado = df_agg.sort_values(by='horas_assistidas', ascending=False)

print(df_ordenado)