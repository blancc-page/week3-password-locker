import csv
import os
import os.path
from pathlib import Path

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
    
    def delete_account(self, account_name):
        """Method:
        deletes account
        """
        
        with open (f"{account_name}_credentials.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([])
        os.remove(f"{account_name}_credentials.csv")

    account_det = None
    @classmethod
    def find_by_account_name(cls, account_name):
        """Method:
        finds account using login

        Args:
            login (str): user name credential
        """
        if os.path.exists(f"{account_name}_credentials.csv"):
            with open (f"{account_name}_credentials.csv", "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    cls.account_list.append(row)
                    
            for account in cls.account_list:
                if account == account_name:
                    pass
            return account
        else:
            return False
        
            
            
    @classmethod
    def account_exists(cls, account_name):
        """Method:
        checks if account exists

        Args:
            login (str): user name credential
        """

        path = Path(f"{account_name}_credentials.csv")
        if path.is_file(): 
            with open (f"{account_name}_credentials.csv", "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    cls.account_list.append(row)
                    
            for account  in cls.account_list:
                if account == account_name:
                    return True
            return False

        else: 
            return False
    @classmethod
    def display_accounts(cls):
        """Method: 
        displays all the accounts
        """
        with open ("account_credentials.csv", "r", newline="") as f:
            acc_reader = csv.reader(f)
            for row in acc_reader:
                cls.account_list.append(Credentials(row, row, row))
        return cls.account_list

  