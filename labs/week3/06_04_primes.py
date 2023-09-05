# Exercise

# Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there
# if you don't know an algorithm to check for primes
# ask Dr. Kurunandan Sir
# google it

ctr = 0
for i in range(2, 100):
    for j in range(2, i):
        if not i % j:
            break
    else:
        ctr += 1
        print(i, end = ", ")

print(f"\nThere are {ctr} primes!")