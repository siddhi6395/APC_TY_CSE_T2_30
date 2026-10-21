import pandas as pd

# Q1: Student marks DataFrame - total, average, students with average above 75
d1 = {"Student_ID": [1, 2, 3, 4, 5],
      "Student_Name": ["Asha", "Ravi", "Meena", "Karan", "Sita"],
      "Python": [85, 60, 92, 70, 78],
      "DBMS": [80, 65, 88, 72, 74],
      "Maths": [90, 55, 95, 68, 80]}
df1 = pd.DataFrame(d1)
print("Q1")
print(df1)
df1["Total"] = df1["Python"] + df1["DBMS"] + df1["Maths"]
print("Total marks:\n", df1[["Student_Name", "Total"]])
df1["Average"] = df1["Total"] / 3
print("Average marks:\n", df1[["Student_Name", "Average"]])
print("Students with average above 75:\n", df1[df1["Average"] > 75])

# Q2: Employee DataFrame
d2 = {"Employee_ID": [101, 102, 103, 104, 105],
      "Employee_Name": ["Amit", "Neha", "Rahul", "Priya", "Vijay"],
      "Department": ["CSE", "HR", "CSE", "Finance", "IT"],
      "Salary": [60000, 45000, 75000, 40000, 52000],
      "Experience": [5, 3, 8, 2, 6]}
df2 = pd.DataFrame(d2)
print("\nQ2")
print("Salary greater than 50000:\n", df2[df2["Salary"] > 50000])
print("Average salary:", df2["Salary"].mean())
print("Highest salary:", df2["Salary"].max())
print("Employee with highest experience:\n", df2[df2["Experience"] == df2["Experience"].max()])

# Q3: Product DataFrame - total amount and highest sales
d3 = {"Product_ID": [1, 2, 3, 4, 5],
      "Product_Name": ["Pen", "Book", "Bag", "Bottle", "Lamp"],
      "Category": ["Stationery", "Stationery", "Accessories", "Accessories", "Electronics"],
      "Price": [10, 150, 800, 250, 600],
      "Quantity": [100, 40, 15, 30, 20]}
df3 = pd.DataFrame(d3)
df3["Total_Amount"] = df3["Price"] * df3["Quantity"]
print("\nQ3")
print(df3)
print("Product with highest total sales:\n", df3[df3["Total_Amount"] == df3["Total_Amount"].max()])

# Q4: Patient DataFrame
d4 = {"Patient_ID": [1, 2, 3, 4, 5],
      "Patient_Name": ["Ramesh", "Sunita", "Mohan", "Lata", "Suresh"],
      "Age": [65, 45, 70, 30, 62],
      "Disease": ["Diabetes", "Fever", "Heart", "Flu", "Asthma"],
      "Medical_Charges": [55000, 3000, 120000, 2000, 48000]}
df4 = pd.DataFrame(d4)
print("\nQ4")
print("Patients above 60 years:\n", df4[df4["Age"] > 60])
print("Average medical charge:", df4["Medical_Charges"].mean())
print("Maximum medical charge:", df4["Medical_Charges"].max())
print("Charges greater than 50000:\n", df4[df4["Medical_Charges"] > 50000])

# Q5: Orders DataFrame - final amount
d5 = {"Order_ID": [1, 2, 3, 4, 5],
      "Customer": ["Anil", "Bina", "Chitra", "Dev", "Esha"],
      "Product": ["Phone", "Pen", "Laptop", "Book", "Watch"],
      "Quantity": [1, 10, 1, 5, 2],
      "Price": [8000, 20, 45000, 300, 2500],
      "Discount": [500, 0, 3000, 50, 200]}
df5 = pd.DataFrame(d5)
df5["Final_Amount"] = df5["Quantity"] * df5["Price"] - df5["Discount"]
print("\nQ5")
print("All orders:\n", df5)
print("Orders above 5000:\n", df5[df5["Final_Amount"] > 5000])
print("Highest-value order:\n", df5[df5["Final_Amount"] == df5["Final_Amount"].max()])
print("Average order value:", df5["Final_Amount"].mean())

