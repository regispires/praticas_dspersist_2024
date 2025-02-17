import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import time

client = AsyncIOMotorClient("mongodb://localhost:27017/")
db = client.mydatabase
collection = db.mycollection

async def fetch_data():
    start = time.time()

    # As consultas podem ser executadas simultaneamente
    result1, result2, result3 = await asyncio.gather(
        collection.find_one({"name": "João"}),
        collection.find_one({"name": "Maria"}),
        collection.find_one({"name": "José"})
    )

    end = time.time()
    print(f"Tempo total (assíncrono): {end - start:.2f} segundos")

asyncio.run(fetch_data())
