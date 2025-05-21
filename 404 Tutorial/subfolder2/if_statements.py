# If I'm hungry
#     I eat breakfast
#
# I leave my house
# If it's cloudy
#     I bring an umbrella
# otherwise
#     I bring sunglasses
#
# I'm at a restaurant
# If I want meat
#     I order a steak
# otherwise if I want pasta
#     I order spaghetti & meatballs
# otherwise
#     I order a salad.

is_male = True
is_tall = True
# else/or
if is_male or is_tall:
    print("You are a male or tall")
else:
    print("You are not a male or tall")
# else/and
if is_male and is_tall:
    print("You are a male and tall")
else:
    print("You are not a male or not tall")
# elif/not
is_tall = False

if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not is_tall:
        print("You are male but not tall")
elif not is_male and is_tall:
        print("You are not male but tall")
else:
    print("You are not a male or not tall")

# Comparisons

# Function
def max_num(num1, num2, num3):
    # Comparisons
    if  num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and  num2 >= num3:
        return num2
    else:
        return num3
print (max_num(300, 40,5))

# Playing
# is_male = "male"
# is_female = "female"
# print(is_male, is_female)
#
# gender = input("Are you male or female?")
# print(gender)
# print(type(gender))
#
# if gender == is_male:
#     print("male")
# elif gender == is_female:
#     print("female")
# else:
#     print("invalid entry")


