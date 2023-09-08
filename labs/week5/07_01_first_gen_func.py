## Write a generator that will produce a list of even numbers

# use a function


def list_of_even_nums(start, stop):
    ceil = lambda a: ((a+1)//2)*2
    for i in range(ceil(start), stop, 2):
        yield i

# use your generator
for i in list_of_even_nums(2, 11):
    print(i)
## should print out 2,4,6,8,10
