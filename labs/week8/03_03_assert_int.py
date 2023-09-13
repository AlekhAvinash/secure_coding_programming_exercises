"""
write a function that asks for user input with the input() function
Ask them to create a password that is greater than >6 and <12 characters long ( 6< pwd < 12)

Use an assert statement to validate their password choice

"""

inp = input("Enter the password: ")

assert 6 < len(inp) < 12

print(f"Password is accepted!")