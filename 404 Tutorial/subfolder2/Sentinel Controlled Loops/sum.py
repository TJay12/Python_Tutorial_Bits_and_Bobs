total = 0
temp = 0
while(temp >= 0):
    temp = input("Enter a positive integer (negative to end series): ")
    temp = int(temp)
    if (temp >= 0):
        total = total + temp
print("Sum total of the series", total)