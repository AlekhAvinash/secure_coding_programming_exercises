# 1) Initialize variable a to true, b to false and c to true

a = True
b = False
c = True

# 2) If you print(a and b or c) what it will return? Why?
# Does the order of operations matter?
print(a and b or c)
print("Yes the logical order is to evaluate 'and' operations first then the 'or' operators.")

# 3) Is print(a or b and c) different?
print(a or b and c)
print("Logical output and the evalutation process is still the same.")

c = False
# 4)Assign c to false and print the value of a and b or c
print(a and b or c)

# Understand the difference in each scenario
# What is happening here?
print("""Here 'and' operation evaluates to False and 
      the 'or' operator has both inputs as false thus produces a false output.""")

# 5) Now try to use some ()'s to force python to evaluate it differently.
print(a and (b or c))
print("Althought the logical operation is forced to alter the output ends up the same.")