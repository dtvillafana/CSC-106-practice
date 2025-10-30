# Problem 0
# Adding a new entry
# Update the dictionary of three countries and their capitals.
# Add two new country-capital pairs and print the updated dictionary.

capitals = {"France": "Paris", "Japan": "Tokyo", "USA": "Washington D.C."}
# your code here


# Problem 1
# Checking membership
# Given a dictionary of fruits and colors, ask the user for a fruit and print its color,
# or print "unknown fruit" if not found.

fruits = {"apple": "red", "banana": "yellow", "grape": "purple"}
# your code here


# Problem 2
# Dictionary Iteration
# Create a dictionary of students and grades, then print each student's name
# and grade on a new line using a for loop.

students = {"tom": "B", "amy": "A", "rob": "C"}
# your code here


# Problem 3
# Replacing simple branching
# Replace simple if/elif/else structures.
# Rewrite the below code to use a dictionary instead.

code = input("Enter letter grade, options: 'A', 'B', 'C', 'D', 'F'")

# Original code for reference:
# if code == "A":
#     grade = "Excellent"
# elif code == "B":
#     grade = "Good"
# elif code == "C":
#     grade = "Average"
# elif code == "D":
#     grade = "Poor"
# elif code == "F":
#     grade = "Fail"
# else:
#     grade = "Invalid"
# print(grade)

# your rewritten code here


# Problem 4
# Dictionaries for counting
# Use a dictionary to show character frequency.
# Count all the characters in a string.

string = "adskfljhsldnmbuqiosduixv"
# your code here

# Problem 5
# Create a function that takes a dictionary and a string, and returns a string with the words mapped.
# the input string should have each word replaced with the values of their corresponding key in the dictionary before it's returned

grug_map = {
    "utilize": "use",
    "commence": "begin",
    "termination": "ending",
    "miscreance": "immorality",
    "ascertain": "find out",
    "endeavor": "try",
    "ameliorate": "improve",
    "expedite": "speed up",
    "procure": "get",
    "demonstrate": "show",
    "inquire": "ask",
    "contemplate": "think about",
    "endeavour": "attempt",
    "assist": "help",
    "reside": "live",
    "inform": "tell",
    "commenced": "began",
    "necessitate": "require",
    "endeavoring": "trying",
    "facilitate": "make easier"
}

# your code here


# Problem 6
# observe how caches work by calling this function with 5,6,7, etc
# print the cache between calls
def factorial(n, cache):
    # Check if result is already cached
    if n in cache:
        print("Cache hit!")
        return cache[n], cache

    print("Cache miss!")
    result = 1
    for i in range(1, n + 1):
        result *= i
        cache[i] = result  # store intermediate results in cache

    return result, cache

# your code here


# For extra credit on the lab, solve the last finger excercise in section 5.8 of the textbook, the "Don Quixote encryption" (2 pts)
# your code here
