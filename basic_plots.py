import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 7, 4, 9, 6, 12, 8, 15, 11, 14]
subjects = ["Python", "DBMS", "Maths", "AI", "Networks"]
marks = [85, 72, 90, 65, 78]
boys = [80, 70, 85, 60, 75]
girls = [85, 75, 90, 68, 80]

# 1: Scatter plot
plt.scatter(x, y, color="red", marker="o")
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 2: Bar plot (simple)
plt.bar(subjects, marks, color="green")
plt.title("Bar Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 3: Pie chart
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()

# 4: Bar chart types
# 4a: Vertical bar chart
plt.bar(subjects, marks, color="skyblue")
plt.title("Vertical Bar Chart")
plt.show()

# 4b: Horizontal bar chart
plt.barh(subjects, marks, color="orange")
plt.title("Horizontal Bar Chart")
plt.show()

# 4c: Grouped (clustered) bar chart
pos = np.arange(len(subjects))
plt.bar(pos - 0.2, boys, width=0.4, label="Boys")
plt.bar(pos + 0.2, girls, width=0.4, label="Girls")
plt.xticks(pos, subjects)
plt.title("Grouped Bar Chart")
plt.legend()
plt.show()

# 4d: Stacked bar chart
plt.bar(subjects, boys, label="Boys")
plt.bar(subjects, girls, bottom=boys, label="Girls")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()

# 5: Line plot
plt.plot(x, y, color="blue", marker="o", linestyle="-")
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
