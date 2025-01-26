from typing import Callable

def feeder(get_nex_item: Callable[[], str])->None:
    ...
def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None])->None:
    pass




