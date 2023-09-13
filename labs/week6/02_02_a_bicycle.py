"""
create a simple bicylce class

# Attributes
number of tires
type of of tires (road vs mountain bike)
model
color
number of speeds
brakes (front or back or both)
current speed.

# Methods
brake
pedal faster (should affect speed)
"""

from random import choice, randbytes, randint

class bicycle:
    _nTyrs = 2
    _tyrTp = choice(["road", "mountain bike"])
    _model = randbytes(3)
    _color = f"{randint(0, 0xFFFFFF):06x}"
    _nSpds = randint(0, 8)
    _brake = choice(["front", "back", "both"])
    _cSpds = randint(0, 8)

    def apyBrakes(self):
        self._cSpds -= 1
    
    def pdlFaster(self):
        self._cSpds += 1