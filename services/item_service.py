from core.firebase import db
collection = db.collection("items")

def createItem(data):
    doc = collection.add(data)
    return {"id": doc[1].id}
def getAllItems():
    doc = collection.stream()
    items = []
    for item in doc:
        item_data = item.to_dict()
        item_data["id"] = item.id
        items.append(item_data)
    return items

def getItemById(id):
    doc = collection.document(id).get()
    if doc.exists:
        item_data = doc.to_dict()
        item_data["id"] = doc.id
        return item_data
    else:
        return {"error": "Item not found"}

def updateItemById(id, data):
    doc_ref = collection.document(id)
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.update(data)
        return {"message": "Item updated successfully"}
    else:
        return {"error": "Item not found"}




def deleteItemById(id):
    doc_ref = collection.document(id)     
    doc = doc_ref.get()  
    if doc.exists:
       doc_ref.delete()
       return {"message": "Item deleted successfully"}
    else:
        return {"error": "Item not found"}