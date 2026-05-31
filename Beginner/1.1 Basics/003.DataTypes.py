"""
Data Types: Understanding the Building Blocks of Python
This module introduces the fundamental data types in Python, explaining their purpose, usage, and key characteristics. Mastering data types is crucial for writing effective and efficient Python code.

What you will learn:
*   Identify and use Python's core primitive data types (integers, floats, strings, booleans, None).
*   Work with common collection data types (lists, tuples, sets, dictionaries).
*   Understand the concepts of mutability and immutability in Python.
*   Navigate common pitfalls related to type conversion, comparison, and identity.
*   Apply Pythonic idioms for efficient data manipulation using built-in structures.
*   Consider performance and memory implications when choosing data types for larger applications.

Prerequisites:
*   Basic understanding of variables and assignment in Python.
*   Familiarity with executing Python scripts from the command line.

Key Concepts Covered:
*   Primitive Data Types: int, float, str, bool, NoneType
*   Collection Data Types: list, tuple, set, dict
*   Mutability vs. Immutability
*   Type Conversion (Casting)
*   Identity vs. Equality (is vs. ==)
*   Truthiness
*   Type Hinting
*   List, Set, and Dictionary Comprehensions
*   Unpacking, zip(), enumerate()
*   Memory Usage (sys.getsizeof)
*   Class Definition for Data Encapsulation
"""

import sys  # Required for sys.getsizeof to inspect memory usage
from typing import Any, Union, List, Dict, Tuple, Set # For type hinting

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: Fundamental Data Types
# ═══════════════════════════════════════════════════════════════

def demonstrate_primitive_types() -> None:
    """
    Illustrates Python's core primitive data types:
    integers, floats, strings, booleans, and NoneType.
    """
    print("SECTION 1: Core Concept: Fundamental Data Types")
    print("-" * 50)

    # 🔑 Key insight: Python is dynamically typed, but values have types.
    # The `type()` function reveals the type of a variable's value.

    # 1. Integers (int): Whole numbers
    integer_number: int = 100               # Define an integer variable
    print(f"Integer: {integer_number}, Type: {type(integer_number)}")
    # → Integer: 100, Type: <class 'int'>

    # 2. Floating-Point Numbers (float): Numbers with decimal points
    floating_number: float = 3.14159        # Define a float variable
    print(f"Float: {floating_number}, Type: {type(floating_number)}")
    # → Float: 3.14159, Type: <class 'float'>
    scientific_notation: float = 1.23e-5    # Floats can also be in scientific notation
    print(f"Scientific Float: {scientific_notation}, Type: {type(scientific_notation)}")
    # → Scientific Float: 1.23e-05, Type: <class 'float'>

    # 3. Strings (str): Sequences of characters
    single_quote_string: str = 'Hello Python!' # Strings can use single quotes
    double_quote_string: str = "Learning Data Types" # Or double quotes
    triple_quote_string: str = """This is a
multi-line string.""" # Triple quotes for multi-line strings
    print(f"String 1: '{single_quote_string}', Type: {type(single_quote_string)}")
    # → String 1: 'Hello Python!', Type: <class 'str'>
    print(f"String 2: '{double_quote_string}', Type: {type(double_quote_string)}")
    # → String 2: 'Learning Data Types', Type: <class 'str'>
    print(f"String 3:\n{triple_quote_string}\nType: {type(triple_quote_string)}")
    # → String 3:
    # → This is a
    # → multi-line string.
    # → Type: <class 'str'>

    # 4. Booleans (bool): Represent truth values (True or False)
    is_active: bool = True                  # Boolean variable set to True
    has_permission: bool = False            # Boolean variable set to False
    print(f"Boolean 1: {is_active}, Type: {type(is_active)}")
    # → Boolean 1: True, Type: <class 'bool'>
    print(f"Boolean 2: {has_permission}, Type: {type(has_permission)}")
    # → Boolean 2: False, Type: <class 'bool'>

    # 5. NoneType (None): Represents the absence of a value
    no_value: None = None                   # A variable explicitly holding no value
    print(f"None Value: {no_value}, Type: {type(no_value)}")
    # → None Value: None, Type: <class 'NoneType'>

    # Example of type checking
    # We can use `isinstance()` to check if an object is an instance of a particular type.
    if isinstance(integer_number, int):     # Check if integer_number is an integer
        print(f"'{integer_number}' is indeed an integer.")
        # → '100' is indeed an integer.

    if not isinstance(single_quote_string, float): # Check if string is NOT a float
        print(f"'{single_quote_string}' is not a float.")
        # → 'Hello Python!' is not a float.

# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns: Collections and Immutability
# ═══════════════════════════════════════════════════════════════

def demonstrate_collections_and_mutability() -> None:
    """
    Explores Python's fundamental collection data types (list, tuple, set, dict)
    and introduces the concept of mutability vs. immutability.
    """
    print("\nSECTION 2: Syntax & Common Patterns: Collections and Immutability")
    print("-" * 50)

    # 🔑 Key insight: Collections group multiple items. Some are mutable (changeable), some are immutable.

    # 1. Lists (list): Ordered, mutable collection of items. Allows duplicates.
    shopping_list: List[str] = ["Apples", "Milk", "Bread", "Apples"] # Define a list with some duplicates
    print(f"Initial shopping list: {shopping_list}, Type: {type(shopping_list)}")
    # → Initial shopping list: ['Apples', 'Milk', 'Bread', 'Apples'], Type: <class 'list'>

    # List operations
    shopping_list.append("Eggs")            # Add an item to the end of the list
    print(f"After appending 'Eggs': {shopping_list}")
    # → After appending 'Eggs': ['Apples', 'Milk', 'Bread', 'Apples', 'Eggs']
    shopping_list.remove("Apples")          # Remove the first occurrence of 'Apples'
    print(f"After removing 'Apples': {shopping_list}")
    # → After removing 'Apples': ['Milk', 'Bread', 'Apples', 'Eggs']
    print(f"First item: {shopping_list[0]}") # Access item by index (0-based)
    # → First item: Milk
    print(f"Last item: {shopping_list[-1]}") # Access last item using negative index
    # → Last item: Eggs
    print(f"Slice (1st to 3rd): {shopping_list[0:3]}") # Slicing creates a new list
    # → Slice (1st to 3rd): ['Milk', 'Bread', 'Apples']

    # 2. Tuples (tuple): Ordered, immutable collection of items. Allows duplicates.
    coordinates: Tuple[int, int] = (10, 20) # Define a tuple
    rgb_color: Tuple[int, int, int] = (255, 0, 128) # Another tuple example
    print(f"Coordinates: {coordinates}, Type: {type(coordinates)}")
    # → Coordinates: (10, 20), Type: <class 'tuple'>

    # Tuple operations
    print(f"First coordinate: {coordinates[0]}") # Access item by index
    # → First coordinate: 10
    # ⚠️ Common mistake: Trying to modify an immutable tuple
    # coordinates[0] = 50 # This line would raise a TypeError
    # print(f"Attempted to change tuple: {coordinates}")
    print("Tuples are immutable, cannot change items after creation.")

    # 3. Sets (set): Unordered, mutable collection of *unique* items.
    unique_numbers: Set[int] = {1, 2, 3, 2, 4} # Define a set; duplicates are automatically removed
    print(f"Initial unique numbers: {unique_numbers}, Type: {type(unique_numbers)}")
    # → Initial unique numbers: {1, 2, 3, 4}, Type: <class 'set'> (Order might vary)

    # Set operations
    unique_numbers.add(5)                   # Add a new item
    unique_numbers.add(3)                   # Adding an existing item has no effect
    print(f"After adding 5 and 3: {unique_numbers}")
    # → After adding 5 and 3: {1, 2, 3, 4, 5}
    unique_numbers.remove(2)                # Remove an item
    print(f"After removing 2: {unique_numbers}")
    # → After removing 2: {1, 3, 4, 5}
    print(f"Is 4 in set? {4 in unique_numbers}") # Check for membership efficiently
    # → Is 4 in set? True

    # 4. Dictionaries (dict): Unordered, mutable collection of key-value pairs. Keys must be unique and immutable.
    user_profile: Dict[str, Any] = {        # Define a dictionary
        "name": "Alice",
        "age": 30,
        "is_active": True
    }
    print(f"User profile: {user_profile}, Type: {type(user_profile)}")
    # → User profile: {'name': 'Alice', 'age': 30, 'is_active': True}, Type: <class 'dict'>

    # Dictionary operations
    print(f"User's name: {user_profile['name']}") # Access value by key
    # → User's name: Alice
    user_profile["age"] = 31                # Update an existing value
    user_profile["city"] = "New York"       # Add a new key-value pair
    print(f"Updated user profile: {user_profile}")
    # → Updated user profile: {'name': 'Alice', 'age': 31, 'is_active': True, 'city': 'New York'}
    user_profile.pop("is_active")           # Remove a key-value pair
    print(f"Profile after removing 'is_active': {user_profile}")
    # → Profile after removing 'is_active': {'name': 'Alice', 'age': 31, 'city': 'New York'}
    print(f"All keys: {user_profile.keys()}") # Get all keys
    # → All keys: dict_keys(['name', 'age', 'city'])
    print(f"All values: {user_profile.values()}") # Get all values
    # → All values: dict_values(['Alice', 31, 'New York'])

# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas: Type Coercion, Comparison, and Identity
# ═══════════════════════════════════════════════════════════════

def demonstrate_type_gotchas() -> None:
    """
    Highlights common pitfalls related to type conversion, object identity,
    and truthiness in Python.
    """
    print("\nSECTION 3: Edge Cases & Gotchas: Type Coercion, Comparison, and Identity")
    print("-" * 50)

    # 1. Type Conversion (Casting)
    # Python allows explicit conversion between certain types.
    string_number: str = "123"              # A string that looks like a number
    integer_value: int = int(string_number) # Convert string to integer
    print(f"String '{string_number}' converted to int: {integer_value}, Type: {type(integer_value)}")
    # → String '123' converted to int: 123, Type: <class 'int'>

    float_value: float = float(integer_value) # Convert integer to float
    print(f"Int {integer_value} converted to float: {float_value}, Type: {type(float_value)}")
    # → Int 123 converted to float: 123.0, Type: <class 'float'>

    # ⚠️ Common mistake: Trying to convert non-numeric string to number
    # non_numeric_string = "hello"
    # invalid_int = int(non_numeric_string) # This would raise a ValueError
    # print(invalid_int)
    print("Cannot convert 'hello' to an integer; it would cause a ValueError.")

    # Convert numbers to strings
    converted_string: str = str(123.45)     # Convert float to string
    print(f"Float 123.45 converted to string: '{converted_string}', Type: {type(converted_string)}")
    # → Float 123.45 converted to string: '123.45', Type: <class 'str'>

    # 2. Identity (is) vs. Equality (==)
    # `==` checks if values are equal. `is` checks if two variables refer to the *exact same object* in memory.
    list_a: List[int] = [1, 2, 3]           # Define list_a
    list_b: List[int] = [1, 2, 3]           # Define list_b with same values
    list_c: List[int] = list_a              # list_c refers to the same object as list_a

    print(f"list_a == list_b: {list_a == list_b}") # Values are equal
    # → list_a == list_b: True
    print(f"list_a is list_b: {list_a is list_b}") # Different objects in memory
    # → list_a is list_b: False
    print(f"list_a is list_c: {list_a is list_c}") # Same object in memory
    # → list_a is list_c: True

    # Immutables (like small integers and strings) might sometimes share objects for optimization.
    # But generally, `is` should be used for identity, not value equality.
    int_x: int = 100                        # Define int_x
    int_y: int = 100                        # Define int_y
    print(f"int_x == int_y: {int_x == int_y}") # Values are equal
    # → int_x == int_y: True
    print(f"int_x is int_y: {int_x is int_y}") # Often True for small integers due to interning
    # → int_x is int_y: True (May vary for larger numbers or different Python versions/implementations)

    # 3. Truthiness
    # In conditional contexts (e.g., `if` statements), many non-boolean values are treated as `True` or `False`.
    # Falsy values: `None`, `False`, `0` (int), `0.0` (float), `""` (empty string), `[]` (empty list),
    # `{}` (empty dict), `set()` (empty set). All others are truthy.
    if 0:                                   # 0 is falsy
        print("0 is truthy")
    else:
        print("0 is falsy")
        # → 0 is falsy

    if "hello":                             # Non-empty string is truthy
        print("'hello' is truthy")
        # → 'hello' is truthy

    empty_list: List[Any] = []              # Empty list is falsy
    if empty_list:
        print("Empty list is truthy")
    else:
        print("Empty list is falsy")
        # → Empty list is falsy

    # 🐛 Bug source: Accidentally using `is` instead of `==` for comparisons.
    # 🐛 Bug source: Relying on object identity for values that might be interned or optimized.

# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns: Advanced Collections and Type Hinting
# ═══════════════════════════════════════════════════════════════

