from pymongo import MongoClient

from app.core.config import settings

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]


def get_colecao():
    return db[settings.MONGO_COLLECTION]


def configurar_banco():
    """Cria o índice único na placa."""
    get_colecao().create_index("placa", unique=True, name="idx_placa_unica")