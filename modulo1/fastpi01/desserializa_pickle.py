import pickle

# Desserializar do arquivo usando pickle
with open("itens.pkl", "rb") as f:
    itens_desserializados = pickle.load(f)

print("Dados desserializados do arquivo:")
for item in itens_desserializados:
    print(item)
