# Defining the initial variables
sum_total = 0
pos_num = 0
# Defining the condition "while variable pos_num has a value greater than or equal to 0"
while pos_num >= 0:
    # Prompt user input to update variable pos_num
    pos_num = int(input("Enter a positive number (negative to finish): "))
    # Defining the condition to state if pos_num is greater than or equal to 0
    if pos_num >= 0:
        # States that if condition is met add pos_num value to sum_total value
        # Update sum_total value
        sum_total = sum_total + pos_num
    # if pos_num >= 0 conditions not met program ends
# Print the value of sum_total
print("Sum of entered positive numbers:", sum_total)