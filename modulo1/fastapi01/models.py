from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    nome: str
    valor: float
    is_oferta: Union[bool, None] = None