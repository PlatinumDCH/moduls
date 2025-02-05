from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pattern.creational.sengletonFastAPI.models import Todo
from pattern.creational.sengletonFastAPI.schemas import TodoCreate, TodoUpdate

async def get_todos(db: AsyncSession):
    result = await db.execute(select(Todo))
    return result.scalars().all()

async def create_todo(db: AsyncSession, todo: TodoCreate):
    new_todo = Todo(**todo.model_dump())
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo

async def update_todo(db: AsyncSession, todo_id: int, todo: TodoUpdate):
    result = await db.execute(select(Todo).where(Todo.id == todo_id))
    db_todo = result.scalars().first()
    if db_todo:
        for key, value in todo.dict(exclude_unset=True).items():
            setattr(db_todo, key, value)
        await db.commit()
        await db.refresh(db_todo)
    return db_todo

async def delete_todo(db: AsyncSession, todo_id: int):
    result = await db.execute(select(Todo).where(Todo.id == todo_id))
    db_todo = result.scalars().first()
    if db_todo:
        await db.delete(db_todo)
        await db.commit()
    return db_todo
