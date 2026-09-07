# Q1
s = {10, 20, 30, 40, 50}
for x in s:
    print(x)
print()

# Q2
lst = [1, 2, 2, 3, 4, 4, 5, 1]
s = set(lst)
print(lst)
print(s)
print()

# Q3
s = {"apple", "banana", "mango", "grapes", "orange"}
s.add("kiwi")
s.update(["papaya"])
print(s)
print()

# Q4
s = {5, 10, 15, 20, 25}
s.discard(15)
print(s)
print()

# Q5
s = {"Amit", "Priya", "Ravi", "Sneha"}
name = "Ravi"
if name in s:
    print(f"{name} is present in the set.")
else:
    print(f"{name} is not present in the set.")
print()

# Q6
s = {"Delhi", "Mumbai", "Chennai", "Kolkata"}
print(len(s))
print()

# Q7
s = {"Python", "Java", "C++", "JavaScript"}
for x in s:
    print(x)
print()

# Q8
lst = [4, 5, 5, 6, 7, 7, 8]
s = set(lst)
print(lst)
print(s)
print()

# Q9
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print()

# Q10
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)
print()

# Q11
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b)
print(b - a)
print()

# Q12
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a ^ b)
print()

# Q13
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))
print()

# Q14
a = {1, 2, 3, 4}
b = {1, 2}
print(a.issuperset(b))
print()

# Q15
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))
print()

# Q16
a = {1, 2, 3}
b = {3, 2, 1}
print(a == b)
print()

# Q17
a = {"Math", "Physics", "Chemistry"}
b = {"Physics", "Biology", "Math"}
print(a & b)
print()

# Q18
text = "the quick brown fox jumps over the lazy dog the fox runs"
s = set(text.split())
print(s)
print()

# Q19
a = {"Amit", "Priya", "Ravi", "Sneha"}
b = {"Ravi", "Sneha", "Kiran", "Meera"}
print(a & b)
print(a - b)
print(b - a)
print(a | b)
print()

# Q20
a = {"Amit", "Priya", "Ravi"}
b = {"Ravi", "Sneha", "Kiran"}
print(a & b)
print(a ^ b)
print()

# Q21
a = {"Python", "SQL", "Excel", "Java"}
b = {"Java", "AWS", "Excel", "Docker"}
print(a & b)
print(a - b)
print(b - a)
print(a | b)
print()

# Q22
a = {"Python Basics", "Data Science", "AI Guide", "Web Dev"}
b = {"AI Guide", "Web Dev", "Machine Learning"}
print(b & a)
print()

# Q23
a = {101, 102, 103, 104}
b = {103, 104, 105, 106}
print(a | b)
print(a & b)
print(a - b)
print(b - a)
print()

# Q24
a = {"Laptop", "Mouse", "Keyboard", "Monitor"}
b = {"Mouse", "Keyboard", "Webcam", "Speaker"}
print(a & b)
print()

# Q25
a = {"Aman", "Neha", "Ravi", "Sonal"}
b = {"Ravi", "Sonal", "Kabir", "Divya"}
print(a & b)
print(a - b)
print(b - a)
print(a | b)
