
from enum import Enum


class AccountType(Enum):
    CHEQUE = 1
    SAVINGS = 2
    NONE = -5


class Account:

    def __init__(self):
        self.balance = 0.0
        self.type = AccountType.NONE
        self.account_number = 0

    def credit(self, amount):
        self.balance += amount

    def debit(self, amount):
        if 0 < self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


def pay_account(account_to_debit, account_to_credit, amount):
    """
    Transfer money from one account to another
    :param account_to_debit: account to subtract money from.
    :param account_to_credit: account to put money into
    :param amount: the amount of the transaction
    :return: true if the transaction was successful.
    """
    success = account_to_debit.debit(amount)
    if success:
        account_to_credit.credit(amount)
    return success


# def purchase(item_to_buy, account):




class AccountFactory():
    @staticmethod
    def open_new_account(account_type, opening_balance):
        if opening_balance < 1000:
            raise ValueError("Opening balance does not meet the minimum requirement.")
        elif account_type == AccountType.NONE:
            raise AssertionError("No account type specified.")

        new_account = Account()
        new_account.type = account_type
        new_account.opening_balance = opening_balance
        return new_account
