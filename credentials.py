import csv

class Credentials:
    """Class:
    Class that generates new instances of credentials
    """
    account_list = []
    
    def __init__(self,account_name,login,password):

        """Method:
        initializes class attributes
        """
        
        self.account_name = account_name
        self.login= login
        self.password = password
        
    def save_account_details(self):
        """Method:
        saves account
        """
        Credentials.account_list.append(self)
        file = "user_credentials.csv"
        with open(file, "a") as f:
            writer = csv.writer(f)
            writer.writerow(Credentials.account_list)
    
    def delete_account(self):
        """Method:
        deletes account
        """
        Credentials.account_list.remove(self)
    
    @classmethod
    def find_by_account_name(cls, account_name):
        """Method:
        finds account using login

        Args:
            login (str): user name credential
        """
        for account in cls.account_list:
            if account.account_name == account_name:
                return account
            
            
    @classmethod
    def account_exists(cls, account_name):
        """Method:
        checks if account exists

        Args:
            login (str): user name credential
        """
        for account in cls.account_list:
            if account.account_name == account_name:
                return True
        return False
    
    @classmethod
    def display_accounts(cls):
        """Method: 
        displays all the accounts
        """
        return cls.account_list
    

    # create account with login details 
    # store already existing account details 

    # choose self-generated or machine generated password
  