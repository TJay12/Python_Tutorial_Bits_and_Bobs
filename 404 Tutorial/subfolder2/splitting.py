# The .split() method breaks a string into a list, using a seperator (default is space)
# Basic Syntax
# string.split(seperator, maxsplit)
    # seperator: What to split on (space. comma, etc.)
    # maxsplit: Optional. Limits number of splits

# Default Split (by space)
line = "Elira Mage 5"
parts = line.split()
print(parts)

# Split by comma
data = "Health,72,100"
values = data.split(',')
print(values)

# Split with maxsplit
text = "A B C D"
parts = text.split(" ", 2)
print(parts)

# Splitting and Assigning
line = "Potion 5 25"
item, qty, value = line.split()
print(item)
print(qty, value)

# .rsplit() starts splitting from the right
text = "A B C D E F"
end = text.rsplit(" ", 3)
print(end)
print(end[0])
print(end[1])
print(end[2])
print(end[3])

# splitlines() splits on line breaks
nums = "one\ntwo\nthree"
split_nums = nums.splitlines()
print(split_nums)