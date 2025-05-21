country = ""
province = ""
country = input("What is you country of citizenship: ")

if country == "Canada":
    province = input("What province: ")
    while province != "AB" and province != "BC":
        print("Valid provinces: AB, BC")
        province = input("What province: ")
    print("Country =", country, "Province =", province)