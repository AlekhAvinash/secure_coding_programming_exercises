"""
Create a class (you pick the name) that has
at least 5 methods.
3 of the methods must call other methods within them (using self.method name)
Run at least one method automatically in __init__ so it will run at start up

Demonstrate your methods work by creating an instance and running all the methods
"""

from math import pi

szeLst = {1: range(200), 2: range(200, 400), 3: range(400, 600)}

class baloon:
    def __init__(self, rad: int) -> None:
        self.rad = rad
        self.pop = False
        self.vol = self.calcVol()
    
    def calcVol(self):
        vol = (4*pi*pow(self.rad, 3))/3
        self.setSize(vol)
        self.setDiam()
        return vol
    
    def setSize(self, vol):
        for i in sorted(szeLst.keys()):
            if vol in szeLst[i]:
                self.siz = i
        
        if szeLst[i].stop<vol:
            self.hasPopped()
    
    def setDiam(self):
        self.dia = self.rad*2
    
    def hasPopped(self):
        self.pop = True