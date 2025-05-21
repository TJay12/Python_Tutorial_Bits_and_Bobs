import os
# The os module in Python is part of the standard library and gives you a way to interact with the
    # operating system — like handling files, directories, and paths.

os.path.exists("filename.txt")  # Returns True if file/folder exists
# 💡 Extra Tip: If "data.txt" is in a different folder, you'd need to provide the full or relative path,
    # like "my_folder/filename.txt".

# 📂 Path Handling

# These are all under os.path:
os.path.exists(path) # Checks if the path exists.
os.path.isfile(path) # Is it a file?
os.path.isdir(path) # Is it a directory?
os.path.join("folder", "file.txt") # Joins parts of a path safely (cross-platform).
os.path.abspath("file.txt") # Returns the full absolute path.
os.path.basename(path) # Gets the filename from the path.
os.path.dirname(path) # Gets the folder part of the path.

# 🗂️ Working with Directories

os.listdir("folder") # Lists everything in a folder.
os.mkdir("new_folder") # Makes a new folder.
os.makedirs("a/b/c") # Makes folders recursively.
os.remove("file.txt") # Deletes a file.
os.rmdir("folder") # Deletes an empty folder.
os.getcwd() # Gets the current working directory.
os.chdir("new/folder") # Changes the working directory.