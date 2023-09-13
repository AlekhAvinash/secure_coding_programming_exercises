"""
implement a key-lookup procedure for a dictionary

Try to get the key and update the value by n
If an en exception is raised, handle it by creating the key with a default value
if no exception is raised, update the value
Regardless of what happens, print the dictionary
"""

def lookup(book: dict, n: int) -> dict:
    for i in book.keys():
        try:
            book[i] += n
        except TypeError:
            book[i] = n
    return book

print(lookup({1: 5, 2: 'hi', 3: 7}, 2))