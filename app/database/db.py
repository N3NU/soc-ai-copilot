import sqlite3

#Move path DB_PATH to config file
DB_PATH = "soc_ai.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
