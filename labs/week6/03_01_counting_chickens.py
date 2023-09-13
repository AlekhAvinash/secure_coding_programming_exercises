"""
create a chicken class that has the following

# class attributes
time_of_day
number_of_eggs_laid

# instance attributes (uses the self variable)
breed
gender
weight
lays_eggs (boolean)

# methods
lay_egg --> this function should depend on time of day (chickens only lay eggs at night!),
it should also use random numbers to deterimine if laying the egg worked or not


## Create 100 instances of your chickens using a for loop

Use a for loop to update the time of day (go through each hour of the day)
within the loop have your chickens all try to lay eggs
Afterwards, print out how many total eggs were hatched -- for all chickens and individually.
What was the average number of eggs per chicken?
"""

from random import choice, randint

breedLst = ["Marans", "Cochin", "Ayam"]
gendrLst = ["Female", "Male"]

class chickens:
    _time = 0
    _eggs = 0

    def __init__(self, breed, time = None):
        self.breed = breed
        self.gendr = choice(gendrLst)
        self.wigts = randint(0, 6)
        self.laid_ = False
        if time:
            self._time = time

    def lay_eggs(self):
        self._eggs += 1
        self.laid_ = True
        return chickens(self.breed, self._time-1)
    
    def update_time(self):
        self._time = (self._time+1)%24
        if ((self._time+6)%24 in range(12)\
            and not bool(randint(0, 4))\
            and self.gendr == "Female"):
            return [self.lay_eggs()]
        return []
    
    def __str__(self):
        return f"{self._time}"

chiks = [chickens(choice(breedLst)) for i in range(10)]

for i in range(24*4):
    ctr = 0
    beg = len(chiks)
    while True:
        chiks += chiks[ctr].update_time()
        if ctr == len(chiks)-1:
            break
        ctr += 1
    fin = len(chiks)
    print(f"Day [{(i//12)+1}] Hour [{i%24:02}]:\nNumber of Tot Chikens: {fin}\nNumber of New Chickens: {fin-beg}\n\n")