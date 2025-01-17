from typing import Annotated, get_type_hints
import sys


x: Annotated[int, "metadata_1", "metadata_2"] = 10

print(get_type_hints(sys.modules[__name__]))
# {'x': <class 'int'>}
print(get_type_hints(sys.modules[__name__], include_extras=True))
# {'x': typing.Annotated[int, 'metadata_1', 'metadata_2'}
print(get_type_hints(sys.modules[__name__], include_extras=True)['x'].__metadata__)
# {'metadata_1', 'metadata_2'}

