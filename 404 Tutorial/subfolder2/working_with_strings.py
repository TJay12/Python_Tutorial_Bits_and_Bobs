# Strings are basically just plain text

print("Whatever text I want this string to have")
#new line
print("Whatever text I want \nthis string to have")
# quotiation
print("Whatever text I want \"this\" string to have")
# \ == escape.. Hey python I want to print this

phrase = "Aspire Education"
# concatination
print(phrase + " is cool")

# Print in Lower or Uppercase
print(phrase.lower())
print(phrase.upper())

# Check the phrase is all uppercase
print(phrase.isupper())

# Make the phrase in uppercase and check it's in uppercase
print(phrase.upper().isupper())

# Length function
print(len(phrase))

# Indexing in python starts at 0
print(phrase[0])
print(phrase[3])

print(phrase.index("d"))
print(phrase.index("E"))

print(phrase.replace("Aspire", "ASPIRE"))


