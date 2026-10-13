# API de Veículos — FastAPI + MongoDB

CRUD de veículos usando FastAPI e PyMongo.

## Como rodar

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

Requer MongoDB rodando em `mongodb://localhost:27017`.

## Endpoints

| Método | Rota           | Descrição     | Sucesso |
|--------|----------------|---------------|---------|
| POST   | /veiculos      | Criar         | 201     |
| GET    | /veiculos      | Listar todos  | 200     |
| GET    | /veiculos/{id} | Buscar por ID | 200     |
| PUT    | /veiculos/{id} | Atualizar     | 200     |
| DELETE | /veiculos/{id} | Excluir       | 204     |

Erros: 400 (ID inválido), 404 (não encontrado), 409 (placa duplicada), 422 (dados inválidos).

## Autores

- Carlos Henrique Cardoso Da Silva Rocha
- Daniel Carvalho Silva