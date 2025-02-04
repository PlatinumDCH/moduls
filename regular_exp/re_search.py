import re
from enum import Enum

class ExempleSrv(str, Enum):
    text1 = "Вивчення Python може бути веселим."
    pattern1 = r'в\w*м'

    text2 = "Моя електронна адреса: example@example.com,  example2@example.com"
    pattern2 = r"\w+@\w+\.\w+"

    text3 = "username@domain.com"
    pattern3 = r"(\w+)@(\w+\.\w+)"

    text4 = "Рік 2023 був складнішим, ніж 2022"
    pattern4 = r'\d+'

    text5 = "Python - це проста, але потужна мова програмування."
    patter5 = r'\w+'

    text6 = 'My file Python.txt'
    pattern6 = r'\s'
def re_match(text, pattern):
    """
    в - начало слова 
    \w* - любое количество симоволов 
    м - конец слова
    """
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        print(f"Match found {match.group()}")
    else:
        print('Not found')


def email_first(text, pattern) -> None|str:
    match = re.search(pattern, text)
    if match:
        print('email found:', match.group())
    return None

def email_all(text, pattern)->None|list:
    match = re.findall(pattern, text)
    if match:
        print('email found:', match)
    return None

def partitial_email(email, pattern)->None|tuple:
    match  = re.search(pattern, email)
    if match:
        user_name = match.group(1)
        domain_name = match.group(2)
        return user_name, domain_name
    else:
        return None
    
def find_data(pattern, data):
    matches = re.findall(pattern, data)
    return matches

def patitial_text(text, pattern):
    matches = re.findall(pattern, text)
    return matches

def replace_space(replacemant, pattern, file_name):
    formated_name = re.sub(pattern, replacemant, file_name)
    return formated_name

