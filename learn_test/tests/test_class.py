import unittest
from src.my_class.main import Cat, CatDog, Dog, DogCat, Animal


class TestClass(unittest.TestCase):
    def test_dog(self):
        self.assertEqual(
            Dog.__base__, Animal, msg="Sobaka ne nasleyetsia ot class Animal"
        )

    def test_cat_dog(self):
        assert Dog in CatDog.__bases__, "Class Sobaka  must by parent dlia class CatDog"
        assert "info" in dir(CatDog), "ne naiden method info v class CatDog"
        "toge samoe shto i prohlii test tolko use python assert"
