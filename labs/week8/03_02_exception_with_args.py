"""
rewrite inner_multiple from  Week 8

# write a function accepts as input an infinite amount of tuples
# it returns a list, where each element is the inner multiplication

# example input: (1,2), (2,2), (3,2), (4,5)
# output: [2,4,6,20]


Iterate over the args summing them up. 
Use an if statement ot check if the user passed tuples.
Raise an exception if they passed something else
"""
def innerMx(*inp: tuple) -> list[int]:
    if not all([isinstance(i, tuple) and len(i) == 2  for i in inp]):
        raise Exception("Only two integer tuples are accepted.")
    return [i*j for i, j in inp]

print(innerMx((4, 6, 3), (2, 3), (3, 5), (1, 2)))