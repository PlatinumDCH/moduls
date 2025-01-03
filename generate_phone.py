"""
Module a generatiom phone number using faker and phone_gen library.
"""

from faker import Faker
from phone_gen import PhoneNumber
from logger.set_logger import logger
from faker.providers.phone_number import Provider

faker = Faker()

class UKPhoneProvider(Provider):
    def ukraine_phone_number(self):
        return f'+380 {self.msisdn() [3:]}'

def generate_phone_number(country: str='')->str|None:
    """
    Returns a random phone number.
    

    Args:
        country (str, optional): The country code for the phone number.
        If provided, the phone number will be generated based on the spesified
        country.If not provided, the function will return 'None'.Defaults to ''.

    Returns:
        str: A randomly generated phone number in international format 
        (e.g. +12344567890).If country specified, the function returns 'None'
    """
    if country:
        try:
            gen_phone = PhoneNumber(country)
            return gen_phone.get_number(full=True)
        except ValueError as e:
            return None
    return None

def gen_phone():
    list_phone = [
        faker.phone_number() for _ in range(10)
    ]
    return list_phone

def main():
    country_code = "+380"  # Код страны Украины
    operator_codes = ["67", "68", "96", "97", "98", "50", "66", "95", "99", "63", "93"]  # Действительные коды операторов
    operator_code = faker.random_element(operator_codes)
    subscriber_number = faker.random_number(digits=7, fix_len=True)
    return f"{country_code}{operator_code}{subscriber_number}"

if __name__ == '__main__':
    # result = (gen_phone())
    # logger.debug(f'{result}')
    for _ in range(10):
        print(main())
