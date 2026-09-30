# Q1
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print(self.roll_no, self.name, self.marks, "Percentage:", percentage)

s1 = Student(101, "Amit", [80, 85, 90])
s2 = Student(102, "Priya", [95, 92, 88])
s1.display()
s2.display()

# Q2
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.2

    def calculate_da(self):
        return self.basic_salary * 0.1

    def gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

e1 = Employee("E1", "Ravi", 30000)
print(e1.gross_salary())

# Q3
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

r1 = Rectangle(10, 5)
print(r1.area(), r1.perimeter())

# Q4
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

c1 = Circle(7)
print(c1.area(), c1.circumference())

# Q5
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(self.book_id, self.title, self.author, self.price)

b1 = Book("B1", "Python Basics", "John", 350)
b2 = Book("B2", "Data Structures", "Smith", 450)
b3 = Book("B3", "Algorithms", "Cormen", 800)
for b in [b1, b2, b3]:
    b.display()

# Q6
class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        units = self.units
        if units <= 100:
            return units * 5
        elif units <= 300:
            return 100 * 5 + (units - 100) * 7
        else:
            return 100 * 5 + 200 * 7 + (units - 300) * 10

bill = ElectricityBill("C1", "Amit", 350)
print(bill.calculate_bill())

# Q7
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print(self.brand, self.model, self.storage, self.price)

    def price_after_discount(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)

phone = MobilePhone("Samsung", "Galaxy", "128GB", 25000)
phone.display_specs()
print(phone.price_after_discount(10))

# Q8
class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print(self.patient_id, self.name, self.age, self.disease)

    def total_bill(self, extra_charges=0):
        return self.consultation_fee + extra_charges

p1 = Patient("P1", "Amit", 30, "Fever", 500)
p1.display()
print(p1.total_bill(200))

# Q9
class ATM:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_details(self):
        print("Account holder:", self.name, "Balance:", self.balance)

atm = ATM("Amit", 1000)
while True:
    print("1.Check Balance 2.Deposit 3.Withdraw 4.Display Details 5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        atm.deposit(float(input("Enter amount: ")))
    elif choice == "3":
        atm.withdraw(float(input("Enter amount: ")))
    elif choice == "4":
        atm.display_details()
    elif choice == "5":
        break
    else:
        print("Invalid choice")

# Q10
class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate):
        self.vehicle_number = vehicle_number
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self):
        self.available = False

    def return_vehicle(self):
        self.available = True

    def calculate_rent(self, days):
        return self.rental_rate * days

v1 = Vehicle("V1", "Swift", 1500)
v1.rent()
print(v1.calculate_rent(5))
v1.return_vehicle()

# Q11
class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, product, price):
        self.products.append((product, price))

    def remove_product(self, product):
        self.products = [p for p in self.products if p[0] != product]

    def total_bill(self):
        return sum(p[1] for p in self.products)

    def __del__(self):
        print("Shopping cart destroyed for", self.customer_name)

cart = ShoppingCart("Amit", "C1")
cart.add_product("Shoes", 1500)
cart.add_product("Shirt", 800)
print(cart.total_bill())
cart.remove_product("Shirt")
del cart

# Q12
class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self, tax_percent=5):
        amount = self.quantity * self.price
        return amount + (amount * tax_percent / 100)

    def __del__(self):
        print("Order completed for", self.customer_name)

order = FoodOrder("O1", "Amit", "Pizza", 2, 300)
print(order.total_bill())
del order

# Q13
class StudentResult:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        pct = self.percentage()
        if pct >= 90: return "A"
        elif pct >= 75: return "B"
        elif pct >= 60: return "C"
        else: return "D"

    def __del__(self):
        print("Result processing completed for", self.student_name)

result = StudentResult("Amit", [85, 90, 78, 88, 92])
print(result.total(), result.percentage(), result.grade())
del result
