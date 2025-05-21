# Concept Application
# Input/Output - input() and print()
# Data validation - get_valid_minutes() with try-except
# Conditional statements - get_feedback() with if-elif-else
# Looping - while true: for repetition
# Functions - Modular approach with get_feedback() and get_valid_minutes()
# Arithmetic - Average calculation (w+c+r)/3
# def = define function

# Function to give feedback based on minutes of activity
def get_feedback(minutes):
    if minutes >= 300:
        return 'Excelent'
    elif minutes >= 200:
        return 'Good'
    elif minutes >= 100:
        return 'Fair'
    else:
        return 'Poor'
    #This function categorizes the excercize effort level bassed on time.

# Function to get valid minutes for each activity
def get_valid_minutes(activity):
    while True:
        try:
            mins = float(input(f"Enter minutes for {activity}: "))
            if 0 <= mins <= 600:
                return mins
            else:
                print("Please enter a number between 0 and 600.")
        except ValueError:
            print("Please enter a valid number.")
    # This function ensures the input is a number and within the acceptable range.

# Main function that runs the app
def main():
    while True:
        print("\n--- Weekley Fitness Tracker ---")
        name = input("Enter your name: ")

        # Get minutes for each activity
        walk = get_valid_minutes("Walking")
        cycle = get_valid_minutes("Cycling")
        swim = get_valid_minutes("Swimming")

        # Calculate average time
        average = (walk + cycle + swim) / 3

        # Display Report
        print("\nFitness Report")
        print(f"User: {name}")
        print(f"Walking: {get_feedback(walk)}")
        print(f"Cycling: {get_feedback(cycle)}")
        print(f"Swiming: {get_feedback(swim)}")
        print(f"Average Exercize Time: {average:.2f} minutes")

        # Ask if user wants to try again
        again = input("Do you want to enter another record? (Y/N): ").strip().lower()
        if again != 'y':
            print("Thanks for using the Fitness Tracker. Stay active!")
            break

# Run the program
if __name__ == "__main__":
    main()
