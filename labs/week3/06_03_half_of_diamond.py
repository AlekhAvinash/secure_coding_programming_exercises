#Exercise

#Write a Python program to construct the following pattern, using a nested for loop.
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

val = int(input("Enter number: "))
print(*["* "*(val-abs(i)) for i in range(-val+1, val)], sep='\n')