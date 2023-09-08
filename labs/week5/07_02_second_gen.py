# recreate your previous generator from 01, but use a generator expression

ceil = lambda a: ((a+1)//2)*2
my_gen = (i for i in range(ceil(1), 11))  # fill out the code to make it work!


# practice using your generator
for i in my_gen:
    print(i)


print("second run!")
print()
# does it work two times?
for i in my_gen:
    print(i)

print("It will not, next() of my_gen has reached null value.")