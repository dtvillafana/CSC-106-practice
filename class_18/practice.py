# ============================================================================
# PART 1: EXCEPTION HANDLING PRACTICE PROBLEMS
# ============================================================================

# For each practice problem, write code to test each function or class
# It is up to you to figure out the correct data attributes for each class
# You must also include test code that showcases all the behaviours of each function or method


# Problem 0: Safe Division
# ============================================================================
def safe_divide(numerator, denominator):
    """
    Problem 0: Safe Division

    Write a function that safely divides two numbers.
    - Handle ZeroDivisionError by returning None
    - Handle TypeError (if inputs aren't numbers) by returning "Invalid input"
    - Return the result if successful

    Example:
        safe_divide(10, 2) -> 5.0
        safe_divide(10, 0) -> None
        safe_divide("10", 2) -> "Invalid input"
    """
    # YOUR CODE HERE
    pass


# Problem 1: Get Valid Integer
# ============================================================================
def get_valid_integer(prompt, min_val=None, max_val=None):
    """
    Problem 1: Get Valid Integer Input

    Write a function that repeatedly prompts the user for an integer until
    a valid one is entered. Optionally check if it's within min_val and max_val.
    - Use try/except to handle ValueError
    - Keep asking until valid input is received
    - If min_val or max_val provided, validate the range

    Example:
        get_valid_integer("Enter age: ", 0, 120)
        # If user enters "abc", ask again
        # If user enters -5, ask again
        # If user enters 25, return 25
    """
    # YOUR CODE HERE
    pass


# Problem 2: List Element Access
# ============================================================================
def safe_get_element(lst, index, default=None):
    """
    Problem 2: Safe List Element Access

    Write a function that safely gets an element from a list.
    - Handle IndexError by returning the default value
    - Handle TypeError (if lst is not a list) by raising a custom error message
    - Return the element if successful

    Example:
        safe_get_element([1, 2, 3], 1) -> 2
        safe_get_element([1, 2, 3], 10) -> None
        safe_get_element([1, 2, 3], 10, "Not found") -> "Not found"
    """
    # YOUR CODE HERE
    pass


# Problem 3: Dictionary Operations
# ============================================================================
def safe_dict_operations(data_dict, key, operation="get", value=None):
    """
    Problem 3: Safe Dictionary Operations

    Write a function that performs safe dictionary operations.
    - operation can be 'get', 'set', or 'delete'
    - Handle KeyError appropriately for each operation
    - Handle TypeError if data_dict is not a dictionary
    - For 'get': return the value or None if key doesn't exist
    - For 'set': set the value and return True
    - For 'delete': delete the key and return True, or False if key doesn't exist

    Example:
        safe_dict_operations({'a': 1}, 'a', 'get') -> 1
        safe_dict_operations({'a': 1}, 'b', 'get') -> None
        safe_dict_operations({'a': 1}, 'b', 'set', 5) -> True (and modifies dict)
    """
    # YOUR CODE HERE
    pass


# Problem 4: Parse Data String
# ============================================================================
def parse_data_string(data_string, data_type="int"):
    """
    Problem 4: Parse Data String

    Write a function that takes a comma-separated string of values and converts
    them to a list of the specified data type.
    - data_type can be 'int', 'float', or 'str'
    - Handle ValueError when conversion fails by skipping that value
    - Handle TypeError if data_string is not a string
    - Return a list of successfully converted values
    - Use a finally block to print how many values were successfully parsed

    Example:
        parse_data_string("1,2,3,4", 'int') -> [1, 2, 3, 4]
        parse_data_string("1.5,2.7,abc,3.9", 'float') -> [1.5, 2.7, 3.9]
        parse_data_string("10,20,xyz,30", 'int') -> [10, 20, 30]
    """
    # YOUR CODE HERE
    pass


# ============================================================================
# PART 2: OBJECT-ORIENTED PROGRAMMING PRACTICE PROBLEMS
# ============================================================================


