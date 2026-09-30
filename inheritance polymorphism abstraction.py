from abc import ABC, abstractmethod

# ---------- Inheritance ----------

# Q1
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.emp_id, self.name, self.salary)

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def annual_salary(self):
        return self.salary * 12

m1 = Manager("M1", "Amit", 50000, "IT")
m1.display()
print(m1.department, m1.annual_salary())

# Q2
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(self.brand, self.model)

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)

car1 = Car("Toyota", "Corolla", "Petrol", 2000000)
car1.display()
print(car1.discounted_price(10))

# Q3
class Academic:
    def __init__(self, academic_marks):
        self.academic_marks = academic_marks

class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points

class Student(Academic, Sports):
    def __init__(self, academic_marks, sports_points):
        Academic.__init__(self, academic_marks)
        Sports.__init__(self, sports_points)

    def overall_performance(self):
        return self.academic_marks + self.sports_points

s1 = Student(85, 10)
print(s1.overall_performance())

# Q4
class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary

class Employee2(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print(self.name, self.age, self.emp_id, self.designation, self.salary)

e1 = Employee2("Ravi", 28, "E1", "Manager", 60000)
e1.display()

# Q5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student2(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

class ResearchStudent(Student2):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print(self.name, self.age, self.roll_no, self.course, self.research_topic, self.guide_name)

rs1 = ResearchStudent("Amit", 24, 101, "MTech", "AI", "Dr. Rao")
rs1.display()

# Q6
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print(self.account_number, self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, benefits):
        super().__init__(account_number, balance, interest_rate)
        self.benefits = benefits

psa = PremiumSavingsAccount("A1", 50000, 0.05, "Free locker")
psa.display()
print(psa.calculate_interest(), psa.benefits)

# Q7
class Shape:
    def display_name(self):
        print("This is a shape")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

for shape in [Circle(5), Rectangle(4, 6), Triangle(3, 8)]:
    shape.display_name()
    print(shape.area())

# Q8
class Employee3:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

class Manager2(Employee3):
    def calculate_salary(self):
        return self.basic_salary + 10000

class Developer(Employee3):
    def calculate_salary(self):
        return self.basic_salary + 7000

class Tester(Employee3):
    def calculate_salary(self):
        return self.basic_salary + 5000

for emp in [Manager2("E1", "Amit", 30000), Developer("E2", "Priya", 28000), Tester("E3", "Rahul", 25000)]:
    print(emp.name, emp.calculate_salary())

# Q9
class Person2:
    def __init__(self, name):
        self.name = name

class Student3(Person2):
    def __init__(self, name, roll_no):
        Person2.__init__(self, name)
        self.roll_no = roll_no

class Faculty(Person2):
    def __init__(self, name, faculty_id):
        Person2.__init__(self, name)
        self.faculty_id = faculty_id

class TeachingAssistant(Student3, Faculty):
    def __init__(self, name, roll_no, faculty_id):
        Student3.__init__(self, name, roll_no)
        Faculty.__init__(self, name, faculty_id)

    def display(self):
        print(self.name, self.roll_no, self.faculty_id)

ta = TeachingAssistant("Amit", 101, "F1")
ta.display()

# Q10
class Vehicle2:
    def __init__(self, brand):
        self.brand = brand

class Car2(Vehicle2):
    def car_info(self):
        print("Car brand:", self.brand)

class Bike(Vehicle2):
    def bike_info(self):
        print("Bike brand:", self.brand)

class SportsCar(Car2):
    def top_speed(self):
        print("Top speed: 300 km/h")

class ElectricBike(Bike):
    def battery_range(self):
        print("Range: 100 km")

sc = SportsCar("Ferrari")
sc.car_info()
sc.top_speed()
eb = ElectricBike("Ather")
eb.bike_info()
eb.battery_range()

# Q11
class Student4:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

class Result(Student4):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        pct = self.percentage()
        return "A" if pct >= 75 else "B" if pct >= 50 else "C"

r1 = Result(101, "Amit", "BCA", [80, 85, 90])
print(r1.total(), r1.percentage(), r1.grade())

# Q12
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)

ep = ElectronicProduct("P1", "TV", 40000, "Sony", 2)
print(ep.final_price(15))

# Q13
class Printer:
    def print_doc(self):
        print("Printing document")

class Scanner:
    def scan_doc(self):
        print("Scanning document")

class MultifunctionDevice(Printer, Scanner):
    pass

mfd = MultifunctionDevice()
mfd.print_doc()
mfd.scan_doc()

# Q14
class Camera:
    def take_photo(self):
        print("Taking photo")

class Phone:
    def make_call(self):
        print("Making call")

class Smartphone(Camera, Phone):
    pass

sp = Smartphone()
sp.take_photo()
sp.make_call()

