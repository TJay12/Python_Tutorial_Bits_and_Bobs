MIN_INCOME = 0
runAgain = "yes"

while runAgain == "yes":
    print("CALCULATING A TAX RETURN")
    income = -1
    while income < MIN_INCOME:
        income = int(input("Income $"))
    runAgain = input("To calculate another return enter 'yes': ")