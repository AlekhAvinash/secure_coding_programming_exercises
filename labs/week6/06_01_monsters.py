"""
Write 3 classes which are related to each other
1) a monster class
2) a night-monster class (they only come out at night)
3) a full moon monster class (they only come out at night and on the full moon)

Make use of inheritance to save your code!

## Monster class
# class attribute
time_of_day (will need to activate night monsters)
day_of_month
full_moon (boolean)

# attributes
name
number of limbs
attack mode (magic, physical, mental hypnosis etc)
scare factor
weakness
life points

# methods
basic attack (attack something)
sleep (get life points back)
defend (something attacks it!)

## Night monster
same as above, but also special powers that activate at night
vulnerable in daylight


## full moon monster
only active in the full moon
"""

class Monster:
    time_of_day = 0
    day_of_month = 0
    full_moon = False
    fctr = {"vampire": 5, "undead": 4, "werewolf": 3, "dargon": 2, "mummy": 1}
    atks = {"slash": 1, "intimidate": 3, "poison": 5}

    def __init__(self, name: str, limbs: int, atkMode: str, scrFctr: str, weaknes: str, lp: int):
        self.name = name
        self.limbs = limbs
        self.atkMode = atkMode
        self.scrFctr = scrFctr
        self.weaknes = weaknes
        self.lp = lp
    
    def attack(self, other):
        dmg = 1
        if other.weakness == self.scrFctr:
            dmg += self.fctr[self.scrFctr]
        
        dmg += self.atks[self.atkMode]

        dmg = other.defend(dmg)
    
    def sleep(self):
        self.lp += 1
    
    def defend(self, dmg):
        if self.limbs>2:
            dmg -= 2
        
        self.lp -= dmg

class NightMonster(Monster):
    def __init__(self, name: str, limbs: int, atkMode: str, scrFctr: str, weaknes: str, lp: int):
        super().__init__(name, limbs, atkMode, scrFctr, weaknes, lp)
        self.check = lambda: (self.time_of_day + 6)%24 < 12

    def attack(self):
        super().attack()
        if self.check():
            self.lp += 2

    def sleep(self):
        super.sleep()
        if self.check():
            self.lp += 1            

    def defend(self, dmg):
        super().defend(dmg)
        if self.check():
            self.dmg += 2
        else:
            self.dmg -= 2

class FullMoonMonster(NightMonster):
    def __init__(self, name: str, limbs: int, atkMode: str, scrFctr: str, weaknes: str, lp: int):
        super().__init__(name, limbs, atkMode, scrFctr, weaknes, lp)
        if not self.full_moon:
            self.lp = None