# with open() - The Safe Way to Handle Files
    # It auto-closes the file, even if there's an error inside the block.
    # Cleaner and more readable.

# Instead of:
file = open("myfile.txt", "r")
    # work with file
file.close()

# Use:
with open("myfile.txt", "r") as file:
    data = file.read()
    print(data)
# file auto closes after the block

# Writing Formatted Data
    # Example: Save File

player_name = "TJ"
level = 5
health = 87.5
inventory = ["Sword", "Potion", "Shield"]

with open("savegame.txt", "w") as save_file:
    save_file.write(f"Name: {player_name}\n")
    save_file.write(f"Level: {level}\n")
    save_file.write(f"Health: {health}\n")
    save_file.write(f"Inventory:\n")
    for item in inventory:
        save_file.write(f" - {item}\n")

with open("savegame.txt", "r") as save_file:
    print(save_file.read())