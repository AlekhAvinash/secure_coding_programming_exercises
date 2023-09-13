"""
Construct a code sample where you force an error to happen.
Then run it in a try-except-finally block. But, do NOT catch your error! (Or re-raise it)
Print something out in the finally block.
Does it print out? Why?

The main purpose of the finally is to ensure that some safety code / exit condition will run no matter what, even 
if an error happens.

The purpose of this exercise is to just practice observing that
"""

try:
    print(f"{4+'5'}")
except TypeError as e:
    print(f"Error: {e}")
finally:
    print(f"{4+int('5')}")