"""
Update your chicken class to include the following dunders

__str__  : make some nice str format for your chicken. 
When we print your chicken it should tell us: how heavy the chicken is, the gender and how many eggs it has laid (if has)

__add__ : what happens when you add two chickens together? If they are male and female, create a baby chicken! (a new chicken) Otherwise, nothing?

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
    
    def __add__(self, other):
        if self.gendr != other.gendr:
            return [self.lay_eggs()]
        return []

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