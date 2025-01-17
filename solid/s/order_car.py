from abc import ABC, abstractmethod
from decimal import Decimal

class Car:
    """создать обьект машины"""
    def __init__(self, car_no:str, car_type:str):
        self.car_no = car_no
        self.car_type = car_type


class Client:
    """создать обьект человека"""
    def __init__(self, name):
        self.name = name


class Order:
    def __init__(self, car, client):
        self.car = car
        self.client = client

class CarSercive:
    @staticmethod
    def find_car(car_no, cars):
        """поиск машины по номеру"""
        for car in cars:
            if car.car_no == car_no:
                return car
        return None
    
class OrderServise:

    @staticmethod
    def order_car(car_no, client, cars):
        """Order a car for a client."""
        car = CarSercive.find_car(car_no, cars)
        if car:
            return Order(car, client)
        return None

    @staticmethod
    def print_order(order):
        """Print order details."""
        if order:
            print(f"Order Details:\nCar No: {order.car.car_no}\nClient: {order.client.name}")
        else:
            print("Order not found!")

class CarInfoService:
    @staticmethod
    def get_car_interest_info(car_type):
        """Get information about the car type."""
        if car_type == "sedan":
            print("Sedan: Comfortable and efficient.")
        elif car_type == "pickup":
            print("Pickup: Great for transporting goods.")
        elif car_type == "van":
            print("Van: Ideal for group travel.")
        else:
            print("Unknown car type.")

class NotificationSetvise(ABC):
    
    @abstractmethod
    def sendMessage(message:str):
        pass

class EmailNotification(NotificationSetvise):
    @staticmethod
    def send_message(message):
        """Send a message  use email"""
        print('pricessing compile email')
        print(f"Sending email: {message}")
        # You can integrate email sending using libraries like `smtplib` or external APIs.

class MibileNotification(NotificationSetvise):

    @staticmethod
    def send_message(message):
        """отправка сообщения используя смс"""
        print('pricessing compile sms')
        print(f"Sending sms :{message}")

class Account:
    def __init__(self):
        self.accounts = {}
    
    def balance(self, numberAccount:str):
        """Возвращает баланс аккаунта"""
        raise NotImplementedError('This method should be overrided')

    def refill(self, numberAccount:str, sum_: Decimal):
        """пополнение щета"""
        raise NotImplementedError('This method should be overrided')

class PymentAccaut(Account):

    def payment(self, numberAccont:str, sum_: Decimal):
        """снятие указанной сумы со счета"""
        if numberAccont not in self.accounts:
            raise ValueError(f'Account {numberAccont} does not exists')
        if self.accounts[numberAccont] < sum_:
            raise ValueError(f'Insufficient balance in accont {numberAccont}')
        self.accounts[numberAccont] -= sum_
        print(f'Accont {numberAccont} devided by {sum_}. New balance: {self.accounts[numberAccont]}')

class SalaryAccount(PymentAccaut):

    def balance(self, numberAccount:str)->Decimal:
        """возвращает баланс указанного аккаунта"""
        return self.accounts.get(numberAccount, Decimal('0.0'))
    
    def refill(self, numberAccont:str, sum_: Decimal):
        """пополнение щета на указанную сумму"""
        if numberAccont not in self.accounts:
            self.accounts[numberAccont] = Decimal(
                0.0
            )
        self.accounts[numberAccont] += sum_
        print(f'Accont {numberAccont} refilled be {sum_}.New balance {self.accounts[numberAccont]}')


class DepositAccont(Account):

    def balance(self, numberAccount:str)->Decimal:
        """возвращает баланс указанного аккаунта"""
        return self.accounts.get(numberAccount, Decimal('0.0'))
    
    def refill(self, numberAccont:str, sum_: Decimal):
        """пополнение щета на указанную сумму"""
        if numberAccont not in self.accounts:
            self.accounts[numberAccont] = Decimal(
                0.0
            )
        self.accounts[numberAccont] += sum_
        print(f'Accont {numberAccont} refilled be {sum_}.New balance {self.accounts[numberAccont]}')

class WebMoneyPaument(ABC):
    
    @abstractmethod
    def pay_web_money(self):
        pass

class CreditCardPayment(ABC):
    @abstractmethod
    def pay_credit_card(self):
        pass

class PhoneNumberPayment(ABC):
    @abstractmethod
    def pay_phone_number(self):
        pass


class InternetPaymentServise(WebMoneyPaument, CreditCardPayment, PhoneNumberPayment):
    
    def pay_web_money(self):
        pass

    def pay_credit_card(self):
        pass

    def pay_phone_number(self):
        pass

class TerminamlPaymentServise(WebMoneyPaument, CreditCardPayment):

    def pay_web_money(self):
        pass

    def pay_credit_card(self):
        pass





# Пример использования
if __name__ == "__main__":
    #create object car
    cars = [
        Car("1234", "sedan"),
        Car("5678", "pickup"),
        Car("9101", "van"),
    ]

    