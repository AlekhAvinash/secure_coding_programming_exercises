## use ** unpacking to merge these dictionaries

dict1 = {1: 2, 3: 4, 5: 6}
dict2 = {2: 2, 10: 12, 15: 17}

## finish this code
merged_dict1 = {**dict1, **dict2}


big_dict = {i:i**2 for i in range(1000)}
other_big = {k:k for k in range(1000,2000)}

merged_dict2 = {**big_dict, **other_big}

print(merged_dict1)
print(merged_dict2)

## merge these two dicts as well ^^