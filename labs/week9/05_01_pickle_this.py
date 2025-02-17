"""
Pickle the following class


"""

import pickle

class Car:
    cars_created = 0
    def __init__(self, num_tires = 2, color = "red", gas=True):
        self.num_tires = num_tires
        self.color = color
        self.gas = gas
    
    def is_gas(self):
        return self.gas

    def honk_horn(self):
        print("HONK HONK")
    
    def can_drive(self):
        if self.num_tires == 4:
            return True
        return False

## pickle the actual class Car 

with open('classfile', 'wb') as f:
    pickle.dump(Car, f)


my_car = Car(4, 'blue', True)
with open('classinst', 'wb') as f:
    pickle.dump(my_car, f)

# pickle your instance of the car


