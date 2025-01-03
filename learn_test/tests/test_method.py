import unittest 
from unittest.mock import patch, mock_open
from src.method.main import read_contacts_from_file
from src.method.main import write_contact_to_file

class TestClass(unittest.TestCase):
    mock_ope_file = mock_open()
    contacts = [
        {'name':'Oleksii','age':18},
         {'name': 'Dmytro', 'age': 12},
         {'name': 'Vladimir', 'age': 25},
         {'name': 'Olia', 'age': 45}
    ]
    @patch('json.dump')
    @patch('builtins.open', mock_ope_file)
    def test_write_one(self, mock_json_dump):
        write_contact_to_file('test.json', self.contacts)
        self.mock_ope_file.assert_called_with('test.json', 'w')
        mock_json_dump.assert_called()
        mock_json_dump.assert_called_with(
            {'contacts': self.contacts},self.mock_ope_file()
        )

    @patch('json.load')
    @patch('builtins.open', mock_ope_file)
    def test_write(self, load_mock):
        load_mock.return_value = {'contacts': self.contacts}
        result = read_contacts_from_file('test.json')
        self.mock_ope_file.assert_called_with('test.json', 'r')
        load_mock.assert_called()
        load_mock.assert_called_with(self.mock_ope_file())
        self.assertEqual(result, self.contacts)
