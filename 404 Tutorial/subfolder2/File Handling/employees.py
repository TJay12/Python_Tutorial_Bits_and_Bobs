employee_file = open('employees.txt', 'r')
print(employee_file.read())
employee_file.close()

# # New Employee
# employee_file = open('employees.txt', 'a')
# employee_file.write("\nToby - Human Resources")
# employee_file.close()

# employee_file = open('employees.txt', 'a')
# employee_file.write("\nKelly - Customer Service")
# employee_file.close()

# # New File
# employee_file = open('employees1.txt', 'w')
# employee_file.write("\nKelly - Customer Service")
# employee_file.close()

# HTML File
employee_file = open('index.html', 'w')
employee_file.write("<p>This is html</p>")
employee_file.close()
