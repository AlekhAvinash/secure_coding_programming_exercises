# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it


from string import ascii_lowercase as asl
from time import sleep

FLAG = 'inquisitive'
CTR = 10

def game(flag: str, ctr: int) -> bool:
    # Firstly set up a tracker for all characters in string
    trck = {i: False for i in set(flag)}

    # A Store for incorrectly guessed characters (flukes)
    # And a flag for loop result (output!)
    fluk = []
    out = False

    # Next loop till Counter Reaches 0!
    while ctr:
        # Print blank spaces for undiscovered characters
        print(" ".join([i if trck[i] else "_" for i in flag]))

        # And take input!
        inp = input(f"\nGuess a character! ('?' to guess)\
                      \nYou have {ctr} tries left!\
                      \nIt's none of these characters: {fluk}\
                      \n> ")
        ctr -= 1

        # Expect 4 Cases:
        # Case 1: Player tries to guess before counter
        if inp == '?': break

        inp = inp.lower() # just lowering the character

        # Case 2: Len of input is not 1! Or not a character!
        if len(inp) != 1 or inp not in asl:
            print("Only one character inputs are accepted...\n\n")
            continue

        # Case 3: Character Input
        # If 'in tracker and not already guessed' -> Update tracker
        # Else -> Update flukes list
        if inp in trck and not trck[inp]:
            trck[inp] = True
            print("--- Good! ---\n\n")
        else:
            fluk += [inp]
            print("--- Oops! ---\n\n")
        
        # Case 4: All characters are guessed before counter
        if all(trck.values()):
            out = True
            break

        sleep(1)

    # Lastly allow contestant to take a guess if 'counter is out' or 'opted for it'.
    return out if out else input("Your Guess: ").lower() == flag

if __name__ == '__main__':
    print("What do you call someone who is always curious?!\n\n")
    if game(FLAG, CTR):
        print(f"Success!! \nThe word is {FLAG}!")
    else:
        print("Op! Your out of tries and guesses!")