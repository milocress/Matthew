






a = 2 + 3


def f(x):
    return x*x

l = [1,3,5,6]

modified_list = [x * 0.15 for x in l]

# modified_list = [x * 0.15 for x in [1,3,5,6]]

# modified_list = [1 * 0.15, 3 * 0.15 ...]

def map (fun, lis):
    return [fun(x) for x in lis]

# Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
# [GCC 8.2.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> def map (fun, lis):
# ...     return [fun(x) for x in lis]
# ... 
# >>> def f(x):
# ...     return x*5
# ... 
# >>> map (f, [3,5,9,16])
# [15, 25, 45, 80]

