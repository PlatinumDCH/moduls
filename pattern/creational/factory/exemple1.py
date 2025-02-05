from abc import ABC, abstractmethod

class ILocalizer(ABC):
    
    @abstractmethod
    def localize(self, message):
        pass



class FrenchLocalizer(ILocalizer):
    def __init__(self):
        self.translations = {
            'car':'voiture',
            'bike':'bycyclette'
        }
    
    def localize(self, message):
        return self.translations.get(message, message)
    
class SpanishLocalizer(ILocalizer):

    def __init__(self):
        self.translations= {
            'car':'coche',
            'bike':'bibiclete'
        }
    
    def localize(self, message):
        return self.translations.get(message, message)

class EnglishLocalizer(ILocalizer):

    def localize(self, message):
        return message


def Factory(lang='English'):
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[lang]()

if __name__ == '__main__':
    
    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = ['car', 'bike']

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))