# Q1. Tuple of five integers
t1 = (10, 20, 30, 40, 50)
print("Tuple:", t1)

# Q2. Tuple of five city names
cities = ("Delhi", "Mumbai", "Chennai", "Kolkata", "Pune")
print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])

# Q3. Tuple of student names, total using len()
students = ("Amit", "Riya", "Sam", "Neha", "Karan")
print("Total students:", len(students))

# Q4. Tuple of colors, check if a color exists
colors = ("red", "green", "blue", "yellow")
check_color = "green"
print("Is", check_color, "present:", check_color in colors)

# Q5. Tuple of fruits, display each using a loop
fruits = ("apple", "banana", "mango", "grapes")
print("Fruits:")
for fruit in fruits:
    print(fruit)

# Q6. Tuple with repeated numbers, count a particular number
nums = (1, 2, 3, 2, 4, 2, 5)
count_num = 2
print("Count of", count_num, ":", nums.count(count_num))

# Q7. Tuple of employee IDs, find index of a given ID
emp_ids = (101, 102, 103, 104, 105)
find_id = 103
print("Index of", find_id, ":", emp_ids.index(find_id))

# Q8. Concatenate two tuples of numbers
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print("Concatenated tuple:", c)

# Q9. Repeat a tuple of three elements four times
t2 = (1, 2, 3)
t2_repeat = t2 * 4
print("Repeated tuple:", t2_repeat)

# Q10. Tuple of 10 numbers, slicing operations
nums10 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("First five:", nums10[:5])
print("Last five:", nums10[-5:])
print("Middle four:", nums10[3:7])
print("Alternate elements:", nums10[::2])
print("Reverse tuple:", nums10[::-1])

# Q11. Convert tuple to list, add new element
t3 = (1, 2, 3)
list3 = list(t3)
list3.append(4)
print("Updated list:", list3)

# Q12. Accept five numbers from user, store in list, convert to tuple
list4 = []
for i in range(5):
    n = int(input("Enter number: "))
    list4.append(n)
tuple4 = tuple(list4)
print("Tuple from list:", tuple4)

# Q13. Modify a tuple by converting to list then back to tuple
t5 = (10, 20, 30)
list5 = list(t5)
list5[1] = 99
t5 = tuple(list5)
print("Modified tuple:", t5)

# Q14. Create a tuple and delete it completely
t6 = (1, 2, 3)
print("Before delete:", t6)
del t6

# Q15. Nested tuple with student details
student_records = (("Amit", 20, "CS"), ("Riya", 21, "IT"), ("Sam", 22, "ME"))
print("Student records:")
for record in student_records:
    print(record)

# Q16. Ten numbers in a tuple, calculate sum
nums_sum = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
total_sum = sum(nums_sum)
print("Sum:", total_sum)

# Q17. Largest and smallest without max()/min()
nums17 = (23, 45, 12, 67, 34)
largest = nums17[0]
smallest = nums17[0]
for n in nums17:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("Largest:", largest)
print("Smallest:", smallest)

# Q18. Average of elements
nums18 = (10, 20, 30, 40)
average = sum(nums18) / len(nums18)
print("Average:", average)

# Q19. 15 integers, count even and odd
nums19 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
even_count = 0
odd_count = 0
for n in nums19:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

# Q20. Accept a number and check if it exists in tuple
nums20 = (5, 10, 15, 20, 25)
check_num = int(input("Enter number to check: "))
print("Exists:", check_num in nums20)

# Q21. Student details tuple
student = ("101", "Amit", "Computer Science", 85)
print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])

# Q22. Employee ID, name, salary
employee = ("E001", "Riya", 45000)
print("Employee ID:", employee[0])
print("Name:", employee[1])
print("Salary:", employee[2])

# Q23. Item prices tuple
prices = (100, 250, 75, 300, 150)
total_bill = sum(prices)
avg_price = total_bill / len(prices)
highest_price = max(prices)
lowest_price = min(prices)
print("Total bill:", total_bill)
print("Average price:", avg_price)
print("Highest priced item:", highest_price)
print("Lowest priced item:", lowest_price)

# Q24. Temperatures of seven days
temps = (30, 32, 28, 35, 31, 29, 33)
print("Maximum temperature:", max(temps))
print("Minimum temperature:", min(temps))
print("Average temperature:", sum(temps) / len(temps))

# Q25. Runs scored in 10 matches
runs = (45, 67, 23, 89, 12, 56, 78, 34, 90, 21)
print("Total runs:", sum(runs))
print("Highest score:", max(runs))
print("Lowest score:", min(runs))
print("Average score:", sum(runs) / len(runs))

# Q26. Common elements between two tuples
set_a = (1, 2, 3, 4, 5)
set_b = (4, 5, 6, 7, 8)
common = tuple(set(set_a) & set(set_b))
print("Common elements:", common)

# Q27. Merge two tuples, remove duplicates
merge_a = (1, 2, 3, 4)
merge_b = (3, 4, 5, 6)
merged = tuple(set(merge_a + merge_b))
print("Merged without duplicates:", merged)

# Q28. Count frequency of each element
nums28 = (1, 2, 2, 3, 3, 3, 4)
print("Frequency count:")
for item in set(nums28):
    print(item, ":", nums28.count(item))

# Q29. Sorted tuple ascending and descending
nums29 = (34, 12, 67, 23, 45)
ascending = tuple(sorted(nums29))
descending = tuple(sorted(nums29, reverse=True))
print("Ascending:", ascending)
print("Descending:", descending)

# Q30. Patient records tuple
patients = (
    ("P001", "Amit", 30, "A+"),
    ("P002", "Riya", 25, "B+"),
    ("P003", "Sam", 40, "A+"),
    ("P004", "Neha", 35, "O+"),
)

print("All records:")
for patient in patients:
    print(patient)

search_id = "P002"
for patient in patients:
    if patient[0] == search_id:
        print("Patient found:", patient)

print("Total patients:", len(patients))

search_blood_group = "A+"
print("Patients with blood group", search_blood_group, ":")
for patient in patients:
    if patient[3] == search_blood_group:
        print(patient)
