from math import *

print("\n \t \t \t Basic List Operations\n")
print(" --- Start List --- ")
# Create a list named fruits containing the elements apple, banana, cherry, and date
fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits)

# Append elderberry to the list
fruits.append('elderberry')

# Remove banana from the list
fruits.remove('banana')

# Change the first element of the list to apricot
fruits[0] = 'apricot'

print(" --- Final List --- ")
print(fruits)
# Print the length of the list
print("\nNumber of items in list: ")
print(len(fruits))

print("\n \t \t \t  List Comprehensions\n")
# Create a list named squares containing the squares of the numbers from 1 to 10.
print(" --- 1 - 10 Squares List --- ")
squares = []
for num in range(1, 11):
    num = int(pow(num, 2))
    squares.append(num)
print(squares)

# Create a list named even_numbers containing all even numbers between 1 and 20.
print(" --- 1 - 20 Evens List --- ")
even_numbers = []
for num in range(1, 21):
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

print("\n \t \t \t \t List Slicing\n")
# Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Use slicing to print:
print("The first five elements")
print(numbers [:5])
print("The last three elements")
print(numbers [-3 :])
print("Every second element")
for index in range(0, 10, 2):
    print(numbers[index], end="\t")
print("\nThe list in reverse order")
numbers.sort(reverse=True)
print(numbers)
