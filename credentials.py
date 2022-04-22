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
        
    def save_account(self):
        """Method:
        saves account
        """
        Credentials.account_list.append(self)
    
    def delete_account(self):
        """Method:
        deletes account
        """
        Credentials.account_list.remove(self)

    # create account with login details 
    # store already existing account details 
    # create new account details
    # choose self-generated or machine generated password
    # view account credentials and their passwords 
    # delete the credential account 