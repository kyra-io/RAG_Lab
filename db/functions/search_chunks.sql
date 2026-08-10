CREATE OR REPLACE FUNCTION search_chunks(
    p_embedding VECTOR(384),
    p_limit INTEGER DEFAULT 5
)
RETURNS TABLE (
    id BIGINT,
    source TEXT,
    chunk_id INTEGER,
    content TEXT,
    distance REAL
)
LANGUAGE SQL
AS $$
    SELECT
        c.id,
        c.source,
        c.chunk_id,
        c.content,
        c.embedding <=> p_embedding AS distance
    FROM chunks c
    ORDER BY c.embedding <=> p_embedding
    LIMIT p_limit;
$$;
