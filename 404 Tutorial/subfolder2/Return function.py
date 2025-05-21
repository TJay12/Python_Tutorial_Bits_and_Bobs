# Get information back out of the function (return information from the function)
def cube(num):
    num * num * num

cube(3)
print(cube(3))

def cube_return(num):
    # return breaks out of function
    return num * num * num
    # nothing after return will work
    print("No worky")

print(cube_return(3))
print(cube_return(4))

result = cube_return(4)
print(result)