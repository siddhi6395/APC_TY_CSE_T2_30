import array

# Q1. append()
arr1 = array.array('i', [1, 2, 3])
arr1.append(4)
print("After append:", arr1)

# Q2. buffer_info()
arr2 = array.array('i', [1, 2, 3])
print("Buffer info:", arr2.buffer_info())

# Q3. byteswap()
arr3 = array.array('i', [1, 2, 3])
arr3.byteswap()
print("After byteswap:", arr3)

# Q4. count()
arr4 = array.array('i', [1, 2, 2, 3, 2])
print("Count of 2:", arr4.count(2))

# Q5. extend()
arr5 = array.array('i', [1, 2, 3])
arr5.extend([4, 5, 6])
print("After extend:", arr5)

# Q6. frombytes()
arr6 = array.array('i', [1, 2, 3])
byte_data = arr6.tobytes()
arr6_new = array.array('i')
arr6_new.frombytes(byte_data)
print("After frombytes:", arr6_new)

# Q7. fromfile()
arr7_source = array.array('i', [10, 20, 30])
with open("array_data.bin", "wb") as f:
    arr7_source.tofile(f)

arr7 = array.array('i')
with open("array_data.bin", "rb") as f:
    arr7.fromfile(f, 3)
print("After fromfile:", arr7)

# Q8. fromlist()
arr8 = array.array('i')
arr8.fromlist([1, 2, 3, 4])
print("After fromlist:", arr8)

# Q9. fromunicode()
arr9 = array.array('u')
arr9.fromunicode("hello")
print("After fromunicode:", arr9)

# Q10. index()
arr10 = array.array('i', [10, 20, 30, 40])
print("Index of 30:", arr10.index(30))

# Q11. insert()
arr11 = array.array('i', [1, 2, 4])
arr11.insert(2, 3)
print("After insert:", arr11)

# Q12. pop()
arr12 = array.array('i', [1, 2, 3, 4])
popped_value = arr12.pop()
print("Popped value:", popped_value)
print("After pop:", arr12)

# Q13. remove()
arr13 = array.array('i', [1, 2, 3, 4])
arr13.remove(3)
print("After remove:", arr13)

# Q14. reverse()
arr14 = array.array('i', [1, 2, 3, 4])
arr14.reverse()
print("After reverse:", arr14)

# Q15. tobytes()
arr15 = array.array('i', [1, 2, 3])
print("As bytes:", arr15.tobytes())

# Q16. tofile()
arr16 = array.array('i', [5, 10, 15])
with open("array_output.bin", "wb") as f:
    arr16.tofile(f)
print("Array written to file")

# Q17. tolist()
arr17 = array.array('i', [1, 2, 3])
print("As list:", arr17.tolist())

# Q18. tounicode()
arr18 = array.array('u', "hello")
print("As unicode string:", arr18.tounicode())
