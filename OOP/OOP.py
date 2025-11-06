
# %% Example 
class Student:
    def __init__(self,name,rno,marks):
        self.name=name
        self.rno=rno
        self.marks=marks
    def show_details(self):
        print(f'''Name: {self.name}
                  Roll number: {self.rno}
                  Marks: {self.marks}''')
    def result(self):
        if self.marks>=35:
            print("Pass")
        else:
            print("Fail")
name=input()
rno=input()
marks=input()
s1=Student(name,rno,marks)
s1.show_details()
s1.result()
# %% Using class properties
class Employee:
    company_name="Technova Pvt Ltd"
    employee_count=0

    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.salary=salary
        Employee.employee_count+=1 # Since it's a class variable, we need to add class name behind
    
    def show_details(self,name,role,salary):
        print(f"Employee name: {self.name} | Employee role: {self.role} | Salary: {self.salary} | Company: {Employee.company_name} | Employee count: {Employee.employee_count}")
    
    def update_salary(self,new_salary):
        self.salary=new_salary
    
n=int(input("Enter number of employees: "))
employees=[]
for i in range(n):
    name=input("Enter Employee name:")
    role=input("Enter role: ")
    salary=int(input("Enter Salary: "))
    emp=Employee(name,role,salary)
    employees.append(emp)

for i in employees:
    i.show_details()


# Changing Class attributes
Employee.company_name= "CodeVerse Solutions"

# Adding properties
p2=Employee("Aditya","Engineer",60000)
p2.department="Frontend"
p2.show_details()

# Deleting properies
del p2.salary
try:
    print(p2.salary)
except:
    print("Salary doesn't exist")
# %% Inheritance 
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        print(f"{self.name} {self.age}")
class Student(Person):
    def __init__(self,name,age,grade):  # Define all variables in child class first
        super().__init__(name,age) # Call attributes from parent class into child
        self.grade=grade # Now define the extra property
        
    def show_student(self):
        print(f"{self.name} {self.age} {self.grade}")
    
s1=Student("ABC",18,"S")
s1.show_info()
s1.show_student()

s2=Student("BCD",19,"A")
s2.show_info()
s2.show_student()

s2.grade="S"
print(s2.grade)
# %% Polymorphism
# Polymorphism - refers to methods/functions/operators with the same name that can be executed on many objects or classes
# Class Polymorphism:
class Bird:
    def speak(self): # Common method
        print("Flies")

class Dog:
    def speak(self): # Common method
        print("Walks")

class Fish:
    def speak(self): # Common method
        print ("Swims")   
b=Bird()
d=Dog()
f=Fish()
animals=[b,d,f]
for i in animals:
    i.speak() # variable i takes up b or d or f as we iterate thru the loop

# Inheritance Polymorphism
class Animal:
    def __init__(self,name,species="Animal"): # By default species is animal
        self.name=name
        self.species=species
    
    def speak(self):
        print("Sound")
    def move(self):
        print("Move")
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name,"Dog") # Changing the species
        self.breed=breed
    def speak(self):
        print("Bark")
    def move(self):
        print("walks on 4 legs")
    def __str__(self):
        return f"{self.name} the {self.breed} ({self.species})"
class Bird(Animal):
    def __init__(self,name,wing_span):
        super().__init__(name,"Bird") # Changing the species
        self.wing_span=wing_span
    def speak(self):
        print("Chirp")
    def move(self):
        print("Flies")
    def __str__(self):
        return f"{self.name} with wingspan {self.wing_span} ({self.species})"
class Snake(Animal):
    def __init__(self,name,is_venomous):
        super().__init__(name,"Snake") # Changing the species
        self.is_venomous=is_venomous
    def move(self):
        print("Slithers")
    def __str__(self):
        venom_status = "Venomous" if self.is_venomous else "Non-venomous"
        return f"{self.name} ({self.species}) - {venom_status}"
# Making objects
dog=Dog("ABC","Labrador")
bird=Bird("DEF",25)
snake=Snake("EFG",True)
zoo=[dog,bird,snake]
for i in zoo:
    print(i) # Using __str__()
    i.speak()
    i.move()
    if isinstance(i,Snake):  # Use isinstance instead of i==Snake
        print(i.is_venomous)
# %% Encapsulation
# Encapsulation - Making variables private. Done by using __<variable_name>
# For variables - Define a getter method to call private variables and use them
# For methods - Call the function inside an internal function that already exists
# Name mangling - Ex: you define a variable __v under a class Abcdef. You can access it by doing {_Abcdef__v} instead of {__v} as python stores it like that. Not recommended
class ATM:
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
    
    def __verifypin(self,pinuser):  # Use self.__pin everywhere else outside the __init__ function
        if pinuser==self.__pin: 
            return True
    def check_balance(self,pinuser):
        if self.__verifypin(pinuser):
            print(f"Balance is: {self.__balance}") # Use self.__balance everywhere outside the __init__ function
            deposit=int(input("Enter amount to be deposited(0 if you dont wanna): "))
            self.__balance+=deposit
            withdraw=int(input("Enter amount to be withdrawn(0 if you dont wanna): "))
            self.__balance-=withdraw
        else:   
            print("Wrong pin")
# %% Inner classes
# Inner classes - For readability purposes
class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def process(self):
      print("Processing data...")

  class RAM:
    def store(self):
      print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()



        

