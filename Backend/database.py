import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "ai_chat_project")
    )


def create_conversation(title: str = "New chat") -> int:
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO conversations (title)
        VALUES (%s)
    """

    cursor.execute(query, (title,))
    connection.commit()

    conversation_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return conversation_id


def conversation_exists(conversation_id: int) -> bool:
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT id
        FROM conversations
        WHERE id = %s
    """

    cursor.execute(query, (conversation_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result is not None


def save_message(conversation_id: int, role: str, content: str) -> int:
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO messages (conversation_id, role, content)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (conversation_id, role, content))
    connection.commit()

    message_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return message_id


def get_conversation_messages(conversation_id: int):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT id, conversation_id, role, content, created_at
        FROM messages
        WHERE conversation_id = %s
        ORDER BY id ASC
    """

    cursor.execute(query, (conversation_id,))
    messages = cursor.fetchall()

    cursor.close()
    connection.close()

    return messages


def get_all_conversations():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT id, title, created_at
        FROM conversations
        ORDER BY id DESC
    """

    cursor.execute(query)
    conversations = cursor.fetchall()

    cursor.close()
    connection.close()

    return conversations