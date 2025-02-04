from abc import ABC, abstractmethod
import uuid

class PaymentProvider(ABC):

    @abstractmethod
    def make_provider(self, amount:float):
        pass

    @abstractmethod
    def make_invoice(self, user_id:int):
        pass

class TestPaymentProvider(PaymentProvider):
    def make_provider(self, amount):
        print(f'Testing pay {amount}, user Stripe, sucessfull')
    
    def make_invoice(self, user_id:int):
        invoice_id = str(uuid.uuid4())
        print(f'Testing onvoice {invoice_id} created <Stripe> for user {user_id}')
        return invoice_id


class StripePaymentProvider(PaymentProvider):

    def make_provider(self, amount):
        print(f'Pay {amount}, user Stripe, sucessfull')
    
    def make_invoice(self, user_id:int):
        invoice_id = str(uuid.uuid4())
        print(f'Invoice {invoice_id} created <Stripe> for user {user_id}')
        return invoice_id

class PayPalPaymentProvider(PaymentProvider):
    def make_provider(self, amount):
        print(f'Pay {amount}, user PayPall, sucessfull')
    
    def make_invoice(self, user_id:int):
        invoice_id = str(uuid.uuid4())
        print(f'Invoice {invoice_id} created <PayPall> for user {user_id}')
        return invoice_id

class PaymentService:
    def __init__(self, provider: PaymentProvider):
        self.provider = provider
    
    def process_payment(self, user_id, amount):
        invoice = self.provider.make_invoice(user_id=user_id)
        self.provider.make_provider(amount=amount)
        return invoice
    
if __name__ == '__main__':

    stripe = PaymentService(StripePaymentProvider())
    paypal = PaymentService(PayPalPaymentProvider())

    stripe.process_payment(user_id=101, amount=50.0)
    paypal.process_payment(user_id=102, amount=75.0)