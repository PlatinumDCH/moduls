class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def sey(self):
        pass

class Cat(Animal):
    def say(self):
        return "Meow"
    
class Dog(Animal):
    def sey(self):
        return 'Woof'
    
class CatDog(Cat, Dog):
    def info(self):
        return f'{self.name}-{self.weight}'
    
class DogCat(Dog, Cat):
    def info(self):
        return f'{self.name}-{self.weight}'