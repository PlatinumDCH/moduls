from pydantic import BaseModel, Field, HttpUrl

class Image(BaseModel):
    url: str
    name: str | HttpUrl

class Item(BaseModel):
    name:str = Field(examples=['Foo'])
    description: str | None = Field(default=None, examples=['A very nice'])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.3])
    tags: list[str] = []
    image: list[Image] | None = None

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'name': 'Foo',
                    'description': 'A very nice Item',
                    'price': 35.4,
                    'tax': 3.2,

                }
            ]
        }
    }

class Offset(BaseModel):
    name:str
    description: str | None = None
    price: float
    items: list[Item]

