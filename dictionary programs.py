# Q1. Student details dictionary, display all key-value pairs
student1 = {"roll_number": 101, "name": "Amit", "department": "CS", "marks": 85}
print("Student details:")
for key, value in student1.items():
    print(key, ":", value)

# Q2. Employee info dictionary, display value for a specified key
employee2 = {"id": "E001", "name": "Riya", "department": "HR", "salary": 45000}
search_key = "salary"
print("Value for", search_key, ":", employee2[search_key])

# Q3. Dictionary of five products and prices, add a new product
products3 = {"pen": 10, "book": 50, "bag": 500, "pencil": 5, "eraser": 3}
products3["marker"] = 20
print("Updated products:", products3)

# Q4. Dictionary of student marks, update marks of a specified student
marks4 = {"Amit": 85, "Riya": 90, "Sam": 78}
update_student = "Riya"
marks4[update_student] = 95
print("Updated marks:", marks4)

# Q5. Dictionary of cities and populations, remove a specified city
cities5 = {"Delhi": 30000000, "Mumbai": 20000000, "Chennai": 10000000}
remove_city = "Chennai"
del cities5[remove_city]
print("Updated cities:", cities5)

# Q6. Dictionary of employee IDs and names, check if ID exists
employees6 = {"E001": "Amit", "E002": "Riya", "E003": "Sam"}
search_id = input("Enter employee ID: ")
print("Employee ID exists:", search_id in employees6)

# Q7. Student records dictionary, total number of key-value pairs
student7 = {"roll_number": 101, "name": "Amit", "department": "CS", "marks": 85}
print("Total key-value pairs:", len(student7))

# Q8. Display all keys, values, key-value pairs
dict8 = {"a": 1, "b": 2, "c": 3}
print("All keys:", list(dict8.keys()))
print("All values:", list(dict8.values()))
print("All key-value pairs:", list(dict8.items()))

# Q9. Programming languages and creators, display using loop
languages9 = {"Python": "Guido van Rossum", "Java": "James Gosling", "C++": "Bjarne Stroustrup"}
print("Languages and creators:")
for key, value in languages9.items():
    print(key, "-", value)

# Q10. Accept five student names and marks, store in dictionary
students10 = {}
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students10[name] = marks
print("Students dictionary:", students10)

# Q11. Student with highest marks
marks11 = {"Amit": 85, "Riya": 90, "Sam": 78}
topper = max(marks11, key=marks11.get)
print("Student with highest marks:", topper)

# Q12. Student with lowest marks
marks12 = {"Amit": 85, "Riya": 90, "Sam": 78}
lowest_student = min(marks12, key=marks12.get)
print("Student with lowest marks:", lowest_student)

# Q13. Average marks of all students
marks13 = {"Amit": 85, "Riya": 90, "Sam": 78}
avg_marks13 = sum(marks13.values()) / len(marks13)
print("Average marks:", avg_marks13)

# Q14. Character frequency dictionary from a string
text14 = input("Enter a string: ")
char_freq = {}
for ch in text14:
    if ch in char_freq:
        char_freq[ch] += 1
    else:
        char_freq[ch] = 1
print("Character frequency:", char_freq)

# Q15. Word frequency dictionary from a sentence
sentence15 = input("Enter a sentence: ")
words15 = sentence15.split()
word_freq = {}
for word in words15:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Word frequency:", word_freq)

# Q16. Merge two dictionaries into one
dict_a16 = {"a": 1, "b": 2}
dict_b16 = {"c": 3, "d": 4}
merged16 = {**dict_a16, **dict_b16}
print("Merged dictionary:", merged16)

# Q17. Common keys between two dictionaries
dict_a17 = {"a": 1, "b": 2, "c": 3}
dict_b17 = {"b": 20, "c": 30, "d": 40}
common_keys = dict_a17.keys() & dict_b17.keys()
print("Common keys:", common_keys)

# Q18. Common values between two dictionaries
dict_a18 = {"a": 1, "b": 2, "c": 3}
dict_b18 = {"x": 2, "y": 3, "z": 4}
common_values = set(dict_a18.values()) & set(dict_b18.values())
print("Common values:", common_values)

# Q19. Remove duplicate values while retaining keys
dict19 = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
seen_values = set()
unique_dict19 = {}
for key, value in dict19.items():
    if value not in seen_values:
        unique_dict19[key] = value
        seen_values.add(value)
print("Dictionary without duplicate values:", unique_dict19)

# Q20. Display dictionary elements in ascending order of keys
dict20 = {"banana": 2, "apple": 1, "cherry": 3}
sorted_dict20 = dict(sorted(dict20.items()))
print("Sorted by keys:", sorted_dict20)

