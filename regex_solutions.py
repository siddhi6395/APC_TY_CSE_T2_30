import re

# Q1: Extract all digits from a string
text = "My phone is 98765 and room is 42"
print("Q1:", re.findall(r"\d", text))

# Q2: Words beginning with A or a
sentence = "An apple and Amit are at Alpha school"
print("Q2:", re.findall(r"\b[Aa]\w*", sentence))

# Q3: Count vowels
s = "Regular Expressions are useful"
vowels = re.findall(r"[aeiouAEIOU]", s)
print("Q3: Vowel count =", len(vowels))

# Q4: Extract uppercase letters
s = "Hello World From Python"
print("Q4:", re.findall(r"[A-Z]", s))

# Q5: Identify spaces, tabs and newlines
s = "Hello World\tTab here\nNew line"
print("Q5: Spaces =", len(re.findall(r" ", s)),
      ", Tabs =", len(re.findall(r"\t", s)),
      ", Newlines =", len(re.findall(r"\n", s)))

# Q6: Replace multiple spaces with a single space
s = "This   has    too     many   spaces"
print("Q6:", re.sub(r" +", " ", s))

# Q7: Words with exactly five characters
s = "Hello world this is a Python test apple"
print("Q7:", re.findall(r"\b\w{5}\b", s))

# Q8: Words ending with s
s = "cats dogs run books and pens"
print("Q8:", re.findall(r"\b\w*s\b", s))

# Q9: Remove special characters (keep letters, digits, spaces)
s = "Hello, World! #2026 @Python$"
print("Q9:", re.sub(r"[^A-Za-z0-9 ]", "", s))

# Q10: Count words in a sentence
s = "Regular expressions are very powerful"
print("Q10: Word count =", len(re.findall(r"\w+", s)))

# Q11: Validate 10-digit Indian mobile number (starts with 6-9)
mobile = "9876543210"
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Q11: Valid mobile number")
else:
    print("Q11: Invalid mobile number")

# Q12: Validate email format
email = "student123@gmail.com"
if re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.-]+", email):
    print("Q12: Valid email")
else:
    print("Q12: Invalid email")

# Q13: Extract dates in DD-MM-YYYY format
para = "Exam on 15-03-2026 and result on 30-04-2026."
print("Q13:", re.findall(r"\b\d{2}-\d{2}-\d{4}\b", para))

# Q14: Web addresses starting with http:// or https://
para = "Visit https://example.com or http://test.org/page for more"
print("Q14:", re.findall(r"https?://\S+", para))

# Q15: Extract hashtags
post = "Loving #Python and #Regex today #coding"
print("Q15:", re.findall(r"#\w+", post))

# Q16: Password check (8+ chars, upper, lower, digit, special)
pwd = "Passw0rd@123"
if (len(pwd) >= 8 and re.search(r"[A-Z]", pwd) and re.search(r"[a-z]", pwd)
        and re.search(r"\d", pwd) and re.search(r"[^A-Za-z0-9]", pwd)):
    print("Q16: Strong password")
else:
    print("Q16: Weak password")

# Q17: Consecutive repeated words (ignore case)
s = "This is is a test Test of the the code"
print("Q17:", re.findall(r"\b(\w+)\s+\1\b", s, re.IGNORECASE))

# Q18: Six-digit Indian PIN codes
para = "Pune 411001, Mumbai 400001 and phone 12345"
print("Q18:", re.findall(r"\b\d{6}\b", para))

# Q19: Vehicle registration format like MH12AB1234
vehicle = "MH12AB1234"
if re.fullmatch(r"[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}", vehicle):
    print("Q19: Valid registration number")
else:
    print("Q19: Invalid registration number")

# Q20: Extract file extensions
s = "files: report.pdf, photo.jpg, notes.txt, data.csv"
print("Q20:", re.findall(r"\.(\w+)\b", s))

# Q21: Remove HTML tags, extra whitespace and unwanted punctuation
html = "<p>Hello,   <b>World</b>!!!  This   is   <i>HTML</i>...</p>"
clean = re.sub(r"<[^>]+>", "", html)        # remove tags
clean = re.sub(r"[^\w\s]", "", clean)       # remove punctuation
clean = re.sub(r"\s+", " ", clean).strip()  # fix whitespace
print("Q21:", clean)

# Q22: Invoice numbers, dates and amounts
invoice = "Invoice No: INV-2026-001 Date: 21-10-2026 Total: Rs. 5,250.50"
print("Q22 Invoice:", re.findall(r"INV-\d{4}-\d+", invoice))
print("Q22 Date:", re.findall(r"\d{2}-\d{2}-\d{4}", invoice))
print("Q22 Amount:", re.findall(r"Rs\.?\s?[\d,]+(?:\.\d+)?", invoice))

# Q23: Single-line comments in Python code
code = '''x = 5  # set x
print("a # not comment")
# full line comment
y = 10'''
print("Q23:", re.findall(r"#.*", code))
# Note: regex alone is not reliable here. It also matches the '#' inside the
# string "a # not comment", because a regex cannot tell whether the '#' is
# inside a string literal. It also cannot handle multiline strings/docstrings
# or escaped quotes correctly. A proper parser (tokenize module) is needed.

# Q24: Product code pattern ABC-1234-XY
code = "ABC-1234-XY"
if re.fullmatch(r"[A-Z]{3}-\d{4}-[A-Z]{2}", code):
    print("Q24: Valid product code")
else:
    print("Q24: Invalid product code")

# Q25: Student names, roll numbers and marks
para = "Name: Asha Roll: 101 Marks: 85; Name: Ravi Roll: 102 Marks: 72"
for name, roll, marks in re.findall(r"Name:\s*(\w+)\s+Roll:\s*(\d+)\s+Marks:\s*(\d+)", para):
    print("Q25: Name =", name, ", Roll =", roll, ", Marks =", marks)

# Q26: DOIs, years, emails and URLs from references
refs = """Smith, J. (2021). Deep learning. doi:10.1000/xyz123. Contact: smith@uni.edu
Rao, P. (2019). Data mining. https://doi.org/10.1016/j.abc.2019.05.001 email: rao@lab.org
See also https://example.com/paper (2023)."""
print("Q26 DOI:", re.findall(r"10\.\d{4,9}/[^\s]+?(?=[.\s]*(?:\s|$))", refs))
print("Q26 Years:", re.findall(r"\((\d{4})\)", refs))
print("Q26 Emails:", re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", refs))
print("Q26 URLs:", re.findall(r"https?://[^\s)]+", refs))
