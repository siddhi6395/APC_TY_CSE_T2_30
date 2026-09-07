# Q1. Factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial:", factorial(5))

# Q2. Check even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Even or Odd:", check_even_odd(7))

# Q3. Return the greater of two numbers
def greater_number(a, b):
    if a > b:
        return a
    return b

print("Greater number:", greater_number(10, 25))

# Q4. Simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

print("Simple interest:", simple_interest(1000, 5, 2))

# Q5. Check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is prime:", is_prime(17))

# Q6. Area of a circle
def area_of_circle(radius):
    return 3.14 * radius * radius

print("Area of circle:", area_of_circle(7))

# Q7. Sum of first n natural numbers
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("Sum of natural numbers:", sum_natural(10))

# Q8. Power function
def power(base, exponent):
    return base ** exponent

print("Power result:", power(2, 5))

# Q9. Largest element without max()
def find_largest(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest

print("Largest element:", find_largest([23, 45, 12, 67, 34]))

# Q10. Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print("Vowel count:", count_vowels("Hello World"))

# Q11. Reverse a string
def reverse_string(text):
    return text[::-1]

print("Reversed string:", reverse_string("Python"))

# Q12. Check palindrome for string or number
def is_palindrome(value):
    text = str(value)
    return text == text[::-1]

print("Is palindrome:", is_palindrome("madam"))

# Q13. Average of a list of numbers
def find_average(nums):
    return sum(nums) / len(nums)

print("Average:", find_average([10, 20, 30, 40]))

# Q14. Count occurrences of an element in a list
def count_occurrence(nums, element):
    return nums.count(element)

print("Occurrence count:", count_occurrence([1, 2, 2, 3, 2, 4], 2))

# Q15. Unique elements from a list
def get_unique(nums):
    return list(set(nums))

print("Unique elements:", get_unique([1, 2, 2, 3, 3, 4]))

# Q16. Second largest number in a list
def second_largest(nums):
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[1]

print("Second largest:", second_largest([23, 45, 12, 67, 34]))

# Q17. First n Fibonacci numbers
def fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n]

print("Fibonacci numbers:", fibonacci(8))

# Q18. Percentage and grade from marks in five subjects
def calculate_grade(marks):
    total = sum(marks)
    percentage = total / len(marks)
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"
    return percentage, grade

print("Percentage and grade:", calculate_grade([85, 90, 78, 92, 88]))

# Q19. Electricity bill based on slabs
def electricity_bill(units):
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 7
    return bill

print("Electricity bill:", electricity_bill(250))

# Q20. Gross salary after HRA and DA
def gross_salary(basic):
    hra = basic * 0.2
    da = basic * 0.1
    return basic + hra + da

print("Gross salary:", gross_salary(30000))

# Q21. Total bill after discount
def total_bill(prices, quantities, discount):
    total = 0
    for price, qty in zip(prices, quantities):
        total += price * qty
    total -= total * discount / 100
    return total

print("Total bill:", total_bill([100, 200, 50], [2, 1, 3], 10))

# Q22. Min, max, sum, average of a list
def list_stats(nums):
    return min(nums), max(nums), sum(nums), sum(nums) / len(nums)

print("List stats:", list_stats([10, 20, 30, 40, 50]))

# Q23. Student records processing
def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks):
    return sum(marks) / len(marks)

