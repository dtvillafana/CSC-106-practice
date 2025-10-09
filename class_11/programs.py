# INFO: for this exercise, do not modify the comments, and write your code directly beneath each commented section.

# Practice 0
# Given x and y below, the code incorrectly swaps the values.
# Fix the buggy example to swap the values.
x = 1
y = 2
y = x
x = y
print(f"y: {y}, x: {x}")

# Practice 1
# combine num and s and print the result
num = 5
s = "my num is"

# Practice 2
# starting with a fractional approximation of pi, calculate the area of a circle
# with a radius of 14. Remember, to get the area of a circle, it's pi times the
# radius squared. Bind all the values you will use to well named variables, so
# the final calculation is all done with without any primitive numbers
# print the result
pi_approximation = 355/113




# Practice 3
# fix the code.
x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: "))
if x == y:
    print(x,"is not the same as",y)
print("These are equal!")

# Practice 4
# initialize a variable called num with any positive integer as the value, then
# use an if statement to print 'Even' if num is even, and print 'Odd', if num is odd

# Practice 5
# initialize a variable called num with any positive integer as the value, then
# use if statements to print 'Divisible by 2 and 3' if num is divisible by both 2
# and 3, print 'Divisible by 2 and not 3' if num is divisible by 2 and not 3, and
# 'Divisible by 3 and not 2' if num is divisible by 3 and not 2


# Practice 6
# initialize variables x, y, z with positive integers. Using only if statements,
# write a program that prints 'x is least' if x is the lowest value, 'y is least'
# if y is the lowest value, etc


# Practice 7
# print the string "Hello World!"


# Practice 8
# create a new string with only the first three characters of alpha using slicing,
# then print that new string and its length
alpha = "abcdefghijk"


# Practice 9
# print the numbers 2 through 5 using a while loop
x = 2


# Practice 10
# print the numbers 0 through 4 using a for loop and the range function
x = 5


# Practice 11
# use the input function to take a number as user input, then multiply that 
# number by 5, print the result


# Practice 12
# print the total of all the numbers in the nums tuple
nums = (43, 851, 12, 5)


# Practice 13
# implement fizz buzz, a classic interview question
#  For each number 1-100:
#     Print "Fizz" if the number is divisible by 3.
#     Print "Buzz" if the number is divisible by 5.
#     Print "FizzBuzz" if the number is divisible by both 3 and 5.
#     Otherwise, just print the number itself.


# Practice 14
# write a program that utilizes a loop to calculate factorials, remember,
# 5 factorial is 5*4*3*2*1


# Practice 15
# define a function that takes two parameters, adds them, and returns the result
# of the addition. Use this function to print the result of 5 + 8


# Practice 16
# Fix the code here so the function returns the proper exponentiation
def exponentiation(x):
    e = x ** y
    return e

y = 2
x = 4
result = exponentiation(x, y)
print(result)


# Practice 17
# get the element "astrology" from the list using its index, then print it
the_list = ["The" ,"science", "of", "astrology", "has", "ancient", "roots."]


# Practice 18
# reverse the list using a slice
the_list = [1, 2, 3, 4, 8]
print(the_list)

# Practice 19
# create a new list where the first and last elements are swapped.
# print the new list
the_list = ["sentence.", "is", "not", "a", "grammatical", "This"]

# Practice 20
# the general form of a list comprehension is
# [ <expression> for element in iterable if <boolean expression> ]
# create a new list using a lst as the iterable in a comprehension that doubles
# each element
lst = [1, 2, 3, 4, 5]


# Practice 21
# the general form of a list comprehension is
# [ <expression> for element in iterable if <boolean expression> ]
# create a new list using lst as the iterable in a list comprehension that does
# not contain even numbers
lst = [1, 2, 3, 4, 5, 6]


# Practice 22
# implement a bisection search to get the number that is entered, for each iteration of the search, print the current guess. 
secret_number = int(input("Enter a secret number between 0 and 999 to be found: "))
result = 0

print(f"Found! Your number is {result}")
