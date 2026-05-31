"""
Python Basics: The Foundation of Programming.
This script introduces the absolute fundamental concepts necessary to start coding in Python,
from variables and data types to basic control flow and function definitions.

What you will learn:
•  How to declare and use variables with various basic data types (numbers, strings, booleans).
•  Understanding and applying fundamental operators (arithmetic, comparison, logical).
•  Implementing conditional logic using `if`, `elif`, and `else` statements.
•  Mastering looping constructs with `for` and `while` loops for repetitive tasks.
•  Defining and calling functions to organize and reuse your code effectively.
•  Working with Python's core collection types: lists, tuples, and dictionaries.

Prerequisites:
•  Basic computer literacy (e.g., knowing how to save a file and run a command from a terminal).
•  An installed Python 3 interpreter (version 3.8 or higher recommended).
•  A text editor or Integrated Development Environment (IDE) to write and execute code.

Key Concepts Covered:
•  Variables and Assignment
•  Integer, Float, String, Boolean Data Types
•  Type Conversion (`int()`, `float()`, `str()`)
•  Arithmetic Operators (+, -, *, /, //, %, **)
•  Comparison Operators (==, !=, <, >, <=, >=)
•  Logical Operators (and, or, not)
•  f-strings for String Formatting
•  Lists (Creation, Indexing, Slicing, Methods, Mutability)
•  Tuples (Creation, Immutability)
•  Dictionaries (Key-Value Pairs, Access, Modification)
•  `if`, `elif`, `else` Conditional Statements
•  `for` Loops with `range()` and Collection Iteration
•  `while` Loops
•  `break` and `continue` Statements
•  Functions (Definition, Parameters, Return Values, Type Hints, Default Arguments)
•  `None` Keyword
•  Global vs. Local Scope
•  List Comprehensions (basic)
•  `enumerate()` for Indexed Iteration
•  `zip()` for Parallel Iteration
•  Sequence Unpacking
•  Membership Testing (`in` Operator)
•  Conditional Expressions (Ternary Operator)
•  Basic Class Definition and Object Instantiation
•  Measuring Execution Time (`time.time()`)
•  Inspecting Memory Usage (`sys.getsizeof()`)
"""

import time  # Used for measuring execution time in Section 7
import sys   # Used for measuring memory usage in Section 7

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: Absolute Fundamentals of Python
# ═══════════════════════════════════════════════════════════════

