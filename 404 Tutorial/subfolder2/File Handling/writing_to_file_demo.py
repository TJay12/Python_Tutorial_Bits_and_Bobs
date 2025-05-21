import os_tut
if os.path.exsists ("sample5.txt"):
    with open ("sample5.txt") as file:
        print(file.read())

else:
    print("404 File not found")

# Python program to demonstrate
# writing to a file

# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"

# Writing a string to file
file1.write(s)

# Writing multiple strings at a time
file1.writelines(L)

# Closing file
file1.close()

# Checking if the data is written to file
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()