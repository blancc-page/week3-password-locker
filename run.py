import random
import string
from credentials import Credentials
from user import User
import csv


# Store exiting account detials
def create_account(site, user_name, passcode):
    """Method:
    creates a new account

    Args:
        account (str): name of account
        user_name (str): user name credential
        passcode (str): secret code 

    Returns:
        new_account: list
    """
    new_account = Credentials(site, user_name, passcode)
    return new_account

def create_user(login, password):
    """Method:
    creates a new account

    Args:
        account (str): name of account
        user_name (str): user name credential
        passcode (str): secret code 

    Returns:
        new_account: list
    """
    new_user = User(login, password)
    return new_user

def save_account(account):
    """Method:
    saves created accounts

    Args:
        account (list): account info
    """
    account.save_account_details()
    
def save_user(user):
    """Method:
    saves created accounts

    Args:
        account (list): account info
    """
    user.save_user_details()

def find_account(account):
    """searches for number

    Args:
        number (str): phone number
    """
    
    return Credentials.find_by_account_name(account)

def find_user(user):
    """searches for number

    Args:
        number (str): phone number
    """
    
    return User.find_by_user_name(user)

def check_existing_accounts(account):
    """checks if number exists

    Args:
        number (str)): phone number
    """    
    return Credentials.account_exists(account)



# Store exiting account detials
def display_account():
    """
    Function that returns all the saved accounts
    """    
    return Credentials.display_accounts()

# Store exiting account detials
def del_contact(account, account_name):
    """deletes an account

    Args:
        account (list): account info
    """    
    Credentials.delete_account(account, account_name)
    # print(f"{account} deleted.")
    
    
