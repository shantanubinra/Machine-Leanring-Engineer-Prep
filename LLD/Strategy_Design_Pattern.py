from abc import ABC,    abstractmethod  


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self,amount:float):
        pass


class CreditcardProcessor(PaymentStrategy):
    def pay( self, amount:float):
        print(f"Paying using  {amount} using Credit Card")

class UPIProcessor(PaymentStrategy):
    def pay(self,amount:float):
        print(f"Paying using  {amount} using UPI")


class DebitcardProcessor(PaymentStrategy):
    def pay(self,amount:float):
        print(f"Paying using  {amount} using Debit Card")



class PaymentProcessor:
    def __init__(self,strategy:PaymentStrategy):
        self.strategy = strategy

    def make_payment(self,amount:float):
        self.strategy.pay(amount)


if __name__ == "__main__":
    # Let's say the user chooses UPI
    upi = UPIProcessor()
    processor = PaymentProcessor(upi)
    processor.make_payment(100.0)

    # Now user chooses Credit Card
    credit = CreditcardProcessor()
    processor.strategy = credit
    processor.make_payment(250.0)

    # Now user switches to PayPal
    debitcard = DebitcardProcessor()
    processor.strategy = debitcard
    processor.make_payment(500.0)