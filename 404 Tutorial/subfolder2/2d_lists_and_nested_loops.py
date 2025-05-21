# 2d lists
number_grid = [
# r  # Column
# o
# w
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# Row Column
print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)