def process_student_grades(student_data: Dict[str, Union[int, float, List[int]]]) -> Dict[str, Union[int, float]]:
    """
    Processes student data to calculate average grade and categorize by status.
    Demonstrates nested dictionaries and type hinting with Union.

    Args:
        student_data: A dictionary containing student information.
                      Expected keys: 'id' (int), 'name' (str), 'grades' (List[int]).

    Returns:
        A dictionary with processed student information: 'id', 'name', 'average_grade'.
    """
    print("\nSECTION 4: Intermediate Patterns: Advanced Collections and Type Hinting")
    print("-" * 50)

    # 1. Nested Collections
    # Collections can contain other collections, allowing complex data structures.
    all_students_grades: Dict[str, Dict[str, Union[int, str, List[int]]]] = {
        "s001": {"id": 1, "name": "Alice", "grades": [85, 90, 78]},
        "s002": {"id": 2, "name": "Bob", "grades": [70, 65, 72]},
        "s003": {"id": 3, "name": "Charlie", "grades": [92, 88, 95]}
    }
    print(f"All students' raw data: {all_students_grades}")
    # → All students' raw data: {'s001': {'id': 1, 'name': 'Alice', 'grades': [85, 90, 78]}, ...}

    # Accessing nested data
    alice_grades: List[int] = all_students_grades["s001"]["grades"] # Access Alice's grades
    print(f"Alice's grades: {alice_grades}")
    # → Alice's grades: [85, 90, 78]

    # 2. Type Hinting with Union (Python 3.10+ syntax)
    # `Union[Type1, Type2]` indicates a variable can be one of several types.
    # This function uses type hints to improve readability and catch errors early.

    # Calculate average grade for the given student data
    grades = student_data["grades"]         # Extract the list of grades
    if not grades:                          # Handle case of empty grades list
        average_grade: float = 0.0          # Default to 0 if no grades
    else:
        average_grade = sum(grades) / len(grades) # Calculate average

    # ℹ️ Note: Dictionary values can be of mixed types, hence `Union` is useful for type hints.
    processed_student: Dict[str, Union[int, float]] = {
        "id": student_data["id"],           # Student ID
        "average_grade": round(average_grade, 2) # Rounded average grade
    }
    print(f"Processed student data for ID {student_data['id']}: {processed_student}")
    # → Processed student data for ID 1: {'id': 1, 'average_grade': 84.33} (for Alice)

    # Example usage of the function
    print("\nProcessing individual student data:")
    alice_data = all_students_grades["s001"] # Get Alice's full data
    processed_alice = process_student_grades(alice_data) # Process it
    print(f"Processed Alice: {processed_alice}")
    # → Processed Alice: {'id': 1, 'average_grade': 84.33}

    bob_data = all_students_grades["s002"] # Get Bob's full data
    processed_bob = process_student_grades(bob_data) # Process it
    print(f"Processed Bob: {processed_bob}")
    # → Processed Bob: {'id': 2, 'average_grade': 69.0}

    # When to choose between collections:
    # - List: Ordered, mutable, allows duplicates. Good for sequences.
    # - Tuple: Ordered, immutable, allows duplicates. Good for fixed collections (e.g., coordinates, record).
    # - Set: Unordered, mutable, *no duplicates*. Good for membership testing, removing duplicates, math operations (union, intersection).
    # - Dict: Unordered (since Python 3.7 insertion-ordered), mutable, key-value pairs. Good for mapping data.

    # Example demonstrating set for uniqueness
    data_points: List[float] = [1.1, 2.2, 1.1, 3.3, 2.2] # List with duplicates
    unique_data_points: Set[float] = set(data_points) # Convert to set to get unique items
    print(f"\nOriginal data points: {data_points}")
    # → Original data points: [1.1, 2.2, 1.1, 3.3, 2.2]
    print(f"Unique data points (using set): {unique_data_points}")
    # → Unique data points (using set): {3.3, 1.1, 2.2} (Order may vary)

    return processed_student # Return one example for type hint consistency

# ═══════════════════════════════════════════════════════════════
# SECTION 5: Pythonic Idioms: Leveraging Data Structures Effectively
# ═══════════════════════════════════════════════════════════════

