# Built into python modules
# Import modules
import math
import sys
# Alias
import random as rdm
# Import specific function from modules
from enum import Enum

print(math.pi)

# directory...
print("Random Directory")
print(dir(rdm))
# Tidier Directory
print("System Directory")
for item in dir(sys):
    print(item)
print("enum Directory")
for item in dir(Enum):
    print(item)

# Custom module
import kansis

print(kansis.capital)
kansis.random_fun_fact()

# Current file is called main
print(__name__)
print(kansis.__name__)