from fastapi import APIRouter, Depends, Query, status
from fastapi_tutorial.exemple.db import get_connection_db
from fastapi_tutorial.exemple.sheme import CreateContact, ContactResponse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_tutorial.exemple.repo_contact import get_contacts, create
from fastapi_tutorial.exemple.models import Contacts

router = APIRouter(prefix="/contacts", tags=["contacts"])

@router.get('/all', response_model=list[ContactResponse])
async def get_all_contacts(
    limit:int = Query(10, ge=10, le=500),
    offset:int = Query(0, ge=0, le=10),
    db: AsyncSession = Depends(get_connection_db),
    )->list[Contacts]|None:
    contacts = await get_contacts(limit,offset,db)
    return contacts


@router.post('/', response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(
    body:CreateContact, db:AsyncSession = Depends(get_connection_db),
    )->ContactResponse:
    contact = await create( body, db)
    return contact

