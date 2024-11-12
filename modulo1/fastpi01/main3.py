from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from models import Item

app = FastAPI()

itens: list[Item] = []


@app.get("/")
def padrao():
    return {"msg": "Home"}


@app.get("/itens/{item_id}")
def ler_item(item_id: int) -> Item:
    for indice, item_atual in enumerate(itens):
        if item_atual.id == item_id:
            return item_atual
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item não encontrado.")


@app.get("/itens/")
def listar_itens() -> list[Item]:
    return itens


@app.post("/itens/", status_code=HTTPStatus.CREATED)
def adicionar_item(item: Item) -> Item:
    if any(item_atual.id == item.id for item_atual in itens):
        raise HTTPException(status_code=400, detail="ID já existe.")
    itens.append(item)
    return item


@app.put("/itens/{item_id}")
def atualizar_item(item_id: int, item_atualizado: Item) -> Item:
    for indice, item_atual in enumerate(itens):
        if item_atual.id == item_id:
            if item_atualizado.id != item_id:
                item_atualizado.id = item_id
            itens[indice] = item_atualizado
            return item_atualizado
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item não encontrado.")


@app.delete("/itens/{item_id}")
def remover_item(item_id: int):
    for item_atual in itens:
        if item_atual.id == item_id:
            itens.remove(item_atual)
            return {"msg": "Item removido com sucesso."}
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item não encontrado.")
