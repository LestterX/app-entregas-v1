import sqlite3 as sq
from database_controller import get_db_connection


database = get_db_connection()
cursor = database.cursor()
cursor.execute("UPDATE ordens SET pago='tsdfsrue' WHERE id=1")
database.commit()
database.close()