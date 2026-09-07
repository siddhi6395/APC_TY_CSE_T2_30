# Q1. List of five fruits
fruits = ["apple", "banana", "mango", "grapes", "orange"]
print("Fruits list:", fruits)

# Q2. List of five integers
nums2 = [10, 20, 30, 40, 50]
print("First element:", nums2[0])
print("Last element:", nums2[-1])
print("Third element:", nums2[2])

# Q3. List of colors, replace third color
colors = ["red", "green", "blue", "yellow", "black"]
colors[2] = "pink"
print("Updated colors:", colors)

# Q4. List of numbers, add elements at end, beginning, position
nums4 = [1, 2, 3, 4, 5]
nums4.append(6)
nums4.insert(0, 0)
nums4.insert(3, 99)
print("Updated list:", nums4)

# Q5. List of student names, remove first, last, specific student
students5 = ["Amit", "Riya", "Sam", "Neha", "Karan"]
students5.pop(0)
students5.pop(-1)
students5.remove("Sam")
print("Remaining students:", students5)

# Q6. Largest and smallest without max()/min()
nums6 = [23, 45, 12, 67, 34]
largest = nums6[0]
smallest = nums6[0]
for n in nums6:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("Largest:", largest)
print("Smallest:", smallest)

# Q7. Accept 10 numbers, calculate sum and average
list7 = []
for i in range(10):
    n = int(input("Enter number: "))
    list7.append(n)
total7 = sum(list7)
avg7 = total7 / len(list7)
print("Sum:", total7)
print("Average:", avg7)

# Q8. 15 integers, count even and odd
nums8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even_count = 0
odd_count = 0
for n in nums8:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

# Q9. List of cities, check if entered city exists
cities9 = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Pune"]
search_city = input("Enter city name: ")
print("City exists:", search_city in cities9)

# Q10. Reverse a list without using reverse()
nums10 = [1, 2, 3, 4, 5]
reversed_list = []
for n in nums10:
    reversed_list.insert(0, n)
print("Reversed list:", reversed_list)

# Q11. List of 10 numbers, slicing operations
nums11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("First five:", nums11[:5])
print("Last five:", nums11[-5:])
print("Middle four:", nums11[3:7])
print("Alternate elements:", nums11[::2])
print("Reverse list:", nums11[::-1])

# Q12. Elements at even index positions
nums12 = [10, 20, 30, 40, 50, 60, 70]
print("Elements at even index:", nums12[::2])

# Q13. Accept 10 numbers, sort ascending and descending
list13 = []
for i in range(10):
    n = int(input("Enter number: "))
    list13.append(n)
ascending = sorted(list13)
descending = sorted(list13, reverse=True)
print("Ascending order:", ascending)
print("Descending order:", descending)

# Q14. List with duplicates, display unique elements
list14 = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique14 = list(set(list14))
print("Unique elements:", unique14)

# Q15. Second largest element
nums15 = [23, 45, 12, 67, 34]
sorted15 = sorted(nums15, reverse=True)
print("Second largest:", sorted15[1])

# Q16. Nested list - student name, roll number, marks
student_records = [
    ["Amit", 101, 85],
    ["Riya", 102, 90],
    ["Sam", 103, 78],
]
print("Student details:")
for record in student_records:
    print(record)

# Q17. Two 3x3 matrices, matrix addition
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result_matrix.append(row)
print("Matrix addition result:", result_matrix)

# Q18. Shopping cart
cart = []
cart.append("Milk")
cart.append("Bread")
cart.append("Eggs")
cart.remove("Bread")
print("Is Milk in cart:", "Milk" in cart)
print("Shopping cart:", cart)
print("Total items:", len(cart))

# Q19. Students present in class
attendance = ["Amit", "Riya", "Sam", "Neha"]
print("Total students:", len(attendance))
print("Is Riya present:", "Riya" in attendance)
attendance.append("Karan")
attendance.remove("Sam")
print("Updated attendance:", attendance)

# Q20. List of books
books = ["Python Basics", "Data Science", "Machine Learning"]
books.append("Deep Learning")
print("Is Data Science available:", "Data Science" in books)
books.remove("Machine Learning")
print("All books:", books)
print("Total books:", len(books))

