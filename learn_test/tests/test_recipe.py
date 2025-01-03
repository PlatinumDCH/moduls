import unittest
from unittest.mock import patch, mock_open
from src.get_recipe.get_recipe import get_recipe

class TestClass(unittest.TestCase):
    mock_open_file = None
    @classmethod
    def setUpClass(cls):
        cls.mock_open_file = mock_open(
            read_data=(
                '0000,test_name_food,prod1,prod2,prod3,prod4,prod5\n'
                'mock=1111,test_name_food_2,prod1,prod2,prod3,prod4,prod5')
        )
    @classmethod
    def tearDownClass(cls):
        '''poslie togo kak my prodelalu vse testy mi obnyliaem mock_open_file'''
        cls.mock_open_file = None


    def test_first_line(self):
        uuid = '0000'
        filename = 'fake.csv'
        with patch('builtins.open', self.mock_open_file) as mock_file:
            result = get_recipe(filename, uuid)
            self.assertEqual(uuid, result.get('id'))
            
'''
moki - ieto imitatzia, on htoto vozvrashiaet, mi ykazivarm kak on bytet sebia vesty
1. sozdaiem class
2.importirovali nashu functsiu
3. iz unittes.moki dostaiem path mock_open
mokirovanie = shtoto dolgno otdavatsia
patch = perectitia kakihto importov
4.pered vsima testami my imitityem otritia file mokaiem
5. func moc_open bydet povertiat str
'''