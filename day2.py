#! /bin/python3

# bank=input("What is your bank account number?")
# print ("Your bank account number is "+bank+"")

# for i in bank:
#     int_i=int(i)
#     print (int_i+1, end="")

# print("")

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

## Caesar Shift Cipher

# Ask the user whether they want to encode or decode a string

# get the string

# encode or decode it using chr and ord

# that's pretty much it :)

# bonus: ask the user if they want a custom offset
while True:
    offset=int(input("What is the offset? "))
    choice=input("Would you like to encode or decode? ")
    if choice=="encode" or choice=="Encode":
        string=input("What would you like to encode? ")
        print ("Your encoded string is ", end="")
        for i in string:
            print(str((chr(ord(i)+offset))), end="")
        print("")
    if choice=="decode" or choice=="Decode":
        string=input("What would you like to decode? ")
        print ("Your decoded string is ", end="")
        for i in string:
            print (str((chr(ord(i)-offset))), end="")
        print("")
