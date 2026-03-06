from fastapi import APIRouter, UploadFile, File, Form
from schemas.item_schema import ItemCreate, ItemUpdate
from services.item_service import *
import shutil
#The line @app.post("/upload") creates a POST API endpoint called /upload that clients can use to send files. The function async def upload_file(file: UploadFile = File(...)) defines an asynchronous function that receives a required file from the request using FastAPI’s UploadFile type. The condition if file.content_type not in ["image/jpeg", "image/png"] checks the MIME type to ensure only JPEG or PNG images are accepted, otherwise an error response is returned. The line with open(f"uploads/{file.filename}", "wb") as buffer: opens a file in the server’s uploads folder in write-binary mode, and shutil.copyfileobj(file.file, buffer) copies the uploaded file data into that file,
router = APIRouter(prefix="/items", tags=["Items"])
@router.post("/")
async def create_item(
    name: str = Form(...),
    price: float = Form(...),
    description: str = Form(...),
    file: UploadFile = File(None)  # optional file
):
    image_url = None

    # Save the uploaded file locally
    if file:
        if file.content_type not in ["image/jpeg", "image/png"]:
            return {"error": "Only JPEG or PNG images allowed"}
        with open(f"uploads/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        image_url = f"http://127.0.0.1:8000/uploads/{file.filename}"

    # Prepare data for Firebase
    item_data = {
        "name": name,
        "price": price,
        "description": description,
        "image_url": image_url
    }

    # Save to Firebase using your existing service
    return createItem(item_data)

@router.get("/getAllItems")
def getItems():
    return  getAllItems()

@router.get("/{id}")
def getItem(id:str):
    return getItemById(id)

@router.put("/{id}")
def updateItem(id:str, item:ItemUpdate):
    return updateItemById(id, item.dict(exclude_unset=True))

@router.delete("/{id}")
def deleteItem(id:str):
    return deleteItemById(id)    