def section_1_core_concepts() -> None:
    """
    Demonstrates fundamental Python concepts: variables, basic data types, and arithmetic operations.
    """
    print("--- SECTION 1: Absolute Fundamentals ---")

    # 1.1 Variables and Basic Data Types
    # WHY: Variables are used to store data in memory, allowing you to refer to it by a name.
    #      Python is dynamically typed, meaning you don't declare the type explicitly.
    greeting_message: str = "Hello, Python Learners!"  # Declaring a string variable
    student_count: int = 150                          # Declaring an integer variable
    average_score: float = 87.5                       # Declaring a float variable
    is_active_course: bool = True                     # Declaring a boolean variable

    print(f"Greeting: {greeting_message}")            # Displaying the string variable
    # → Greeting: Hello, Python Learners!
    print(f"Students enrolled: {student_count}")      # Displaying the integer variable
    # → Students enrolled: 150
    print(f"Average score: {average_score}")          # Displaying the float variable
    # → Average score: 87.5
    print(f"Course is active: {is_active_course}")    # Displaying the boolean variable
    # → Course is active: True

    # 1.2 Basic Arithmetic Operators
    # WHY: Operators perform operations on variables and values.
    #      Arithmetic operators are fundamental for numerical calculations.
    num1: int = 10                                    # First number
    num2: int = 3                                     # Second number

    sum_result: int = num1 + num2                     # Addition
    print(f"{num1} + {num2} = {sum_result}")          # Displaying addition result
    # → 10 + 3 = 13

    difference_result: int = num1 - num2              # Subtraction
    print(f"{num1} - {num2} = {difference_result}")   # Displaying subtraction result
    # → 10 - 3 = 7

    product_result: int = num1 * num2                 # Multiplication
    print(f"{num1} * {num2} = {product_result}")      # Displaying multiplication result
    # → 10 * 3 = 30

    division_result: float = num1 / num2              # Float division (always returns float)
    print(f"{num1} / {num2} = {division_result}")     # Displaying float division result
    # → 10 / 3 = 3.3333333333333335

    integer_division_result: int = num1 // num2       # Integer division (discards fractional part)
    print(f"{num1} // {num2} = {integer_division_result}") # Displaying integer division result
    # → 10 // 3 = 3

    modulo_result: int = num1 % num2                  # Modulo (remainder of division)
    print(f"{num1} % {num2} = {modulo_result}")       # Displaying modulo result
    # → 10 % 3 = 1

    exponentiation_result: int = num1 ** num2         # Exponentiation (10 to the power of 3)
    print(f"{num1} ** {num2} = {exponentiation_result}") # Displaying exponentiation result
    # → 10 ** 3 = 1000

    # 1.3 Type Conversion
    # WHY: Sometimes you need to change a variable's data type, e.g., to perform arithmetic
    #      on user input which is typically read as a string.
    age_str: str = "30"                               # Age stored as a string
    age_int: int = int(age_str)                       # Convert string to integer
    print(f"Age as int: {age_int}, type: {type(age_int)}") # Display converted age and its type
    # → Age as int: 30, type: <class 'int'>

    price_str: str = "99.99"                          # Price stored as a string
    price_float: float = float(price_str)             # Convert string to float
    print(f"Price as float: {price_float}, type: {type(price_float)}") # Display converted price and its type
    # → Price as float: 99.99, type: <class 'float'>

    number_to_string: str = str(123)                  # Convert integer to string
    print(f"Number to string: '{number_to_string}', type: {type(number_to_string)}") # Display converted number and its type
    # → Number to string: '123', type: <class 'str'>
    🔑 Key insight: Python's `type()` function is useful for inspecting the data type of any variable.

# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns: Everyday Usage
# ═══════════════════════════════════════════════════════════════

