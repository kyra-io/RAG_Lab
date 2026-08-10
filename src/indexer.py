from database import get_connection

def insert_chunks(chunks: list[dict]):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            for chunk in chunks:
                cursor.execute(
                    """
                    INSERT INTO chunks (
                        source,
                        chunk_id,
                        content,
                        embedding
                    )
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        chunk["source"],
                        chunk["chunk_id"],
                        chunk["content"],
                        chunk["embedding"],
                    ),
                )

        connection.commit()
