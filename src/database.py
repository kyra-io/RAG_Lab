import psycopg

def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="rag",
        user="rag",
        password="rag",
    )
