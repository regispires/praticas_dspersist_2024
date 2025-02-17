from pymongo import MongoClient
import time

client = MongoClient("mongodb://localhost:27017/")
db = client.mydatabase
collection = db.mycollection

start = time.time()

# Essas chamadas são bloqueantes - executadas uma após a outra
result1 = collection.find_one({"name": "João"})
result2 = collection.find_one({"name": "Maria"})
result3 = collection.find_one({"name": "José"})

end = time.time()
print(f"Tempo total (síncrono): {end - start:.2f} segundos")
