CREATE OR REPLACE FUNCTION insert_chunks(
    p_chunks JSONB
)
RETURNS INTEGER
LANGUAGE SQL
AS $$
    INSERT INTO chunks (
        source,
        chunk_id,
        content,
        embedding
    )
    SELECT
        item->>'source',
        (item->>'chunk_id')::INTEGER,
        item->>'content',
        (item->>'embedding')::VECTOR(384)
    FROM jsonb_array_elements(p_chunks) AS item;

    SELECT jsonb_array_length(p_chunks);
$$;
