from typing import Sequence
from fastapi import Query, FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi_tutorial.exemple.models import Contacts
from fastapi_tutorial.exemple.sheme import CreateContact


async def get_contacts(limit:int, offset:int, db:AsyncSession):
    query = select(Contacts).offset(offset).limit(limit) 
    result = await db.execute(query)
    contacts:Sequence[Contacts] = result.scalars().all()
    return contacts

async def create(body:CreateContact,db:AsyncSession)->Contacts:
    contact = Contacts(**body.model_dump(exclude_unset=True))
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact




