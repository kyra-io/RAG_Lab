import json

from database import get_connection

def insert_chunks(chunks: list[dict]):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT insert_chunks(%s::jsonb)
                """,
                (json.dumps(chunks),),
            )

            row = cursor.fetchone()
            if row is None:
                raise RuntimeError(
                    "insert_chunks() did not return a result"
                )
            inserted = row[0]

        connection.commit()

    return inserted
