# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

# you will need the `input()` function to collect information from the user

def collector():
    while True:
        try:
            return int(input("Enter a number: "))
        except:
            print("Only integer inputs are accepted!")

def game():
    mem = set()
    pts = 5
    while len(mem)<=10:
        inp = collector()
        if inp in mem:
            print("Used it!")
            pts -= 1
        else:
            print("Good one!")
            mem.add(inp)
        
        if not pts:
            return "You lose.."
    
    return "Winner!!"

print(game())