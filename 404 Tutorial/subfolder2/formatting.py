# <--- Basic print() Formatting in Python --->
# Comma-Separated Printing
# Simple and clean. Python auto adds spaces between items
name = "TJ"
age = 32
print("Name:", name, "| Age:", age)

# String Concatenation (+)
# Usefull for small things, but you need to convert non-strings manually
print("Name: " + name + " | Age: " + str(age))

# f-strings - Your Best Friend
# Cleanest and most powerful for variables and formatting.
print(f"Name: {name} | Age: {age}")
# You can even format numbers
price = 5.6789
print(f"Price: ${price:.2f}") # Rounds to 2 decimal places

# .format() Method
# Older than f-strings but still common
print("Name: {} | Age: {}".format(name, age))

# Alignment and width in f-strings
# Useful when printing tables or neat columns
print("-" * 20)
print(f"  {'Item':<10} {'Qty':>3}")
print("-" * 20)
print(f"  {'Potion':<10} {3:>3}")
print(f"  {'Scroll':<10} {15:>3}")
print("-" * 20)
