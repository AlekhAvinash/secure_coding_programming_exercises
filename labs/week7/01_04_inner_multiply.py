# write a function accepts as input an infinite amount of tuples
# it returns a list, where each element is the inner multiplication

# example input: (1,2), (2,2), (3,2), (4,5)
# output: [2,4,6,20]

def innerMx(*inp: tuple) -> list[int]:
    try:
        for i in inp:
            assert len(i) == 2
    except:
        return []
    return [i*j for i, j in inp]

innerMx((4, 6), (2, 3), (3, 5), (1, 2))