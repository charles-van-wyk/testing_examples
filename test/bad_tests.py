from unittest import TestCase
from account.transaction import Account, AccountFactory


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
        self.assertFalse(self.a.debit(150))

    def test_credit_then_debit(self):
        account = Account()
        account.credit(100)
        # test credit
        self.assertEqual(
            "Amount should be 100.",
            100,
            account.get_balance()
        )

        # test debit
        account.debit(50)
        self.assertEqual(
            "Amount should be 50.",
            50,
            account.get_balance()
        )

    def test_create_new_account_value_error(self):
        """
            Check bal < 1000
        """
        with self.assertRaises(ValueError):
            AccountFactory.open_new_account(1, 500)

    def test_create_new_account_wrong_type(self):
        with self.assertRaises(AssertionError):
                AccountFactory.open_new_account(-5, 1000)

    def test_create_valid_account(self):
        account = AccountFactory.open_new_account(1, 1000)
        self.assertIsNotNone(account, "Not none")
        self.assertEquals(account.get_balance(), 1000, "Incorrect balance")
        self.assertEquals(account.get_type(), 1, "Incorrect type")