# Q15 - same pattern as Q5 (Person -> Student -> ResearchStudent)

# Q16 - same pattern as Q5 (Person -> Student -> ResearchStudent)

# Q17
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(self.name, "is an animal")

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

class Cat(Animal):
    def sound(self):
        print(self.name, "meows")

class Cow(Animal):
    def sound(self):
        print(self.name, "moos")

for animal in [Dog("Rex"), Cat("Whiskers"), Cow("Ginger")]:
    animal.info()
    animal.sound()

# Q18
class Person3:
    def __init__(self, name):
        self.name = name

class Doctor(Person3):
    def treat(self):
        print(self.name, "treats patients")

class Patient(Person3):
    def get_treated(self):
        print(self.name, "gets treated")

class Surgeon(Doctor):
    def operate(self):
        print(self.name, "performs surgery")

class MedicalResearcher(Doctor, Patient):
    def research(self):
        print(self.name, "does medical research")

mr = MedicalResearcher("Dr. Rao")
mr.treat()
mr.research()

# ---------- Polymorphism ----------

# Q19
class Shape2:
    def area(self):
        pass

class Circle2(Shape2):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle2(Shape2):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle2(Shape2):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

for shape in [Circle2(5), Rectangle2(4, 6), Triangle2(3, 8)]:
    print(shape.area())

# Q20
class Employee4:
    def calculate_salary(self):
        pass

class Manager3(Employee4):
    def calculate_salary(self):
        return 60000

class Developer2(Employee4):
    def calculate_salary(self):
        return 50000

class Tester2(Employee4):
    def calculate_salary(self):
        return 40000

for emp in [Manager3(), Developer2(), Tester2()]:
    print(emp.calculate_salary())

# Q21
class Vehicle3:
    def start(self):
        pass

class Car3(Vehicle3):
    def start(self):
        print("Car starts with key")

class Bike2(Vehicle3):
    def start(self):
        print("Bike starts with self-start")

class Bus(Vehicle3):
    def start(self):
        print("Bus starts with ignition")

for v in [Car3(), Bike2(), Bus()]:
    v.start()

# Q22
class Animal2:
    def sound(self):
        pass

class Dog2(Animal2):
    def sound(self):
        print("Woof")

class Cat2(Animal2):
    def sound(self):
        print("Meow")

class Cow2(Animal2):
    def sound(self):
        print("Moo")

class Lion(Animal2):
    def sound(self):
        print("Roar")

for a in [Dog2(), Cat2(), Cow2(), Lion()]:
    a.sound()

# Q23
class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending email notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification")

class PushNotification(Notification):
    def send(self):
        print("Sending push notification")

for n in [EmailNotification(), SMSNotification(), PushNotification()]:
    n.send()

# Q24
class Student5:
    def calculate_grade(self):
        pass

class EngineeringStudent(Student5):
    def calculate_grade(self):
        return "Engineering grading applied"

class MedicalStudent(Student5):
    def calculate_grade(self):
        return "Medical grading applied"

class ManagementStudent(Student5):
    def calculate_grade(self):
        return "Management grading applied"

for s in [EngineeringStudent(), MedicalStudent(), ManagementStudent()]:
    print(s.calculate_grade())

# Q25
class BankAccount2:
    def calculate_interest(self):
        pass

class SavingsAccount2(BankAccount2):
    def calculate_interest(self):
        return "4% interest"

class CurrentAccount(BankAccount2):
    def calculate_interest(self):
        return "No interest"

class FixedDepositAccount(BankAccount2):
    def calculate_interest(self):
        return "7% interest"

for acc in [SavingsAccount2(), CurrentAccount(), FixedDepositAccount()]:
    print(acc.calculate_interest())

# Q26
class Report:
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("Generating PDF report")

class ExcelReport(Report):
    def generate(self):
        print("Generating Excel report")

class HTMLReport(Report):
    def generate(self):
        print("Generating HTML report")

def generate_report(report):
    report.generate()

for r in [PDFReport(), ExcelReport(), HTMLReport()]:
    generate_report(r)

