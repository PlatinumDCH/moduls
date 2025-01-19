from pydantic import BaseModel, Field, ValidationError
from annotated_types import Gt
from typing import Annotated

PositiveInt = Annotated[int, Gt(0)]

class Blog(BaseModel):
    title: str = Field(..., min_length=4)
    is_active: bool
    number:PositiveInt

dict_ = {
    'title':'hero',
    'is_active':False,
    'number':1
}
try:
    Blog(**dict_)
except ValidationError as exc:
    print(repr(exc.errors()))
