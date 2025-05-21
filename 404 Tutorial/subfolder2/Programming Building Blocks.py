print("There once was a man named George,")
print("he was 70 years old.")
print("He really liked the name George,")
print("but didn't like being 70.")

# Variables
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")
# Number Data Storage
character_name = "Tom"
character_age = 50
print("There once was a man named " + character_name + ",")
print("he was " ,character_age, " years old.")
print("He really liked the name " + character_name + ",")
print("but didn't like being " ,character_age, ".")
# Decimal Number Data Storage
character_name = "Tom"
character_age = 50.5678213
print("There once was a man named " + character_name + ",")
print("he was ", character_age, " years old.")
# Change name mid story (reasigning a variable)
character_name = "Mike"
print("He really liked the name " + character_name + ",")
print("but didn't like being ", character_age, ".")

# Identifying Data Type
name = "Bro"
age = 21
gpa = 1.9
student = True
print("Name is",name)
print(type(name))
print("Bro is",age)
print(type(age))
print("Bro's gpa is",gpa)
print(type(gpa))
print("Is Bro a student?" ,student)
print(type(student))

# Typecasting = The process of converting a value of one data type to another
#                (string, integer, float, boolean)
#                Explicit vs Implicit

#Explicit - Manual conversion
# int - float
print(age)
print(type(age))
age = float(age)
print(age)
print(type(age))
# float - int
print(gpa)
print(type(gpa))
gpa = int(gpa)
print(gpa)
print(type(gpa))
#bool - str
print(student)
print(type(student))
student = str(student)
print(student)
print(type(student))

#Implicit - variable data type can be converted when performing certain operations on it like arithmatic expressions
x = 2
y = 2.0

x = x / y
print(x)

# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Calculate the sum
result = num1 + num2
# Print result
print("The sum of", num1, "and", num2, "is:", result)

# take a user input and store it inside a variable
name = input("Enter your name: ")
print("Hello " + name + "!")

# A syntax error is an error, or bug, in your code
# A runtime error is an error that crashes your program while running
# A logic error is an error in the logic within your code