def simp_calc():

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    while True:

        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        operator = input("What would you like to do with these numbers (+, -, *, /): ")

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("Invalid Operation")
            break

        print(f"{num1} {operator} {num2} = {result}")
        break
