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

def iscloser(x):
    return x<75

def product(list):
    p = 1
    for i in list:
        p *= i
    return p

def add13(x):
    return sum([int(a) for a in str(x)])==13

def prod(x):
    return product([int(a) for a in str(x)])>=20

def filteryes (f, l):
    return[x for x in l if f(x)==True]

def filterno (f,l):
    return [x for x in l if f(x)==False]

def toText (x):
    if x:
        return "yes"
    else:
        return "no"

myrange=range(410,420+1)
tally=0
for num in myrange:

    lis=myrange

    prime= isprime(num)
    div_3= div(num)
    end= end1(num)
    even= iseven(num)
    pal= ispal(num)
    digit= dig(num)
    root= square(num)
    cube= iscube(num)
    greater= isgreater(num)
    end5= doesend5(num)
    div8= isdiv8(num)
    evenback= isevenback(num)
    evensum= isevensum(num)
    greatersum=sum7(num)
    proddig=prod(num)
    closer=iscloser(num)
    sum13=add13(num)
    if prime:
        lis=filteryes(isprime, lis)
    else:
        lis=filterno(isprime, lis)
        if div_3:
            lis=filteryes (div, lis)
        else:
            lis=filterno(div, lis)
        if root:
            lis=filteryes(square, lis)
        else:
            lis=filterno(square,lis)
        if cube:
            lis=filteryes(iscube, lis)
        else:
            lis=filterno(iscube, lis)
        if div8:
            lis=filteryes(isdiv8,lis)
        else:
            lis=filterno(isdiv8, lis)
    if evensum:
        lis=filteryes(isevensum, lis)
    else:
        lis=filterno(isevensum, lis)
    if evenback:
        lis=filteryes(isevenback, lis)
    else:
        lis=filterno(isevenback, lis)
    if greatersum:
        lis=filteryes(sum7, lis)
    else:
        lis=filterno(sum7, lis)
    if proddig:
        lis=filteryes(prod, lis)
    else:
        lis=filterno(prod, lis)
    if greater:
        lis=filteryes(isgreater, lis)
        if closer:
            lis=filteryes(iscloser, lis)
        else:
            lis=filterno(iscloser, lis)
    else:
        lis=filterno(isgreater, lis)

    if end:
        lis=filteryes (end1, lis)
    else:
        lis=filterno (end1, lis)
        if even:
            lis=filteryes(iseven, lis)
        else:
            lis=filterno(iseven, lis)

        if end5:
            lis=filteryes(doesend5, lis)
        else:
            lis=filterno(doesend5, lis)
    if pal:
        lis=filteryes(ispal, lis)
    else:
        lis=filterno(ispal, lis)

    if sum13:
        lis=filteryes(add13, lis)
    else:
        lis=filterno(add13, lis)
    if digit:
        lis=filteryes(dig, lis)
    else:
        lis=filterno(dig,lis)

    if len(lis)==1:
        tally+=1
        print (str(lis))

print (tally)
