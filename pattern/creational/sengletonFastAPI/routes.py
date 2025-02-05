from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pattern.creational.sengletonFastAPI.database import db
from pattern.creational.sengletonFastAPI.schemas import TodoCreate, TodoResponse, TodoUpdate
from pattern.creational.sengletonFastAPI.crud import get_todos, create_todo, update_todo, delete_todo

router = APIRouter()
@router.get("/todos", response_model=list[TodoResponse])
async def read_todos(db: AsyncSession = Depends(db.get_session)):
    return await get_todos(db)

@router.post("/todos", response_model=TodoResponse)
async def add_todo(todo: TodoCreate, db: AsyncSession = Depends(db.get_session)):
    return await create_todo(db, todo)

@router.put("/todos/{todo_id}", response_model=TodoResponse)
async def edit_todo(todo_id: int, todo: TodoUpdate, db: AsyncSession = Depends(db.get_session)):
    return await update_todo(db, todo_id, todo)

@router.delete("/todos/{todo_id}")
async def remove_todo(todo_id: int, db: AsyncSession = Depends(db.get_session)):
    return await delete_todo(db, todo_id)