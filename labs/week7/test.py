# write a function that takes an infinite number of arguments
# it should check if the argument are integers and then sum all integeres
# it should return the sum of all the arguments


# example
# input: 1,2,3,4,'hi','hi',(1,2,3), 10
# output: 20

# example 2
# input: 2,2,2,200.2           # **note*** that 200.2 is _not_ an integer, so we don't sum it.
# output: 6


x = 10

def sum_ints(*inp):
    out = 0
    for i in inp:
        if type(i) == int:
            out += i
    return out

def main():
    print(sum_ints(1,2,3,4,'hi','hi',(1,2,3), 10))
    print(sum_ints(2,2,2,200.2))

if __name__ == '__main__':
    main()