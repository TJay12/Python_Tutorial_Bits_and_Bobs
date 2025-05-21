rows = int(input("Rows"))
columns = int(input("Columns"))
symbol = input("Symbol")

for i in range(rows):
    # use j because it comes after I.. I mean variable can be anything
    for j in range(columns):
        print(symbol, end="")
    print("")