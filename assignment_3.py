from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


# Concrete Strategy 2
class DebitCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card.")


# Concrete Strategy 3
class UpiPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


# Concrete Strategy 4
class CashPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash.")


# Context Class
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
amount = float(input("Enter payment amount: "))

print("\nSelect Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Cash")

choice = int(input("Enter your choice: "))

if choice == 1:
    payment = CreditCardPayment()
elif choice == 2:
    payment = DebitCardPayment()
elif choice == 3:
    payment = UpiPayment()
elif choice == 4:
    payment = CashPayment()
else:
    print("Invalid Choice")
    exit()

processor = PaymentProcessor(payment)
processor.process_payment(amount)