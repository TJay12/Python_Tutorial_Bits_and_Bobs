print("Create Your Own List\n")
# Create list called favourite_colors containing 4 colors
favourite_colors = ["red", "blue", "yellow", "green"]
# Print the first and last color
print(favourite_colors[0])
print(favourite_colors[3])
# Replace the second color with another color
favourite_colors[1] = "violet"
# Add one more color to the list
favourite_colors.append("indigo")
# Print the updated list
print(favourite_colors)

print("\nBasic List Operations\n")
# Create a list of 5 animals
animals = ["pig", "horse", "cow", "sheep", "cat"]
# Remove the third animal
animals.remove("cow")
# Insert a new animal at position 2
animals.insert(1,  "dog")
# Print the final list
print(animals)

print("\nBonus Challenge\n")
# Create a list of 5 numbers
numbers = [4, 8, 2, 5, 6]
# Sort them in ascending order
numbers.sort()
print(numbers)
# Sort them in descending order
numbers.sort(reverse=True)
print(numbers)