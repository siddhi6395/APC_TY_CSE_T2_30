# Q1
with open("student.txt", "w") as f:
    f.write("Name: Amit\n")
    f.write("Roll No: 101\n")
    f.write("Branch: CSE\n")
    f.write("Semester: 5\n")

# Q2
with open("student.txt", "r") as f:
    print(f.read())

# Q3
with open("student.txt", "a") as f:
    f.write("Email: amit@example.com\n")

# Q4
with open("student.txt", "r") as f:
    for line in f:
        print(line.strip())

# Q5
with open("student.txt", "r") as f:
    lines = f.readlines()
print("Total lines:", len(lines))

# Q6
with open("student.txt", "r") as f:
    text = f.read()
print("Total words:", len(text.split()))

# Q7
with open("student.txt", "r") as f:
    text = f.read()
print("Total characters:", len(text))

# Q8
with open("student.txt", "r") as f:
    lines = f.readlines()
for line in reversed(lines):
    print(line.strip())

# Q9
vowels = 0
consonants = 0
with open("student.txt", "r") as f:
    text = f.read().lower()
for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels, "Consonants:", consonants)

# Q10
alpha = digit = space = special = 0
with open("student.txt", "r") as f:
    text = f.read()
for ch in text:
    if ch.isalpha():
        alpha += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
    else:
        special += 1
print("Alphabets:", alpha, "Digits:", digit, "Spaces:", space, "Special:", special)

# Q11
with open("student.txt", "r") as f:
    words = f.read().split()
longest = max(words, key=len) if words else ""
print("Longest word:", longest)

# Q12
freq = {}
with open("student.txt", "r") as f:
    words = f.read().split()
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

