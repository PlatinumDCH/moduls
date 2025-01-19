from pydantic import BaseModel, Field, EmailStr
from pydantic.config import ConfigDict # Для указания from_attributes

class CreateContact(BaseModel):
    first_name:str = Field(min_length=1, max_length=50)
    note: None|str

class ContactResponse(CreateContact):
    id:int
    model_config = ConfigDict(from_attributes=True) # Включаем поддержку SQLAlchemy объектов

class UserSchema(BaseModel):
    username:str = Field(min_length=2, max_length=50)
    email: EmailStr
    password:str = Field(min_length=2, max_length=12)

class UserResponse(BaseModel):
    id:int
    username:str
    email:str

class FilterParam(BaseModel):
    model_config = {"extra": "forbid"} #доп поля не разреш
    limit:int = Field(10, gt=0, le=50)
    skip:int = Field(0, ge=0, le=10)
