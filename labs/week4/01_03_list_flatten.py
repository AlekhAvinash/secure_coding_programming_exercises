#Exercise

# Write a Python program to flatten a shallow list

#Sample Input: [[2,4,3],[1,5,6], [9], [7,9,0]]
#Output: [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

def flatten(lst):
    out = []
    for i in lst:
        if type(i)!=int:
            out += flatten(i)
        else:
            out += [i]
    return out

print(flatten([[1,2,3,4], [1,2,[1,2]], 1, 2, [1, [2, [3], 4]]]))