
from enum import Enum


class AccountType(Enum):
    CHEQUE = 1
    SAVINGS = 2
    NONE = -5


class Account:

    def __init__(self):
        self._balance = 0.0
        self._type = AccountType.NONE


    def set_balance(self, new_balance):
        self._balance = new_balance

    def get_balance(self):
        return self._balance

    def set_type(self, new_type):
        self._type = new_type

    def get_type(self):
        return self._type


    def credit(self, amount):
        self._balance += amount

    def debit(self, amount):
        if 0 < self._balance >= amount:
            self._balance -= amount
            return True
        else:
            return False


def pay_account(account_to_debit, account_to_credit, amount):
    success = account_to_debit.debit(amount)
    if success:
        account_to_credit.credit(amount)
    return success

def open_new_account(account_type, opening_balance):
    if opening_balance <= 1000:
        raise ValueError("Opening balance does not meet the minimum requirement.")
    elif account_type == AccountType.NONE:
        raise ValueError("No account type specified.")
    new_account = Account()
    new_account.set_type(account_type)
    new_account.set_balance(opening_balance)
    return new_account
