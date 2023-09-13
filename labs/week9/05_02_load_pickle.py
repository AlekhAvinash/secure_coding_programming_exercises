"""
Load your pickled files from 05_01 and use them here!

"""

import pickle
from test import Car

with open("classfile", "rb") as f:
    out = pickle.load(f)
    print(out.cars_created)

with open("classinst", "rb") as f:
    out = pickle.load(f)
    print(out.is_gas())
