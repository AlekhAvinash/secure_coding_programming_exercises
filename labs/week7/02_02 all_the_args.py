"""
Write a function that accepps the following arguments
INPUT:
    name: str
    job : str
    * args: adjectives (str) that describe things (i.e "happy", " sad")
    **args: possessions (str): value (int / float)
Output:
   Form a  nice string that explains everything relevant



example input:
   ('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike = 2000, house = 1000, shoes = 20)
output:
   "Gilad is a teacher who is happy, amazing, and sooooo cool. Gilad has a bike worth 2000, a house worth 1000, and shoes with 20"


The string should accomadate any number of *args and **kwargs.
"""

def prop(name, job, *args, **kargs):
    return f"{name} is a {job} who is {', '.join(args[:-1])} and {args[-1]}. {name} has a {', '.join([f'{i} worth {j}' for i, j in kargs.items()])}"

print(prop('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike = 2000, house = 1000, shoes = 20))