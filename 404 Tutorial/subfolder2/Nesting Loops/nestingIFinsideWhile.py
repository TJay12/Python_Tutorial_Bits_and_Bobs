age = -1
# Caps indicate this value should never be changed (aesthetics)
MIN_AGE = 1
MAX_AGE = 118
age = int(input("How old are you: "))
# The extra brackets are also aesthetics for human clarity
while ((age <MIN_AGE) or (age > MAX_AGE)):
    if (age < MIN_AGE):
        print("Age can't be lower than", MIN_AGE, "Years")
    age = int(input("How old are you: "))

print("Age=", age, "is age-ok")