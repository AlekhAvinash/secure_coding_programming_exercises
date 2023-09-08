## Write a function with keyword arguments
## your function can be a mix of positional and keyword arguments
## it must use a default value for the keyword argument.


def rectangle(length: int, width: int = 10) -> int:
    return length*width

print(rectangle(5))
