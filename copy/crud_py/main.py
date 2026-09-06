import sqlite3

def connect_db():
    return sqlite3.connect('estoque.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_product(nome, preco, quantidade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)', 
                   (nome, preco, quantidade))
    conn.commit()
    conn.close()
    print(f"Produto '{nome}' adicionado com sucesso!")

def read_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def update_product(id, novo_preco):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE produtos SET preco = ? WHERE id = ?', (novo_preco, id))
    conn.commit()
    conn.close()
    print(f"Produto ID {id} atualizado.")

def delete_product(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print(f"Produto ID {id} removido.")

# Execução de Teste
if __name__ == "__main__":
    create_table()
    create_product("Teclado Mecânico", 250.00, 10)
    print("Lista de Produtos:", read_products())
    update_product(1, 280.00)
    # delete_product(1)