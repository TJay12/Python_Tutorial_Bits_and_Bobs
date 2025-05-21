attendance = int(input("Enter student's attendance"))
if attendance < 75:
    print("automatic fail")

else:
    grade = int(input("enter students grade"))
    if grade >= 90:
        print("Excelent")

    elif 75 <= grade <= 89:
        print("Good")

    elif 60 <= grade <= 74:
        print("pass")

    else:
        print("Fail")

print(input("Do you wish to continue y/n"))