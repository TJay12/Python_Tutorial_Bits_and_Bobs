# * imports all
from array import *

# Arrays are primarily used for numbers
# vals - values # i TypeCode
vals = array('i', [5, 9, -8, 4, 2])
print(vals)

# Address, Size
print(vals.buffer_info())

# Reverse Order
vals.reverse()
print(vals)

# Print Specific value
print(f"One Value {vals[1]}")

# Print all values
print("All Values")
for i in range(5):
    print(vals[i])

# Unknown size
for i in range(len(vals)):
    print(f"{vals[i]}", end= " ")

# Characters in an array
cvals = array('u', ['f', 'y', 'd', 's', 'e'])
print(f"Characters: \n {cvals}")
# DeprecationWarning: The 'u' type code is deprecated and will be removed in Python 3.16

# Unknown type, just take type from vals
newArr = array(vals.typecode, (a for a in vals))

# An Array that squares all numbers from vals
squArr = array(vals.typecode, (a*a for a in vals))
print(f"Squared Values: \n {squArr}")

# For loop makes mor sense but while loop can be used
while i < len(newArr):
    print(newArr[i])
    i += 1