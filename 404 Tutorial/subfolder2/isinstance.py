# Python’s built-in isinstance() function is a way to test the type of a variable.
# isinstance(thing_you_are_checking, type_you_expect)

# Is this variable an interger?
isinstance(5, int)           # True
print(isinstance({"key": 34}, int))
print(isinstance(5, int))
# Is this variable a string
isinstance("hello", str)     # True
print(isinstance(23, str))
print(isinstance("hello", str))
# Is this variable a list
isinstance([1, 2], list)     # True
print(isinstance("hi", list))
print(isinstance([1, 2], list))
# Is this variable a dict
isinstance({"a": 1}, dict)   # True
print(isinstance([3, 6, 9], dict))
print(isinstance({"a": 1}, dict))

# If result is a string, do this (e.g. treat it as an error message).
result = "This is a string"
if isinstance(result, str):
    print(result)