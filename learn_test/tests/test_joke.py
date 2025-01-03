import unittest
from unittest.mock import patch, MagicMock

import requests
from requests.exceptions import Timeout

from src.joke_obj.joke import len_joke, get_joke

class TestJoke(unittest.TestCase):

    @patch('src.joke_obj.joke.get_joke')
    def test_len_joke(self, fake_joke):
        """patch подмениет результат вызова функции get_joke
            и на выходе получаем 'one'
            это обеспечивает замкнутость среды тестирования
        """
        fake_joke.return_value = 'one'
        self.assertEqual(len_joke(), 3)

    @patch('src.joke_obj.joke.requests')
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'value':'Hello world'
        }
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'Hello world')

    @patch('src.joke_obj.joke.requests')
    def test_get_joke_fail(self, mock_requests):
        mock_response = MagicMock(status_code=403 )
        mock_response.json.return_value = {
            'value':'No jokes'
        }
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'No jokes')
    
    @patch('src.joke_obj.joke.requests.get')
    def test_get_joke_raises_exeptions(self, mock_get):
        mock_get.side_effect = Timeout('что-то не так с сервером')
    
        # Вызываем тестируемую функцию
        result = get_joke()
        
        # Проверяем результат
        assert result == 'No jokes, timeout'

    @patch('src.joke_obj.joke.requests')
    def test_get_joke_raises_for_status(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'HTTPError was reised')
