from unittest import TestCase
from account.transaction import Account, AccountType, AccountFactory

# Constants for test cases
MIN_AMOUNT_FOR_NEW_ACCOUNT = 1000


class TestAccount(TestCase):
    # def setUp(self):


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
        account_in_red.balance = -600
        account_in_red.type = AccountType.SAVINGS

    @staticmethod
    def account_with_100_balance():
        """
        :return: a newly created account object with a balance of
                 100.
        """
        account = Account()
        account.balance = 100
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
            account_under_test.balance,
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

    def test_create_new_account_when_opening_balance_less_than_min_then_expect_error(self):
        """
        Attempt to create an account where the opening balance is less than the
        minimum balance allowed for a new account.
        :var MIN_AMOUNT_FOR_NEW_ACCOUNT defined in this test class contains the minimum
             amount for a new account.
        """
        with self.assertRaises(ValueError):
            AccountFactory.open_new_account(AccountType.CHEQUE, MIN_AMOUNT_FOR_NEW_ACCOUNT / 2)

    def test_create_new_account_when_invalid_account_type_then_expect_error(self):
        """
        Create a new account while supplying an invalid account type.
        """
        with self.assertRaises(AssertionError):
            AccountFactory.open_new_account(AccountType.NONE, MIN_AMOUNT_FOR_NEW_ACCOUNT)

    def test_create_new_account_when_all_details_are_valid_then_return_new_account(self):
        """
        Create a new account while meeting all the requirements.
        """
        account = AccountFactory.open_new_account(AccountType.SAVINGS, MIN_AMOUNT_FOR_NEW_ACCOUNT)
        self.assertIsNotNone(
            account,
            "Account should be created as all attributes are within the business rules"
        )
        self.assertEqual(
            account.balance,
            MIN_AMOUNT_FOR_NEW_ACCOUNT,
            "Balance should be the same as what was supplied to the factory."
        )
        self.assertEqual(
            account.type,
            AccountType.SAVINGS,
            "Account type should be the same as what was supplied to the factory."
        )