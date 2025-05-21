# Make List
fruit = ["banana", "apple", "cherry"]
print(fruit[1])

# Change Item in List
fruit[1] = "blueberry"
print(fruit[1])

# Add Item to list
fruit.append("orange")
print(fruit)

# Remove Item from List
fruit.remove("cherry")
print(fruit)

# List Length
print(len(fruit))

#list slicing
fruits = ["apple", "banana", "cherry", "orange", "grape"]

print(fruits[1:4])
print(fruits[:3])

for fruit in fruits:
    print(fruit)

# Insert
fruits.insert(1, "kiwifruit")
print(fruits)

# Remove last item from list
fruits.pop()
print(fruits)

# Sort List Alphabetically
fruits.sort()
print(fruits)

# Copy/Duplicate Lists
fruits2 = fruits.copy()
print(fruits2)