# Q6: Attendance DataFrame
d6 = {"Student_ID": [1, 2, 3, 4, 5],
      "Name": ["Asha", "Ravi", "Meena", "Karan", "Sita"],
      "Department": ["CSE", "IT", "CSE", "ECE", "IT"],
      "Total_Classes": [100, 100, 100, 100, 100],
      "Classes_Attended": [90, 70, 80, 60, 95]}
df6 = pd.DataFrame(d6)
df6["Attendance_Percentage"] = df6["Classes_Attended"] / df6["Total_Classes"] * 100
print("\nQ6")
print(df6)
print("Attendance below 75%:\n", df6[df6["Attendance_Percentage"] < 75])

# Q7: Retail shop sales DataFrame
d7 = {"Product_ID": [1, 2, 3, 4, 5],
      "Product_Name": ["Rice", "Oil", "Sugar", "Tea", "Soap"],
      "Category": ["Grocery", "Grocery", "Grocery", "Beverage", "Personal Care"],
      "Price": [60, 150, 45, 300, 40],
      "Quantity": [200, 100, 150, 30, 500]}
df7 = pd.DataFrame(d7)
print("\nQ7")
print(df7)
df7["Total_Sales"] = df7["Price"] * df7["Quantity"]
print("With Total_Sales:\n", df7)
print("Products with sales greater than 10000:\n", df7[df7["Total_Sales"] > 10000])
print("Product with maximum sales:\n", df7[df7["Total_Sales"] == df7["Total_Sales"].max()])
print("Average sales:", df7["Total_Sales"].mean())

# Q7 (second part): Series of student marks
s1 = pd.Series({"Asha": 85, "Ravi": 60, "Meena": 92, "Karan": 70, "Sita": 78})
print("\nQ7 (Series - student marks)")
print("Series:\n", s1)
print("Marks of Meena:", s1["Meena"])
print("Maximum:", s1.max(), " Minimum:", s1.min())
print("Average:", s1.mean())
print("Students scoring more than 75:\n", s1[s1 > 75])

# Q8: Series of employee salaries
s2 = pd.Series({"Amit": 60000, "Neha": 45000, "Rahul": 75000, "Priya": 40000, "Vijay": 52000})
print("\nQ8")
print("Series:\n", s2)
print("Highest salary:", s2.max())
print("Lowest salary:", s2.min())
print("Average salary:", s2.mean())
print("Earning more than 50000:\n", s2[s2 > 50000])

# Q9: Series of product prices
s3 = pd.Series({"Pen": 10, "Book": 150, "Bag": 800, "Bottle": 1200, "Laptop": 45000})
print("\nQ9")
print("Products and prices:\n", s3)
s3 = s3 * 1.10
print("After 10% increase:\n", s3)
print("Most expensive product:", s3.idxmax())
print("Products costing more than 1000:\n", s3[s3 > 1000])

# Q10: Series of patient ages with patient IDs as index
s4 = pd.Series({101: 65, 102: 45, 103: 70, 104: 30, 105: 62})
print("\nQ10")
print("Average age:", s4.mean())
print("Oldest patient ID:", s4.idxmax(), "Age:", s4.max())
print("Youngest patient ID:", s4.idxmin(), "Age:", s4.min())
print("Patients above 60:\n", s4[s4 > 60])

# Q11: Series of attendance percentages
s5 = pd.Series({"Asha": 90, "Ravi": 70, "Meena": 95, "Karan": 60, "Sita": 92})
print("\nQ11")
print("Average attendance:", s5.mean())
print("Attendance below 75%:\n", s5[s5 < 75])
print("Attendance above 90%:\n", s5[s5 > 90])
print("Highest attendance:", s5.max())

