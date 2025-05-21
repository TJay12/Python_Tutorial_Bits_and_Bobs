# Defining variables num and total with starting values
num = 1
total = 0

# Defining the condition "the value of variable num is less than 101"
while num < 101:
    # Updating total variable to add current value of num
    total = total + num
    # Updating num variable to increment up by 1
    num = num + 1

# Print the value of total variable at end of loop
print("The total sum is: ", total)
