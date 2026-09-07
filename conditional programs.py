#[1]
print("Problem 1")
marks = int ( input("Enter your Percentage marks :"))
if marks<=100 and marks>=90:
    print("Execellent Performance")
elif marks<=89 and marks >=80:
    print(" Very Good Performance")
elif marks<=79 and marks >=70:
    print("Good Performance")
elif marks<=69 and marks>=60:
    print("Poor Performance")
else:
    print("Fail...!")
    
#[2]
print("Problem 2")
x = int(input("Enter vlue of x :"))
if x % 2 == 0:
    print(x," is a Even Number")
else:
    print(x, " is a Odd Number")

# [3]
print("Problem 3")
y = int(input("Enter vlue of y :"))
if y >= 0:
    print(y," is a Positive Number")
elif y < 0:
    print(y, " is a Negative Number")    
else:
    print("Invalid Input.")

# [4]
print("Problem 4")
a = int(input("Enter vlue of a :"))
if a >= 0:
    print("It is a zero ")
elif a < 0:
    print(a, " is a Non-zero ")    
else:
    print("Invalid Input.")
    
# [5]
print("Problem 5")
year = int(input("Enter Year :"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(" This is Leap Year")
else:
        print(" This is not a Leap Year")


# [6]
print("Problem 6")
x = int(input("Enter vlue of x :"))
y = int(input("Enter vlue of y :"))
if x > y :
    print(x," is grater than ",y)
else:
    print(y," is greater than ",x)

# [7]
print("Problem 7")
p = int(input("Enter vlue of p :"))
q = int(input("Enter vlue of q :"))
r = int(input("Enter vlue of r :"))
# greatest
if p > q :
    if p > r:
        print(p," is greatest")
    else:
        print(r," is greatest ")
else:
    if q > r :  
      print(q," is greatest")
    else:
      print(r," is greatest")
#smallest
if p < q:
    if p < r:
        print(p, "is smallest")
    else:
        print(r, "is smallest")
else:
    if q < r:
        print(q, "is smallest")
    else:
        print(r, "is smallest")      

# [8]
print("Problem 8")
char = input("Enter an alphabet :")
if char == 'a' or char == 'e'or char == 'i' or char == 'o' or char == 'u' :
    print(char, " is vowel.")
else:
    print(char, "is consonent")
