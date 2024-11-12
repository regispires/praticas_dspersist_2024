from pydantic import BaseModel

class Item(BaseModel):
    id: int
    nome: str
    valor: float
    is_oferta: bool | None = None