# Problem 5: Rectangle Class
# ============================================================================
class Rectangle:
    """
    Problem 5: Rectangle Class

    Create a Rectangle class with the following:
    - Constructor that takes width and height
    - Method get_area() that returns the area
    - Method get_perimeter() that returns the perimeter
    - Method is_square() that returns True if it's a square
    - Method scale(factor) that scales both dimensions by factor

    Example:
        rect = Rectangle(5, 10)
        rect.get_area() -> 50
        rect.get_perimeter() -> 30
        rect.is_square() -> False
        rect.scale(2)  # Now 10 x 20
    """

    # YOUR CODE HERE


# Problem 6: BankAccount Class
# ============================================================================
class BankAccount:
    """
    Problem 6: Bank Account Class

    Create a BankAccount class with the following:
    - Constructor that takes account_holder name and initial_balance (default 0)
    - Method deposit(amount) that adds to balance
    - Method withdraw(amount) that subtracts from balance
        * Raise ValueError if amount > balance
    - Method get_balance() that returns current balance
    - Method transfer(amount, other_account) that transfers money to another account
        * Should use withdraw and deposit methods

    Example:
        acc1 = BankAccount("Alice", 1000)
        acc2 = BankAccount("Bob", 500)
        acc1.withdraw(200)  # Alice now has 800
        acc1.transfer(300, acc2)  # Alice: 500, Bob: 800
    """

    # YOUR CODE HERE


# Problem 7: Student Class
# ============================================================================
class Student:
    """
    Problem 7: Student Class

    Create a Student class with the following:
    - Constructor that takes name and student_id
    - Attribute grades (initially an empty list)
    - Method add_grade(grade) that adds a grade (0-100)
        * Raise ValueError if grade not in valid range
    - Method get_average() that returns the average grade
        * Return 0 if no grades
    - Method get_letter_grade() that returns letter grade based on average:
        * A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
    - Method is_passing() that returns True if average >= 60

    Example:
        student = Student("Alice", "S001")
        student.add_grade(85)
        student.add_grade(90)
        student.get_average() -> 87.5
        student.get_letter_grade() -> "B"
    """

    # YOUR CODE HERE


# Problem 8: Book Class
# ============================================================================
class Book:
    """
    Problem 8: Book Class

    Create a Book class with the following:
    - Constructor that takes title, author, pages, and is_available (default True)
    - Method checkout() that sets is_available to False
        * Raise Exception if already checked out
    - Method return_book() that sets is_available to True
        * Raise Exception if already available
    - Method __str__() that returns a formatted string with book details
    - Method is_long() that returns True if pages > 300

    Example:
        book = Book("1984", "George Orwell", 328)
        print(book) -> "1984 by George Orwell (328 pages)"
        book.checkout()  # is_available becomes False
        book.checkout()  # Throws Exception
        book.is_long() -> True
    """

    # YOUR CODE HERE


# Problem 9: Temperature Class
# ============================================================================
class Temperature:
    """
    Problem 9: Temperature Class

    Create a Temperature class with the following:
    - Constructor that takes temperature value and unit ('C', 'F', or 'K')
        * Raise ValueError if unit not valid
        * Raise ValueError if Kelvin temperature < 0
    - Method to_celsius() that converts to Celsius
    - Method to_fahrenheit() that converts to Fahrenheit
    - Method to_kelvin() that converts to Kelvin
    - Method is_freezing() that returns True if temp is at or below water's freezing point
    - Method is_boiling() that returns True if temp is at or above water's boiling point

    Conversion formulas:
        C to F: (C * 9/5) + 32
        F to C: (F - 32) * 5/9
        C to K: C + 273.15
        K to C: K - 273.15

    Example:
        temp = Temperature(100, 'C')
        temp.to_fahrenheit() -> 212.0
        temp.is_boiling() -> True
    """

    # YOUR CODE HERE


if __name__ == "__main__":
    # your code here to test your solutions
    safe_divide(10, 2)
    # ...
