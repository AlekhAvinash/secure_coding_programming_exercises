"""
Look up how to use the argv module in python
Run this program as command line and use the argv module to indicate the logging level
Write your logging code to have all the levels of severity
Practice using the different levels of severity on your dog code below. be creative!

"""
import logging

class Dog:
    def __init__(self, limbs=None, eyes=None, color=None, kindness=None):
        self.limbs = limbs
        self.eyes = eyes
        self.color = color
        self.kindness = kindness  # nice, mean, angry, sad, lonely

        print("\n\nCreated New Dog") 
        self.checker()
        ## if limbs < 4 -- log a warning! dog needs help (it's missing legs!)
        ## if kindness is sad or lonely, log a warning. If it's mean or angry it's critical! we must be careful
    
    def checker(self):
        if self.limbs<4:
            logging.warning("Your dog needs help (it's missing legs!)")
        
        if self.kindness in ["sad", "lonely"]:
            logging.warning("Hey! It's sad..")
        
        if self.kindness in ["angry", "mean"]:
            logging.warning("Careful!! It bites!")

if __name__ == "__main__":
    a = Dog(
        limbs=3, eyes=1, color="red", kindness="nice"
    )  # create different dogs and see your logger in action!
    a = Dog(
        limbs=4, eyes=1, color="red", kindness="sad"
    )  # create different dogs and see your logger in action!
    a = Dog(
        limbs=4, eyes=1, color="red", kindness="angry"
    )  # create different dogs and see your logger in action!
