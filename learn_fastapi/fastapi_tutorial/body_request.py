from typing import Union, Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

"""
response - ответ
request  - запрос
"""

class Item(BaseModel):
    name:str
    desckription: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.post('/items')
async def create_item(item:Item): 
    return item

@app.post('/item_change')
async def change_item(item:Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({
            'price_with_tax':price_with_tax
        })
    return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}

@app.put("/itemss/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, 
        Query(
            title='Query String',
            description='Query string for the items to searsh in the database that have a good match',
            min_length=4, 
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
            ),
        ] = None,
    ): 
    
    results = {
        "items": [
            {"item_id": "Foo"}, 
            {"item_id": "Bar"}
                 ]
            }
    if q:
        results.update({"q": q})
    return results

"""
необезательный парамет запроса, значение по умолчанию = fixedquery
@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
"""
#обезательное значение
#=====================
"""
обезательный параметр запроса, значение по умолчанию не указано
@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
"""
"""
Elipsis
альтернативно указать что query param обезательный
@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
"""
"""
Обезательное значение 
None - валидное значение параметра query
альтернативно указать что query param обезательный
@app.get("/items/")
async def read_items(q: Annotated[str|None, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
"""