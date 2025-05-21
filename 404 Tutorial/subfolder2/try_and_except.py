# Basic example of try-except
from logging import exception


def divide_numbers():
    # Hey Python, try this code. If it works awesome. If it doesn't, don't crash - go to except instead
    try:
        # If the user types something like two or ! it raises a value error because it cant convert that to a number
        a = int(input("Enter num 1: "))
        b = int(input("Enter num 2: "))
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("No divide by 0")
    # Catches that error and lets you respond to it nicely (instead of game crashing with big red traceback).
    except ValueError:
        print("Please enter valid numbers")
    # Ends the function early if input is invalid
    return

# Try with multiple exceptions
def convert_input():
    try:
        value = input("Enter a number: ")
        number = int(value)
        print(f"You entered number {number}")
    except ValueError:
        print("Not valid num")
    # "catch any error that is a kind of exception, and call it e"
    except Exception as e:
        # Then e holds the error msg/info
        print(f"Something went wrong {e}")

# Try with file reading
def read_file():
    try:
        filename = input("Enter file name to open: ")
        # With is a cleaner way to work with resources like files that need to be opened and then closed
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File no found, check spelling")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# Try-Finally
# Always runs the finally block, whether there's error or not
def division_demo():
    try:
        num = int(input("Enter a num: "))
        print(100 / num)
    except ZeroDivisionError:
        print("No divide by 0")
    # will always run
    finally:
        print("End of division demo")

# Catching multiple specific errors at once
def demo_multiple():
    try:
        x = int(input("Enter Integer: "))
        y = int(input("Enter another: "))
        print("Result", x / y)
    except (ValueError, ZeroDivisionError) as e:
        print(f"error: {e}")