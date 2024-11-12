import pickle
from models import Item

# Exemplo de dados - lista de objetos Item
itens = [
    Item(id=1, nome="Produto A", valor=29.99, is_oferta=True),
    Item(id=2, nome="Produto B", valor=15.49, is_oferta=False),
    Item(id=3, nome="Produto C", valor=9.99),  # Valor padrão para is_oferta é None
]

# Serializar para arquivo usando pickle
with open("itens.pkl", "wb") as f:
    pickle.dump(itens, f)

print("Dados serializados e salvos em 'itens.pkl'.")