# Q13
search_word = input("Enter word to search: ")
occurrences = 0
line_numbers = []
with open("student.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        count = line.split().count(search_word)
        if count > 0:
            occurrences += count
            line_numbers.append(i)
print("Occurrences:", occurrences, "Lines:", line_numbers)

# Q14
old_word = "Amit"
new_word = "Rahul"
with open("student.txt", "r") as f:
    text = f.read()
text = text.replace(old_word, new_word)
with open("student.txt", "w") as f:
    f.write(text)

# Q15
with open(__file__, "r") as f:
    lines = f.readlines()
clean_lines = [line for line in lines if not line.strip().startswith("#")]
with open("no_comments.py", "w") as f:
    f.writelines(clean_lines)

# Q16
with open("student.txt", "r") as f:
    text = f.read()
with open("student_upper.txt", "w") as f:
    f.write(text.upper())

# Q17
with open("records.txt", "w") as f:
    f.write("RollNo,Name,Marks\n")
    f.write("101,Amit,85\n")
    f.write("102,Priya,92\n")
    f.write("103,Rahul,78\n")

def read_records(filename):
    records = []
    with open(filename, "r") as f:
        next(f)
        for line in f:
            roll, name, marks = line.strip().split(",")
            records.append((roll, name, int(marks)))
    return records

records = read_records("records.txt")
print("All records:", records)
topper = max(records, key=lambda r: r[2])
print("Highest marks:", topper)
avg_marks = sum(r[2] for r in records) / len(records)
print("Average marks:", avg_marks)
above_80 = [r for r in records if r[2] > 80]
print("Above 80:", above_80)

# Q18
with open("employees.txt", "w") as f:
    f.write("E1,Anil,IT,50000\n")
    f.write("E2,Sunita,HR,45000\n")
    f.write("E3,Rakesh,Finance,60000\n")

def read_employees():
    emps = []
    with open("employees.txt", "r") as f:
        for line in f:
            emp_id, name, dept, salary = line.strip().split(",")
            emps.append((emp_id, name, dept, float(salary)))
    return emps

def display_employees(emps):
    for e in emps:
        print(e)

def highest_paid(emps):
    return max(emps, key=lambda e: e[3])

def average_salary(emps):
    return sum(e[3] for e in emps) / len(emps)

def above_salary(emps, limit):
    return [e for e in emps if e[3] > limit]

emps = read_employees()
display_employees(emps)
print("Highest paid:", highest_paid(emps))
print("Average salary:", average_salary(emps))
print("Above 50000:", above_salary(emps, 50000))

# Q19
with open("attendance.txt", "w") as f:
    f.write("Amit,80,100\n")
    f.write("Priya,60,100\n")
    f.write("Rahul,90,100\n")

with open("attendance.txt", "r") as f:
    for line in f:
        name, present, total = line.strip().split(",")
        percentage = int(present) / int(total) * 100
        print(name, percentage, "%")
        if percentage < 75:
            print(name, "is below 75% attendance")

# Q20
with open("transactions.txt", "w") as f:
    f.write("deposit,1000\n")
    f.write("withdraw,300\n")
    f.write("deposit,500\n")
    f.write("withdraw,200\n")

total_deposit = 0
total_withdraw = 0
largest = 0
with open("transactions.txt", "r") as f:
    for line in f:
        kind, amount = line.strip().split(",")
        amount = float(amount)
        if kind == "deposit":
            total_deposit += amount
        else:
            total_withdraw += amount
        if amount > largest:
            largest = amount

balance = total_deposit - total_withdraw
print("Total deposits:", total_deposit)
print("Total withdrawals:", total_withdraw)
print("Final balance:", balance)
print("Largest transaction:", largest)

# Q21
def add_book(book_id, title, author):
    with open("books.txt", "a") as f:
        f.write(f"{book_id},{title},{author},available\n")

def search_book(book_id):
    with open("books.txt", "r") as f:
        for line in f:
            if line.startswith(book_id + ","):
                return line.strip()
    return None

def update_status(book_id, status):
    with open("books.txt", "r") as f:
        lines = f.readlines()
    with open("books.txt", "w") as f:
        for line in lines:
            parts = line.strip().split(",")
            if parts[0] == book_id:
                parts[3] = status
            f.write(",".join(parts) + "\n")

def issue_book(book_id):
    update_status(book_id, "issued")

def return_book(book_id):
    update_status(book_id, "available")

def display_available():
    with open("books.txt", "r") as f:
        for line in f:
            if line.strip().split(",")[3] == "available":
                print(line.strip())

add_book("B1", "Python Basics", "John")
add_book("B2", "Data Structures", "Smith")
print(search_book("B1"))
issue_book("B1")
display_available()
return_book("B1")

# Q22
with open("file1.txt", "w") as f:
    f.write("Hello from file1\n")
with open("file2.txt", "w") as f:
    f.write("Hello from file2\n")

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("file3.txt", "w") as f3:
    f3.write(f1.read())
    f3.write(f2.read())

# Q23
def compare_files(file_a, file_b):
    with open(file_a, "r") as fa, open(file_b, "r") as fb:
        lines_a = fa.readlines()
        lines_b = fb.readlines()
    if lines_a == lines_b:
        print("Files are identical")
        return
    for i, (la, lb) in enumerate(zip(lines_a, lines_b), start=1):
        if la != lb:
            print("Files differ at line", i)
            return
    print("Files differ in length")

compare_files("file1.txt", "file2.txt")

# ---------- Problems on module, Package and Directory ----------

# Q24
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Cannot divide by zero"

choice = input("Enter operation (add/sub/mul/div): ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
if choice == "add":
    print(add(x, y))
elif choice == "sub":
    print(sub(x, y))
elif choice == "mul":
    print(mul(x, y))
elif choice == "div":
    print(div(x, y))

# Q25
def total_marks(marks): return sum(marks)
def percentage(marks): return sum(marks) / len(marks)
def grade(pct):
    if pct >= 90: return "A"
    elif pct >= 75: return "B"
    elif pct >= 60: return "C"
    else: return "D"

marks = [85, 90, 78, 88, 92]
t = total_marks(marks)
p = percentage(marks)
g = grade(p)
print("Total:", t, "Percentage:", p, "Grade:", g)

# Q26
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

num = 28
print(is_prime(num), is_palindrome(num), is_armstrong(153), is_perfect(num))

# Q27
def count_vowels(s): return sum(1 for ch in s.lower() if ch in "aeiou")
def reverse_string(s): return s[::-1]
def is_str_palindrome(s): return s == s[::-1]
def count_words(s): return len(s.split())
def remove_spaces(s): return s.replace(" ", "")

text = "madam i am learning python"
print(count_vowels(text), reverse_string(text), is_str_palindrome("madam"), count_words(text), remove_spaces(text))

# Q28
def gross_salary(basic, allowances): return basic + allowances
def deductions(basic): return basic * 0.1
def net_salary(basic, allowances):
    gross = gross_salary(basic, allowances)
    return gross - deductions(basic)

print(net_salary(30000, 5000))

# Q29
def factorial(n): return 1 if n == 0 else n * factorial(n - 1)
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)
def sum_of_digits(n): return (n % 10) + sum_of_digits(n // 10) if n > 0 else 0
def to_binary(n): return "" if n == 0 else to_binary(n // 2) + str(n % 2)

print(factorial(5), fibonacci(6), sum_of_digits(123), to_binary(10) or "0")

# Q30 (mathutils package: basic.py, number.py, statistics.py combined here)
def basic_add(a, b): return a + b
def basic_sub(a, b): return a - b
def number_is_prime(n): return is_prime(n)
def number_is_armstrong(n): return is_armstrong(n)
def stats_mean(values): return sum(values) / len(values)
def stats_max(values): return max(values)
def stats_min(values): return min(values)

print(basic_add(2, 3), number_is_prime(7), stats_mean([1, 2, 3]))

# Q31 (student package: marks.py, grade.py, attendance.py combined here)
def marks_total(marks): return sum(marks)
def marks_percentage(marks): return sum(marks) / len(marks)
def grade_calc(pct): return grade(pct)
def attendance_eligible(present, total): return (present / total) * 100 >= 75

print(marks_total([80, 90]), attendance_eligible(80, 100))

# Q32 (banking package: account.py, transaction.py, loan.py combined here)
def account_create(name, balance): return {"name": name, "balance": balance}
def transaction_deposit(acc, amount): acc["balance"] += amount
def transaction_withdraw(acc, amount): acc["balance"] -= amount
def loan_calculate(principal, rate, years): return principal * (1 + rate * years)

acc = account_create("Amit", 1000)
transaction_deposit(acc, 500)
print(acc, loan_calculate(10000, 0.05, 2))

# Q33 (texttools package: cleaning.py, tokenization.py, frequency.py combined here)
import string
def cleaning_remove_punctuation(text): return text.translate(str.maketrans("", "", string.punctuation))
def tokenization_tokenize(text): return text.split()
def frequency_word_count(tokens):
    freq = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    return freq

sample = "Hello, world! Hello Python."
clean_text = cleaning_remove_punctuation(sample)
tokens = tokenization_tokenize(clean_text)
print(frequency_word_count(tokens))

# Q34 (college_project directory: student/details.py, student/marks.py, faculty/details.py)
def student_details(): return {"name": "Amit", "roll": 101}
def student_marks(): return {"total": 450}
def faculty_details(): return {"name": "Dr. Rao", "dept": "CSE"}

print(student_details(), student_marks(), faculty_details())

# Q35 (library app directory: books, members, transactions packages)
def books_list(): return ["Python Basics", "Data Structures"]
def members_list(): return ["Amit", "Priya"]
def transactions_issue(book, member): return f"{book} issued to {member}"

print(books_list(), members_list(), transactions_issue("Python Basics", "Amit"))

# Q36 (ecommerce directory: products, customers, orders, payments packages)
def products_list(): return ["Laptop", "Phone"]
def customers_list(): return ["Ravi", "Sneha"]
def orders_create(product, customer): return f"Order: {product} for {customer}"
def payments_process(amount): return f"Paid {amount}"

print(products_list(), customers_list(), orders_create("Laptop", "Ravi"), payments_process(50000))

# Q37 (hospital project directory: patient, doctor, billing, medical_records packages)
def patient_register(name): return {"name": name, "id": 1}
def doctor_assign(patient, doctor): return f"{doctor} assigned to {patient}"
def billing_generate(amount): return f"Bill amount: {amount}"
def medical_record_add(patient, diagnosis): return f"{patient}: {diagnosis}"

print(patient_register("Amit"), doctor_assign("Amit", "Dr. Rao"), billing_generate(2000), medical_record_add("Amit", "Fever"))
