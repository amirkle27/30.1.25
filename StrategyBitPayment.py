from typing import override
from StrategyPaymentInterface import StrategyPaymentInterface

class StrategyBitPayment(StrategyPaymentInterface):

    def __init__(self, bank_account: str):
        self.bank_account = bank_account

    @override
    def pay(self, amount: float):
        print(f"Paid {amount: .2f} using Bit from Bank Account {self.bank_account[-4:]}")