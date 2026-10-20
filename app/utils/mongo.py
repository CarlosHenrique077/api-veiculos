from bson import ObjectId
from bson.errors import InvalidId


def validar_id(id: str) -> ObjectId | None:
    """Retorna o ObjectId ou None se for inválido."""
    try:
        return ObjectId(id)
    except (InvalidId, TypeError):
        return None


def serializar(doc: dict) -> dict:
    doc["id"] = str(doc.pop("_id"))
    return doc