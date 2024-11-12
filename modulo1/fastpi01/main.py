from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"msg": "Hello World!!!"}


@app.get("/itens/{item_id}")
def le_item(item_id: int, nome: Union[str, None] = None):
    return {"item_id": item_id, "nome": nome}
