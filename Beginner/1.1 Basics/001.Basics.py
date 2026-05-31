"""Python Basics: Your First Steps into Programming

This module introduces the foundational concepts of Python programming, designed for absolute beginners.
You will learn to write, execute, and understand simple Python scripts, building a solid base for further learning.

What you will learn:
- How to declare variables and understand fundamental data types.
- Basic arithmetic, string manipulation, and input/output operations.
- Control flow structures like conditional statements and loops.
- How to define and use functions to organize your code.
- Essential data structures: lists, tuples, dictionaries, and sets.
- Pythonic ways to write clean, efficient, and readable code.
- Basic principles of object-oriented programming with a simple class.

Prerequisites:
- A computer with Python 3 installed (preferably 3.8+).
- A text editor (like VS Code, Sublime Text, or even Notepad).
- Basic familiarity with your operating system's command line or terminal.

Key Concepts Covered:
- Variables, Data Types (int, float, str, bool)
- Operators (Arithmetic, Comparison, Logical, Assignment)
- `print()`, `input()`
- `if/elif/else` statements
- `for` and `while` loops
- Lists, Tuples, Dictionaries, Sets
- Functions (definition, parameters, return values, type hints)
- Error Handling (`try-except`)
- Pythonic Iteration (`enumerate`, `zip`)
- Classes and Objects
- Generators
- Basic Performance Measurement (`time` module)
"""

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: Absolute Fundamentals
# ═══════════════════════════════════════════════════════════════

def section_1_core_fundamentals() -> None:
    """
    Demonstrates basic variables, data types, operators, and I/O.
    """
    print("\nSECTION 1: Core Concept: Absolute Fundamentals")
    print("--------------------------------------------------")

    # 1.1 Variables and Basic Data Types
    # Variables are used to store data values. Python is dynamically typed.
    # ℹ️  Note: Python automatically infers the data type based on the assigned value.
    my_integer: int = 10                  # An integer number
    my_float: float = 3.14                # A floating-point number (decimal)
    my_string: str = "Hello, Python!"     # A string (sequence of characters)
    my_boolean: bool = True               # A boolean (True or False)

    print(f"Integer: {my_integer}, Type: {type(my_integer)}")
    # → Integer: 10, Type: <class 'int'>
    print(f"Float: {my_float}, Type: {type(my_float)}")
    # → Float: 3.14, Type: <class 'float'>
    print(f"String: {my_string}, Type: {type(my_string)}")
    # → String: Hello, Python!, Type: <class 'str'>
    print(f"Boolean: {my_boolean}, Type: {type(my_boolean)}")
    # → Boolean: True, Type: <class 'bool'>

    # 1.2 Basic Arithmetic Operators
    # Perform mathematical calculations.
    num_a: int = 20                       # First number for operations
    num_b: int = 7                        # Second number for operations

    addition: int = num_a + num_b         # Addition
    subtraction: int = num_a - num_b      # Subtraction
    multiplication: int = num_a * num_b   # Multiplication
    division: float = num_a / num_b       # Float division (always returns float)
    floor_division: int = num_a // num_b  # Floor division (discards fractional part)
    modulus: int = num_a % num_b          # Modulus (remainder of division)
    exponentiation: int = num_a ** 2      # Exponentiation (num_a to the power of 2)

    print(f"\nArithmetic Operations with {num_a} and {num_b}:")
    print(f"  Addition ({num_a} + {num_b}): {addition}")
    # →   Addition (20 + 7): 27
    print(f"  Subtraction ({num_a} - {num_b}): {subtraction}")
    # →   Subtraction (20 - 7): 13
    print(f"  Multiplication ({num_a} * {num_b}): {multiplication}")
    # →   Multiplication (20 * 7): 140
    print(f"  Division ({num_a} / {num_b}): {division:.2f}") # Format to 2 decimal places
    # →   Division (20 / 7): 2.86
    print(f"  Floor Division ({num_a} // {num_b}): {floor_division}")
    # →   Floor Division (20 // 7): 2
    print(f"  Modulus ({num_a} % {num_b}): {modulus}")
    # →   Modulus (20 % 7): 6
    print(f"  Exponentiation ({num_a} ** 2): {exponentiation}")
    # →   Exponentiation (20 ** 2): 400

    # 1.3 String Concatenation and Formatting
    # Combining strings and embedding variables.
    greeting_part1: str = "Hello"         # First part of the greeting
    greeting_part2: str = "World"         # Second part of the greeting
    combined_greeting: str = greeting_part1 + ", " + greeting_part2 + "!" # Concatenate strings
    print(f"\nString Concatenation: {combined_greeting}")
    # → String Concatenation: Hello, World!

    # 🔑 Key insight: f-strings are the preferred way for string formatting.
    name: str = "Alice"                   # A name for a personalized message
    age: int = 30                         # An age for a personalized message
    formatted_message: str = f"My name is {name} and I am {age} years old." # Using an f-string
    print(f"Formatted Message: {formatted_message}")
    # → Formatted Message: My name is Alice and I am 30 years old.

    # 1.4 Basic Input/Output (`input()` and `print()`)
    # `input()` takes user input as a string.
    # `print()` displays output to the console.
    print("\n--- Interactive Input Example ---")
    # ℹ️  Note: For demonstration, we'll use a hardcoded value instead of actual input()
    #    to ensure the script runs non-interactively for testing.
    # user_name = input("Please enter your name: ")
    user_name: str = "Bob"                # Simulating user input for script execution
    # user_age_str = input("Please enter your age: ")
    user_age_str: str = "25"              # Simulating user input for script execution

    # ⚠️ Common mistake: input() always returns a string. Convert to int if needed.
    user_age: int = int(user_age_str)     # Convert string age to integer

    print(f"Hello, {user_name}! You are {user_age} years old.")
    # → Hello, Bob! You are 25 years old.
    print("--- End Interactive Input Example ---")


# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns: Everyday Usage
# ═══════════════════════════════════════════════════════════════

def section_2_syntax_common_patterns() -> None:
    """
    Covers conditional statements, loops, and basic data structures.
    """
    print("\nSECTION 2: Syntax & Common Patterns: Everyday Usage")
    print("--------------------------------------------------")

    # 2.1 Conditional Statements (`if`, `elif`, `else`)
    # Execute different code blocks based on conditions.
    temperature: int = 25                 # Current temperature in Celsius

    print(f"\nChecking temperature: {temperature}°C")
    if temperature > 30:                  # Condition for hot weather
        print("  It's a hot day!")
    elif temperature > 20:                # Condition for warm weather (if not hot)
        print("  It's a pleasant day.")
    else:                                 # Default condition (if neither hot nor warm)
        print("  It's a bit chilly.")
    # →   It's a pleasant day.

    # Example 2: Checking a number's parity
    number_to_check: int = 17             # An integer to check if it's even or odd
    if number_to_check % 2 == 0:          # Check if remainder after division by 2 is 0
        print(f"  {number_to_check} is an even number.")
    else:                                 # If not even, it must be odd
        print(f"  {number_to_check} is an odd number.")
    # →   17 is an odd number.

    # 2.2 Loops (`for` and `while`)
    # `for` loop: Iterate over a sequence (like a list, string, or range).
    print("\n--- For Loop Examples ---")
    fruits: list[str] = ["apple", "banana", "cherry"] # A list of fruits
    print("Iterating through fruits:")
    for fruit in fruits:                  # Loop through each item in the 'fruits' list
        print(f"  I love {fruit}s!")
    # →   I love apples!
    # →   I love bananas!
    # →   I love cherrys!

    # `range()` function generates a sequence of numbers.
    print("Counting from 0 to 4:")
    for i in range(5):                    # Loop from 0 up to (but not including) 5
        print(f"  Count: {i}")
    # →   Count: 0
    # →   Count: 1
    # →   Count: 2
    # →   Count: 3
    # →   Count: 4

    # `while` loop: Continues as long as its condition is true.
    print("\n--- While Loop Example ---")
    count: int = 0                        # Initialize count for the while loop
    print("Counting up to 3:")
    while count < 3:                      # Loop as long as count is less than 3
        print(f"  Current count: {count}")
        count += 1                        # Increment count to eventually stop the loop
    # →   Current count: 0
    # →   Current count: 1
    # →   Current count: 2

    # 2.3 Basic Data Structures
    # Lists: Ordered, mutable collections of items.
    my_list: list[int] = [1, 2, 3, 4]     # Create a list of integers
    my_list.append(5)                     # Add an element to the end of the list
    print(f"\nList: {my_list}")
    # → List: [1, 2, 3, 4, 5]
    print(f"First element of list: {my_list[0]}") # Access by index (0-based)
    # → First element of list: 1
    print(f"Length of list: {len(my_list)}")
    # → Length of list: 5

    # Tuples: Ordered, immutable collections of items.
    my_tuple: tuple[str, int, float] = ("apple", 1, 2.5) # Create a tuple
    print(f"Tuple: {my_tuple}")
    # → Tuple: ('apple', 1, 2.5)
    print(f"Second element of tuple: {my_tuple[1]}")
    # → Second element of tuple: 1
    # ⚠️ Common mistake: my_tuple[0] = "orange" # This would raise a TypeError (tuples are immutable)

    # Dictionaries: Unordered collections of key-value pairs.
    my_dict: dict[str, int] = {"name": 1, "age": 2, "city": 3} # Create a dictionary
    print(f"\nDictionary: {my_dict}")
    # → Dictionary: {'name': 1, 'age': 2, 'city': 3}
    print(f"Value for key 'name': {my_dict['name']}") # Access value by key
    # → Value for key 'name': 1
    my_dict["age"] = 31                   # Update value for an existing key
    my_dict["job"] = 4                    # Add a new key-value pair
    print(f"Updated dictionary: {my_dict}")
    # → Updated dictionary: {'name': 1, 'age': 31, 'city': 3, 'job': 4}

    # Sets: Unordered collections of unique items.
    my_set: set[int] = {1, 2, 3, 2, 1}    # Create a set; duplicates are automatically removed
    print(f"\nSet: {my_set}")
    # → Set: {1, 2, 3}
    my_set.add(4)                         # Add an element to the set
    my_set.add(2)                         # Adding an existing element has no effect
    print(f"Updated set: {my_set}")
    # → Updated set: {1, 2, 3, 4}
    print(f"Is 3 in set? {3 in my_set}")  # Check for membership
    # → Is 3 in set? True


# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas: What Beginners Always Get Wrong
# ═══════════════════════════════════════════════════════════════

def section_3_edge_cases_gotchas() -> None:
    """
    Highlights common beginner mistakes and how to avoid them.
    """
    print("\nSECTION 3: Edge Cases & Gotchas: What Beginners Always Get Wrong")
    print("--------------------------------------------------")

    # 3.1 Type Conversion Errors
    # ⚠️ Common mistake: Trying to convert non-numeric string to int/float.
    string_number: str = "123"            # A string containing only digits
    string_text: str = "hello"            # A string containing non-digits

    print(f"\nConverting '{string_number}' to int: {int(string_number)}")
    # → Converting '123' to int: 123
    # print(int(string_text)) # This would raise a ValueError: invalid literal for int()
    print("  Attempting to convert 'hello' to int would cause a ValueError.")

    # 3.2 Mutable vs. Immutable Types (and Aliasing)
    # Immutable types (int, float, str, tuple): Value cannot change after creation.
    # Mutable types (list, dict, set): Value can be modified in place.

    # Example: List aliasing (mutable type)
    list_a: list[int] = [1, 2, 3]         # Original list
    list_b: list[int] = list_a            # list_b now refers to the SAME list object as list_a
    print(f"\nInitial lists: list_a={list_a}, list_b={list_b}")
    # → Initial lists: list_a=[1, 2, 3], list_b=[1, 2, 3]

    list_b.append(4)                      # Modify list_b
    print(f"After list_b.append(4): list_a={list_a}, list_b={list_b}")
    # → After list_b.append(4): list_a=[1, 2, 3, 4], list_b=[1, 2, 3, 4]
    # 🔑 Key insight: Both list_a and list_b point to the same list in memory.
    #    Modifying one affects the other.

    # ✅ Preferred/Pythonic: To create an independent copy of a list:
    list_c: list[int] = [5, 6, 7]         # Another list
    list_d: list[int] = list_c[:]         # Create a shallow copy using slicing
    # Or: list_d = list_c.copy()           # Using the .copy() method
    print(f"Initial independent lists: list_c={list_c}, list_d={list_d}")
    # → Initial independent lists: list_c=[5, 6, 7], list_d=[5, 6, 7]

    list_d.append(8)                      # Modify list_d
    print(f"After list_d.append(8): list_c={list_c}, list_d={list_d}")
    # → After list_d.append(8): list_c=[5, 6, 7], list_d=[5, 6, 7, 8]
    # 🔑 Key insight: list_c remains unchanged because list_d is a separate object.

    # 3.3 Integer Division vs. Float Division
    # ⚠️ Common mistake: Forgetting the difference between / and //.
    div_num_a: int = 10                   # Numerator
    div_num_b: int = 3                    # Denominator

    float_result: float = div_num_a / div_num_b # Standard division, always float
    int_result: int = div_num_a // div_num_b # Floor division, truncates to integer
    print(f"\nDivision of {div_num_a} by {div_num_b}:")
    print(f"  Float division (/) result: {float_result}")
    # →   Float division (/) result: 3.3333333333333335
    print(f"  Integer division (//) result: {int_result}")
    # →   Integer division (//) result: 3

    # 3.4 Equality (`==`) vs. Identity (`is`)
    # `==` checks if values are equal.
    # `is` checks if two variables refer to the *exact same object* in memory.
    val1: list[int] = [1, 2, 3]           # First list
    val2: list[int] = [1, 2, 3]           # Second list, same content but different object
    val3: list[int] = val1                # val3 refers to the same object as val1

    print(f"\nComparing lists: val1={val1}, val2={val2}, val3={val3}")
    print(f"  val1 == val2: {val1 == val2}") # True, because their contents are the same
    # →   val1 == val2: True
    print(f"  val1 is val2: {val1 is val2}") # False, because they are different objects
    # →   val1 is val2: False
    print(f"  val1 is val3: {val1 is val3}") # True, because val3 points to the same object as val1
    # →   val1 is val3: True

    # 3.5 Scope of Variables (Local vs. Global)
    # Variables defined inside a function are local to that function.
    # Variables defined outside functions are global.
    global_var: str = "I am global"       # A global variable

    def my_scoped_function() -> None:
        local_var: str = "I am local"     # A local variable
        print(f"\nInside function:")
        print(f"  Accessing global_var: {global_var}") # Can access global_var
        # →   Accessing global_var: I am global
        print(f"  Accessing local_var: {local_var}")   # Can access local_var
        # →   Accessing local_var: I am local

        # ⚠️ Common mistake: Modifying global variable without 'global' keyword.
        # This creates a new local variable named `global_var` instead of modifying the global one.
        # global_var = "I am a new local global_var"
        # print(f"  (Inside) Attempted to modify global_var: {global_var}")

        # ✅ Preferred/Pythonic: If you MUST modify a global, use the 'global' keyword.
        # Generally, avoid modifying global variables from within functions if possible.
        nonlocal_var: str = "I am nonlocal" # A variable in an enclosing scope (not global)

    my_scoped_function()
    print(f"\nOutside function:")
    print(f"  Accessing global_var: {global_var}")
    # →   Accessing global_var: I am global
    # print(local_var) # This would raise a NameError because local_var is not defined in global scope.
    print("  Attempting to access local_var outside function would cause a NameError.")


# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns: One Level Up From Basics
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """
    Introduces functions, default arguments, and basic error handling.
    """
    print("\nSECTION 4: Intermediate Patterns: One Level Up From Basics")
    print("--------------------------------------------------")

    # 4.1 Functions: Definition, Parameters, Return Values
    # Functions encapsulate reusable blocks of code.
    # Type hints improve code readability and help with static analysis.

    def greet_user(name: str, message: str = "Hello") -> str:
        """
        Greets a user with a personalized message.

        Args:
            name (str): The name of the user to greet.
            message (str, optional): The greeting message. Defaults to "Hello".

        Returns:
            str: The complete greeting string.
        """
        return f"{message}, {name}!"

    print("\n--- Function Examples ---")
    # Calling the function with required and default arguments
    greeting1: str = greet_user("Charlie") # Call with only 'name'
    print(f"Greeting 1: {greeting1}")
    # → Greeting 1: Hello, Charlie!

    # Calling the function with both required and optional arguments
    greeting2: str = greet_user("Diana", "Good morning") # Call with 'name' and 'message'
    print(f"Greeting 2: {greeting2}")
    # → Greeting 2: Good morning, Diana!

    # Using keyword arguments for clarity
    greeting3: str = greet_user(message="Hi there", name="Eve") # Keyword arguments can be out of order
    print(f"Greeting 3 (keyword args): {greeting3}")
    # → Greeting 3 (keyword args): Hi there, Eve!

    # Function with multiple return values (returned as a tuple)
    def calculate_stats(numbers: list[int]) -> tuple[int, float, int]:
        """
        Calculates the sum, average, and maximum of a list of integers.

        Args:
            numbers (list[int]): A list of integers.

        Returns:
            tuple[int, float, int]: A tuple containing (sum, average, max_value).
                                     Returns (0, 0.0, 0) for an empty list.
        """
        if not numbers:                   # Handle empty list case
            return 0, 0.0, 0
        total_sum: int = sum(numbers)     # Calculate sum using built-in function
        average: float = total_sum / len(numbers) # Calculate average
        max_value: int = max(numbers)     # Calculate max using built-in function
        return total_sum, average, max_value # Return as a tuple

    data_points: list[int] = [10, 20, 30, 40, 50] # List of numbers for stats
    total, avg, maximum = calculate_stats(data_points) # Unpack the returned tuple
    print(f"\nStats for {data_points}:")
    print(f"  Sum: {total}, Average: {avg}, Max: {maximum}")
    # →   Sum: 150, Average: 30.0, Max: 50

    # 4.2 List Comprehensions
    # A concise way to create lists.
    # WHY: More readable and often more efficient than traditional for loops for list creation.
    numbers_for_comp: list[int] = [1, 2, 3, 4, 5] # Original list of numbers

    # Traditional loop approach (commented out for comparison)
    # squared_numbers_loop = []
    # for num in numbers_for_comp:
    #     squared_numbers_loop.append(num * num)

    # ✅ Preferred/Pythonic: List comprehension
    squared_numbers_comp: list[int] = [num * num for num in numbers_for_comp] # Square each number
    print(f"\nOriginal numbers: {numbers_for_comp}")
    print(f"Squared numbers (list comprehension): {squared_numbers_comp}")
    # → Squared numbers (list comprehension): [1, 4, 9, 16, 25]

    # List comprehension with a condition
    even_numbers: list[int] = [num for num in numbers_for_comp if num % 2 == 0] # Filter for even numbers
    print(f"Even numbers (list comprehension with condition): {even_numbers}")
    # → Even numbers (list comprehension with condition): [2, 4]

    # 4.3 Error Handling (`try-except`)
    # Gracefully handle runtime errors (exceptions).
    print("\n--- Error Handling Example ---")

    def divide_numbers(numerator: int | float, denominator: int | float) -> float | str:
        """
        Divides two numbers, handling division by zero.

        Args:
            numerator (int | float): The number to be divided.
            denominator (int | float): The divisor.

        Returns:
            float | str: The result of the division, or an error message if division by zero occurs.
        """
        try:
            result: float = numerator / denominator # Attempt the division
            return result
        except ZeroDivisionError:               # Catch specific error type
            return "Error: Cannot divide by zero!"
        except TypeError:                       # Catch another specific error type
            return "Error: Invalid input types for division!"
        except Exception as e:                  # Catch any other unexpected error
            return f"An unexpected error occurred: {e}"

    print(f"10 / 2 = {divide_numbers(10, 2)}")
    # → 10 / 2 = 5.0
    print(f"5 / 0 = {divide_numbers(5, 0)}")
    # → 5 / 0 = Error: Cannot divide by zero!
    print(f"'hello' / 2 = {divide_numbers('hello', 2)}") # This will hit TypeError
    # → 'hello' / 2 = Error: Invalid input types for division!


# ═══════════════════════════════════════════════════════════════
# SECTION 5: Pythonic Idioms: The Right Way vs The Naive Way
# ═══════════════════════════════════════════════════════════════

def section_5_pythonic_idioms() -> None:
    """
    Demonstrates common Pythonic approaches for cleaner and more efficient code.
    """
    print("\nSECTION 5: Pythonic Idioms: The Right Way vs The Naive Way")
    print("--------------------------------------------------")

    #