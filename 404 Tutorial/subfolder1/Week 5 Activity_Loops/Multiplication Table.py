# Defining i will start at a value of 1 and stop when it has a value of 10 (default increment 1)
for i in range(1, 11):
    # Defining j will start at a value of 1 and stop when it has a value of 10 (default increment 1)
    for j in range(1, 11):
        # print current value of j and i followed by the result of j * i
        print (f"{j} x {i} = {j * i:<5}", end="\t")
    # Blank line for clarity of reading
    print("")