def section_2_syntax_patterns() -> None:
    """
    Covers common Python syntax for strings, collections (lists, tuples, dictionaries),
    and basic control flow (if/else, for, while loops).
    """
    print("\n--- SECTION 2: Syntax & Common Patterns ---")

    # 2.1 String Manipulation with f-strings
    # WHY: f-strings provide a concise and readable way to embed expressions inside string literals.
    name: str = "Alice"                               # User's name
    age: int = 25                                     # User's age
    city: str = "New York"                            # User's city

    # Using f-string for easy formatting
    personal_info: str = f"Name: {name}, Age: {age}, City: {city}."
    print(personal_info)                              # Display formatted string
    # → Name: Alice, Age: 25, City: New York.

    # String methods
    message: str = "  python programming is fun!  "   # A string with leading/trailing spaces and mixed case
    print(f"Original message: '{message}'")           # Display original message
    # → Original message: '  python programming is fun!  '
    print(f"Uppercase: '{message.upper()}'")          # Convert to uppercase
    # → Uppercase: '  PYTHON PROGRAMMING IS FUN!  '
    print(f"Capitalized: '{message.capitalize()}'")    # Capitalize first letter
    # → Capitalized: '  python programming is fun!  '
    print(f"Stripped & Title Case: '{message.strip().title()}'") # Remove whitespace, then title case
    # → Stripped & Title Case: 'Python Programming Is Fun!'

    # 2.2 Lists: Ordered, Mutable Collections
    # WHY: Lists are versatile for storing sequences of items that can be changed.
    fruits: list[str] = ["apple", "banana", "cherry"] # Create a list of strings
    print(f"Initial fruits: {fruits}")                # Display the list
    # → Initial fruits: ['apple', 'banana', 'cherry']

    fruits.append("date")                             # Add an item to the end
    print(f"After append: {fruits}")                  # Display list after append
    # → After append: ['apple', 'banana', 'cherry', 'date']

    fruits.insert(1, "grape")                         # Insert an item at a specific index
    print(f"After insert: {fruits}")                  # Display list after insert
    # → After insert: ['apple', 'grape', 'banana', 'cherry', 'date']

    removed_fruit: str = fruits.pop(2)                # Remove and return item at index 2 ('banana')
    print(f"After pop ('{removed_fruit}'): {fruits}") # Display list after pop
    # → After pop ('banana'): ['apple', 'grape', 'cherry', 'date']

    fruits[0] = "apricot"                             # Modify an item by index
    print(f"After modifying first item: {fruits}")    # Display list after modification
    # → After modifying first item: ['apricot', 'grape', 'cherry', 'date']

    # List slicing
    sub_fruits: list[str] = fruits[1:3]               # Get elements from index 1 up to (but not including) 3
    print(f"Sliced fruits (index 1 to 2): {sub_fruits}")
    # → Sliced fruits (index 1 to 2): ['grape', 'cherry']

    # 2.3 Tuples: Ordered, Immutable Collections
    # WHY: Tuples are used for collections of items that should not change after creation.
    coordinates: tuple[int, int] = (10, 20)           # Create a tuple of integers
    print(f"Coordinates: {coordinates}")              # Display the tuple
    # → Coordinates: (10, 20)
    print(f"First coordinate: {coordinates[0]}")      # Accessing elements by index
    # → First coordinate: 10

    # ⚠️ Common mistake: Trying to modify a tuple
    # coordinates[0] = 5 # This would raise a TypeError: 'tuple' object does not support item assignment

    # 2.4 Dictionaries: Unordered, Mutable Key-Value Pairs
    # WHY: Dictionaries store data in key-value pairs, allowing efficient lookup by key.
    person: dict[str, str | int] = {                  # Create a dictionary
        "name": "Bob",
        "age": 30,
        "occupation": "Engineer"
    }
    print(f"Person details: {person}")                # Display the dictionary
    # → Person details: {'name': 'Bob', 'age': 30, 'occupation': 'Engineer'}

    print(f"Bob's age: {person['age']}")              # Accessing a value using its key
    # → Bob's age: 30

    person["age"] = 31                                # Update an existing value
    person["city"] = "London"                         # Add a new key-value pair
    print(f"Updated person details: {person}")        # Display updated dictionary
    # → Updated person details: {'name': 'Bob', 'age': 31, 'occupation': 'Engineer', 'city': 'London'}

    del person["occupation"]                          # Remove a key-value pair
    print(f"Person after removing occupation: {person}")
    # → Person after removing occupation: {'name': 'Bob', 'age': 31, 'city': 'London'}

    # 2.5 Conditional Statements (if, elif, else)
    # WHY: Control flow based on conditions, allowing your program to make decisions.
    temperature: int = 28                             # Current temperature
    if temperature > 30:                              # Check if temperature is greater than 30
        print("It's a hot day!")
    elif temperature > 20:                            # Else if temperature is greater than 20
        print("It's a warm day.")
    else:                                             # Otherwise
        print("It's a cool day.")
    # → It's a warm day.

    # 2.6 Looping with 'for'
    # WHY: Iterating over sequences (lists, strings, ranges) to perform actions repeatedly.
    print("--- For Loop Examples ---")
    fruits_list: list[str] = ["apple", "banana", "kiwi"] # A list of fruits
    for fruit in fruits_list:                         # Iterate over each fruit in the list
        print(f"I like {fruit}.")                     # Print a message for each fruit
    # → I like apple.
    # → I like banana.
    # → I like kiwi.

    # Looping with range()
    # WHY: `range()` generates a sequence of numbers, useful for fixed-number iterations.
    for i in range(3):                                # Loop 3 times (0, 1, 2)
        print(f"Loop iteration {i}")                  # Print the current iteration number
    # → Loop iteration 0
    # → Loop iteration 1
    # → Loop iteration 2

    # 2.7 Looping with 'while'
    # WHY: Repeating a block of code as long as a condition is true.
    print("--- While Loop Example ---")
    count: int = 0                                    # Initialize a counter
    while count < 3:                                  # Loop as long as count is less than 3
        print(f"Count is: {count}")                   # Print the current count
        count += 1                                    # Increment the count (important to avoid infinite loops!)
    # → Count is: 0
    # → Count is: 1
    # → Count is: 2

    # Using break and continue in loops
    print("--- Break and Continue Example ---")
    for num in range(5):                              # Iterate from 0 to 4
        if num == 2:                                  # If number is 2
            print("Skipping 2 with continue")         # Indicate skipping
            continue                                  # Skip the rest of the current iteration
        if num == 4:                                  # If number is 4
            print("Breaking loop at 4")               # Indicate breaking
            break                                     # Exit the loop entirely
        print(f"Processing number: {num}")            # Process number if not skipped or broken
    # → Processing number: 0
    # → Processing number: 1
    # → Skipping 2 with continue
    # → Processing number: 3
    # → Breaking loop at 4

# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas: What Beginners Always Get Wrong
# ═══════════════════════════════════════════════════════════════

def section_3_edge_cases_gotchas() -> None:
    """
    Highlights common pitfalls and misunderstandings for beginners in Python.
    """
    print("\n--- SECTION 3: Edge Cases & Gotchas ---")

    # 3.1 Type Mismatch Errors
    # WHY: Python is strongly typed, so you cannot implicitly combine incompatible types.
    # 🐛 Bug source: Trying to add a number and a string directly.
    # print("Result: " + 5) # This would raise a TypeError: can only concatenate str (not "int") to str
    print("Result: " + str(5))                        # ✅ Preferred: Convert number to string explicitly
    # → Result: 5

    num_str: str = "10"
    # total: int = num_str + 5 # This would raise a TypeError: can only concatenate str (not "int") to str
    total: int = int(num_str) + 5                     # ✅ Preferred: Convert string to int for arithmetic
    print(f"Converted sum: {total}")                  # Display the sum
    # → Converted sum: 15

    # 3.2 Mutable vs. Immutable Types (Lists vs. Tuples/Strings)
    # WHY: Understanding mutability is crucial for avoiding unexpected side effects,
    #      especially when passing objects to functions or assigning them.
    # ℹ️ Note: Lists are mutable (can be changed), while tuples, strings, and numbers are immutable (cannot be changed after creation).

    # Example with a mutable list
    list_a: list[int] = [1, 2, 3]                     # Initial list
    list_b: list[int] = list_a                        # list_b points to the SAME list object as list_a
    list_b.append(4)                                  # Modifying list_b
    print(f"List A after list B append: {list_a}")    # list_a is also changed!
    # → List A after list B append: [1, 2, 3, 4]

    # To create an independent copy of a list:
    list_c: list[int] = [5, 6, 7]                     # Initial list C
    list_d: list[int] = list_c[:]                     # Create a SHALLOW copy using slicing
    list_d.append(8)                                  # Modify list_d
    print(f"List C after list D append: {list_c}")    # List C remains unchanged
    # → List C after list D append: [5, 6, 7]
    print(f"List D: {list_d}")                        # List D is independent
    # → List D: [5, 6, 7, 8]

    # Example with an immutable string
    string_a: str = "hello"                           # Initial string
    string_b: str = string_a                          # string_b points to the SAME string object
    string_b = string_b + " world"                    # This creates a NEW string object for string_b
    print(f"String A after string B change: {string_a}") # String A remains unchanged
    # → String A after string B change: hello
    print(f"String B: {string_b}")                    # String B is the new string
    # → String B: hello world

    # 3.3 Integer Division vs. Float Division
    # WHY: `//` and `/` behave differently and choosing the wrong one can lead to incorrect results.
    result_float_div: float = 10 / 3                  # Float division
    print(f"10 / 3 = {result_float_div}")             # Result is a float
    # → 10 / 3 = 3.3333333333333335

    result_int_div: int = 10 // 3                     # Integer division (floor division)
    print(f"10 // 3 = {result_int_div}")              # Result is an integer (fractional part discarded)
    # → 10 // 3 = 3

    # 3.4 Variable Scope (Local vs. Global)
    # WHY: Understanding where variables are accessible prevents `NameError` and unexpected behavior.
    global_variable: str = "I am global"              # Declared in global scope

    def scope_example() -> None:
        local_variable: str = "I am local"            # Declared in local scope of function
        print(f"Inside function: {local_variable}")   # Accessible: local_variable
        # → Inside function: I am local
        print(f"Inside function: {global_variable}")  # Accessible: global_variable
        # → Inside function: I am global

        # ⚠️ Common mistake: Trying to modify a global variable without `global` keyword.
        # global_variable = "Modified locally" # This would create a NEW local variable named global_variable
        # To actually modify the global variable:
        # global global_variable
        # global_variable = "Modified globally"

    scope_example()                                   # Call the function
    print(f"Outside function: {global_variable}")     # Accessible: global_variable
    # → Outside function: I am global
    # print(local_variable) # This would raise a NameError: name 'local_variable' is not defined
    #                       # local_variable only exists within scope_example()

    # 3.5 Off-by-one Errors in Indexing/Slicing
    # WHY: Python uses 0-based indexing and exclusive end-points for slicing, which can be tricky.
    data_list: list[str] = ["A", "B", "C", "D", "E"]  # A list of 5 elements
    print(f"List: {data_list}")                       # Display the list
    # → List: ['A', 'B', 'C', 'D', 'E']
    print(f"First element: {data_list[0]}")           # Accessing the first element
    # → First element: A
    print(f"Last element: {data_list[len(data_list) - 1]}") # Accessing the last element explicitly
    # → Last element: E
    print(f"Last element (Pythonic): {data_list[-1]}") # ✅ Preferred: Use negative indexing for last element
    # → Last element (Pythonic): E

    # Slicing: [start:end] -> end index is EXCLUSIVE
    print(f"Elements from index 1 to 3 (exclusive): {data_list[1:3]}") # Gets elements at index 1 and 2
    # → Elements from index 1 to 3 (exclusive): ['B', 'C']
    # If you want elements up to and including index 3, you need `data_list[1:4]`

    # Range: range(start, stop) -> stop is EXCLUSIVE
    print("Range from 0 to 2:")
    for i in range(3):                                # Generates 0, 1, 2
        print(f"  {i}")
    # → Range from 0 to 2:
    # →   0
    # →   1
    # →   2
    # If you want 0 to N, use `range(N + 1)`

# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns: One Level Up From Basics
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """
    Introduces functions with type hints, default arguments, `None`, and simple list comprehensions.
    """
    print("\n--- SECTION 4: Intermediate Patterns ---")

    # 4.1 Functions with Type Hints and Return Values
    # WHY: Functions encapsulate reusable blocks of code. Type hints improve readability
    #      and allow static analysis tools to catch errors early.
    def calculate_area(length: float, width: float) -> float:
        """
        Calculates the area of a rectangle.
        Args:
            length: The length of the rectangle.
            width: The width of the rectangle.
        Returns:
            The calculated area as a float.
        """
        return length * width                         # Return the product of length and width

    area1: float = calculate_area(5.0, 3.0)           # Call the function with float arguments
    print(f"Area of 5x3 rectangle: {area1}")          # Display the calculated area
    # → Area of 5x3 rectangle: 15.0

    area2: float = calculate_area(7.2, 4.1)           # Call with different arguments
    print(f"Area of 7.2x4.1 rectangle: {area2:.2f}")  # Display with 2 decimal places
    # → Area of 7.2x4.1 rectangle: 29.52

    # 4.2 Functions with Default Arguments
    # WHY: Default arguments allow functions to be called with fewer arguments,
    #      providing flexibility and reducing boilerplate.
    def greet(name: str, message: str = "Hello") -> str:
        """
        Greets a person with a customizable message.
        Args:
            name: The name of the person to greet.
            message: The greeting message (defaults to "Hello").
        Returns:
            A formatted greeting string.
        """
        return f"{message}, {name}!"                  # Return the formatted greeting

    greeting1: str = greet("Charlie")                 # Call with only required argument (uses default message)
    print(greeting1)                                  # Display the