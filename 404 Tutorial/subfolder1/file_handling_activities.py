# # -------------------------------------------------------------------------------------------1-   <--- EASY --->
# # Create a file and add fav subject to it # Read and print file contents
# with open("file_handling_practice.txt", "w") as file:
#     fav_sub = input("Enter Favourite Subject: ")
#     file.write(f"Users fav subject is: {fav_sub}\n")
# # -------------------------------------------------------------------------------------------2-   <--- MEDIUM --->
# # A program that asks for 3 lines of text and saves them to file # Read the file and print each line in uppercase
# def write_lines():
#     with open("file_handling_practice.txt", "a") as pract_file:
#         for line in range(1, 4):
#             text = input(f"Write line {line}: ")
#             pract_file.write(f"{text}\n")
# def view_in_upper():
#     with open("file_handling_practice.txt", "r") as pract_file:
#         for line in pract_file:
#             print(f"{line.strip().upper()}")
# write_lines()
# view_in_upper()
# # -------------------------------------------------------------------------------------------3-   <--- HARDER --->
# # Build a simple notes app # The user can add notes to a file # The user can view all notes stored
# def add_note():
#     with open("notes.txt", "a") as notes:
#         write_note = input("Add Note To Memo: ")
#         notes.write(f" * {write_note}\n")
# def view_notes():
#     with open("notes.txt", "r") as notes:
#         lines = notes.readlines()
#         for note_line in lines:
#             print(note_line.strip())
# while True:
#     option = input("\nDo you wish to add note, view notes or exit? (a/v/x): ").lower()
#     if option == "a":
#         add_note()
#     elif option == "v":
#         view_notes()
#     elif option == "x":
#         break
#     else:
#         print("Invalid option")
# ---------------------------------------------------4-   <--- CHALLENGE --->
# Write a program that:
    # Checks if a file exists
    # If exists, append current date and message: "Checked on [current_date]"
    # If not, creates file and writes: "File created on [current_date]"
# (Use datetime module for current date)

import os
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d at %H:%M:%S")

if os.path.exists("filename.txt"):
    with open("filename.txt", "a") as file:
        file.write(f"Checked on {timestamp}\n")
else:
    with open("filename.txt", "w") as file:
        file.write(f"Created on {timestamp}\n")