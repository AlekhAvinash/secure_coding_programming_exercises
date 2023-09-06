### This code creates a random list for you to use
from random import randint as rin

randlent = rin(1, 20)
randlist = [rin(1, 100) for i in range(randlent)]

def pair_fnct(lst, lnt):
    lst = sorted(lst)
    if lnt%2:
        lst += [0]
        lnt += 1
    return [(lst[i], lst[i+1]) for i in range(0, lnt, 2)]

print(randlent, randlist)
print(pair_fnct(randlist, randlent))

# Write a script that takes randlist (a list of numbers) and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.

# Note: This lab might be challenging! Make sure to discuss ask questions
# and get help!  You will need a python function called `sort`

# example input :[1,2,5,1,2]
# example output :[(1,1), (2,2), (5,0)]
