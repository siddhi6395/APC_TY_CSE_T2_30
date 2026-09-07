"""
STRING PROGRAMS IN PYTHON
==========================
A collection of simple Python programs solving common string
problem statements. Each function is self-contained and easy
to read. Run this file directly to see a demo of every program.
"""


# 1. String Length (without using len())
def string_length(s):
    count = 0
    for ch in s:
        count += 1
    return count


# 2. Character Count (vowels, consonants, digits, spaces, special chars)
def character_count(s):
    vowels = consonants = digits = spaces = special = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            special += 1
    return {
        "vowels": vowels,
        "consonants": consonants,
        "digits": digits,
        "spaces": spaces,
        "special": special,
    }


# 3. Reverse a String (without built-in reverse)
def reverse_string(s):
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    return reversed_str


# 4. Palindrome Check
def is_palindrome(s):
    return s == reverse_string(s)


# 5. Uppercase and Lowercase Count
def upper_lower_count(s):
    upper = lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower


# 6. Replace Characters
def replace_char(s, old_char, new_char):
    result = ""
    for ch in s:
        if ch == old_char:
            result += new_char
        else:
            result += ch
    return result


# 7. Remove Spaces
def remove_spaces(s):
    result = ""
    for ch in s:
        if ch != " ":
            result += ch
    return result


# 8. Frequency of a Character
def char_frequency_single(s, char):
    count = 0
    for ch in s:
        if ch == char:
            count += 1
    return count


# 9. First and Last Character
def first_last_char(s):
    if len(s) == 0:
        return None, None
    return s[0], s[-1]


# 10. ASCII Values
def ascii_values(s):
    return [(ch, ord(ch)) for ch in s]


# 11. Word Count
def word_count(sentence):
    words = sentence.split()
    return len(words)


# 12. Longest Word
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# 13. Shortest Word
def shortest_word(sentence):
    words = sentence.split()
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest


# 14. Title Case
def title_case(sentence):
    words = sentence.split()
    result = []
    for word in words:
        result.append(word[0].upper() + word[1:].lower())
    return " ".join(result)


# 15. Duplicate Characters
def duplicate_characters(s):
    seen = {}
    for ch in s:
        if ch != " ":
            seen[ch] = seen.get(ch, 0) + 1
    return [ch for ch, count in seen.items() if count > 1]


# 16. Character Frequency (every character)
def character_frequency_all(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# 17. Anagram Check
def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


# 18. Remove Duplicate Characters (keep order)
def remove_duplicate_chars(s):
    seen = set()
    result = ""
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch
    return result


# 19. Substring Search
def substring_search(main_string, sub_string):
    return sub_string in main_string


# 20. Count Occurrences of a Word
def count_word_occurrences(sentence, word):
    words = sentence.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count


# 21. Password Validator
def validate_password(password):
    if len(password) < 8:
        return False
    has_upper = has_lower = has_digit = has_special = False
    special_chars = "!@#$%^&*()-_+=<>?/{}[]~"
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True
    return has_upper and has_lower and has_digit and has_special


# 22. Run-Length Encoding
def run_length_encoding(s):
    if len(s) == 0:
        return ""
    result = ""
    count = 1
    prev = s[0]
    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            result += prev + str(count)
            prev = ch
            count = 1
    result += prev + str(count)
    return result


# 23. String Compression (return original if compression doesn't help)
def string_compression(s):
    compressed = run_length_encoding(s)
    if len(compressed) < len(s):
        return compressed
    return s


# 24. Most Frequent Character
def most_frequent_char(s):
    freq = character_frequency_all(s)
    return max(freq, key=freq.get)


# 25. Second Most Frequent Character
def second_most_frequent_char(s):
    freq = character_frequency_all(s)
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_chars) < 2:
        return None
    return sorted_chars[1][0]


# 26. Caesar Cipher
def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# 27. Email Validator
def validate_email(email):
    if email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if len(local) == 0 or len(domain) == 0:
        return False
    if "." not in domain:
        return False
    domain_parts = domain.split(".")
    if any(len(part) == 0 for part in domain_parts):
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True


# 28. Word Frequency Dictionary
def word_frequency(paragraph):
    words = paragraph.lower().split()
    freq = {}
    for word in words:
        clean_word = "".join(ch for ch in word if ch.isalnum())
        if clean_word:
            freq[clean_word] = freq.get(clean_word, 0) + 1
    return freq


# 29. Sentence Reversal (reverse order of words)
def reverse_sentence(sentence):
    words = sentence.split()
    return " ".join(words[::-1])


# 30. String Rotation Check
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)


# ----------------------------------------------------------------
# DEMO: Run this file directly to see every program in action
# ----------------------------------------------------------------
if __name__ == "__main__":
    print("1. String Length:", string_length("hello"))
    print("2. Character Count:", character_count("Hello World 123!"))
    print("3. Reverse String:", reverse_string("hello"))
    print("4. Palindrome Check:", is_palindrome("madam"))
    print("5. Upper/Lower Count:", upper_lower_count("Hello World"))
    print("6. Replace Characters:", replace_char("banana", "a", "o"))
    print("7. Remove Spaces:", remove_spaces("h e l l o"))
    print("8. Frequency of Character:", char_frequency_single("banana", "a"))
    print("9. First and Last Character:", first_last_char("hello"))
    print("10. ASCII Values:", ascii_values("abc"))
    print("11. Word Count:", word_count("Python is easy to learn"))
    print("12. Longest Word:", longest_word("Python is easy to learn"))
    print("13. Shortest Word:", shortest_word("Python is easy to learn"))
    print("14. Title Case:", title_case("python is easy"))
    print("15. Duplicate Characters:", duplicate_characters("programming"))
    print("16. Character Frequency:", character_frequency_all("hello"))
    print("17. Anagram Check:", is_anagram("listen", "silent"))
    print("18. Remove Duplicate Characters:", remove_duplicate_chars("programming"))
    print("19. Substring Search:", substring_search("hello world", "world"))
    print("20. Count Word Occurrences:", count_word_occurrences("the cat sat on the mat", "the"))
    print("21. Password Validator:", validate_password("Passw0rd!"))
    print("22. Run-Length Encoding:", run_length_encoding("aaabbccccd"))
    print("23. String Compression:", string_compression("aaabbccccd"))
    print("24. Most Frequent Character:", most_frequent_char("programming"))
    print("25. Second Most Frequent Character:", second_most_frequent_char("programming"))
    print("26. Caesar Cipher Encrypt:", caesar_encrypt("hello", 3))
    print("26. Caesar Cipher Decrypt:", caesar_decrypt(caesar_encrypt("hello", 3), 3))
    print("27. Email Validator:", validate_email("test@example.com"))
    print("28. Word Frequency Dictionary:", word_frequency("the cat sat on the mat the cat ran"))
    print("29. Sentence Reversal:", reverse_sentence("Python is easy"))
    print("30. String Rotation Check:", is_rotation("ABCD", "CDAB"))
