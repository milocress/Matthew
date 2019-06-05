import math

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

def isevensum(x):
    return sum([int(a) for a in str(x)])%5==0

def sum7(x):
    return sum([int(a) for a in str(x)])>=7

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

lis=range(1, 100+1)


prime=input("Is your number prime? ")
if prime=="Yes" or prime=="yes":
    lis=filteryes(isprime, lis)
else:
    lis=filterno(isprime, lis)
    div_3=input("Is your number divisible by 3? ")
    if div_3=="yes" or div_3=="Yes":
        lis=filteryes (div, lis)
    else:
        lis=filterno(div, lis)
    root=input("Is your number square? ")
    if root=="yes" or root=="Yes":
        lis=filteryes(square, lis)
    else:
        lis=filterno(square,lis)
    cube=input("Is your number a cube? ")
    if cube=="yes" or cube=="Yes":
        lis=filteryes(iscube, lis)
    else:
        lis=filterno(iscube, lis)
        div8=input("Is your number divisible by 8? ")
        if div8=="yes" or div8=="Yes":
            lis=filteryes(isdiv8, lis)
        else:
            lis=filterno(isdiv8, lis)
evenback=input("Is your number even when written backwards? ")
if evenback=="yes" or evenback=="Yes":
    lis=filteryes(isevenback, lis)
else:
    lis=filterno(isevenback, lis)
evensum=input("Is the sum of the digits of your number a multiple of 5? ")
if evensum=="yes" or evensum=="Yes":
    lis=filteryes(isevensum, lis)
else:
    lis=filterno(isevensum, lis)
greatersum=input("is the sum of the digits of your number greater than 7?" )
if greatersum=="yes" or greatersum=="Yes":
    lis=filteryes(sum7, lis)
else:
    lis=filterno(sum7, lis)
proddig=input("Is the product of the digits of your number greater than or equal to 20? ")
if proddig=="yes" or proddig=="Yes":
    lis=filteryes(prod, lis)
else:
    lis=filterno(prod, lis)
greater=input("Is your number greater than 50?")
if greater=="yes" or greater=="Yes":
    lis=filteryes(isgreater, lis)
else:
    lis=filterno(isgreater, lis)
end=input("Does your number end in 1? ")
if end=="Yes" or end=="yes":
    lis=filteryes (end1, lis)
else:
    lis=filterno (end1, lis)
    even=input("Is your number even? ")
    if even=="yes" or even=="Yes":
        lis=filteryes(iseven, lis)
    else:
        lis=filterno(iseven, lis)

    end5=input("Does your number end in 5? ")
    if end5=="yes" or end5=="Yes":
        lis=filteryes(doesend5, lis)
    else:
        lis=filterno(doesend5, lis)
pal=input("Is your number a palindrome? ")
if pal=="yes" or pal=="Yes":
    lis=filteryes(ispal, lis)
else:
    lis=filterno(ispal, lis)

digit=input("Does your number have 2 digits? ")
if digit=="Yes" or digit=="yes":
    lis=filteryes(dig, lis)
else:
    lis=filterno(dig,lis)

print (str(lis))
