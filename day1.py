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

# Logs
# Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
# [GCC 8.2.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 9+3
# 12
# >>> a=5
# >>> a+3
# 8
# >>> a=2+3
# >>> b=3-2
# >>> a+b
# 6
# >>> def f(x):
# ...     return x*x
# ... 
# >>> f(8)
# 64
# >>> f(f(8))
# 4096
# >>> l = [12, 23, 45, 66]
# >>> [x * 0.15 for x in l]
# [1.7999999999999998, 3.4499999999999997, 6.75, 9.9]
# >>> def map (fun, lis):
# ...     return [fun(x) for x in lis]
# ... 
# >>> map
# <function map at 0x7f1610652c80>
# >>> g(x) = x * 8
#   File "<stdin>", line 1
# SyntaxError: can't assign to function call
# >>> def g(x):
# ...     return x * 8
# ... 
# >>> map (g, [3,6,9])
# [24, 48, 72]

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def filter (fun, lis):
    return [x for x in lis if fun(x)]

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
# >>> range(5)
# range(0, 5)
# >>> range(5).toList()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'range' object has no attribute 'toList'
# >>> range(5)
# range(0, 5)
# >>> xrange(5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'xrange' is not defined
# >>> list(range(5))
# [0, 1, 2, 3, 4]
# >>> True
# True
# >>> False
# False
# >>> 1
# 1
# >>> 2
# 2
# >>> 2 == 3
# False
# >>> 2 != 3
# True
# >>> sum(list(range(100))
# ... 
# ... )
# 4950
# >>> mod(2,3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'mod' is not defined
# >>> def f(x):
# ...     return (x%3==0)or (x%5==0)
# ... 
# >>> f(12)
# True
# >>> f(15)
# True
# >>> f(14)
# False
# >>> 
# >>> lis = (range(1000))
# >>> 
# >>> def filter = (f, lis):
#   File "<stdin>", line 1
#     def filter = (f, lis):
#                ^
# SyntaxError: invalid syntax
# >>> def filter (fun, lis):
# ...     return [x for x in lis if fun(x)==True]
# ... 
# >>> filter (f, lis)
# [0, 3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50, 51, 54, 55, 57, 60, 63, 65, 66, 69, 70, 72, 75, 78, 80, 81, 84, 85, 87, 90, 93, 95, 96, 99, 100, 102, 105, 108, 110, 111, 114, 115, 117, 120, 123, 125, 126, 129, 130, 132, 135, 138, 140, 141, 144, 145, 147, 150, 153, 155, 156, 159, 160, 162, 165, 168, 170, 171, 174, 175, 177, 180, 183, 185, 186, 189, 190, 192, 195, 198, 200, 201, 204, 205, 207, 210, 213, 215, 216, 219, 220, 222, 225, 228, 230, 231, 234, 235, 237, 240, 243, 245, 246, 249, 250, 252, 255, 258, 260, 261, 264, 265, 267, 270, 273, 275, 276, 279, 280, 282, 285, 288, 290, 291, 294, 295, 297, 300, 303, 305, 306, 309, 310, 312, 315, 318, 320, 321, 324, 325, 327, 330, 333, 335, 336, 339, 340, 342, 345, 348, 350, 351, 354, 355, 357, 360, 363, 365, 366, 369, 370, 372, 375, 378, 380, 381, 384, 385, 387, 390, 393, 395, 396, 399, 400, 402, 405, 408, 410, 411, 414, 415, 417, 420, 423, 425, 426, 429, 430, 432, 435, 438, 440, 441, 444, 445, 447, 450, 453, 455, 456, 459, 460, 462, 465, 468, 470, 471, 474, 475, 477, 480, 483, 485, 486, 489, 490, 492, 495, 498, 500, 501, 504, 505, 507, 510, 513, 515, 516, 519, 520, 522, 525, 528, 530, 531, 534, 535, 537, 540, 543, 545, 546, 549, 550, 552, 555, 558, 560, 561, 564, 565, 567, 570, 573, 575, 576, 579, 580, 582, 585, 588, 590, 591, 594, 595, 597, 600, 603, 605, 606, 609, 610, 612, 615, 618, 620, 621, 624, 625, 627, 630, 633, 635, 636, 639, 640, 642, 645, 648, 650, 651, 654, 655, 657, 660, 663, 665, 666, 669, 670, 672, 675, 678, 680, 681, 684, 685, 687, 690, 693, 695, 696, 699, 700, 702, 705, 708, 710, 711, 714, 715, 717, 720, 723, 725, 726, 729, 730, 732, 735, 738, 740, 741, 744, 745, 747, 750, 753, 755, 756, 759, 760, 762, 765, 768, 770, 771, 774, 775, 777, 780, 783, 785, 786, 789, 790, 792, 795, 798, 800, 801, 804, 805, 807, 810, 813, 815, 816, 819, 820, 822, 825, 828, 830, 831, 834, 835, 837, 840, 843, 845, 846, 849, 850, 852, 855, 858, 860, 861, 864, 865, 867, 870, 873, 875, 876, 879, 880, 882, 885, 888, 890, 891, 894, 895, 897, 900, 903, 905, 906, 909, 910, 912, 915, 918, 920, 921, 924, 925, 927, 930, 933, 935, 936, 939, 940, 942, 945, 948, 950, 951, 954, 955, 957, 960, 963, 965, 966, 969, 970, 972, 975, 978, 980, 981, 984, 985, 987, 990, 993, 995, 996, 999]
# >>> sum(filter(f, lis))
# 233168