# Q27
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = (self.feet + other.feet) * 12 + (self.inches + other.inches)
        return Distance(total_inches // 12, total_inches % 12)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")

d1 = Distance(5, 8)
d2 = Distance(3, 9)
d3 = d1 + d2
d3.display()

# Q28
class Student6:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        return self.total_marks < other.total_marks

s1 = Student6("Amit", 450)
s2 = Student6("Priya", 470)
print(s1 > s2, s1 < s2)

# Q29
class ProductP:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

p1 = ProductP("Phone", 20000)
p2 = ProductP("Tablet", 20000)
print(p1 == p2, p1 > p2)

# Q30
class Payment:
    def make_payment(self, amount):
        pass

class UPIPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using UPI")

class CardPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using Card")

class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using Wallet")

def process_payment(payment, amount):
    payment.make_payment(amount)

for p in [UPIPayment(), CardPayment(), WalletPayment()]:
    process_payment(p, 500)

# Q31
class Person4:
    def display_role(self):
        pass

class Student7(Person4):
    def display_role(self):
        print("I am a Student")

class Faculty2(Person4):
    def display_role(self):
        print("I am a Faculty member")

class Administrator(Person4):
    def display_role(self):
        print("I am an Administrator")

people = [Student7(), Faculty2(), Administrator()]
for person in people:
    person.display_role()

# Q32
class Media:
    def play(self):
        pass

class Audio(Media):
    def play(self):
        print("Playing audio")

class Video(Media):
    def play(self):
        print("Playing video")

class Podcast(Media):
    def play(self):
        print("Playing podcast")

for m in [Audio(), Video(), Podcast()]:
    m.play()

# Q33
class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(SmartDevice):
    def turn_on(self):
        print("Light on")

    def turn_off(self):
        print("Light off")

class Fan(SmartDevice):
    def turn_on(self):
        print("Fan on")

    def turn_off(self):
        print("Fan off")

class AC(SmartDevice):
    def turn_on(self):
        print("AC on")

    def turn_off(self):
        print("AC off")

class TV(SmartDevice):
    def turn_on(self):
        print("TV on")

    def turn_off(self):
        print("TV off")

for d in [Light(), Fan(), AC(), TV()]:
    d.turn_on()
    d.turn_off()

# ---------- Abstraction ----------

# Q34
class Shape3(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle3(Shape3):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle3(Shape3):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle3(Shape3):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

for shape in [Circle3(5), Rectangle3(4, 6), Triangle3(3, 8)]:
    print(shape.area())

# Q35
class Vehicle4(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car4(Vehicle4):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class Bike3(Vehicle4):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")

class Bus2(Vehicle4):
    def start(self):
        print("Bus started")

    def stop(self):
        print("Bus stopped")

for v in [Car4(), Bike3(), Bus2()]:
    v.start()
    v.stop()

# Q36
class BankAccount3(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount3(BankAccount3):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class CurrentAccount2(BankAccount3):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

sa = SavingsAccount3()
sa.deposit(1000)
sa.withdraw(200)
print(sa.balance)

# Q37
class FoodOrder2(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder2):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 0

class HomeDeliveryOrder(FoodOrder2):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 50

for order in [RestaurantOrder(), HomeDeliveryOrder()]:
    print(order.calculate_bill(), order.delivery_charge())

# Q38
class Patient2(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass

class InPatient(Patient2):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-patient treatment")

class OutPatient(Patient2):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        print("Out-patient treatment")

class EmergencyPatient(Patient2):
    def calculate_bill(self):
        return 8000

    def treatment(self):
        print("Emergency treatment")

for p in [InPatient(), OutPatient(), EmergencyPatient()]:
    p.treatment()
    print(p.calculate_bill())

# Q39
class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass

class Bus3(Transport):
    def calculate_fare(self, distance):
        return distance * 2

class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5

class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10

class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 20

for t in [Bus3(), Train(), Taxi(), Flight()]:
    print(t.calculate_fare(100))

# Q40
class Question(ABC):
    @abstractmethod
    def evaluate_answer(self):
        pass

class MCQQuestion(Question):
    def evaluate_answer(self):
        print("Evaluating MCQ answer")

class TrueFalseQuestion(Question):
    def evaluate_answer(self):
        print("Evaluating True/False answer")

class DescriptiveQuestion(Question):
    def evaluate_answer(self):
        print("Evaluating descriptive answer")

for q in [MCQQuestion(), TrueFalseQuestion(), DescriptiveQuestion()]:
    q.evaluate_answer()

# Q41
class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using password")

class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")

class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using biometrics")

for auth in [PasswordAuthentication(), OTPAuthentication(), BiometricAuthentication()]:
    auth.authenticate()

# Q42
class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("Uploading to Google Drive")

    def download_file(self):
        print("Downloading from Google Drive")

    def delete_file(self):
        print("Deleting from Google Drive")

class Dropbox(CloudStorage):
    def upload_file(self):
        print("Uploading to Dropbox")

    def download_file(self):
        print("Downloading from Dropbox")

    def delete_file(self):
        print("Deleting from Dropbox")

for storage in [GoogleDrive(), Dropbox()]:
    storage.upload_file()
    storage.download_file()
    storage.delete_file()

# Q43
class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass

class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 300

class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 800

class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 1500

for a in [GeneralAppointment(), SpecialistAppointment(), EmergencyAppointment()]:
    a.book_appointment()
    print(a.calculate_fee())
