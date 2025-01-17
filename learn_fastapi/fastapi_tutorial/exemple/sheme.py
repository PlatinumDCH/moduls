from pydantic import BaseModel, Field
from pydantic.config import ConfigDict # Для указания from_attributes

class CreateContact(BaseModel):
    first_name:str = Field(min_length=1, max_length=50)
    note: None|str

class ContactResponse(CreateContact):
    id:int
    model_config = ConfigDict(from_attributes=True) # Включаем поддержку SQLAlchemy объектов