# A dictionary is a way to store data using a key-value system
# You give it a key (label) and it returns a value

fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

# "apple" is the key, "red" is the value

# access value
print(fruit_colors["apple"]) # Output: red
# You use square brackets [] and put the key inside quotes

# What if the key doesn't exsist?
#print(fruit_colors["orange"]) # Error: KeyError
# To avoid these errors, you can check first
if "orange" in fruit_colors:
    print(fruit_colors["orange"])
else:
    print("No such fruit")
# Or use .get() which gives back none (or a default) if the key isn't there
print(fruit_colors.get("orange", "not found")) # Output: not found

# Looping through a dictionary
for fruit in fruit_colors:
    print(fruit)
# Or through both keys and values
for fruit, color in fruit_colors.items():
    print(f"{fruit} is {color}")

# Practise
animal_sounds = {
    "cat": "meow",
    "dog": "woof",
    "lion": "roar"
}
print(animal_sounds["lion"])
for animal, sound in animal_sounds.items():
    print(f"{animal} goes {sound}")

# Add new animal
animal_sounds["cow"] = "moo"
print("Added cow:", animal_sounds)

# Update an existing animals sound
animal_sounds["cat"] = "mew"
print("Updated cat:", animal_sounds)

# Delete an animal
del animal_sounds["dog"]
print("Deleted dog", animal_sounds)

# Check if animal exists
if "lion" in animal_sounds:
    print("Yes, lion is here!")

# Get a sound with .get() safely (wont crash if key is missing)
print("Monkey says", animal_sounds.get("monkey", "unknown sound"))

#-------Adding a dictionary entry-------
# Ask how many entries to add
try:
    entries = int(input("How many animals would you like to add: "))
# try-except to prevent crashes if user doesn't enter a numerical value
except ValueError:
    print("Please enter a number")
else:
    #
    for _ in range(entries):
        # defining local variables inside loop
        animal = input("Enter Animal Name: ").lower()
        # .lower() is a string method that converts all characters in a string to lowercase
        # "Dog" == "dog". User types "DOG", it stores it as "dog"
        sound = input(f"What sound does {animal} make?: ").lower()
        # Checking for duplicates: is local var animal already in dict animal_sounds
        if animal in animal_sounds:
            print(f"{animal} is already in the dictionary")
        # Add user input local var animal to dict and give it the value user input local var sound
        else:
            animal_sounds[animal] = sound

    # Start a new line with "Heading"
    print("\nAnimal Sound Dictionary")
    # "for each animal and it's sound do this..." .items() is a built-in dictionary method that returns key-value pairs.
    #for key, value in ...
    for animal, sound in animal_sounds.items():
        print(f"{animal} goes {sound}")
    # # Only Keys
    # for key in my_dict.keys():
    # # Only Values
    # for value in my_dict.values():
    # Both
    # for key, value in my_dict.items():