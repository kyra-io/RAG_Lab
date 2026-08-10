# Kyra IO Labs - RAG

A small RAG (Retrieval-Augmented Generation) lab / experimentation project.

It loads Markdown documents, splits them into chunks, embeds them with a local
sentence-transformers model, stores the vectors in PostgreSQL (pgvector), and
answers questions by retrieving the most relevant chunks and feeding them to an
LLM served through OpenRouter.

## Pipeline

```
Markdown docs          All-MiniLM-L6-v2        pgvector (PostgreSQL 16)
    |                        |                        |
loader.py -> chunker.py -> embedder.py -> indexer.py -> search_chunks()
                                                          |
                      question -> query embedding ----+
                                                          |
                                      retriever.py -> prompt.py -> llm.py
```

| Step    | Module          | What it does |
|---------|-----------------|--------------|
| Load    | `src/loader.py` | Reads all `*.md` files from `data/documents/` |
| Chunk   | `src/chunker.py`| Splits text into chunks of 100 words |
| Embed   | `src/embedder.py` | Encodes chunks with `sentence-transformers/all-MiniLM-L6-v2` (384 dims) |
| Index   | `src/indexer.py`| Inserts chunks as JSONB via the `insert_chunks()` DB function |
| Retrieve| `src/retriever.py` | Runs cosine-similarity search via the `search_chunks()` DB function |
| Prompt  | `src/prompt.py` | Builds the context block and the final prompt |
| Answer  | `src/llm.py`   | Calls an OpenRouter model (`openrouter/free`) |

## Requirements

- Python >= 3.12
- Docker (for the database)

> Note: `pyproject.toml` does not list the project dependencies yet. Install
> them manually:

``` bash
pip install sentence-transformers psycopg[binary] openai
```

The LLM step requires an API key for OpenRouter:

``` bash
export OPENROUTER_API_KEY=your_key_here
```

## Setup

### 1. Start the PostgreSQL database

``` bash
docker compose up -d
```

This starts a `pgvector/pgvector:pg16` container (`rag-postgres`) on port 5432.

### 2. Create the tables

Execute the SQL files in `db/steps/` in order:

``` bash
# 000_create_vector_extensions.sql
# 001_create_table_chunks.sql
```

### 3. Create the functions

Execute the SQL files in `db/functions/`:

- `insert_chunk.sql` — `insert_chunks(p_chunks JSONB)`, inserts chunks with their vector embedding
- `search_chunks.sql` — `search_chunks(p_embedding VECTOR(384), p_limit INTEGER)`, returns the closest chunks ordered by distance

Example, dropping into the container shell:

``` bash
docker exec -it rag-postgres psql -U rag -d rag
```

## Usage

Run the full flow (embedding + retrieval + prompt + LLM answer):

``` bash
python src/main.py
```

Run only retrieval and prompt building (no LLM call):

``` bash
python src/_main.py
```

## Repository structure

```
data/documents/   Markdown source documents
db/functions/     SQL functions (insert_chunks, search_chunks)
db/steps/         SQL migration steps (vector extension, chunks table)
src/main.py       Full RAG flow (embed -> retrieve -> prompt -> LLM)
src/_main.py      Retrieval + prompt only (no LLM)
src/loader.py     Document loading
src/chunker.py    Text chunking (100-word chunks)
src/embedder.py   Local embeddings (all-MiniLM-L6-v2, 384 dims)
src/indexer.py    Inserts chunks into PostgreSQL
src/retriever.py  Vector similarity search
src/prompt.py     Context + prompt construction
src/llm.py        LLM call via OpenRouter
```

## Status / limitations (lab notes)

- Chunking is a naive word split (fixed 100-word chunks, no overlap).
- The embedding model is fixed (`all-MiniLM-L6-v2`) and the DB column
  `chunks.embedding` is `VECTOR(384)` and must match the model's output size.
- There is no end-to-end indexing script yet: `insert_chunks()` expects a JSON
  array that includes the `embedding` field, but the current `indexer.py` /
  `main.py` don't wire the `Embedder` output into it (the DB must be populated
  some other way for retrieval to return results).
- `main.py` executes the pipeline sequentially and prints each intermediate
  stage; it is a lab script, not an application.