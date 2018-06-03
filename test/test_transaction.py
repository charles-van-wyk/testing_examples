from unittest import TestCase
from account.transaction import Account, AccountType

class TestAccount(TestCase):
    #def setUp(self):

    # ===================================================================
    # ====================== CREATION METHODS ===========================
    # ===================================================================

    @staticmethod
    def account_with_negative_balance():
        """
        This account is used when testing available credit logic while trying
        to debit an account.
        :return: account with negative balance
        """
        account_in_red = Account()
        account_in_red.set_balance(-600)
        account_in_red.set_type(AccountType.SAVINGS)

    @staticmethod
    def account_with_100_balance():
        """
        :return: a newly created account object with a balance of
                 100.
        """
        account = Account()
        account.set_balance(100)
        return account

    # ===================================================================
    # ==================== START ACTUAL TESTS ===========================
    # ===================================================================

    def test_credit_when_balance_is_100_add_50_then_balance_is_150(self):
        """
        Testing that when the credit method is called
        that the balance increases by the specified amount.
        """
        account_under_test = TestAccount.account_with_100_balance()
        account_under_test.credit(50)
        self.assertEqual(
            150,
            account_under_test.get_balance(),
            "Opening balance was 100 and the account is credited with 50, "
            " the total should be 150."
        )

    def test_debit_when_balance_less_than_amount_then_fail_to_debit(self):
        """
        Attempt to debit an account with an amount which is more then
        the balance of the account.

        Account balance = 100
        attempt to debit = 500
        """
        account_under_test = TestAccount.account_with_100_balance()
        self.assertFalse(
            account_under_test.debit(500),
            "Account has insufficient balance to perform the debit, balance is 100 and attempt to"
            " debit 500."
        )