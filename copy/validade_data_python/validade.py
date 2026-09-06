from functions import *

print("########################\n")
print("Qual a data de vencimento?")
print("Formato: DIA-MES-ANO. Exemplo: 01-01-0001\n")
print("########################\n")

bau_data = input("")

if len(bau_data) == 10:
    print(verify_due(bau_data))
else:
    print("Entrada inválida!")