def calculate_student_grade(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 50:
        return "B"
    return "C"

students23 = [
    {"name": "Amit", "roll_number": 1, "marks": [85, 90, 78, 92, 88]},
    {"name": "Riya", "roll_number": 2, "marks": [70, 65, 80, 75, 60]},
]

for student in students23:
    total = calculate_total(student["marks"])
    percentage = calculate_percentage(student["marks"])
    grade = calculate_student_grade(percentage)
    print(student["name"], "Total:", total, "Percentage:", percentage, "Grade:", grade)

all_percentages = [calculate_percentage(s["marks"]) for s in students23]
class_average = sum(all_percentages) / len(all_percentages)
highest_scorer = students23[all_percentages.index(max(all_percentages))]["name"]
lowest_scorer = students23[all_percentages.index(min(all_percentages))]["name"]
print("Class average:", class_average)
print("Highest scorer:", highest_scorer)
print("Lowest scorer:", lowest_scorer)

# Q24. Bank functions
transactions24 = []
balance24 = 0

def deposit(amount):
    global balance24
    balance24 += amount
    transactions24.append("Deposited " + str(amount))

def withdraw(amount):
    global balance24
    if amount > balance24:
        print("Insufficient balance")
    else:
        balance24 -= amount
        transactions24.append("Withdrew " + str(amount))

def balance_enquiry():
    return balance24

deposit(5000)
withdraw(2000)
withdraw(10000)
print("Current balance:", balance_enquiry())
print("Transaction history:", transactions24)

# Q25. Library functions
library25 = {}

def add_book(book_id, name, quantity):
    library25[book_id] = {"name": name, "quantity": quantity}

def issue_book(book_id):
    if library25[book_id]["quantity"] > 0:
        library25[book_id]["quantity"] -= 1
    else:
        print("Book not available")

def return_book(book_id):
    library25[book_id]["quantity"] += 1

def search_book(book_id):
    return library25.get(book_id)

def display_books():
    print("Available books:")
    for book_id, details in library25.items():
        print(book_id, details)

add_book("B001", "Python Basics", 3)
add_book("B002", "Data Science", 2)
issue_book("B001")
return_book("B002")
print("Search result:", search_book("B001"))
display_books()

# Q26. Modular electricity billing program
def calculate_units_charge(units):
    if units <= 100:
        return units * 3
    elif units <= 200:
        return 100 * 3 + (units - 100) * 5
    return 100 * 3 + 100 * 5 + (units - 200) * 7

def calculate_fixed_charge():
    return 50

def calculate_tax(amount):
    return amount * 0.05

def calculate_discount(amount):
    return amount * 0.02

def generate_bill(units):
    units_charge = calculate_units_charge(units)
    fixed_charge = calculate_fixed_charge()
    subtotal = units_charge + fixed_charge
    tax = calculate_tax(subtotal)
    discount = calculate_discount(subtotal)
    final_bill = subtotal + tax - discount
    return final_bill

print("Final electricity bill:", generate_bill(250))

# Q27. Hospital billing functions
def consultation_charge():
    return 500

def lab_charge(tests):
    return tests * 200

def medicine_charge(amount):
    return amount

def room_charge(days):
    return days * 1000

def calculate_final_bill(tests, medicine_amount, days, category):
    total = consultation_charge() + lab_charge(tests) + medicine_charge(medicine_amount) + room_charge(days)
    if category == "senior_citizen":
        total -= total * 0.1
    return total

print("Hospital final bill:", calculate_final_bill(3, 1500, 2, "senior_citizen"))

# Q28. Shopping cart invoice functions
cart28 = {}

def add_product(name, price, quantity):
    cart28[name] = {"price": price, "quantity": quantity}

def remove_product(name):
    if name in cart28:
        del cart28[name]

def calculate_subtotal():
    subtotal = 0
    for item in cart28.values():
        subtotal += item["price"] * item["quantity"]
    return subtotal

def apply_coupon(subtotal, coupon_percent):
    return subtotal - (subtotal * coupon_percent / 100)

def calculate_gst(amount):
    return amount * 0.18

def generate_invoice(coupon_percent):
    subtotal = calculate_subtotal()
    after_coupon = apply_coupon(subtotal, coupon_percent)
    gst = calculate_gst(after_coupon)
    final_amount = after_coupon + gst
    return final_amount

add_product("Shirt", 800, 2)
add_product("Shoes", 2000, 1)
remove_product("Shoes")
print("Final invoice amount:", generate_invoice(10))

# Q29. Recursive binary search
def binary_search(nums, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums, target, mid + 1, high)
    else:
        return binary_search(nums, target, low, mid - 1)

sorted_nums29 = [10, 20, 30, 40, 50, 60]
print("Index found at:", binary_search(sorted_nums29, 40, 0, len(sorted_nums29) - 1))

# Q30. Decimal to binary using recursion
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

print("Binary value:", decimal_to_binary(25))

# Q31. Palindrome check using recursion
def is_palindrome_recursive(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome_recursive(text[1:-1])

print("Is palindrome:", is_palindrome_recursive("madam"))

# Q32. Pass functions as arguments to calculate()
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(func, a, b):
    return func(a, b)

print("Addition:", calculate(add, 10, 5))
print("Subtraction:", calculate(subtract, 10, 5))
print("Multiplication:", calculate(multiply, 10, 5))
print("Division:", calculate(divide, 10, 5))


# ---------------- Programs on Lambda Function ----------------

# Q33. Lambda for square of a number
square = lambda n: n * n
print("Square:", square(6))

# Q34. Lambda for cube of a number
cube = lambda n: n ** 3
print("Cube:", cube(3))

# Q35. Lambda for even check
is_even = lambda n: n % 2 == 0
print("Is even:", is_even(8))

# Q36. Lambda for maximum of two numbers
max_of_two = lambda a, b: a if a > b else b
print("Maximum:", max_of_two(15, 25))

# Q37. Lambda for simple interest
simple_interest_lambda = lambda p, r, t: (p * r * t) / 100
print("Simple interest:", simple_interest_lambda(1000, 5, 2))

# Q38. map() and lambda to get squares of a list
nums38 = [1, 2, 3, 4, 5]
squares38 = list(map(lambda n: n * n, nums38))
print("Squares list:", squares38)

# Q39. map() and lambda to get cubes of a list
nums39 = [1, 2, 3, 4, 5]
cubes39 = list(map(lambda n: n ** 3, nums39))
print("Cubes list:", cubes39)

# Q40. map() and lambda to add corresponding elements of two lists
list_a40 = [1, 2, 3]
list_b40 = [4, 5, 6]
sum_list40 = list(map(lambda x, y: x + y, list_a40, list_b40))
print("Sum list:", sum_list40)

# Q41. filter() and lambda to extract even numbers
nums41 = [1, 2, 3, 4, 5, 6, 7, 8]
evens41 = list(filter(lambda n: n % 2 == 0, nums41))
print("Even numbers:", evens41)

# Q42. filter() and lambda to extract prime numbers
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nums42 = [10, 11, 13, 15, 17, 20, 23]
primes42 = list(filter(lambda n: check_prime(n), nums42))
print("Prime numbers:", primes42)

# Q43. filter() and lambda to extract positive numbers
nums43 = [-5, 3, -2, 8, -1, 10]
positives43 = list(filter(lambda n: n > 0, nums43))
print("Positive numbers:", positives43)

# Q44. filter() and lambda for numbers greater than 50
nums44 = [10, 60, 45, 80, 30, 90]
greater_than_50 = list(filter(lambda n: n > 50, nums44))
print("Numbers greater than 50:", greater_than_50)

# Q45. filter() and lambda for words having more than five characters
words45 = ["cat", "elephant", "dog", "giraffe", "ant"]
long_words = list(filter(lambda w: len(w) > 5, words45))
print("Words with more than five characters:", long_words)

# Q46. Sort words according to length using lambda
words46 = ["banana", "kiwi", "apple", "fig"]
sorted_words46 = sorted(words46, key=lambda w: len(w))
print("Sorted by length:", sorted_words46)

# Q47. Sort students by marks using lambda
students47 = [("Amit", 85), ("Riya", 90), ("Sam", 78)]
sorted_students47 = sorted(students47, key=lambda s: s[1])
print("Sorted by marks:", sorted_students47)

# Q48. Sort employee records by salary using lambda
employees48 = [("Amit", 45000), ("Riya", 60000), ("Sam", 30000)]
sorted_employees48 = sorted(employees48, key=lambda e: e[1])
print("Sorted by salary:", sorted_employees48)

# Q49. Student marks - average, filter above 75, sort by marks
students49 = [("Amit", 85), ("Riya", 90), ("Sam", 60), ("Neha", 78)]

def average_marks(students):
    total = sum(map(lambda s: s[1], students))
    return total / len(students)

above_75 = list(filter(lambda s: s[1] > 75, students49))
sorted_students49 = sorted(students49, key=lambda s: s[1])
print("Average marks:", average_marks(students49))
print("Students above 75:", above_75)
print("Sorted students:", sorted_students49)

# Q50. Employee records - filter, increase salary, sort
employees50 = [("Amit", "HR", 45000), ("Riya", "IT", 60000), ("Sam", "Sales", 30000)]
above_50000_50 = list(filter(lambda e: e[2] > 50000, employees50))
increased_salaries = list(map(lambda e: (e[0], e[1], e[2] * 1.1), employees50))
sorted_employees50 = sorted(employees50, key=lambda e: e[2])
print("Employees earning above 50000:", above_50000_50)
print("Salaries after increase:", increased_salaries)
print("Sorted by salary:", sorted_employees50)

# Q51. Products - total value, filter, sort by total value
products51 = [("Shirt", 800, 2), ("Shoes", 2000, 1), ("Cap", 150, 3)]
total_value51 = list(map(lambda p: (p[0], p[1] * p[2]), products51))
above_1000 = list(filter(lambda p: p[1] > 1000, total_value51))
sorted_products51 = sorted(total_value51, key=lambda p: p[1])
print("Total value of each product:", total_value51)
print("Products costing more than 1000:", above_1000)
print("Sorted by total value:", sorted_products51)

# Q52. Words - length, filter, sort by length
words52 = ["cat", "elephant", "dog", "giraffe", "ant"]
word_lengths52 = list(map(lambda w: (w, len(w)), words52))
long_words52 = list(filter(lambda w: len(w) > 5, words52))
sorted_words52 = sorted(words52, key=lambda w: len(w))
print("Word lengths:", word_lengths52)
print("Words with more than five characters:", long_words52)
print("Sorted by length:", sorted_words52)
