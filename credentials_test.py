
import unittest
import csv
from credentials import Credentials



class TestCredentials(unittest.TestCase):
    """Test Class:
    defines test case for the credentail class behaviours

    Args:
        unittest (module): helps to create test cases
    """
    def setUp(self):
        """Method:
        runs before each test case
        """
        self.new_account = Credentials("Instagram","Moses","123")
    
    def tearDown(self):
        """
        does cleanup after each test case has run 
        """

        Credentials.account_list = []
        
    def test_init(self):
        """Method:
        check if initialization is successful
        """
        self.assertEqual(self.new_account.account_name, "Instagram")
        self.assertEqual(self.new_account.login, "Moses")
        self.assertEqual(self.new_account.password, "123")
    
    def test_save_account(self):
        """Method:
        tests if save is successful
        """
        self.new_account.save_account()
        self.assertEqual(len(Credentials.account_list), 1)
    
    def test_save_accounts(self):
        """Method:
        tests if multiple accounts can be saved successfully
        """
        self.new_account.save_account()
        test_account = Credentials("Test","Test","Test")
        test_account.save_account()
        self.assertEqual(len(Credentials.account_list), 2)
        
    def test_delete_account(self):
        """Method:
        tests if deletion is succesful
        """
        self.new_account.save_account()
        test_account = self.new_account = Credentials("Instagram","Moses","123")
        test_account.save_account()
        
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.account_list), 1)
        
if __name__ == "__main__":
    unittest.main() 