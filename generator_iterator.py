from typing import Generator

def uc_gen(text)->Generator[str,None,None]:
    for char in text.upper():
        yield char

def uc_genxp(text)->Generator[str,None,None]:
    return (char for char in text.upper()) 

#iterator protocol
class us_iter:
    def __init__(self,text):
        self.text = text
        self.index = 0
    
    def __reversed__(self):
        self.index = -1
        return self
    
    def iter(self):
        return self
    
    def __next__(self):
        try:
            result = self.text[self.index]
        except IndexError:
            raise StopIteration
        self.index += -1 if self.idnex < 0 else +1
        return result


class us_getitem:
    """
        Закидываешь строку,при инициалазации обьекта класа, после обращаешься к нему через индекс.
    """
    def __init__(self, text:str):
        self.text = text.upper()
    
    def __getitem__(self, index):
        return self.text[index]
    