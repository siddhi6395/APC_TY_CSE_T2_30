import numpy as np

# Q1: 1D array of 10 integers - display array, size, dtype, ndim
a = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
print("Q1")
print("Array:", a)
print("Size:", a.size)
print("Data type:", a.dtype)
print("Dimensions:", a.ndim)

# Q2: Two arrays of 5 integers - arithmetic operations
x = np.array([10, 20, 30, 40, 50])
y = np.array([1, 2, 3, 4, 5])
print("\nQ2")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)

# Q3: Array of 10 numbers - max, min, sum, average
b = np.array([12, 45, 7, 23, 56, 89, 34, 21, 67, 90])
print("\nQ3")
print("Maximum:", b.max())
print("Minimum:", b.min())
print("Sum:", b.sum())
print("Average:", b.mean())

# Q4: Numbers 1 to 20 - Boolean indexing for even and odd
c = np.arange(1, 21)
print("\nQ4")
print("Even numbers:", c[c % 2 == 0])
print("Odd numbers:", c[c % 2 != 0])

# Q5: Numbers 1 to 12 - reshape into 2x6, 3x4, 4x3
d = np.arange(1, 13)
print("\nQ5")
print("2 x 6:\n", d.reshape(2, 6))
print("3 x 4:\n", d.reshape(3, 4))
print("4 x 3:\n", d.reshape(4, 3))

# Q6: Two 3x3 matrices - addition
m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("\nQ6")
print("Matrix addition:\n", m1 + m2)

# Q7: Two compatible matrices - matrix multiplication (2x3 and 3x2)
p = np.array([[1, 2, 3], [4, 5, 6]])
q = np.array([[7, 8], [9, 10], [11, 12]])
print("\nQ7")
print("Matrix multiplication:\n", np.dot(p, q))

# Q8: 3x4 matrix - transpose
t = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("\nQ8")
print("Original:\n", t)
print("Transpose:\n", t.T)

# Q9: 4x4 array - first row, last column, diagonal, 2nd and 3rd rows
e = np.arange(1, 17).reshape(4, 4)
print("\nQ9")
print("Array:\n", e)
print("First row:", e[0])
print("Last column:", e[:, -1])
print("Diagonal:", np.diag(e))
print("Second and third rows:\n", e[1:3])

# Q10: 4x4 matrix - sum of each row and each column
f = np.arange(1, 17).reshape(4, 4)
print("\nQ10")
print("Row sums:", f.sum(axis=1))
print("Column sums:", f.sum(axis=0))

# Q11: Numbers 1 to 20 - slicing
g = np.arange(1, 21)
print("\nQ11")
print("First 5:", g[:5])
print("Last 5:", g[-5:])
print("Alternate elements:", g[::2])
print("Reverse order:", g[::-1])

# Q12: 10 integers - replace elements greater than 50 with 0
h = np.array([10, 60, 25, 80, 45, 51, 30, 99, 50, 70])
print("\nQ12")
print("Original:", h)
h[h > 50] = 0
print("Modified:", h)

# Q13: Unsorted array - ascending and descending order
u = np.array([34, 7, 23, 90, 1, 56, 12])
print("\nQ13")
print("Original:", u)
print("Ascending:", np.sort(u))
print("Descending:", np.sort(u)[::-1])

# Q14: Array with duplicates - unique elements
dup = np.array([1, 2, 2, 3, 4, 4, 4, 5, 6, 6])
print("\nQ14")
print("Original:", dup)
print("Unique:", np.unique(dup))

# Q15: Two arrays - concatenate horizontally and vertically
r1 = np.array([[1, 2], [3, 4]])
r2 = np.array([[5, 6], [7, 8]])
print("\nQ15")
print("Horizontal:\n", np.hstack((r1, r2)))
print("Vertical:\n", np.vstack((r1, r2)))

# Q16: Marks of 10 students - statistics
marks = np.array([78, 85, 92, 67, 74, 88, 95, 60, 81, 70])
print("\nQ16")
print("Highest:", marks.max())
print("Lowest:", marks.min())
print("Average:", marks.mean())
print("Median:", np.median(marks))
print("Standard deviation:", marks.std())

# Q17: Marks of 20 students - class average and students above average
marks20 = np.array([55, 68, 72, 90, 45, 83, 77, 61, 94, 50,
                    66, 88, 73, 59, 81, 97, 42, 70, 64, 85])
avg = marks20.mean()
print("\nQ17")
print("Class average:", avg)
print("Marks above average:", marks20[marks20 > avg])

# Q18: 3D array (2,3,4) with numbers 1 to 24 - ndim, shape, size
a3 = np.arange(1, 25).reshape(2, 3, 4)
print("\nQ18")
print("Array:\n", a3)
print("Dimensions:", a3.ndim)
print("Shape:", a3.shape)
print("Size:", a3.size)

# Q19: 3D array (2,3,4) - access specific elements
b3 = np.arange(1, 25).reshape(2, 3, 4)
print("\nQ19")
print("First element:", b3[0, 0, 0])
print("Last element:", b3[-1, -1, -1])
print("Element at [0,1,2]:", b3[0, 1, 2])
print("Element at [1,2,3]:", b3[1, 2, 3])

# Q20: (2,3,4) array - various sums
c3 = np.arange(1, 25).reshape(2, 3, 4)
print("\nQ20")
print("Sum of all elements:", c3.sum())
print("Sum of each layer:", c3.sum(axis=(1, 2)))
print("Sum along rows:\n", c3.sum(axis=2))
print("Sum along columns:\n", c3.sum(axis=1))

# Q21: 3D random integers 1-100 - replace values > 50 with 0
r3 = np.random.randint(1, 101, size=(2, 3, 4))
print("\nQ21")
print("Original:\n", r3)
r3[r3 > 50] = 0
print("Modified:\n", r3)

# Q22: Random 3D array (3,4,5) - mean, median, std, var, min, max
s3 = np.random.rand(3, 4, 5)
print("\nQ22")
print("Mean:", np.mean(s3))
print("Median:", np.median(s3))
print("Standard deviation:", np.std(s3))
print("Variance:", np.var(s3))
print("Minimum:", np.min(s3))
print("Maximum:", np.max(s3))

# Q23: 3D array (2,3,4) 1 to 24 - original and flattened
f3 = np.arange(1, 25).reshape(2, 3, 4)
print("\nQ23")
print("Original:\n", f3)
print("Flattened:", f3.flatten())

# Q24: 3D array 1 to 27 - flatten and sum, average, max, min
g3 = np.arange(1, 28).reshape(3, 3, 3)
flat = g3.flatten()
print("\nQ24")
print("Flattened:", flat)
print("Sum:", flat.sum())
print("Average:", flat.mean())
print("Maximum:", flat.max())
print("Minimum:", flat.min())

# Q25: Random 3D array (3,4,5) - flatten, then filter elements
h3 = np.random.randint(1, 101, size=(3, 4, 5))
flat2 = h3.flatten()
print("\nQ25")
print("Flattened:", flat2)
print("Greater than 50:", flat2[flat2 > 50])
print("Even numbers:", flat2[flat2 % 2 == 0])
print("Less than average:", flat2[flat2 < flat2.mean()])
