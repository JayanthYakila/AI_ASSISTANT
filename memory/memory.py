from memory.database import get_connection


def remember(key, value):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO memory(key, value)
        VALUES(?, ?)
        """,
        (key, value),
    )

    conn.commit()

    conn.close()


def recall(key):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT value
        FROM memory
        WHERE key=?
        """,
        (key,),
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return None