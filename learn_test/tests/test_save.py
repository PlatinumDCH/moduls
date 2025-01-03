import unittest
from unittest.mock import patch, mock_open, call
from src.save_data.answer import save_aplivant_data,applicant

class TestClass(unittest.TestCase):
   
    mock_open_file = mock_open()

    @patch('builtins.open', mock_open_file)
    def test_open_file(self):
        save_aplivant_data(applicant, 'fake.csv')
        #mock_open_file.call_count - специальный щетчие, сколько раз он запкскался
        self.assertEqual(self.mock_open_file.call_count, 1), 'Function bytes otkryta 1 raz' # проверка на то что фунуия вызывалась  1 раз 
        print(self.mock_open_file.call_args[0])
        print(self.mock_open_file.call_args[1])
        self.mock_open_file.assert_called() #проверка того что функция вызывалась в общем
        self.mock_open_file.assert_called_with('fake.csv', 'w', encoding='utf-8') # проверка на то что когда мы запускали наш мое ему пришло именно эти параметры 'fake.csv', 'w', encoding='utf-8'
    
    @patch('builtins.open', mock_open_file)
    def test_write_file(self):

        save_aplivant_data(applicant, 'fake.csv')

        calls = [
            call('test_name1,101,111,111,111\n'),
            call('test_name2,101,111,111,111\n'),

        ]
        self.mock_open_file().write.call_with('test_name1,101,111,111,111\n')
        self.mock_open_file().write.call_with('test_name2,101,111,111,111\n')
        self.mock_open_file().write.assert_has_calls(calls, any_order=True)
        
    
