import json
from models import Item

with open("itens.json", "r") as f:
    itens_desserializados = [Item.model_validate(item) for item in json.load(f)]
print("Dados desserializados do arquivo:")

for item in itens_desserializados:
    print(item)
