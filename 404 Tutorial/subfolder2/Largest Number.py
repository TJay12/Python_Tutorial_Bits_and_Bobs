# We will find the largest from two numbers

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

if a > b:
    print(a, "is greater than", b)

elif b > a:
    print(b, "is greater than", a)
else:
    print("They are the same")

# We will find the largest from three numbers

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))

if a > b and a > c:
    print(a, "is the greatest number")
elif b > a and b > c:
    print(b, "is the greatest number")
elif c > a and c > b:
    print(c, "is the greatest number")
else:
    print("They are all equal")