import sqlite3

DATABASE = "assistant.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def create_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            key TEXT UNIQUE,

            value TEXT

        )
    """)

    conn.commit()

    conn.close()