"""
Use JSON to serialize the following dictionary

"""
import json

my_dict = {f'{i}': i ** 2 for i in range(10)}
with open("tester", "w") as f:
    json.dump(my_dict, f)

with open("tester", "r") as f:
    nx_dict = json.load(f)

print(nx_dict)
assert nx_dict == my_dict
# after creating your JSON file, try opening it the file by double clicking it in the explorer
# can you read it ? Why or why not?

# use code to load your json file into a new variable
# print it out to make sure it's the same.
