from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi import FastAPI, Depends, HTTPException
from fastapi_tutorial.exemple.rout_contact import router
from fastapi_tutorial.exemple.db import get_connection_db

app = FastAPI()

app.include_router(router=router, prefix="/api")

@app.get('/')
async def index():
    return {'message':'home page'}

@app.get("/healthchecker",)
async def healthchecker(db: AsyncSession = Depends(get_connection_db)
                        ):
    """
    вроверка подклюяения к базе данных
    
    Depends:
        role_dependency_admin - зависимось которая проверяет что у пользователя
        роль админ

    Args:
        звисимось подключения к базе данных
        
    Returns:
        if connection data pase corect, return messages
        else HTTPExeption
    """
    try:
        result = await db.execute(text("SELECT 1"))
        row = result.fetchone()
        if not row:
            raise HTTPException(
                status_code=500, 
                detail="Database is not configured correctly"
                )
        return {
            "message": "Data base normaly work"
            }
    except Exception as err:    

        raise HTTPException(
            status_code=500, 
            detail="Error connecting to the database"
            )