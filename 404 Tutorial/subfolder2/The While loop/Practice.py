# Variable Initiation
age = int(input("Age: "))

while (age < 0):
    print("Age cannot be negative")
    age = int(input("Age: "))

print("Age is: ", age)