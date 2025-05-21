# Tuple - Uses ()
colors = ("red", "green", "blue")
print(colors)

#Acess a tuple
print(colors[0])

# # Tuples are immutable
# colors[1] = "green" # This will cause error

# You can't modify tuple elements after creation
# You can't add remove or change

# Length
print(len(colors))

# Check if item is in tuple
print("red" in colors)

# Count times an entry appears
# Duplicates are allowed in tuples
numbers = (1, 2, 2, 3, 4)
print(numbers.count(2))

# Find an items index number
print(numbers.index(3))

# Single tuple
# Must include comma
single_item = ("apple",)
print(type(single_item))

# Pack and unpack
student = ("John", 20, "A")
print(student)
student2 = "John", 18, "B", "James", 19, "A"
print(student2)
print(type(student2))

# Unpacking
name, age, grade = student
print(name)
print(age)
print(grade)

