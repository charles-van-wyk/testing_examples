from unittest import TestCase
from account.transaction import (
    Account,
    AccountFactory,
    AccountType,
    find_interest_calculator,
    calculate_interest,
    ChequeAccountInterestCalculator
)


class TestAccountBad(TestCase):
    def setUp(self):
        self.a = Account()

    def test_credit_150(self):
        self.a.balance = 100
        self.a.credit(50)
        self.assertEqual(150, self.a.balance, "Should be 150")

    def test_debit_insufficient_funds(self):
        # Not enough funds in account
        self.a.balance = 100
        self.assertFalse(self.a.debit(150))

    def test_credit_then_debit(self):
        account = Account()
        account.credit(100)
        # test credit
        self.assertEqual(
            100,
            account.balance,
            "Amount should be 100."
        )

        # test debit
        account.debit(50)
        self.assertEqual(
            50,
            account.balance,
            "Amount should be 50."
        )

    def test_create_new_account_value_error(self):
        """
            Check bal < 1000
        """
        with self.assertRaises(ValueError):
            AccountFactory.open_new_account(AccountType.SAVINGS, 500)

    def test_create_new_account_wrong_type(self):
        with self.assertRaises(AssertionError):
                AccountFactory.open_new_account(AccountType.NONE, 1000)

    def test_create_valid_account(self):
        a = AccountFactory.open_new_account(1, 1000)
        self.assertIsNotNone(a, "Not none")
        self.assertEqual(a.balance, 1000, "Incorrect balance")
        self.assertEqual(a.type, 1, "Incorrect type")

    def test_cheque_account_interest(self):
        account = Account()
        account.balance = 100
        account.type = AccountType.CHEQUE
        calculator = find_interest_calculator(account.type)
        self.assertTrue(isinstance(calculator, ChequeAccountInterestCalculator), "Is a cheque account.")

        interest = calculate_interest(account, calculator)
        self.assertEqual(interest, 3, "3% of 100 is 3.")
