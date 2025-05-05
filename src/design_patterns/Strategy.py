from abc import ABC, abstractmethod

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# Concrete strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"Paid {amount} using credit card."

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"Paid {amount} using PayPal."

# Context class
class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def checkout(self, amount: float):
        return self.strategy.pay(amount)
