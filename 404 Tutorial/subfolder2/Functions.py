# defining/creating function
def sayhi():
    print("Hello User")

# calling function
sayhi()
# Control flow
print("Top")
sayhi()
print("bottom")

# additional info (parameters)
def greet_user(name, age):
    print(f"Hello {name}, you are {age}")

greet_user("Steve", "16")
greet_user("Mike", "34")