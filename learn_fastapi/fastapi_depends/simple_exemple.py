from typing import Annotated
from fastapi import FastAPI, HTTPException, status, Depends, Query

development_db = ['DB for Development']

def get_db_session():
    return development_db

app = FastAPI()

@app.get('/add-item/')
def add_item(item: Annotated[str, Query()], db = Depends(get_db_session)):
    db.append(item)
    print(db)
    return {'message':f'added item {item}'}
