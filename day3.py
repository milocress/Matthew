# balance = 2000
# while True:
#     bank=int(input("what is your bank account number? "))
#     if bank%2==0:
#         print ("Access Granted")
#         choice=input("Withdraw or deposit?")
#         if choice=="Withdraw" or choice=="withdraw":
#             amount=int(input("How much money would you like to withdraw? "))
#             if amount < balance:
#                 balance = balance-amount
#                 print ("Your balance is " + str(balance))
#             if amount > balance:
#                 print ("Insufficient Funds")
#         if choice=="Deposit" or choice=="deposit":
#             amount=int(input("How much money would you like to deposit? "))
#             balance = balance+amount
#             print ("Your balance is " + str(balance))
#         # ask if the customer wants to deposit or withdraw
#         # ask how much
#         # change balance accordingly
#         # BONUS: don't let them withdraw more than they have.
#     if bank%2!=0:
#         print ("Access Denied")


# Day 3

# Add the ability to access individual accounts

# Add the ability to create new accounts

# Dictionary data structure python
def withdraw(username, manual=True, amount=0): # you may need an argument here
    if manual == True:
        amount=int(input("How much money would you like to withdraw? "))
    if amount < users[username]["balance"]:
        users[username]["balance"] -= amount
        if manual == True:
            print ("Your balance is " + str(users[username]["balance"]))
            return True
    if amount > users[username]["balance"]:
        print ("Insufficient Funds")
        return False

def deposit(username, manual=True, amount=0): # you may need an argument here
    if manual == True:
        amount=int(input("How much money would you like to deposit? "))
    users[username]["balance"] += amount
    if manual == True:
        print ("Your balance is " + str(users[username]["balance"]))

def transfer(username):
    recipient=input("To whom would you like to transfer your money?")
    amount=int(input("How much money would you like to transfer?"))
    if withdraw(username, manual=False, amount=amount) == True:
        deposit(recipient, manual=False, amount=amount)
    print ("Your new balance is " + str(users[username]["balance"]) + ". " + recipient + "'s new balance is " + str(users[recipient]["balance"]) + ".")

def view(username):
    print ("Your balance is " + str(users[username]["balance"]) + ".")

def f(username):
    print ("Access Granted")
    choice=input("Would you like to view, withdraw, deposit or transfer? ")
    if choice=="View" or choice=="view":
        view(username)
    if choice=="Withdraw" or choice=="withdraw":
        withdraw(username)
    if choice=="Deposit" or choice=="deposit":
        deposit(username)
    if choice=="Transfer" or choice== "transfer":
        transfer(username)

def add_interest():
    for username in users:
        users[username]["balance"] *= 1.01

users = { "milo" : {"password" : "password123", "balance" : 2000000}
          , "matthew" : {"password" : "123", "balance" : -100000}
        }
while True:
    # add_interest()
    username=input("What is your username? ")
    if username in users:
        password=input("What is your password? ")
        if password == users[username]["password"]:
            # ... snip ...
            f(username)
        else:
            print("Access Denied")
    else:
        new_user=input("User not found. Would you like to create an account? ")
        if new_user=="yes" or new_user=="Yes":
            new_username=username
            new_password=input("What is your new password? ")
            users[new_username] = {"password" : new_password, "balance" : 0}
            print ("Account Created")
            f(new_username)
        if new_user=="no" or new_user=="No":
            print ("Access Denied")


