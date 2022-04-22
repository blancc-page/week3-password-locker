from credentials import Credentials

# create account with login details 


# store already existing account details 
# create new account details
def create_account(account, user_name, passcode):
    """Method:
    creates a new account

    Args:
        account (str): name of account
        user_name (str): user name credential
        passcode (str): secret code 

    Returns:
        new_account: list
    """
    new_account = Credentials(account, user_name, passcode)
    return new_account

def save_account(account):
    """Method:
    saves created accounts

    Args:
        account (list): account info
    """
    account.save_account()
# choose self-generated or machine generated password
# view account credentials and their passwords 
def display_account():
    """
    Function that returns all the saved accounts
    """    
    return Credentials.display_accounts()

# delete the credential account
def del_contact(account):
    """deletes an account

    Args:
        account (list): account info
    """    
    Credentials.delete_account(account)
    print(f"{account} deleted.")
    
    
