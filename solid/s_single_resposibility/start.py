class Person:
    def __init__(self, phone, operator_code, name):
        self.name = name
        self.phone = phone
        self.operator_code = operator_code
    
    def get_phone_number(self):
        return f'{self.name}: +380{self.operator_code}{self.phone}'

if __name__ == '__main__':
    peron = Person('2730962', '067', 'amid')
    print(peron.get_phone_number())
