from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    price: float


class GetItem(BaseModel):
    id: str
    name: str
    price: float

class GetItembyId(BaseModel):
    id: str
    name: str
    price: float    

class ItemUpdate(BaseModel):
    name: str | None = None
    price: float | None = None


class ItemDelete(BaseModel):
    id: str

