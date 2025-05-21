#---------------------------------------------------------------   <---Functions--->
# <--- Function to take/store and validate score values
#      as well as calculate average score --->
def input_results(learner_name):
    # Make sure the entered value is a number
    try:
        math_score = int(input(f"Enter {learner_name}'s Math Score: "))
        eng_score = int(input(f"Enter {learner_name}'s English Score: "))
        sci_score = int(input(f"Enter {learner_name}'s Science Score: "))
    # If not number entered, don't crash
    except:
        print("Please enter a numerical value (0 - 100)")
    # All scores stored in a list
    scores = [math_score, eng_score, sci_score]
    # Check the stored values are in range
    for value in scores:
        if value < 0 or value > 100:
            print("Please enter a numerical value (0 - 100)")
        else:
            # Calculate Average of scores
            avg_score = int((math_score + eng_score + sci_score) / 3)
            # return the values scores and average
            return scores, avg_score

# <--- Function to calculate grade from score --->
def calculate_grade(score):
    if score > 90:
        grade = "A"
    elif score > 80:
        grade = "B"
    elif score > 70:
        grade = "C"
    elif score > 60:
        grade = "D"
    else:
        grade = "F"
    # Return the value grade
    return grade

#----------------------------------------------------------------------------   <--- Run Program --->
while True:
    learner_name = input("Enter Learners Name: ")
    # Get scores and average from input_results() function
    learner_scores, learner_avg_score = input_results(learner_name)
    # create blank list to store grades in
    grades = []
    # For each of the values in learner_scores, calculate grade with calculate_grade() function
    # and store grade in grades list
    for value in learner_scores:
        score = int(value)
        grading = calculate_grade(score)
        grades.append(grading)
    # Print the results
    print(f"{learner_name}'s Results:")
    print(f"Maths:   {learner_scores[0]} \t Grade: {grades[0]}")
    print(f"English: {learner_scores[1]} \t Grade: {grades[1]}")
    print(f"Science: {learner_scores[2]} \t Grade: {grades[2]}")
    print(f"Average Score: {learner_avg_score}")
    # Check if the user want's to add another entry
    cont = input("Do you have another entry (y/n): ")
    if cont == "n":
        # End the program
        print("Thank you for using this app")
        break
