# Load SaveFile Back into Variables
    # Read the file line by line,
    # Split values where needed (like Name: TJ)
    # Store them into Python variables

player_name = ""
level = 0
health = 0.0
inventory = []

# STEP 1: Read the File Line-by-Line
with open("savegame.txt", "r") as save_file:
    # readlines() reads each line of the file and returns a list
    lines = save_file.readlines()
    # So lines becomes:
    # [
    #     "Name: TJ\n",
    #     "Level: 5\n",
    #     "Health: 87.5\n",
    #     "Inventory:\n",
    #     " - Sword\n",
    #     " - Potion\n",
    #     " - Shield\n"
    # ]

# STEP 2: Strip Newlines
# This removes the leading and trailing characters from each line
lines = [line.strip() for line in lines] # Remove newline characters
# Now lines is:
# [
#     "Name: TJ",
#     "Level: 5",
#     "Health: 87.5",
#     "Inventory:",
#     "- Sword",
#     "- Potion",
#     "- Shield"
# ]

# STEP 3: Parse Basic Values (Name, Level, Health)
# Parse the first 3 lines
player_name = lines[0].split(": ")[1]
# lines[0] is "Name: TJ"
    # .split(": ") gives ["Name", "TJ"]
    # We take th second part: "TJ"
level = int(lines[1].split(": ")[1])
# lines[1] is "Level: 5"
    # .split(": ") gives ["Level", "5"]
    # Convert "5" to an integer: int("5")
health = float(lines[2].split(": ")[1])
# lines[2] is "Health: 87.5"
    # Convert "87.5" to a float: float("87.5")

# STEP 4: Parse the Inventory List
# Parse inventory items (lines after "Inventory")
inventory = []
# lines.index("Inventory:") finds the line where inventory begins (index 3)
    # We start from the next line using + 1
inventory_start = lines.index("Inventory:") + 1
for line in lines[inventory_start:]:
    # Each item line begins with - , so we check for that
    if line.startswith("- "):
        # line[2:] slices off the - part.
        inventory.append(line[2:])
# Result:
# inventory = ['Sword', 'Potion', 'Shield']

# Final Output (for checking)
print("Name:", player_name)
print("Level:", level)
print("Health", health)
print("Inventory", inventory)