from unittest import TestCase
from account.transaction import Account


class TestAccountBad(TestCase):
    def setUp(self):
        self.a = Account()

    def test_credit_150(self):
        self.a.set_balance(100)
        self.a.credit(50)
        self.assertEqual(150, self.a.get_balance(), "Should be 150")


    def test_debit_insufficient_funds(self):
        # Not enough funds in account
        self.a.set_balance(100)
        self.assertFalse(
            self.a.debit(150),
        )
