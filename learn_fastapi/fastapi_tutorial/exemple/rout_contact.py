from fastapi_tutorial.exemple.sheme import FilterParam
from fastapi_tutorial.exemple.repo_contact import get_contact_by_id
from typing import Annotated
from fastapi import APIRouter, Depends, Query, status, Path, HTTPException
from fastapi_tutorial.exemple.db import get_connection_db
from fastapi_tutorial.exemple.sheme import CreateContact, ContactResponse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_tutorial.exemple.repo_contact import get_contacts_process, create
from fastapi_tutorial.exemple.models import Contacts

router = APIRouter(prefix="/contacts", tags=["contacts"])

@router.get('/all', response_model=list[ContactResponse])
async def get_contacts(
    filter_query: Annotated[FilterParam, Query()],
    db: AsyncSession = Depends(get_connection_db),
    )->list[Contacts]|None:
    contacts = await get_contacts_process(filter_query.limit, filter_query.skip, db)
    return contacts


@router.post('/', response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(
    body:CreateContact, db:AsyncSession = Depends(get_connection_db),
    )->Contacts:
    contact = await create( body, db)
    return contact


@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(
    contact_id:Annotated[
        int,
        Path(title='The ID of the contact in database',
             ge=1, le=1000)
    ],
    db:AsyncSession = (Depends(get_connection_db)),
):
    
    #logic work in db
    contact =  await get_contact_by_id(
        contact_id=contact_id,
        db=db,
    )
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='not found ')
    return contact