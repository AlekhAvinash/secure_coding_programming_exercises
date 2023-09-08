# rewrite your function from the previous exercise (01_01_dry.py)
# this time your function should be able change the divisible by number.

# I should be able to return the list of numbers which is divisible by "n", where
# 'n' can be any number.

## Input: a list of integers, a number 'n'
## output: a new list that only has retains numbers which are divisible by n

numbers = [2, 1, 3, 5, 1, 2, 3, 12, 3, 45, 1, 2, 3]
other_numbers = [213, 2, 3, 125, 12, 32, 21, 3, 6, 23, 12, 3, 326, 45, 12, 32, 14, 2]

def filter_even(lst, n):
    return [i for i in lst if i % n == 0]

print(filter_even(numbers, 5))
print(filter_even(other_numbers, 5))