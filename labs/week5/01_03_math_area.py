# write a function that takes the length and width of a rectangle and returns the area


# write another function that finds the area of a cube
# bonus challenge: use your first function inside this function!


# write a function that finds the area of a sphere
# hint: you can get `pi` by importing math (google it!)

from math import pi

def area(l, b):
    return l*b

def volm(n):
    return area(area(n, n), n)

def svol(r):
    return (4*pi*volm(r))/3

print(area(5, 4))
print(volm(5))
print(svol(5))