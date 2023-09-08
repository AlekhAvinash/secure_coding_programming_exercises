"""
experiment with the function below
1. run the script as is. What prints out? Are you surprised?
2. Modify the function so that x becomes a local variable. There are two ways to do this.
   a. pass x into the function through the arguments
   b. create a new x variable inside the function.
3. After modifying the function, is the x inside the function the same as the x outside? Are they different? Why or why not?
"""
x = 100


def add_to_me(num):
    y = num + x
    print(f"x inside the function is: {x}")
    return y

z = add_to_me(10)
print(z, x)

def add_to_me_2a(num, x):
    y = num + x
    print(f"x inside the function is: {x}")
    return y

z = add_to_me_2a(10, 10)
print(z, x)

def add_to_me_2b(num):
    x = 20
    y = num + x
    print(f"x inside the function is: {x}")
    return y

z = add_to_me_2b(10)
print(z, x)


print(x)  # what do you think will print out?
print("100 as is, this is due to the scope of certain variables. Local intergers do not affect a global integers.")