"""
HackerRank Python - 20 Questions with Solutions
------------------------------------------------
"""


# ---------------------------------------------------------------
# Q1. Say "Hello, World!" With Python
# Print "Hello, World!" to stdout.
# ---------------------------------------------------------------
def q1_hello_world():
    print("Hello, World!")


# ---------------------------------------------------------------
# Q2. Python If-Else
# Given n:
#   - odd                       -> "Weird"
#   - even and in 2..5          -> "Not Weird"
#   - even and in 6..20         -> "Weird"
#   - even and greater than 20  -> "Not Weird"
# ---------------------------------------------------------------
def q2_if_else(n):
    if n % 2 == 1:
        return "Weird"
    if 2 <= n <= 5:
        return "Not Weird"
    if 6 <= n <= 20:
        return "Weird"
    return "Not Weird"


# ---------------------------------------------------------------
# Q3. Arithmetic Operators
# Given a and b, return their sum, difference and product.
# ---------------------------------------------------------------
def q3_arithmetic(a, b):
    return a + b, a - b, a * b


# ---------------------------------------------------------------
# Q4. Python: Division
# Return integer division (a // b) and float division (a / b).
# ---------------------------------------------------------------
def q4_division(a, b):
    return a // b, a / b


# ---------------------------------------------------------------
# Q5. Loops
# Given n, return the squares of all integers from 0 to n-1.
# ---------------------------------------------------------------
def q5_loops(n):
    return [i ** 2 for i in range(n)]


# ---------------------------------------------------------------
# Q6. Write a Function (Leap Year)
# A year is a leap year if divisible by 4, except century years
# which must be divisible by 400.
# ---------------------------------------------------------------
def q6_is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# ---------------------------------------------------------------
# Q7. Print Function
# Given n, print the numbers 1..n on one line with no spaces.
# ---------------------------------------------------------------
def q7_print_function(n):
    return "".join(str(i) for i in range(1, n + 1))


# ---------------------------------------------------------------
# Q8. List Comprehensions
# Given x, y, z, n: return all [i, j, k] with 0<=i<=x, 0<=j<=y,
# 0<=k<=z where i + j + k != n.
# ---------------------------------------------------------------
def q8_list_comprehension(x, y, z, n):
    return [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]


# ---------------------------------------------------------------
# Q9. Find the Runner-Up Score
# Given a list of scores, return the second-highest score.
# ---------------------------------------------------------------
def q9_runner_up(scores):
    return sorted(set(scores), reverse=True)[1]


# ---------------------------------------------------------------
# Q10. Nested Lists
# Given [name, score] pairs, return the names of students with the
# second-lowest grade, in alphabetical order.
# ---------------------------------------------------------------
def q10_nested_lists(students):
    second_lowest = sorted({score for _, score in students})[1]
    return sorted(name for name, score in students if score == second_lowest)


# ---------------------------------------------------------------
# Q11. Finding the Percentage
# Given a dict of student -> marks and a query name, return the
# average of their marks rounded to 2 decimal places.
# ---------------------------------------------------------------
def q11_percentage(marks, query_name):
    scores = marks[query_name]
    return f"{sum(scores) / len(scores):.2f}"


# ---------------------------------------------------------------
# Q12. Lists
# Process commands on a list: insert, print, remove, append,
# sort, pop, reverse. Return the printed states.
# ---------------------------------------------------------------
def q12_lists(commands):
    result, output = [], []
    for cmd in commands:
        parts = cmd.split()
        name, args = parts[0], list(map(int, parts[1:]))
        if name == "print":
            output.append(list(result))
        else:
            getattr(result, name)(*args)
    return output


# ---------------------------------------------------------------
# Q13. Tuples
# Given a tuple of integers, return hash(tuple).
# ---------------------------------------------------------------
def q13_tuples(values):
    return hash(tuple(values))


# ---------------------------------------------------------------
# Q14. sWAP cASE
# Swap the case of every letter in a string.
# ---------------------------------------------------------------
def q14_swap_case(s):
    return s.swapcase()


# ---------------------------------------------------------------
# Q15. String Split and Join
# Split a string on spaces and join it back with hyphens.
# ---------------------------------------------------------------
def q15_split_and_join(line):
    return "-".join(line.split(" "))


# ---------------------------------------------------------------
# Q16. What's Your Name?
# Given first and last name, return the greeting.
# ---------------------------------------------------------------
def q16_whats_your_name(first, last):
    return f"Hello {first} {last}! You just delved into python."


# ---------------------------------------------------------------
# Q17. Mutations
# Strings are immutable. Replace the character at index
# `position` with `character`.
# ---------------------------------------------------------------
def q17_mutate_string(s, position, character):
    return s[:position] + character + s[position + 1:]


# ---------------------------------------------------------------
# Q18. Find a String
# Count how many times `sub` occurs in `s`, including overlaps.
# ---------------------------------------------------------------
def q18_count_substring(s, sub):
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            count += 1
    return count


# ---------------------------------------------------------------
# Q19. String Validators
# For a string, report whether it has any alphanumeric, alphabetical,
# digit, lowercase and uppercase characters.
# ---------------------------------------------------------------
def q19_string_validators(s):
    return [
        any(c.isalnum() for c in s),
        any(c.isalpha() for c in s),
        any(c.isdigit() for c in s),
        any(c.islower() for c in s),
        any(c.isupper() for c in s),
    ]


# ---------------------------------------------------------------
# Q20. Introduction to Sets
# Given a list of plant heights, return the average of the
# distinct heights.
# ---------------------------------------------------------------
def q20_average(heights):
    distinct = set(heights)
    return round(sum(distinct) / len(distinct), 3)


# ---------------------------------------------------------------
# Demo runner
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("Q1 :", end=" ")
    q1_hello_world()
    print("Q2 :", q2_if_else(3), q2_if_else(24), q2_if_else(18))
    print("Q3 :", q3_arithmetic(3, 2))
    print("Q4 :", q4_division(4, 3))
    print("Q5 :", q5_loops(5))
    print("Q6 :", q6_is_leap(1990), q6_is_leap(2000), q6_is_leap(1900))
    print("Q7 :", q7_print_function(5))
    print("Q8 :", q8_list_comprehension(1, 1, 1, 2))
    print("Q9 :", q9_runner_up([2, 3, 6, 6, 5]))
    print("Q10:", q10_nested_lists([["Harry", 37.21], ["Berry", 37.21],
                                    ["Tina", 37.2], ["Akriti", 41],
                                    ["Harsh", 39]]))
    print("Q11:", q11_percentage({"Krishna": [67, 68, 69],
                                   "Arjun": [70, 98, 63],
                                   "Malika": [52, 56, 60]}, "Malika"))
    print("Q12:", q12_lists(["insert 0 5", "insert 1 10", "insert 0 6",
                              "print", "remove 6", "append 9", "append 1",
                              "sort", "print", "pop", "reverse", "print"]))
    print("Q13:", q13_tuples([1, 2]))
    print("Q14:", q14_swap_case("HackerRank.com presents Pythonist 2."))
    print("Q15:", q15_split_and_join("this is a string"))
    print("Q16:", q16_whats_your_name("Ross", "Taylor"))
    print("Q17:", q17_mutate_string("abracadabra", 5, "k"))
    print("Q18:", q18_count_substring("ABCDCDC", "CDC"))
    print("Q19:", q19_string_validators("qA2"))
    print("Q20:", q20_average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]))
