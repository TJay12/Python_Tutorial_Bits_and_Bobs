# Loop statements
# basic syntax:
# for i in range():
#     print(i)

# Number 1 - 5
for i in range(1,6):
    print(i)
print("end")
# 0 - 10 even numbers
for i in range(2,12,2):
    print(i)
print("end")
# Number 0 - 100 in 5's
for i in range(0,105,5):
    print(i)
print("end")
# User Input
x = int(input("Enter the start number"))
y = int(input("Enter the end number"))

for i in range(x,y,1):
    print(i)
# From List
fruits = ["Apple","Banana","Grape","Pear"]
for i in fruits[1:3]:
    print(i)
for i in fruits[0:4]:
    print(i)
