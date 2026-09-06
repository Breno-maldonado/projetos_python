from datetime import datetime

def today():
    return datetime.now()

def verify_date(date_str):
    try:
        return datetime.strptime(date_str, "%d-%m-%Y")
    except:
        raise Exception("Entrada inválida! Formato sugerido: DIA-MES-ANO. Exemplo: 01-01-0001")

def verify_due(data_ref):
    bau_data = verify_date(data_ref)
    if today() > bau_data:
        return "Data expirou..."
    else:
        return "Data válida..."
