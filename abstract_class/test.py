import pytest
from abstract_class.paymentSys import StripePaymentProvider
from abstract_class.paymentSys import PayPalPaymentProvider 
from abstract_class.paymentSys import PaymentService 
from abstract_class.paymentSys import TestPaymentProvider

#тест два в одном, логика будет обработана на два класса
@pytest.mark.parametrize('provider_class', [StripePaymentProvider,PayPalPaymentProvider])
def test_make_invoice(provider_class):
    provider = provider_class()
    invoice_id = provider.make_invoice(user_id=1)
    assert isinstance(invoice_id, str) and len(invoice_id) > 0

#тест два в одном, логика будет обработана на два класса
@pytest.mark.parametrize('provider_class', [StripePaymentProvider,PayPalPaymentProvider])
def test_process_payment(provider_class):
    provider = provider_class()
    service = PaymentService(provider)
    invoice_id = service.process_payment(user_id=1, amount=100.0)
    assert isinstance(invoice_id, str) and len(invoice_id) > 0

def test_make_invoice_stripe():
    provider = StripePaymentProvider()
    invoice_id = provider.make_invoice(user_id=1)
    assert isinstance(invoice_id, str) and len(invoice_id) > 0

def test_make_invoice_paypal():
    provider = PayPalPaymentProvider()
    invoice_id = provider.make_invoice(user_id=1)
    assert isinstance(invoice_id, str) and len(invoice_id) > 0

def test_make_invoice_test_provider():
    """не вызываеься реально API"""
    provider = TestPaymentProvider()
    invoice_id = provider.make_invoice(user_id=1)
    assert isinstance(invoice_id, str) and len(invoice_id) > 0

def test_process_payment_stripe():
    provider = StripePaymentProvider()
    service = PaymentService(provider)
    invoice_id = service.process_payment(user_id=1, amount=100.0)
    assert isinstance(invoice_id, str) and len(invoice_id) > 0

def test_process_payment_paypal():
    provider = PayPalPaymentProvider()
    service = PaymentService(provider)
    invoice_id = service.process_payment(user_id=1, amount=100.0)
    assert isinstance(invoice_id, str) and len(invoice_id) > 0

def test_process_payment_test_provider():
    """не вызывается реальное API"""
    provider = TestPaymentProvider()
    service = PaymentService(provider)
    invoice_id = service.process_payment(user_id=1, amount=100.0)
    assert isinstance(invoice_id, str) and len(invoice_id) > 0