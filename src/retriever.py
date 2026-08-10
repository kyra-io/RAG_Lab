from database import get_connection

def search_chunks(
    query_embedding: list[float],
    limit: int = 5,
) -> list[dict]:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    id,
                    source,
                    chunk_id,
                    content,
                    distance
                FROM search_chunks(%s::vector, %s)
                """,
                (query_embedding, limit),
            )

            rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "source": row[1],
            "chunk_id": row[2],
            "content": row[3],
            "distance": row[4],
        }
        for row in rows
    ]
