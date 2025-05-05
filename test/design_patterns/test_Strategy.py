import unittest

from src.design_patterns.Strategy import ShoppingCart, CreditCardPayment, PayPalPayment


class TestStrategy(unittest.TestCase):
    def test_credit_card_payment(self):
        cart = ShoppingCart(CreditCardPayment())
        self.assertEqual(cart.checkout(100), "Paid 100 using credit card.")

    def test_paypal_payment(self):
        cart = ShoppingCart(PayPalPayment())
        self.assertEqual(cart.checkout(50), "Paid 50 using PayPal.")
