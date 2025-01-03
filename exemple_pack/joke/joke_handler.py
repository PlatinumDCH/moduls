import random
import pathlib

#путь к текущей директории
current_dir = pathlib.Path(__file__).parent

def get_rundom_joke():
    try:
        with open(current_dir / 'jokes.txt', 'r',encoding='utf-8') as joke_file:
            jokes = joke_file.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError:
        return 'Not found jokes.txt file'
