# write a recursive function to calculate the factorial


def factorial(n):
    if n<=2:
        return n
    return n*factorial(n-1)

print(factorial(4))