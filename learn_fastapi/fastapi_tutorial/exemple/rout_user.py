from pydantic import BaseModel
from typing import Annotated
from fastapi_tutorial.exemple.repo_user import get_user_by_email, create_user
from fastapi_tutorial.exemple.db import get_connection_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_tutorial.exemple.sheme import UserResponse, UserSchema
from fastapi import APIRouter, status, Depends, HTTPException, Body

router = APIRouter(prefix='/user', tags=['users'])

@router.post('/signup', response_model=UserResponse,status_code=status.HTTP_201_CREATED)
async def signup(
    body: Annotated[
        UserSchema, # ож тип д
        Body(
            examples=[ #мож вкл неск dict
                { #буд отобр в авт док 
                    'username':'Foo',
                    'email':'example@gmail.com',
                    'password':'123654'
                },
                {
                    'name':'Baz',
                    'email':'email2@gmail.com',
                    # 'passwprd':'123'
                }
            ]
        )],

    connect_db:AsyncSession = Depends(get_connection_db)
):
    if_exists = await get_user_by_email(body.email, connect_db)
    if if_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='account already exists')
    new_user = await create_user(body, connect_db)
    return {
        new_user
    }

class Item(BaseModel):
    name:str
    description: str|None = None
    price : float
    tax:float|None = None
    
@router.put('/items/{item_id}')
async def update_item(
    *, # п э парам именнованные
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
                {
                    "name": "Bar",
                    "price": "35.4",
                },
                {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            ],
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results
