class Person:
    def __init__(self, name:str, phone:str, opetarot_code:str):
        self.name = name
        self.phone = phone
        self.opetator_code = opetarot_code
    
    def get_phone_number(self):
        return f'{self.name}: +380({self.operator_code}){self.phone}'

