

import csv


# with open("credentials.csv", "a", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow (["Account Name","User name","Password"])
#             writer.writerow(["Instagram","Moses","123"])
        
# with open("credentials.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(["", "", ""])

# new_account = ["Instagram","Moses","123"]
# with open("credentials.csv", "a", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow(new_account)

f = open("credentials.csv", "w", newline="")
writer = csv.writer(f)
writer.writerow(["Instagram","Moses","123"])






# create account with login details @
# store already existing account details @
# create new account details @
# choose self-generated or machine generated password
# view account credentials and their passwords @
# delete the credential account 

