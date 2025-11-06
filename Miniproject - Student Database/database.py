import csv
import os
import sys 

class StudentManagement:
    file_path = r"C:\Users\Vishnu S\OneDrive\Documents\Desktop\python\Miniproject - Student Database"
    os.chdir(file_path)
    fileheader = ["Roll Number", "Name", "Age", "Grade"]

    def __init__(self):
        pass

    def create_file(self):
        with open("records.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fileheader)
            writer.writeheader()        
          
    def add_student(self, students):
        if not os.path.exists("records.csv"):
            with open("records.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.fileheader)
                writer.writeheader()
        with open("records.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fileheader)
            writer.writerows(students)


    def show_info(self):  # 2. Show info
        with open("records.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"{row['Roll Number']} - {row['Name']} - {row['Age']} - {row['Grade']}")

    def search_student(self, roll):  # 3. Searching for student
        found = False
        with open("records.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Roll Number"] == roll:
                    print(row)
                    found = True
                    break
        if not found:
            print("Roll No does not exist. Do you want to make a new entry?")  

    def delete_record(self, record):  # 4. Deleting a record - can be optimised using pandas
        with open("records.csv", "r") as file:
            reader = list(csv.DictReader(file))
            if not reader:
                print("No records found.")
                return
            fileheader = reader[0].keys()

        with open("records.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fileheader)
            writer.writeheader()
            deleted = 0  # Flag variable
            for row in reader:
                if row["Roll Number"] != record:
                    writer.writerow(row)
                else:
                    deleted = 1
            if deleted:
                print("Record deleted.")
            else:
                print("Record not found.")

    def update_record(self, roll):  # 5. Updating a record - can be optimised using pandas
        with open("records.csv", "r") as file:
            reader = list(csv.DictReader(file))
            if not reader:
                print("No records found.")
                return
            fileheader = reader[0].keys()

        with open("records.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fileheader)
            writer.writeheader()
            flag = 0
            for row in reader:
                if row["Roll Number"] == roll:
                    name = str(input("Enter new name: "))
                    grade = str(input("Enter new grade: "))
                    row["Name"], row["Grade"] = name, grade
                    flag = 1
                writer.writerow(row)

            if flag:
                print("Record Updated.")
            else:
                print("Record not found.")

    def clearall(self):  # 6. Clear all records
        with open("records.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fileheader)
            writer.writeheader()
            print("All records cleared.")

    def prog_exit(self, c):  # 7. Exit
        if c == "Y":
            sys.exit()


# ------------------- MAIN -------------------
print('''Welcome to Student Manager!
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Update Student
6. Clear All Records
7. Exit''')

obj = StudentManagement()
choice = str(input("Enter choice: "))
students = []

match choice:
    case "1":
        n = int(input("Enter number of students to be recorded: "))
        for i in range(n):
            roll_no = input("Enter roll number: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            dict_ = {"Roll Number": roll_no, "Name": name, "Age": age, "Grade": grade}
            students.append(dict_)
        obj.add_student(students)
    case "2":
        obj.show_info()
    case "3":
        roll_no = input("Enter roll number: ")
        obj.search_student(roll_no)
    case "4":
        record = input("Enter roll number to delete: ")
        obj.delete_record(record)
    case "5":
        roll_no = input("Enter roll number to update: ")
        obj.update_record(roll_no)
    case "6":
        obj.clearall()
    case "7":
        obj.prog_exit("Y")
    case _:
        print("Invalid choice.")
