import os
# %% Getting and changing the current directory
print(os.getcwd()) # prints current working directory

os.chdir(r"C:\Users\Vishnu S\OneDrive\Documents") # change cwd
print(os.getcwd())
# %% Listing directories
print(os.listdir()) # lists stuff in this directory
print(os.listdir(r"C:\Users\Vishnu S\OneDrive\Documents")) # lists stuff in a specific directory
# %% Making and removing folders
os.mkdir("Test1") # creates a new folder
os.rmdir("Test1") # deletes folder
# %% File operations
os.remove("text.txt") # deletes a file

if os.path.exists("notes.txt"): # check if file exists
    print("File exists")
else:
    print("No such file")

print(os.path.isfile("text.txt"))      # True if it's a file
print(os.path.isdir("Documents"))       # True if it's a directory
# %% Working with paths
# Joining paths
path = os.path.join(r"C:\\Users\\Aditya", "data.txt")
print(path)
# Output: C:\Users\Aditya\data.txt

#Spliting paths
print(os.path.split(r"C:\\Users\\Aditya\\data.txt"))
# ('C:\\Users\\Aditya', 'data.txt')

print(os.path.basename(r"C:\\Users\\Aditya\\data.txt"))  # data.txt
print(os.path.dirname(r"C:\\Users\\Aditya\\data.txt"))   # C:\Users\Aditya
print(os.path.splitext(r"data.txt"))                     # ('data', '.txt')
# %% System commands
# We can run system commands from python
os.system("notepad")     # opens Notepad
os.system("dir")         # lists files (Windows)