def main():    
    users = []
    accounts = []
    user_name=""
    with open ("user_credentials.csv", "r", newline="") as f:
        user_reader = csv.reader(f)
        for row in user_reader:
            users.append(row)
            
        with open ("account_credentials.csv", "r", newline="") as f:
            acc_reader = csv.reader(f)
            for row in acc_reader:
                accounts.append(row)
                
    while True:        
        print("***********************************************")
        print('\n')
        print("       Hello Welcome to Password Locker.       ")
        print('\n')
        print("***********************************************")
        print('\n')

    
        print("Would you like to:")
        print("( 1 ) Sign Up?")
        print("( 2 ) Log In?")
        print("( 3 ) Exit?")
            
        short_code = input().lower()
        print('\n')

        if short_code == '1':
                    print("***********************************************")
                    print("                   Sign Up                     ")
                    print("***********************************************")

                    print("Login ...")
                    user_name = input()

                    print("Password ...")
                    passcode_input = input()
                    print("Confirm Password ...")
                    passcode_confirm = input()

                    while passcode_input != passcode_confirm:
                        print("Oooops! Passwords didn't match")
                        print('\n')
                        print("Re-enter your password:")
                        passcode_input = input()
                        print("Re-confirm your password:")
                        passcode_confirm = input()
                    else:
                        print(f"Congratulations {user_name}! Account creation successful. Sign in again to access your account.")
                        print('\n')
                        file = "user_credentials.csv"
                        with open(file, "a", newline="") as f:
                            writer = csv.writer(f)
                            writer.writerow([user_name, passcode_input])
                        
                    save_user(create_user(f"user_name", f"passcode_input"))
                    # print("***********************************************")
                    # print("                    Log In                     ")
                    # print("***********************************************")
                    # print('\n')
                    # print("User name")
                    # user_name_input = input()
                    # print("Password")
                    # password_input = input()
                    
                    # while user_name_input != user_name or passcode_input != password_input:
                    #     print("Invalid username or password. please try again.")
                    #     print("User name")
                    #     user_name_input = input()
                    #     print("Password")
                    #     password_input = input()
                    
                    # else:
                    #     print(f"Welcome to your account {user_name}")
                    #     print('\n')
                        # file = "user_credentials.csv"
                        # with open(file, "a", newline="") as f:
                        #     writer = csv.writer(f)
                        #     writer.writerow([user_name, password_input])
                        
                        # save_user(create_user(user_name, password_input))
                    # print('\n')
                    # print(f"New {site} account created for {user_name}.")
                    # print('\n')
                    
        elif short_code == '2':
                    with open ("user_credentials.csv", "r", newline="") as f:
                        reader = csv.reader(f)
                        for row in reader:
                            User.user_list.append(row)
                    print('\n')
                    print("***********************************************")
                    print("                    Log In                     ")
                    print("***********************************************")
                    print('\n')
                    print("Welcome \n Enter User Name:")
                    user_name_input = input()
                    print("Enter password:")
                    password_input = input()
                    credentials_combination = [user_name_input, password_input]
                    
                    #todo: csv search
                    
                    while find_user(credentials_combination) != True:
                        print("Login Failed")
                        print("Invalid username or password. please try again.")
                        print("User name")
                        user_name_input = input()
                        print("Password")
                        password_input = input()
                        credentials_combination = [user_name_input, password_input]
                        
                    else:
                        print("***********************************************")
                        print(f"               {user_name_input}'s Account                ")
                        print("***********************************************")
                        print('\n')

                    print("Would you like to:\n")
                    print("( 1 ) Store account detials ?")
                    print("( 2 ) View account details with passwords ?")
                    print("( 3 ) Delete an account ?")
                    print("( 4 ) Exit ?")
                    
                    short_code = input().lower()
                    print('\n')
                    
                    if short_code == '1':
                        print("***********************************************")
                        print("                 Store Details                 ")
                        print("***********************************************")
                        print("Software ...")
                        site = input()
                        print("Login ...")
                        user_name = input()
                        print("Would you like me to generate a password for you?( Y ) \n Or would you like to input your own?( N )")
                        answer = input().lower()
                        print("\n")

                        if answer == "y":
                        #     # todo: password generation
                            length = int(input('\nEnter the length of password: '))                      
                            #define data
                            lower = string.ascii_lowercase
                            upper = string.ascii_uppercase
                            num = string.digits
                            symbols = string.punctuation
                            #string.ascii_letters

                            #combine the data
                            all = lower + upper + num + symbols

                            #use random 
                            temp = random.sample(all,length)

                            #create the password 
                            passcode_input = "".join(temp)
                            print(passcode_input)
                            
                            file = f"{user_name}_credentials.csv"
                            with open(file, "a", newline="") as f:
                                writer = csv.writer(f)
                                writer.writerow([Credentials(site, user_name, passcode_input)])
                            
                            file = "account_credentials.csv"
                            with open(file, "a", newline="") as f:
                                writer = csv.writer(f)
                                writer.writerow([site, user_name, passcode_input])
                        
                            save_account(create_account(site, user_name, passcode_input))

                            print("Password Created Successfully.")
                            #print the password
                            # print(password)
                        elif answer == "n":
                            print("Password ...")
                            passcode_input = input()
                            print("Confirm Password ...")
                            passcode_confirm = input()
                            
                            while passcode_input != passcode_confirm:
                                print("Oooops! Passwords didn't match")
                                print('\n')
                                print("Re-enter your password:")
                                passcode_input = input()
                                print("Re-confirm your password:")
                                passcode_confirm = input()
                            else:
                                print(f"Congratulations details for {user_name}'s account stored successfuly.")
                                print('\n')
                                
                            file = f"{user_name}_credentials.csv"
                            with open(file, "a", newline="") as f:
                                writer = csv.writer(f)
                                writer.writerow([site, user_name, passcode_input])
                            
                            file = "account_credentials.csv"
                            with open(file, "a", newline="") as f:
                                writer = csv.writer(f)
                                writer.writerow([site, user_name, passcode_input])
                                                        
                        
                            save_account(create_account(site, user_name, passcode_input))
                               
                    elif short_code == '2':
                        print("***********************************************")
                        print("             View Account Details              ")
                        print("***********************************************")
                        if display_account():
                            print("Here is a list of all your accounts")
                            print('\n')

                            with open ("account_credentials.csv", "r", newline="") as f:
                                acc_reader = csv.reader(f)
                                for row in acc_reader:
                                    accounts.append(row)
                            for accounts in display_account():
                                print(f"Account Name: {accounts.account_name[0]} Login: {accounts.login[1]} Password:{accounts.password[2]}")
                                print('\n')
                        else:
                            print('\n')
                            print("You dont seem to have any accounts saved yet")
                            print('\n')
                        
                    elif short_code == '3':
                        print("***********************************************")
                        print("               Delete an Account               ")
                        print("***********************************************")
                        print("Enter the contact you wish to delete:")
                        search_site = input()
                        # if check_existing_accounts(search_site):
                        
                        while find_account(search_site):
                            search_account = find_account(search_site)
                            print(f"Are you sure you want to delete {search_account[1]}'s account for the {search_account[0]} website/app/platform? Y for Yes and N for No.")
                            answer = input().lower()
                            if answer == "y":
                                    del_contact(search_account, search_site)
                                    print(f"{search_account[1]}'s account is deleted.")
                            elif answer == "n":
                                    print("Not Deleted")
                            else:
                                print("Invalid Option")

                    elif short_code == '4':
                        print("***********************************************")
                        print("                     Exit                      ")
                        print("***********************************************")
                        print("\n")
                        print("Sad to see you go. Bye :(")
                        exit()
                    else:
                        print("Ooops! Please Pick ( 1 ) - ( 4 )")
                        
        elif short_code == "3":
                    print("***********************************************")
                    print("                     Exit                      ")
                    print("***********************************************")
                    print("\n")
                    print("Sad to see you go. Bye :(")
                    print("\n")
                    exit()


        else:
                    print("I really didn't get that. Please use the short codes")
                    
if __name__ == '__main__':
    
    main()