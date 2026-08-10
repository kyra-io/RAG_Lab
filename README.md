# Kyra IO Labs - RAG

## Create postgreSQL docker database
``` bash
docker compose up -d
```

## Enter docker database
``` bash
docker exec -it rag-postgres psql -U rag -d rag
```

## Create tables
* Execute, by order, steps in ``` bash /db/steps/```
