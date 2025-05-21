# Read example.txt
file = open('example.txt', 'r')
print(file.read())

# Write to file
file = open('output.txt', 'w')
L = ['This is the first line\n', 'This is the second line\n']
file.writelines(L)
file.close()

# Append new line
file = open('output.txt', 'a')
file.write('This is the appended line.\n')
file.close()