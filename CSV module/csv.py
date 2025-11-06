import csv
import os 
# %% Reading into a CSV file
os.chdir(r"C:\Users\Vishnu S\OneDrive\Documents\Desktop\python\CSV module") # changing directory 
with open("csv.csv","r") as file:
    reader=csv.reader(file) # We create a reader object. You can typecast this to a list
    for row in reader:
        print(row) # Each row is a list
# %% Writing into a CSV file
with open("csv.csv","a") as file:
    writer=csv.writer(file)
    writer.writerow(["Aditya",20,"Chennai","Software",60000])
# %% Reading using DictReader
# DictReader reads the CSV file using dictionaries. The first row of the CSV file become the keys for the remaining entries
with open("csv.csv","r") as file:
    reader=csv.DictReader(file) # Each line becomes a dictionary
    for row in reader:
        print(row["Name"],row["City"]) # Helps us access specific fields in the file
# %% Writing using DictWriter
with open("csvtest.csv","w") as file:
    fileheader=["Name","Age","Grade"]
    writer=csv.DictWriter(file,fieldnames=fileheader) # defining the structure of the entries. <write_object>=csv.DictWriter(<file_object>,fieldnames=<file_header>)
    writer.writeheader() # Writes the header i.e. name,age etc. Gets the info from 2nd term in DictWriter
    
    # Start writing rows now
    writer.writerow("Aditya",18,"A")
# When you're appending files, you dont need to use writeheader as you already have a header
# Also note we're using writerow() and writerows() instead of writeline() and writelines() for CSV files