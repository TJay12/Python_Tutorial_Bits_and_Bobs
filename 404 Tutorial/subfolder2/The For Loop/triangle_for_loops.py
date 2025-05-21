print("Columns")
for x in range(1, 10):
    print(x)

print("Rows")
for x in range(1, 10):
    # No Space
    print(x, end="")

print("\nNested")
for y in range(3):
    for x in range(0, 10):
        # Space
        print(x, end=" ")

print("\nUser input")
rows = int(input("Rows: "))
cols = int(input("Columns: "))
symbol = input("Symbol: ")

for y in range(rows):
    for x in range(cols -1):
        print(symbol, end=" ")
    print(symbol)

print("\nTriangles")

print("\nTriangle 1")
for y in range(rows + 1):
    for x in range(y):
        print(symbol, end=" ")
    print()

print("\nTriangle 2")
for y in range(rows, 0, -1):
    for x in range(y):
        print(symbol, end=" ")
    print()

print("\nTriangle 3")

for y in range(1, rows + 1, 1): #loop from 1 - rows
    # print the space first
    for space in range(rows - y, 0, -1): # Print decreasing spaces
        print(" ", end="")
    # print the symbols
    for x in range(y): # Print increasing stars
        print(symbol, end="")
    print()

print("\nPyramid")

for y in range(1, rows +1, 1): #loop from 1 - rows
    # print the space first
    for space in range(rows -y): # Print decreasing spaces
        print(" ", end="")
    # print for the symbols
    for stars in range(2 * y -1): # Print increasing stars
        print(symbol, end="")
    print()

print("\nPyramid 2")

for y in range(1, rows + 1, 1): #loop from 1 - rows
    # print the space first
    for space in range(y): # Print increasing spaces
        print(" ", end="")
    # print for the symbols
    for stars in range(2 * rows + 1 - y * 2): # Print decreasing stars
        print(symbol, end="")
    print()