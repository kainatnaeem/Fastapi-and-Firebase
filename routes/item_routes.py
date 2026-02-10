from fastapi import APIRouter
from schemas.item_schema import ItemCreate, ItemUpdate
from services.item_service import *


router = APIRouter(prefix="/items", tags=["Items"])
@router.post("/")
def create(item:ItemCreate):
    return createItem(item.dict())

@router.get("/getAllItems")
def getItems():
    return getAllItems()

@router.get("/{id}")
def getItem(id:str):
    return getItemById(id)

@router.put("/{id}")
def updateItem(id:str, item:ItemUpdate):
    return updateItemById(id, item.dict(exclude_unset=True))

@router.delete("/{id}")
def deleteItem(id:str):
    return deleteItemById(id)    