# Q21. Accept two lists and merge them
list_a21 = [1, 2, 3]
list_b21 = [4, 5, 6]
merged21 = list_a21 + list_b21
print("Merged list:", merged21)

# Q22. Common elements between two lists
list_a22 = [1, 2, 3, 4, 5]
list_b22 = [4, 5, 6, 7, 8]
common22 = list(set(list_a22) & set(list_b22))
print("Common elements:", common22)

# Q23. Frequency count of each element
list23 = [1, 2, 2, 3, 3, 3, 4]
print("Frequency count:")
for item in set(list23):
    print(item, ":", list23.count(item))

# Q24. Rotate list left and right by one
list24 = [1, 2, 3, 4, 5]
left_rotate = list24[1:] + list24[:1]
right_rotate = list24[-1:] + list24[:-1]
print("Left rotated:", left_rotate)
print("Right rotated:", right_rotate)

# Q25. Remove duplicates preserving order
list25 = [1, 2, 2, 3, 4, 3, 5, 1]
unique25 = []
for item in list25:
    if item not in unique25:
        unique25.append(item)
print("Unique list:", unique25)

# Q26. Marks of 20 students
marks = [56, 78, 90, 45, 67, 88, 34, 76, 92, 60, 55, 70, 85, 40, 65, 95, 50, 72, 80, 62]
highest_marks = max(marks)
lowest_marks = min(marks)
avg_marks = sum(marks) / len(marks)
above_avg = 0
below_avg = 0
for m in marks:
    if m > avg_marks:
        above_avg += 1
    elif m < avg_marks:
        below_avg += 1
print("Highest marks:", highest_marks)
print("Lowest marks:", lowest_marks)
print("Average marks:", avg_marks)
print("Students above average:", above_avg)
print("Students below average:", below_avg)

# Q27. Salaries of employees
salaries = [25000, 55000, 40000, 60000, 28000, 45000, 70000, 32000]
highest_salary = max(salaries)
lowest_salary = min(salaries)
avg_salary = sum(salaries) / len(salaries)
above_50000 = 0
below_30000 = 0
for s in salaries:
    if s > 50000:
        above_50000 += 1
    if s < 30000:
        below_30000 += 1
print("Highest salary:", highest_salary)
print("Lowest salary:", lowest_salary)
print("Average salary:", avg_salary)
print("Employees earning above 50000:", above_50000)
print("Employees earning below 30000:", below_30000)

# Q28. Batsman scores in 10 matches
scores = [45, 67, 102, 89, 12, 56, 78, 34, 105, 21]
highest_score = max(scores)
lowest_score = min(scores)
total_runs = sum(scores)
avg_runs = total_runs / len(scores)
centuries = 0
half_centuries = 0
for s in scores:
    if s >= 100:
        centuries += 1
    elif 50 <= s < 100:
        half_centuries += 1
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Total runs:", total_runs)
print("Average runs:", avg_runs)
print("Number of centuries:", centuries)
print("Number of half-centuries:", half_centuries)

# Q29. Temperature of 30 days
temps = [30, 32, 28, 35, 31, 29, 33, 27, 36, 34, 30, 31, 28, 29, 33,
         32, 35, 27, 26, 34, 30, 31, 29, 28, 33, 32, 35, 27, 36, 34]
hottest_day = max(temps)
coldest_day = min(temps)
avg_temp = sum(temps) / len(temps)
above_avg_days = 0
below_avg_days = 0
for t in temps:
    if t > avg_temp:
        above_avg_days += 1
    elif t < avg_temp:
        below_avg_days += 1
print("Hottest day:", hottest_day)
print("Coldest day:", coldest_day)
print("Average temperature:", avg_temp)
print("Days above average:", above_avg_days)
print("Days below average:", below_avg_days)

# Q30. Patient names and ages
patient_names = ["Amit", "Riya", "Sam"]
patient_ages = [30, 25, 40]
patient_names.append("Neha")
patient_ages.append(35)
del patient_names[1]
del patient_ages[1]
print("Is Sam a patient:", "Sam" in patient_names)
print("Patient names:", patient_names)
print("Patient ages:", patient_ages)
print("Total patients:", len(patient_names))
