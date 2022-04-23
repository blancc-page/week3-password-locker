import csv

class User:
    """Class:
    Class that generates new instances of users
    """
    user_list = []
    
    def __init__(self,login,password):
        self.login = login
        self.password = password
        
    def save_user_details(self):
        """Method:
        saves account
        """
        User.user_list.append(self)
        
    
    @classmethod
    def find_by_user_name(cls, cred_combo):
        """Method:
        finds account using login

        Args:
            login (str): user name credential
        """
        with open ("user_credentials.csv", "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                cls.user_list.append(row)
        # print(cls.user_list)
        # print(cred_combo)
                
        for user in cls.user_list:
            if user[1] == cred_combo[1]:
                # return user
                return True
        return False
        

                
