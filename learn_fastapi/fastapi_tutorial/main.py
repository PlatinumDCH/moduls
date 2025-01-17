from enum import Enum
from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/') #<- декоратор операции пути
async def root(): return {'message':'hello world'}
# @app.get('/items/{item_id}')
# async def get_item(item_id): return {'item_id':item_id}
@app.get('/items/{item_id}')
async def read_item(
    item_id: int = Path(..., title='ID element', ge=1)):
    """
    Args:
        item_id (int, optional): должен быть целым числом
        больше или равно 1
    Returns:
        dict: {'item_idd':item_id}
    """
    return {'item_idd':item_id}

#use Enum validation path parametr
#===========================================
class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {
            "model_name": model_name, 
            "message": "Deep Learning FTW!"
            }

    if model_name.value == "lenet":
        return {
            "model_name": model_name, 
            "message": "LeCNN all the images"
            }

    return {
        "model_name": model_name, 
        "message": "Have some residuals"
        }

#conflict endpoint, correct
#========================================
@app.get("/users/me")
async def read_user_me():
    return {"user_id":"the current user"}
@app.get("users/{user_id}")
async def read_user(user_id:str):
    return {"user_id":user_id}
#=========================================

@app.get('/files/{file_path:path}')
async def read_file(file_parth:str):
    return {'file_parth':file_parth}

#query
#=========================================
"""                         ↓
http://127.0.0.1:8000/items/?skip=0&limit=10
                                   ↑
"""
fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"}
    ]
@app.get("/items_query")
async def read_item(skip: int = 0, limit: int = 10):
    """значения по умолчанию"""
    return fake_items_db[skip : skip + limit]

# @app.get("/items_query/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     """необезательные параметр запроса"""
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

@app.get("/items_query/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/itemss/{item_id}")
async def read_user_item(item_id: str, needy: str):
    """обезятельный query param"""
    item = {"item_id": item_id, "needy": needy}
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    """path param, quert param в перемешку"""
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

"""
Обявление разного типа параметров
=================================
item_id: str, needy: str, skip: int = 0, limit: int | None = None  => смешивание параметров
---  ---  ---  ---  ---  ---  --- 
item_id:str - path param
needt:str - обезательный параметр
skip:int - параметр по усолчанию
limit:int - не обезательный параметр
"""