def demonstrate_pythonic_data_usage() -> None:
    """
    Showcases Pythonic ways to work with data structures using comprehensions,
    unpacking, zip(), and enumerate().
    """
    print("\nSECTION 5: Pythonic Idioms: Leveraging Data Structures Effectively")
    print("-" * 50)

    # 1. List Comprehensions: Concise way to create lists
    numbers: List[int] = [1, 2, 3, 4, 5]    # Original list
    # ❌ Not Pythonic: Loop and append
    # squared_numbers = []
    # for num in numbers:
    #     squared_numbers.append(num * num)
    # print(squared_numbers)

    # ✅ Preferred/Pythonic: List comprehension
    squared_numbers: List[int] = [num * num for num in numbers] # Square each number
    print(f"Original numbers: {numbers}")
    # → Original numbers: [1, 2, 3, 4, 5]
    print(f"Squared numbers (list comprehension): {squared_numbers}")
    # → Squared numbers (list comprehension): [1, 4, 9, 16, 25]

    even_numbers: List[int] = [num for num in numbers if num % 2 == 0] # Filter even numbers
    print(f"Even numbers (list comprehension with condition): {even_numbers}")
    # → Even numbers (list comprehension with condition): [2, 4]

    # 2. Dictionary Comprehensions: Concise way to create dictionaries
    # Create a dictionary mapping numbers to their cubes
    cubed_dict: Dict[int, int] = {num: num ** 3 for num in numbers}
    print(f"Numbers to cubes (dict comprehension): {cubed_dict}")
    # → Numbers to cubes (dict comprehension): {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

    # 3. Set Comprehensions: Concise way to create sets
    # Create a set of unique characters from a string
    sample_text: str = "hello world"        # Sample string
    unique_chars: Set[str] = {char for char in sample_text if char.isalpha()} # Get unique alpha chars
    print(f"Unique alpha characters from '{sample_text}': {unique_chars}")
    # → Unique alpha characters from 'hello world': {'e', 'l', 'd', 'r', 'o', 'h', 'w'} (Order varies)

    # 4. Unpacking: Assigning elements of an iterable to multiple variables
    # Tuple unpacking
    point: Tuple[int, int] = (10, 20)       # A tuple representing a point
    x_coord, y_coord = point                # Unpack tuple into x_coord and y_coord
    print(f"Unpacked point: x={x_coord}, y={y_coord}")
    # → Unpacked point: x=10, y=20

    # List unpacking (can also use `*` for remaining elements)
    data_list: List[int] = [1, 2, 3, 4, 5]  # A list of data
    first, *middle, last = data_list        # Unpack first, last, and remaining into middle
    print(f"Unpacked list: first={first}, middle={middle}, last={last}")
    # → Unpacked list: first=1, middle=[2, 3, 4], last=5

    # 5. `zip()`: Combining multiple iterables
    names: List[str] = ["Alice", "Bob", "Charlie"] # List of names
    scores: List[int] = [95, 88, 72]        # List of scores
    # Combine names and scores into a list of (name, score) tuples
    name_score_pairs: List[Tuple[str, int]] = list(zip(names, scores))
    print(f"Name-score pairs (using zip): {name_score_pairs}")
    # → Name-score pairs (using zip): [('Alice', 95), ('Bob', 88), ('Charlie', 72)]

    # 6. `enumerate()`: Getting index and value during iteration
    # Iterate through a list and print both index and value
    print("\nIterating with enumerate:")
    for index, item in enumerate(name_score_pairs): # Iterate over the combined list
        print(f"Index {index}: {item}")
        # → Index 0: ('Alice', 95)
        # → Index 1: ('Bob', 88)
        # → Index 2: ('Charlie', 72)

# ═══════════════════════════════════════════════════════════════
# SECTION 6: Real-World Mini-Program: Simple Inventory Management
# ═══════════════════════════════════════════════════════════════

class InventoryItem:
    """
    Represents an item in an inventory system.
    Demonstrates class definition and attribute usage with type hints.
    """
    def __init__(self, item_id: str, name: str, quantity: int, price: float) -> None:
        """
        Initializes an InventoryItem.
        """
        if not isinstance(item_id, str) or not item_id:
            raise ValueError("Item ID must be a non-empty string.")
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")

        self.item_id: str = item_id         # Unique identifier for the item
        self.name: str = name               # Name of the item
        self.quantity: int = quantity       # Number of items in stock
        self.price: float = price           # Price per unit

    def get_total_value(self) -> float:
        """
        Calculates the total monetary value of this item in inventory.
        """
        return self.quantity * self.price   # Multiply quantity by price

    def update_quantity(self, change: int) -> None:
        """
        Updates the quantity of the item. 'change' can be positive (add) or negative (remove).
        Raises ValueError if quantity would become negative.
        """
        if self.quantity + change < 0:
            raise ValueError(f"Cannot reduce quantity below zero for item '{self.name}'.")
        self.quantity += change             # Apply the change to quantity
        print(f"Updated '{self.name}'. New quantity: {self.quantity}")
        # Example output: Updated 'Laptop'. New quantity: 18

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the InventoryItem.
        """
        return f"Item ID: {self.item_id}, Name: {self.name}, Qty: {self.quantity}, Price: ${self.price:.2f}"

def run_inventory_management() -> None:
    """
    A mini-program demonstrating inventory management using the Inventory