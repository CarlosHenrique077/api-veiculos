import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB: str = os.getenv("MONGO_DB", "garagem")
    MONGO_COLLECTION: str = os.getenv("MONGO_COLLECTION", "veiculos")


settings = Settings()