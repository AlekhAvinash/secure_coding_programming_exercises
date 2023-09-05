# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

for i in range(1500, 2700):
    if not i%7 and not i%5:
        print(i)
