from app.database.db import get_connection


def create_session(session_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO sessions(session_id)
        VALUES (?)
    """, (session_id,))

    conn.commit()
    conn.close()

def save_message(session_id, role, content):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO messages
        (session_id, role, content)
        VALUES (?, ?, ?)
    """, (session_id, role, content))

    conn.commit()
    conn.close()

def get_chat_history(session_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT role, content
        FROM messages
        WHERE session_id=?
        ORDER BY id
    """, (session_id,))

    rows = cursor.fetchall()

    conn.close()

    history = []

    for row in rows:
        history.append(
            f"{row['role'].capitalize()}: {row['content']}"
        )

    return history

def get_current_topic(session_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT current_topic
        FROM sessions
        WHERE session_id=?
    """, (session_id,))

    row = cursor.fetchone()

    conn.close()

    if row:
        return row["current_topic"]

    return None

def update_current_topic(session_id, topic):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE sessions
        SET current_topic=?
        WHERE session_id=?
    """, (topic, session_id))

    conn.commit()
    conn.close()

