from abc import ABC


class Discount(ABC):
    @classmethod
    def apply(self, price):
        pass

class SummerDiscount(Discount):
    def apply(self, price):
        return price * 0.9

class BlackFridayDiscont(Discount):
    def apply(self, price):
        return price * 0.7
    
#----

class PaymentMethod(ABC):
    @classmethod
    def process(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing PayPal payment of {amount}")

class CryptoPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing cryptocurrency payment of {amount}")

        
class PaymentProcessor:
    def pocess_payment(self, payment_method:PaymentMethod, amount):
        payment_method.process(amount)
    