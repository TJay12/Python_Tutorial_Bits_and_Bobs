# A for loop in Python can iterate through each character_stats in a string.
activity = input("What are you doing with dog now: ")
print("We are taking the dog for a ", end="")

for ch in activity:
    print(ch + "-", end="")
print("")