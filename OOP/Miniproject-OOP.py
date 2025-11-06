# 🧾 Project: SmartBank System
# ------------------------------------------------------------
# 🎯 Objective:
# Design a SmartBank System using OOP concepts that simulates 
# basic bank operations for multiple customers.
# 
# ------------------------------------------------------------
# 🏗️ Class Structure:
# 1️⃣ Class Person:
#     - Attributes: name, age, address
#     - Method: show_info()
#
# 2️⃣ Class Customer(Person):
#     - Private Attributes: __balance, __pin
#     - Methods: deposit(), withdraw(), check_balance()
#     - Must verify pin before transactions (Encapsulation)
#
# ------------------------------------------------------------
# 💳 Inner Class:
# Inside Customer, create an inner class `Card`:
#     - Attributes: card_number, expiry_date, cvv
#     - Method: display_card_details()
#
# ------------------------------------------------------------
# 🧠 Polymorphism:
# Create another derived class `Staff(Person)`:
#     - Overrides show_info()
#     - Attributes: emp_id, department
#     - Method: authorize_transaction(customer)
#
# ------------------------------------------------------------
# 🏦 Class Variables:
#     - bank_name = "SmartBank" (shared by all)
#     - total_customers (count of Customer objects)
#
# ------------------------------------------------------------
# 🔒 Encapsulation:
#     - Private methods for PIN verification and validation.
#     - Prevent direct access to __balance and __pin.
#
# ------------------------------------------------------------
# 🧪 Demonstration:
# In main:
#     - Create a few customers and one staff member.
#     - Perform deposits, withdrawals, and balance checks.
#     - Use polymorphism:
#           for person in [customer1, customer2, staff1]:
#               person.show_info()
#     - Display card details via Customer.Card inner class.
#
# ------------------------------------------------------------
# ⚡ Bonus Challenge:
#     - Handle errors:
#           • Wrong PIN entry
#           • Negative deposit/withdrawal
#           • Deleting or blocking customer card
# ------------------------------------------------------------


class Person:
    bank_name = "SmartBank"
    total_customers = 0
    
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def show_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Address: {self.address}")


class Customer(Person):
    def __init__(self, name, age, address, balance, pin):
        super().__init__(name, age, address)
        self.__balance = balance
        self.__pin = pin
        Customer.total_customers += 1

        # Each customer has one card
        card_number = input(f"Enter card number for {self.name}: ")
        expiry_date = input("Enter expiry date: ")
        cvv = input("Enter CVV: ")
        self.card = self.Card(card_number, expiry_date, cvv)

    # ✅ Inner class
    class Card:
        def __init__(self, card_number, expiry_date, cvv):
            self.__card_number = card_number
            self.__expiry_date = expiry_date
            self.__cvv = cvv
        
        def get_cardno(self):
            return self.__card_number
        
        def get_expdate(self):
            return self.__expiry_date
        
        def display_card_details(self):
            print(f"Card Number: {self.__card_number} | Expiry: {self.__expiry_date} | CVV: {self.__cvv}")

    # ✅ Private method for PIN verification
    def __verifypin(self, userpin):
        return userpin == self.__pin

    # ✅ Transaction method
    def transactions(self, userpin):
        if self.__verifypin(userpin):
            print(f"Current Balance: {self.__balance}") 
            deposit = int(input("Enter amount to deposit (0 if none): "))
            if deposit >= 0:
                self.__balance += deposit
            withdraw = int(input("Enter amount to withdraw (0 if none): "))
            if 0 <= withdraw <= self.__balance:
                self.__balance -= withdraw
            print(f"Updated Balance: {self.__balance}")
        else:
            print("❌ Wrong PIN")

    # ✅ Public method to check balance only   
    def check_balance(self, userpin):
        if self.__verifypin(userpin):
            print(f"Balance is: {self.__balance}")
        else:
            print("❌ Wrong PIN")


class Staff(Person):
    def __init__(self, name, age, address, emp_id, department):
        super().__init__(name, age, address)
        self.emp_id = emp_id
        self.department = department
    
    def show_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Address: {self.address} | "
              f"Employee ID: {self.emp_id} | Department: {self.department}")

    # ✅ Authorize transaction (using polymorphism)
    def authorise_transaction(self, customer):
        print(f"✅ Staff {self.name} authorized transaction for {customer.name}")
        customer.card.display_card_details()


customers = []
staff = []

nc = int(input("Enter number of customers: "))
for i in range(nc):
    name = input("Enter Customer name: ")
    age = int(input("Enter Age: "))
    address = input("Enter Address: ")
    balance = int(input("Enter Initial Balance: "))
    pin = input("Set a 4-digit PIN: ")

    c = Customer(name, age, address, balance, pin)
    customers.append(c)

ns = int(input("Enter number of staff: "))
for i in range(ns):
    name = input("Enter Staff name: ")
    age = int(input("Enter Age: "))
    address = input("Enter Address: ")
    emp_id = input("Enter Employee ID: ")
    department = input("Enter Department: ")

    s = Staff(name, age, address, emp_id, department)
    staff.append(s)

print("\n--- Showing Info ---")
for person in customers + staff:
    person.show_info()

print("\n--- Transaction Demo ---")
for customer in customers:
    pin = input(f"Enter PIN for {customer.name}: ")
    customer.transactions(pin)

print("\n--- Staff Authorization ---")
if staff and customers:
    staff[0].authorise_transaction(customers[0])








        