# Q21. Numbers 1 to 10 as keys, squares as values
squares21 = {}
for n in range(1, 11):
    squares21[n] = n * n
print("Squares dictionary:", squares21)

# Q22. Numbers 1 to 20 as keys and squares as values, only even numbers
squares22 = {}
for n in range(1, 21):
    if n % 2 == 0:
        squares22[n] = n * n
print("Even squares dictionary:", squares22)

# Q23. Unique number and frequency from a list
nums23 = [1, 2, 2, 3, 3, 3, 4, 5, 5]
freq23 = {}
for n in nums23:
    if n in freq23:
        freq23[n] += 1
    else:
        freq23[n] = 1
print("Number frequency:", freq23)

# Q24. Integers 1 to 10 and their cubes
cubes24 = {}
for n in range(1, 11):
    cubes24[n] = n ** 3
print("Cubes dictionary:", cubes24)

# Q25. Student names and marks - add, update, delete, search, display, highest, average
students25 = {"Amit": 85, "Riya": 90, "Sam": 78}
students25["Neha"] = 88
students25["Sam"] = 82
del students25["Amit"]
print("Is Riya present:", "Riya" in students25)
print("All students:", students25)
print("Highest marks student:", max(students25, key=students25.get))
print("Average marks:", sum(students25.values()) / len(students25))

# Q26. Employee names and salaries - highest, lowest, average, above 50000
employees26 = {"Amit": 45000, "Riya": 60000, "Sam": 30000, "Neha": 75000}
print("Highest salary:", max(employees26.values()))
print("Lowest salary:", min(employees26.values()))
print("Average salary:", sum(employees26.values()) / len(employees26))
above_50000 = []
for name, salary in employees26.items():
    if salary > 50000:
        above_50000.append(name)
print("Employees earning above 50000:", above_50000)

# Q27. Product names and quantities - add, update, delete, search, low stock
products27 = {"pen": 50, "book": 5, "bag": 20, "pencil": 8}
products27["marker"] = 15
products27["book"] = 12
del products27["bag"]
print("Is pencil available:", "pencil" in products27)
low_stock = []
for name, qty in products27.items():
    if qty < 10:
        low_stock.append(name)
print("Products with quantity below 10:", low_stock)

# Q28. Names and phone numbers - add, search, update, delete, display all
contacts28 = {"Amit": "9876543210", "Riya": "9123456780"}
contacts28["Sam"] = "9988776655"
print("Is Riya a contact:", "Riya" in contacts28)
contacts28["Amit"] = "9000000000"
del contacts28["Sam"]
print("All contacts:", contacts28)

# Q29. Book IDs and names - add, search, remove, display all, count total
books29 = {"B001": "Python Basics", "B002": "Data Science"}
books29["B003"] = "Machine Learning"
print("Is B002 available:", "B002" in books29)
del books29["B001"]
print("All books:", books29)
print("Total books:", len(books29))

# Q30. Group students by department
student_department = {"Amit": "CS", "Riya": "IT", "Sam": "CS", "Neha": "ME"}
grouped30 = {}
for name, dept in student_department.items():
    if dept in grouped30:
        grouped30[dept].append(name)
    else:
        grouped30[dept] = [name]
print("Grouped by department:", grouped30)

# Q31. Dictionary of word length to list of words of that length
words31 = ["cat", "dog", "apple", "bat", "banana", "ant"]
length_dict = {}
for word in words31:
    length = len(word)
    if length in length_dict:
        length_dict[length].append(word)
    else:
        length_dict[length] = [word]
print("Words grouped by length:", length_dict)

# Q32. Two numbers whose sum equals target using a dictionary
nums32 = [2, 7, 11, 15]
target32 = 9
seen32 = {}
for i, n in enumerate(nums32):
    diff = target32 - n
    if diff in seen32:
        print("Pair found:", diff, "and", n)
        break
    seen32[n] = i

# Q33. First character that occurs only once
text33 = "swiss"
char_count33 = {}
for ch in text33:
    if ch in char_count33:
        char_count33[ch] += 1
    else:
        char_count33[ch] = 1
first_unique = None
for ch in text33:
    if char_count33[ch] == 1:
        first_unique = ch
        break
print("First character occurring once:", first_unique)

# Q34. First character that occurs more than once
text34 = "swiss"
char_count34 = {}
first_repeated = None
for ch in text34:
    if ch in char_count34:
        first_repeated = ch
        break
    char_count34[ch] = 1
print("First character occurring more than once:", first_repeated)

# Q35. Word length to count of words having that length
paragraph35 = input("Enter a paragraph: ")
words35 = paragraph35.split()
length_count = {}
for word in words35:
    length = len(word)
    if length in length_count:
        length_count[length] += 1
    else:
        length_count[length] = 1
print("Word length count:", length_count)
