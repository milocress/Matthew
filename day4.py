import math
import sys

def isprime(x):
    if (x)==1:
        return False
    lis_prime=range(2,x)
    return [a for a in lis_prime if x%a==0] == []

def end1(x):
    return x%10==1

def div(x):
    return x%3==0

def iseven(x):
    return x%2==0

def ispal(x):
    return str(x)[::-1]==str(x)

def dig(x):
    return len(str(x))==2

def square(x):
    return math.sqrt(x)==int(math.sqrt(x))

def iscube(x):
    return int(round(x ** (1. / 3))) ** 3 == x

def isgreater(x):
    return x>50

def doesend5 (x):
    return x%10==5

def isdiv8 (x):
    return x%8==0

def isevenback(x):
    return int(str(x)[::-1])%2==0

def isdiv5(x):
    return sum([int(a) for a in str(x)])%5==0

def sum7(x):
    return sum([int(a) for a in str(x)])>=7

def iscloser(x):
    return x<75

def add13(x):
    return sum([int(a) for a in str(x)])==13

def product(list):
    p = 1
    for i in list:
        p *= i
    return p

def prod(x):
    return product([int(a) for a in str(x)])>=20

def filteryes (f, l):
    return[x for x in l if f(x)==True]

def filterno (f,l):
    return [x for x in l if f(x)==False]

lis=list(range(1, 100+1))

def helper(question, pred):
    yesno=input(question)
    if yesno=="yes" or yesno=="Yes" or yesno=="y":
        lis[:]=filteryes(pred, lis)
        testExitCondition()
        return True
    else:
        lis[:]=filterno(pred, lis)
        testExitCondition()
        return False

def testExitCondition():
    if len(lis)==1:
        if lis[0] == 69:
            print ("hehehe")
            print ("hehehe")
            print ("nice")
        print("Your number is " + str(lis[0]))
        sys.exit()

if helper("Is your number prime? ", isprime):
    pass
else:
    helper("Is your number divisible by 3? ", div)
    helper("Is your number square? ", square)
    helper("Is your number cube? ", iscube)
    helper("Is your number divisible by 8? ", isdiv8)

helper("Is your number even when written backwards? ", isevenback)
helper("Is the sum of the digits of your number divisible by 5? ", isdiv5)
helper("Is the sum of the digits of your number greater than or equal to 7? ", sum7)
helper("Is the product of the digits of your number greater than or equal to 20? ", prod)

if helper("Is your number greater than 50? ", isgreater):
    helper("Is your number closer to 50 than it is to 100? ", iscloser)

if helper("Does your number end in 1? ", end1):
    pass
else:
    if helper("Is your number even? ", iseven):
        pass
    else:
        helper("Does your number end in 5? ", doesend5)

helper("Is your number a palindrome? ", ispal)
helper("Is the sum of your digits 13? ", add13)
helper("Does your number have 2 digits? ", dig)

if len(lis)==2:
    guess=input("Is your number " + str(lis[0]) + "? ")
    if guess=="Yes" or guess=="yes":
        sys.exit()
    else:
        print("Your number is " + str(lis[1]))
if len(lis)==0:
    print("Check your answers and try again")
