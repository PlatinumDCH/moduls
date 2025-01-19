from typing import Sequence
from fastapi import Query, FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi_tutorial.exemple.models import Contacts
from fastapi_tutorial.exemple.sheme import CreateContact


async def get_contacts_process(limit:int, offset:int, db:AsyncSession)->list[Contacts]|None:
    query = select(Contacts).offset(offset).limit(limit) 
    result = await db.execute(query)
    contacts = result.scalars().all()
    return contacts

async def create(body:CreateContact,db:AsyncSession)->Contacts:
    contact = Contacts(**body.model_dump(exclude_unset=True))
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


async def get_contact_by_id(contact_id:int, db:AsyncSession)->Contacts|None:
    """
    получить контакт по его id для конткретного пользователя.

    Args:
        contact_id (int): id контакта, который нужно получить.
        db (AsyncSession): сессия базы данных для выполнения запроса.
        user (Users): пользователь чей контакт извлекается.

    Returns:
        Contacts | None: обьект контакта,если найден иначе None.
    """
    query = (
        select(Contacts)
        .filter(Contacts.id == contact_id)
    )
    contact = await db.execute(query)
    return contact.scalar_one_or_none()

