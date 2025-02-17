from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# MongoDB connection
DATABASE_URL = os.getenv("DATABASE_URL")
client = AsyncIOMotorClient(DATABASE_URL)
db = client.mydatabase
engine = AIOEngine(client=client, database="mydatabase")

def get_engine() -> AIOEngine:
    return engine
