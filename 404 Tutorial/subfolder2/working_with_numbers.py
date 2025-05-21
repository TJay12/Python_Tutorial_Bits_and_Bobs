print(f"2 is a number, python also accepts: \nDecimals: {2.0987} \t Negatives: {-2.0987} \t Basic Math: 3 + 4.5 = {3 + 4.5}"
      f"\nBEDMAS: 3 * 4 + 5 = {3 * 4 + 5} \t Order of Operations: 3 * (4 + 5) = {3 * (4 + 5)} \t  Modulas: 10 % 3 = {10 % 3}")

#Modulas (remainder)
print("Modulas: 10 % 3 =", end=" \t ")
print(10 % 3)

my_num = 5
print(my_num)
print(f"My Favourite Number = {my_num}")

#Absolute Value
my_num2 = -5
print(abs(my_num))

# Power to (A to the power of B)
print(f"{my_num} To the power of 2" , end=" \t ")
print(pow(my_num, 2))

# Min/Max
print("Min/Max (4, 7.5)", end=" \t ")
print(min((4, 7.5)), end=" \t ")
print(max((4, 7.5)))

#Rounding
print("Rounding (4.3, 4.5, 4.7)", end=" \t ")
print(round((4.3)), end=" \t ")
print(round((4.5)), end=" \t ")
print(round((4.7)))

from math import *

print("Always round down", end=" \t ")
print(floor((4.4)))
print("Always round Up", end=" \t ")
print(ceil((4.4)))
print("Square Root", end=" \t ")
print(sqrt((36)))