# Exercise

# Write a program by accepting 2 numbers from the user and check number is greater than other and print the result
# you can use the function `input()` to get user input

# example
first_number = int(input("please enter a number: "))
second_number = int(input("please enter another number!: "))

if first_number > second_number:
    higher_number = first_number
else:
    higher_number = second_number

print(f"Largest number is: {higher_number}")

## note, what type is your first_number? Is it what you expected?
## look-up the input() documentation to find out what type it will create by default
