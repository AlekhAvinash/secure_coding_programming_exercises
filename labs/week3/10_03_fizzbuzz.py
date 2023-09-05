# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

# feel free to adjust n for debugging
n = 100
fz = "Fizz"
bz = "Buzz"
nt = ""
for i in range(1, n+1):
    print(f"{fz if i%3 else nt}{bz if i%5 else nt}")