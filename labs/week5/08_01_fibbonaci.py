# wrtie a recursive fibonacci function


cache = [0, 0, 1]
lengt = 3
def fib(n):
    global lengt, cache
    if n<lengt:
        return cache[n]
    else:
        cache += [fib(n-1)+fib(n-2)]
        lengt += 1
        return cache[n]
    return -1

print(fib(6))
print(fib(10))

# fib(6) should return 5
# fib(10) should return 34
