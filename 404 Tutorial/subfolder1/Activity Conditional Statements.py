# Variables
num1 = 2
num2 = -4

# Which number is greater, num1 or num2?
# If num2 is greater
if num1 < num2:
    print(num2, "is greater than", num1)
# If they are the same
elif num1 == num2:
    print(num1, "is equal to", num2)
# If num1 is greater
else:
    print(num2, "is less than", num1)

# Are either num1 or num2 negative?
# If either num1 or num2 are negative
if num1 < 0 or num2 < 0:
    # If it's num1 that's negative
    if num1 < 0:
        print(num1, "is a negative integer")
    # It must be num2 that's negative
    elif num2 < 0:
        print(num2, "is a negative integer")
# If neither of the numbers are negative
# If it's num1 that's positive
elif num1 != 0 and num2 < 0:
    print(num1, "is a positive integer")
# If it's num2 that's positive
elif num2 != 0 and num2 < 0:
    print(num2, "is a negative integer")
# If they are both positive
else:
    print("They are both positive integers")