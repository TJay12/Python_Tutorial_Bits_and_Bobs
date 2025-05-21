import math
import operations

print("\n1) Basic Function\n")
name =  input("Enter Name: ")

def hello(name):
    print(f"Hello {name}")

hello(name)

print("\n2) Function With Return Value\n")
radius = float(input("Circle Radius: "))

def calculate_area(radius):
    area = math.pi * pow(radius, 2)
    return area
print(f"The area of this circle is {calculate_area(radius):.2f}\n")

print("\n3) Function with Multiple Parameters")
price = float(input("Enter Price: $"))
quantity = float(input("Enter Quantity: "))

def calculate_total(price, quantity):
    total = price * quantity
    return total
print(f"The total cost of this purchase is: ${calculate_total(price, quantity):.2f}")

print("\n4) Using Modules\n")
number = float(input("Enter Number: "))
square_root = math.sqrt(number)
print(f"The square root of that number is {square_root:.2f}")

print("\n5) Creating and Importing a Module\n")
a = int(input("Enter first number: "))
b = int(input("Enter second number number: "))

print(f"The sum of these 2 numbers is: {operations.add(a, b)} \nThe difference "
      f"between these numbers is: {operations.subtract(a, b)}")