# ---- Sample CSV files (created so Q12 to Q15 can run; replace with your own files) ----
pd.DataFrame({"Student_ID": range(1, 9),
              "Name": ["Asha", "Ravi", "Meena", "Karan", "Sita", "Tara", "Uday", "Veena"],
              "Department": ["CSE", "IT", "CSE", "ECE", "IT", "CSE", "ECE", "IT"],
              "Python": [85, 60, 92, 70, 78, 88, 55, 74],
              "DBMS": [80, 65, 88, 72, 74, 90, 60, 70],
              "Maths": [90, 55, 95, 68, 80, 85, 50, 72]}).to_csv("students.csv", index=False)
pd.DataFrame({"Employee_ID": range(101, 109),
              "Name": ["Amit", "Neha", "Rahul", "Priya", "Vijay", "Zoya", "Om", "Lina"],
              "Department": ["CSE", "HR", "CSE", "Finance", "IT", "CSE", "HR", "IT"],
              "Experience": [5, 3, 8, 2, 6, 4, 7, 1],
              "Salary": [60000, 45000, 75000, 40000, 52000, 58000, 48000, 35000]}).to_csv("employees.csv", index=False)
pd.DataFrame({"Patient_ID": range(1, 9),
              "Name": ["Ramesh", "Sunita", "Mohan", "Lata", "Suresh", "Geeta", "Hari", "Indu"],
              "Age": [65, 45, 70, 30, 62, 55, 68, 25],
              "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
              "Disease": ["Diabetes", "Fever", "Heart", "Flu", "Diabetes", "Fever", "Heart", "Flu"],
              "Medical_Expense": [55000, 3000, 120000, 2000, 48000, 4000, 90000, 1500]}).to_csv("patients.csv", index=False)
pd.DataFrame({"Date": ["2026-05-01", "2026-05-01", "2026-05-02", "2026-05-02", "2026-05-03", "2026-05-03"],
              "City": ["Delhi", "Pune", "Delhi", "Pune", "Delhi", "Pune"],
              "Temperature": [38, 33, 40, 31, 36, 34],
              "Humidity": [30, 55, 28, 60, 35, 50],
              "Rainfall": [0, 2, 0, 5, 0, 1]}).to_csv("weather.csv", index=False)

# Q12: students.csv
st = pd.read_csv("students.csv")
print("\nQ12")
print("First 5 records:\n", st.head())
print("Last 5 records:\n", st.tail())
st["Total"] = st["Python"] + st["DBMS"] + st["Maths"]
st["Average"] = st["Total"] / 3
print("Total and average:\n", st[["Name", "Total", "Average"]])
print("Average above 75:\n", st[st["Average"] > 75])
print("Highest average:\n", st[st["Average"] == st["Average"].max()])
print("Average marks per subject:\n", st[["Python", "DBMS", "Maths"]].mean())

# Q13: employees.csv
em = pd.read_csv("employees.csv")
print("\nQ13")
print("CSE employees:\n", em[em["Department"] == "CSE"])
print("Average salary:", em["Salary"].mean())
print("Highest salary:", em["Salary"].max(), " Lowest salary:", em["Salary"].min())
print("Salary greater than 50000:\n", em[em["Salary"] > 50000])
print("Department-wise average salary:\n", em.groupby("Department")["Salary"].mean())

# Q14: patients.csv
pa = pd.read_csv("patients.csv")
print("\nQ14")
print("Patients above 60:\n", pa[pa["Age"] > 60])
print("Average medical expense:", pa["Medical_Expense"].mean())
print("Highest medical expense:\n", pa[pa["Medical_Expense"] == pa["Medical_Expense"].max()])
print("Patients per disease:\n", pa["Disease"].value_counts())
print("Expense above 50000:\n", pa[pa["Medical_Expense"] > 50000])

# Q15: weather.csv
we = pd.read_csv("weather.csv")
print("\nQ15")
print("Maximum temperature:", we["Temperature"].max())
print("Minimum temperature:", we["Temperature"].min())
print("Average temperature:", we["Temperature"].mean())
print("Temperature above 35:\n", we[we["Temperature"] > 35])
print("City-wise average temperature:\n", we.groupby("City")["Temperature"].mean())
