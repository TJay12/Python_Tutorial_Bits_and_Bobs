#Given the string quote = " To be, or not to be, that is the question. "
from operator import index

quote = " To be, or not to be, that is the question. "
print(f"Quote of the day: \n - {quote}")
# Remove the leading and trailing whitespace.
quote2 = quote.strip()
print(f"Quote Without Whitespace: \n - {quote2}")
# Print the length of the string
print(f"\nThis quote has {len(quote2)} characters")
# Count the occurrences of the temp_word "be"
times = quote2.count('be')
print(f"\nIt mentions the word \"be\" {times} times")

# Split the string into a list of words
print("\nThe words in this quote are:")
char = []
words = []
temp_word = ""
# Loop through all characters in quote2
for index in range(len(quote2)):
    # If the index character isn't a space, comma or full stop
    if quote2[index] != " " and quote2[index] != "," and quote2[index] != ".":
        # add the index character to char list
        char.append(quote2[index])
    # When the index is a space, comma or full stop
    else:
        # add the characters from char into temp_word to turn them into a string
        for ch in char:
            temp_word += ch
        # add temp word to words list
        words.append(temp_word)
        # Clear char and temp_word variables
        char = []
        temp_word = ""
# Remove the extra bits that appeared
words.remove("")
words.remove("")
# from the words list - print words 1 by 1.
for word in words:
    print(f" - {word}")

# Check if the string starts with "To"
if words[0] == 'To':
    print("\nThis phrase starts correctly")
else:
    print("Nope, check starting word")