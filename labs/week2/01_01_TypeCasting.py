#!/usr/bin/python3
# Type Casting Exercise



a = 7



# 1. print the type of the variable
print(a, type(a), sep='\t')
# Convert integer variable to float and confirm the type cast worked (print it out)
b = float(a)
print(b, type(b), sep='\t')

# 2. Now, Convert your float variable to string and print out the type
c = str(b)
print(c, type(c), sep='\t')

# 3. Finally, Convert your string variable back to integer and print it out (the type)
d = int(float(c))
print(d, type(d), sep='\t')