from dataclasses import dataclass
import sqlite3 as sq

# ----- LINUX (upjetservidor) -----
# DATABASE_PATH = '/home/upjetservidor/Área de Trabalho/AppEntregas/app/static/database/database.db'
# DATABASE_SCHEMA = '/home/upjetservidor/Área de Trabalho/AppEntregas/app/static/database/schema.sql'

# ----- WINDOWS -----
DATABASE_PATH = 'app/static/database/database.db'
DATABASE_SCHEMA = 'app/static/database/schema.sql'

def get_db_connection():
    database = sq.connect(DATABASE_PATH)
    database.row_factory = sq.Row
    return database

def create_database():
    connection = get_db_connection()
    with open(DATABASE_SCHEMA) as f:
        connection.executescript(f.read())
    cursor = connection.cursor()
    connection.commit()
    connection.close()

def add_onDatabase(nome_cliente, endereco, telefone, valor, forma_pagamento, pago, entregue, descricao, coletado):
    database = get_db_connection()
    cursor = database.cursor()
    cursor.execute("INSERT INTO ordens (cliente, endereco, telefone, valor, forma_pagamento, pago, entregue, descricao, coletado) VALUES ('"+nome_cliente+"', '"+endereco+"', '"+telefone+"', '"+valor+"', '"+forma_pagamento+"', '"+pago+"', '"+entregue+"', '"+descricao+"', '"+coletado+"')")
    database.commit()
    database.close()

def update_onDatabase(id, nome_cliente, endereco_cliente, telefone_cliente, valor_servico, forma_de_pagamento, descricao_servico, pagamento_feito, entrega_feita, coleta_feita):
    database = get_db_connection()
    cursor = database.cursor()
    cursor.execute("UPDATE ordens SET cliente='"+nome_cliente+"' WHERE id='"+id+"'")
    cursor.execute("UPDATE ordens SET endereco='"+endereco_cliente+"' WHERE id='"+id+"'")
    cursor.execute("UPDATE ordens SET telefone='"+telefone_cliente+"' WHERE id='"+id+"'")
    cursor.execute("UPDATE ordens SET valor='"+valor_servico+"' WHERE id='"+id+"'")
    cursor.execute("UPDATE ordens SET forma_pagamento='"+forma_de_pagamento+"' WHERE id='"+id+"'")
    cursor.execute("UPDATE ordens SET descricao='"+descricao_servico+"' WHERE id='"+id+"'")
    cursor.execute("UPDATE ordens SET pago='"+pagamento_feito+"' WHERE id='"+id+"'")
    cursor.execute("UPDATE ordens SET entregue='"+entrega_feita+"' WHERE id='"+id+"'")
    cursor.execute("UPDATE ordens SET coletado='"+coleta_feita+"' WHERE id='"+id+"'")
    database.commit()
    database.close()

def remove_fromDatabase(id):
    database = get_db_connection()
    cursor = database.cursor()
    cursor.execute("DELETE FROM ordens WHERE id='"+id+"'")
    database.commit()
    database.close()