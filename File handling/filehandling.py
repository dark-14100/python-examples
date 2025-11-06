# <file_name> = open(<path>,<mode>) ; mode = r,w,a,r+,w+,a+
# <file_name>.close() - to close a file

# <file_name>.read([n]) - reads at most n bytes, whole file if not specified - output:string
# <file_name>.readline([n]) - reads one full line, n bytes if specified - output: string with \n character
# <file_name>.readlines() -  reads all lines and returns them in a list

# <file_name>.write(str) - writes the given string into the file
# <file_name>.writelines(L) - writes all strings in list L as new lines in file

# <file_name>.flush() - saves all data in buffer into the disk, basically a "save now" function

# <file_name>.tell() - returns current position of file pointer
# <file_name>.seek(offset,[whence]) - Moves to desired byte. Check example 

# %%
# Reading all lines of a file

with open(r"C:\Users\Vishnu S\OneDrive\Documents\Desktop\python\File handling\text.txt","r") as f: # using with...as... automatically closes the file after loop terminates 
    for line in f:
        print(line, end="")
# %%
# Seek and Tell
f=open(r"C:\Users\Vishnu S\OneDrive\Documents\Desktop\python\File handling\text.txt","r")
f.seek(10) # Moves to 10th byte

f.seek(0) # Moves to start of file

f.seek(5,1) # Move 5 bytes from current postion (1 means current position)
f.seek(2,2) # Move 2 bytes from end of file (2 means end of file)

f.close()
# %%




