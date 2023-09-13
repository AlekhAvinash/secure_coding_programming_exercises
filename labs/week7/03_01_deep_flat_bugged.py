# debug this code
# I broke all kinds of things. NOTHING is safe !!!


# Make your list flatten code do a DEEP flatten and account for other datatypes

hard_nested_list = [
    [1, 2, [1, [1, 2], 2], 3, 4],
    [5, 6],
    [7, 8, 9],
    "shiva",
    10,
    [1, 2, [8, 9,], "Devi"],
    10.0,
    (1, 2),
]

# should get back
# [1, 2, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 'shiva', 10, 1,2,8,9, "Devi", 10.0, 1, 2]

many_nests = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", "h"]
# should get back
# ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']

final_list = hard_nested_list
while True:
    flag = True
    print(final_list)
    for c, element in enumerate(final_list):
        if isinstance(element, list):
            final_list += final_list.pop(c)
            flag &= False
        elif isinstance(element, tuple):
            final_list += list(final_list.pop(c))
            flag &= False
        else:
            flag &= True
        
    if flag:
        break

print(final_list)