# <--- Dictionary to store values from file --->
students = {

}

# Read File and store values in dictionary
def import_data():
    file = input("Open File: ")

    with open(file, "r") as file:
        all_lines = file.readlines()

        for line in all_lines:
            line = line.strip()
            split = line.rsplit(",", 2)
            student, mid_score, end_score = split
            student_id, student_name1, student_name2 = student.split(" ")
            students[student_id] = {"first_name": student_name1, "last_name": student_name2,
                                    "mid_score": int(mid_score), "end_score": int(end_score)}

# <--- Function to Calculate The Average Score for Each Student and Add to Dictionary --->
def calculate_final_score():

    for stud_id, student_data in students.items():
        score_average = (student_data['mid_score'] + student_data['end_score']) / 2
        students[stud_id]['avg_score'] = float(score_average)

# <--- Function to Assign Grade based on Average Score for Each Student and Add to Dictionary --->
def assign_grade():

    for stud_id, student_data in students.items():
        stud_grade = student_data['avg_score']
        if stud_grade >= 90:
            grade = "A"
        elif stud_grade >= 80:
            grade = "B"
        elif stud_grade >= 70:
            grade = "C"
        elif stud_grade >= 60:
            grade = "D"
        else:
            grade = "F"
        students[stud_id]['grade'] = grade

# <--- Function to Calculate the Grade Totals for All Students --->
def total_grade_count():

    all_grades = "",
    for stud_id, stud_data in students.items():
        stud_grade = stud_data['grade']
        all_grades += stud_grade,
    grade_count = [all_grades.count("A"), all_grades.count("B"), all_grades.count("C"), all_grades.count("D"),
                   all_grades.count("F")]
    return grade_count

# <--- Function to Print Full Report with Scores, Grades and Total Grade Count --->
def print_report():

    print(f"{'-' * 51}")
    print(f"| {'Students Scores and Grade':^47} |")
    print(f"{'-' * 51}")

    print(f"| {'ID':<8} {'Name':<14} {'Mid':^5} {'End':^5} {'Avg':<5} {'Grade':<5} |")
    print(f"{'-' * 51}")
    for stud_id, stud_data in students.items():
        print(f"| {stud_id:<8} {stud_data['first_name'] + " " + stud_data['last_name']:<14} {stud_data['mid_score']:^5} "
              f"{stud_data['end_score']:^5} {stud_data['avg_score']:^5} {stud_data['grade']:^5} |")

    print(f"{'-' * 51}")
    print(f"| {'Students Total Grade Count':^47} |")
    print(f"{'-' * 51}")
    print(f"|{'A = '+str(grade_count[0]):^16}{'C = '+str(grade_count[2]):^17}{'F = '+str(grade_count[4]):^16}|\n"
          f"|{'B = '+str(grade_count[1]):^16}{'D = '+str(grade_count[3]):^17}{' ' * 16}|")
    print(f"{'-' * 51}")

def main():
    import_data()
    calculate_final_score()
    assign_grade()
    grade_count = total_grade_count()
    print_report()

if __name__ == "__main__":
    main()
