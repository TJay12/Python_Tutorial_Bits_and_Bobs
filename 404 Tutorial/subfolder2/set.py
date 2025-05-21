# sets are unordered, unorganised lists
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits) # duplicates not allowed

# add
fruits.add("orange")

#remove
fruits.remove("banana")
print(fruits)

# Check if item in fruits
print("apple" in fruits)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b)) # Join a and b (no duplicates allowed)
print(a.intersection(b)) # in a and b
print(a.difference(b)) # in a not in b

# opposite of a.difference
print(b.difference(a)) # in b not in a
print(b-a) # Items in b - items in a