"""
Dictionaries: Unlocking Key-Value Data Storage in Python

This script provides a comprehensive introduction to Python dictionaries,
a fundamental data structure for storing collections of key-value pairs.
You will learn how to create, manipulate, and effectively utilize dictionaries
for various programming tasks.

What you will learn:
•  How to define and initialize dictionaries using various syntaxes.
•  Methods for adding, updating, and deleting key-value pairs.
•  Techniques for accessing dictionary values safely and efficiently.
•  How to iterate over dictionary keys, values, and items.
•  Common pitfalls and best practices when working with dictionaries.
•  Pythonic idioms for concise and effective dictionary manipulation.

Prerequisites:
•  Basic understanding of Python variables and data types (strings, integers).
•  Familiarity with Python's conditional statements (if/else).
•  Knowledge of basic looping constructs (for loops).

Key Concepts Covered:
•  Key-Value Pairs
•  Mutable vs. Immutable Keys
•  Dictionary Creation (`{}` and `dict()`)
•  Accessing Values (`[]` and `get()`)
•  Adding and Updating Entries
•  Deleting Entries (`del` and `pop()`)
•  Checking for Key Existence (`in` operator)
•  Dictionary Methods (`keys()`, `values()`, `items()`, `update()`, `setdefault()`, `popitem()`)
•  Dictionary Comprehensions
•  Nested Dictionaries
•  Merging Dictionaries (`|` operator)
•  Hash Tables and Performance Characteristics
"""

import sys # Used for sys.getsizeof() in performance section
from typing import Any, Dict, List, Tuple, Union # Type hints for clarity

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: Absolute Fundamentals of Dictionaries
# ═══════════════════════════════════════════════════════════════

def section_1_core_concept() -> None:
    """
    Demonstrates the absolute fundamentals of Python dictionaries.
    Covers creation, basic access, modification, and key requirements.
    """
    print("\n--- SECTION 1: Core Concept ---")

    # 1.1 What is a Dictionary?
    # A dictionary is an unordered collection of key-value pairs.
    # Each key must be unique and immutable (like strings, numbers, tuples).
    # Values can be of any type and can be duplicated.

    # 1.2 Creating a Dictionary
    # Dictionaries are defined by enclosing a comma-separated list of key: value pairs
    # within curly braces `{}`.

    # Example 1: Basic dictionary creation
    student_profile: Dict[str, Union[str, int, List[str]]] = { # Declare dictionary with type hints
        "name": "Alice Smith",       # Key "name" maps to string value "Alice Smith"
        "age": 20,                   # Key "age" maps to integer value 20
        "major": "Computer Science", # Key "major" maps to string value
        "courses": ["Python 101", "Data Structures"] # Key "courses" maps to a list
    }
    print(f"\n1.2.1 Created student_profile: {student_profile}")
    # → 1.2.1 Created student_profile: {'name': 'Alice Smith', 'age': 20, 'major': 'Computer Science', 'courses': ['Python 101', 'Data Structures']}

    # Example 2: Empty dictionary creation
    empty_dict: Dict[str, Any] = {} # Initialize an empty dictionary
    print(f"1.2.2 Created empty_dict: {empty_dict}")
    # → 1.2.2 Created empty_dict: {}

    # 1.3 Accessing Values
    # Values are accessed using their corresponding keys inside square brackets `[]`.

    # Example 3: Accessing specific values
    student_name: str = student_profile["name"] # Access the value associated with the key "name"
    student_age: int = student_profile["age"]   # Access the value associated with the key "age"
    print(f"1.3.1 Student Name: {student_name}, Age: {student_age}")
    # → 1.3.1 Student Name: Alice Smith, Age: 20

    # ⚠️ Common mistake: Trying to access a non-existent key will raise a KeyError.
    # print(student_profile["address"]) # This line would cause a KeyError if uncommented

    # 1.4 Adding and Modifying Key-Value Pairs
    # You can add new key-value pairs or modify existing ones using the assignment operator `=`.

    # Example 4: Adding a new key-value pair
    student_profile["gpa"] = 3.85 # Add a new key "gpa" with value 3.85
    print(f"1.4.1 Added GPA: {student_profile}")
    # → 1.4.1 Added GPA: {'name': 'Alice Smith', 'age': 20, 'major': 'Computer Science', 'courses': ['Python 101', 'Data Structures'], 'gpa': 3.85}

    # Example 5: Modifying an existing value
    student_profile["age"] = 21 # Update the value for the key "age"
    print(f"1.4.2 Updated Age: {student_profile}")
    # → 1.4.2 Updated Age: {'name': 'Alice Smith', 'age': 21, 'major': 'Computer Science', 'courses': ['Python 101', 'Data Structures'], 'gpa': 3.85}

    # 1.5 Dictionary Length
    # The `len()` function returns the number of key-value pairs in a dictionary.

    # Example 6: Getting the length
    num_entries: int = len(student_profile) # Get the total number of entries
    print(f"1.5.1 Number of entries in student_profile: {num_entries}")
    # → 1.5.1 Number of entries in student_profile: 5

    # 1.6 Key Immutability
    # Dictionary keys must be immutable types (e.g., strings, numbers, tuples).
    # Mutable types like lists or other dictionaries cannot be used as keys.

    # 🐛 Bug source: Using a mutable type (list) as a key will raise a TypeError.
    # invalid_dict = { ["immutable", "key"]: "value" } # This would cause a TypeError if uncommented
    valid_key_types: Dict[Union[str, int, Tuple[str, ...]], str] = { # Keys can be strings, ints, or tuples
        "string_key": "works",      # String key
        123: "also works",          # Integer key
        (1, "tuple_key"): "perfect" # Tuple key (tuples are immutable)
    }
    print(f"1.6.1 Dictionary with valid key types: {valid_key_types}")
    # → 1.6.1 Dictionary with valid key types: {'string_key': 'works', 123: 'also works', (1, 'tuple_key'): 'perfect'}

# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns: Everyday Dictionary Usage
# ═══════════════════════════════════════════════════════════════

def section_2_syntax_common_patterns() -> None:
    """
    Explores common syntax for creating and manipulating dictionaries,
    including different creation methods and safe value access.
    """
    print("\n--- SECTION 2: Syntax & Common Patterns ---")

    # 2.1 Dictionary Creation Methods
    # Besides `{}` literal, `dict()` constructor offers other ways.

    # Example 1: Using `dict()` with keyword arguments
    # Useful when keys are simple strings and don't need quotes.
    user_settings: Dict[str, bool | str] = dict(theme="dark", notifications=True, language="en")
    print(f"\n2.1.1 User settings (keyword args): {user_settings}")
    # → 2.1.1 User settings (keyword args): {'theme': 'dark', 'notifications': True, 'language': 'en'}

    # Example 2: Using `dict()` with a list of key-value tuples
    # Useful when keys are not valid identifiers or are dynamic.
    product_prices: Dict[str, float] = dict([
        ("apple", 1.20),
        ("banana", 0.75),
        ("orange", 1.50)
    ])
    print(f"2.1.2 Product prices (list of tuples): {product_prices}")
    # → 2.1.2 Product prices (list of tuples): {'apple': 1.2, 'banana': 0.75, 'orange': 1.5}

    # 2.2 Safe Value Access with `.get()`
    # The `.get()` method is preferred for accessing values when a key might not exist.
    # It returns `None` by default if the key is not found, or a specified default value.

    # Example 3: Using `.get()` without a default
    fruit_price: float | None = product_prices.get("apple") # Key exists, returns value
    print(f"2.2.1 Price of apple: {fruit_price}")
    # → 2.2.1 Price of apple: 1.2

    non_existent_price: float | None = product_prices.get("grape") # Key doesn't exist, returns None
    print(f"2.2.2 Price of grape (default None): {non_existent_price}")
    # → 2.2.2 Price of grape (default None): None

    # Example 4: Using `.get()` with a custom default value
    grape_price_default: float = product_prices.get("grape", 0.00) # Key doesn't exist, returns 0.00
    print(f"2.2.3 Price of grape (custom default 0.00): {grape_price_default}")
    # → 2.2.3 Price of grape (custom default 0.00): 0.0

    # 2.3 Checking for Key Existence with `in`
    # The `in` operator efficiently checks if a key exists in a dictionary.

    # Example 5: Checking for key presence
    is_apple_in_prices: bool = "apple" in product_prices # Check if "apple" is a key
    is_mango_in_prices: bool = "mango" in product_prices # Check if "mango" is a key
    print(f"2.3.1 Is 'apple' in prices? {is_apple_in_prices}")
    # → 2.3.1 Is 'apple' in prices? True
    print(f"2.3.2 Is 'mango' in prices? {is_mango_in_prices}")
    # → 2.3.2 Is 'mango' in prices? False

    # 2.4 Deleting Key-Value Pairs
    # Two common ways to remove items: `del` statement and `.pop()` method.

    # Example 6: Using `del` to remove an item
    # `del` permanently removes the item. If the key doesn't exist, it raises a KeyError.
    print(f"\n2.4.1 Before del: {product_prices}")
    # → 2.4.1 Before del: {'apple': 1.2, 'banana': 0.75, 'orange': 1.5}
    del product_prices["orange"] # Remove the "orange" entry
    print(f"2.4.2 After del 'orange': {product_prices}")
    # → 2.4.2 After del 'orange': {'apple': 1.2, 'banana': 0.75}

    # Example 7: Using `.pop()` to remove and retrieve an item
    # `.pop()` removes the item and returns its value. It can also take a default value.
    banana_price: float = product_prices.pop("banana") # Remove "banana" and get its price
    print(f"2.4.3 Popped 'banana' price: {banana_price}")
    # → 2.4.3 Popped 'banana' price: 0.75
    print(f"2.4.4 After pop 'banana': {product_prices}")
    # → 2.4.4 After pop 'banana': {'apple': 1.2}

    # Trying to pop a non-existent key without a default will raise a KeyError
    # non_existent_pop = product_prices.pop("grape") # This would raise a KeyError

    # Using pop with a default value prevents KeyError
    non_existent_pop_default: float = product_prices.pop("grape", 0.0)
    print(f"2.4.5 Popped non-existent 'grape' with default: {non_existent_pop_default}")
    # → 2.4.5 Popped non-existent 'grape' with default: 0.0
    print(f"2.4.6 Dictionary after safe pop: {product_prices}")
    # → 2.4.6 Dictionary after safe pop: {'apple': 1.2}

    # 2.5 Clearing a Dictionary
    # The `.clear()` method removes all items from a dictionary.

    # Example 8: Clearing a dictionary
    product_prices.clear() # Remove all key-value pairs
    print(f"2.5.1 After clear: {product_prices}")
    # → 2.5.1 After clear: {}

# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas: What Beginners Always Get Wrong
# ═══════════════════════════════════════════════════════════════

def section_3_edge_cases_gotchas() -> None:
    """
    Highlights common mistakes and tricky aspects of dictionaries,
    such as key immutability, KeyError, and dictionary ordering.
    """
    print("\n--- SECTION 3: Edge Cases & Gotchas ---")

    # 3.1 Immutable Keys Requirement
    # Keys must be hashable (immutable). Lists are mutable and thus not hashable.

    # 🐛 Bug source: Using a list as a dictionary key will raise a TypeError.
    # my_dict = { [1, 2]: "value" } # Uncommenting this line causes: TypeError: unhashable type: 'list'
    # print(my_dict)

    # ✅ Preferred: Use immutable types like strings, numbers, or tuples as keys.
    valid_key_dict: Dict[Union[str, int, Tuple[int, int]], str] = {
        "name": "John",
        101: "ID",
        (1, 2): "Coordinates"
    }
    print(f"\n3.1.1 Valid keys (strings, ints, tuples): {valid_key_dict}")
    # → 3.1.1 Valid keys (strings, ints, tuples): {'name': 'John', 101: 'ID', (1, 2): 'Coordinates'}

    # 3.2 KeyError vs. `get()`
    # Accessing a non-existent key with `[]` raises a KeyError. `get()` handles it gracefully.

    data: Dict[str, int] = {"a": 1, "b": 2}
    print(f"3.2.1 Current dictionary: {data}")
    # → 3.2.1 Current dictionary: {'a': 1, 'b': 2}

    # ⚠️ Common mistake: Direct access without checking or using .get()
    try:
        value_c: int = data["c"] # This line will raise a KeyError
        print(f"Value of 'c': {value_c}") # This line will not be reached
    except KeyError as e:
        print(f"3.2.2 Caught expected KeyError: {e} when accessing 'c' directly.")
        # → 3.2.2 Caught expected KeyError: 'c' when accessing 'c' directly.

    # ✅ Preferred: Use `.get()` with a default value for safe access.
    value_c_safe: int = data.get("c", 0) # Returns 0 if "c" is not found
    print(f"3.2.3 Value of 'c' using .get() with default: {value_c_safe}")
    # → 3.2.3 Value of 'c' using .get() with default: 0

    # 3.3 Dictionary Order (Insertion Order)
    # 🔑 Key insight: Since Python 3.7, dictionaries maintain insertion order.
    # Before 3.7, they were unordered. Relying on order in older Python versions was a gotcha.

    ordered_dict: Dict[str, int] = {}
    ordered_dict["first"] = 1
    ordered_dict["second"] = 2
    ordered_dict["third"] = 3
    print(f"\n3.3.1 Dictionary maintains insertion order (Python 3.7+): {ordered_dict}")
    # → 3.3.1 Dictionary maintains insertion order (Python 3.7+): {'first': 1, 'second': 2, 'third': 3}

    # 3.4 Iterating Over a Dictionary While Modifying It
    # ⚠️ Common mistake: Modifying a dictionary (adding/deleting items) while iterating over it
    # can lead to a `RuntimeError` or unexpected behavior.

    # This loop attempts to modify the dictionary while iterating, which is unsafe.
    # It might work for some operations in some Python versions but is generally discouraged.
    # For safety, iterate over a copy or collect keys/items to modify later.
    sample_dict: Dict[str, int] = {"a": 1, "b": 2, "c": 3}
    print(f"\n3.4.1 Original dictionary: {sample_dict}")
    # → 3.4.1 Original dictionary: {'a': 1, 'b': 2, 'c': 3}

    # 🐛 Bug source: Directly modifying while iterating
    # try:
    #     for key in sample_dict:
    #         if key == "b":
    #             del sample_dict[key] # This might raise RuntimeError: dictionary changed size during iteration
    #         if key == "d":
    #             sample_dict["d"] = 4 # Or lead to unexpected behavior
    # except RuntimeError as e:
    #     print(f"3.4.2 Caught expected RuntimeError: {e}")

    # ✅ Preferred: Iterate over a copy of the keys or items.
    # This allows modifications to the original dictionary without issues.
    for key in list(sample_dict.keys()): # Iterate over a copy of keys
        if key == "b":
            del sample_dict[key] # Safely delete "b"
        elif key == "c":
            sample_dict["d"] = sample_dict[key] * 2 # Safely add a new key "d" based on "c"
            del sample_dict[key] # Safely delete "c"
    print(f"3.4.3 Modified dictionary safely: {sample_dict}")
    # → 3.4.3 Modified dictionary safely: {'a': 1, 'd': 6}

# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns: One Level Up From Basics
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """
    Introduces more advanced dictionary operations like iteration methods,
    dictionary comprehensions, and nested dictionaries.
    """
    print("\n--- SECTION 4: Intermediate Patterns ---")

    # 4.1 Iterating Over Dictionaries
    # Dictionaries provide methods to iterate over keys, values, or key-value pairs.

    inventory: Dict[str, int] = {"apples": 50, "bananas": 100, "oranges": 75}
    print(f"\n4.1.1 Current inventory: {inventory}")
    # → 4.1.1 Current inventory: {'apples': 50, 'bananas': 100, 'oranges': 75}

    # Example 1: Iterate over keys (default behavior)
    print("4.1.2 Iterating keys:")
    for item_name in inventory: # By default, iterating a dict iterates its keys
        print(f"  Item: {item_name}")
        # →   Item: apples
        # →   Item: bananas
        # →   Item: oranges

    # Example 2: Iterate over values
    print("4.1.3 Iterating values:")
    for quantity in inventory.values(): # .values() returns a view of the dictionary's values
        print(f"  Quantity: {quantity}")
        # →   Quantity: 50
        # →   Quantity: 100
        # →   Quantity: 75

    # Example 3: Iterate over key-value pairs (items)
    print("4.1.4 Iterating items:")
    for item_name, quantity in inventory.items(): # .items() returns a view of (key, value) tuples
        print(f"  {item_name}: {quantity} units")
        # →   apples: 50 units
        # →   bananas: 100 units
        # →   oranges: 75 units

    # 4.2 Dictionary Comprehensions
    # A concise way to create dictionaries from iterables, similar to list comprehensions.

    # Example 4: Creating a dictionary from a list, squaring numbers
    numbers: List[int] = [1, 2, 3, 4]
    squared_dict: Dict[int, int] = {num: num**2 for num in numbers} # Key is num, value is num squared
    print(f"\n4.2.1 Squared numbers dict: {squared_dict}")
    # → 4.2.1 Squared numbers dict: {1: 1, 2: 4, 3: 9, 4: 16}

    # Example 5: Creating a dictionary from an existing dictionary, with filtering/transformation
    stock_levels: Dict[str, int] = {"pens": 200, "notebooks": 50, "erasers": 10, "staplers": 5}
    low_stock_alerts: Dict[str, int] = {
        item: level for item, level in stock_levels.items() if level < 100 # Filter for items with level < 100
    }
    print(f"4.2.2 Low stock alerts: {low_stock_alerts}")
    # → 4.2.2 Low stock alerts: {'notebooks': 50, 'erasers': 10, 'staplers': 5}

    # 4.3 Nested Dictionaries
    # Dictionaries can contain other dictionaries (or lists, tuples, etc.) as values.

    # Example 6: Representing complex data with nested dictionaries
    user_data: Dict[str, Dict[str, Union[str, int, List[str]]]] = { # Type hint for nested dict
        "john_doe": {
            "name": "John Doe",
            "age": 30,
            "email": "john.doe@example.com",
            "roles": ["admin", "editor"]
        },
        "jane_smith": {
            "name": "Jane Smith",
            "age": 25,
            "email": "jane.smith@example.com",
            "roles": ["viewer"]
        }
    }
    print(f"\n4.3.1 Nested user data: {user_data}")
    # → 4.3.1 Nested user data: {'john_doe': {'name': 'John Doe', 'age': 30, 'email': 'john.doe@example.com', 'roles': ['admin', 'editor']}, 'jane_smith': {'name': 'Jane Smith', 'age': 25, 'email': 'jane.smith@example.com', 'roles': ['viewer']}}

    # Accessing values in a nested dictionary
    johns_email: str = user_data["john_doe"]["email"] # Access email for "john_doe"
    jane_roles: List[str] = user_data["jane_smith"]["roles"] # Access roles for "jane_smith"
    print(f"4.3.2 John's Email: {johns_email}")
    # → 4.3.2 John's Email: john.doe@example.com
    print(f"4.3.3 Jane's Roles: {jane_roles}")
    # → 4.3.3 Jane's Roles: ['viewer']

# ═══════════════════════════════════════════════════════════════
# SECTION 5: Pythonic Idioms: The Right Way vs The Naive Way
# ═══════════════════════════════════════════════════════════════

def section_5_pythonic_idioms() -> None:
    """
    Showcases Pythonic approaches to common dictionary tasks,
    emphasizing readability, efficiency, and idiomatic usage.
    """
    print("\n--- SECTION 5: Pythonic Idioms ---")

    # 5.1 Conditional Assignment / Default Values
    # How to add a key-value pair only if the key doesn't already exist.

    user_preferences: Dict[str, Union[str, bool]] = {"theme": "light", "notifications": True}
    print(f"\n5.1.1 Initial preferences: {user_preferences}")
    # → 5.1.1 Initial preferences: {'theme': 'light', 'notifications': True}

    # ⚠️ Naive way: Check with `in` then assign
    # if "language" not in user_preferences:
    #     user_preferences["language"] = "en-US"
    # print(f"Naive add language: {user_preferences}")

    # ✅ Pythonic way: Use `.setdefault()`
    # `setdefault()` returns the value for key if key is in the dictionary, else inserts key
    # with a value of default and returns default.
    language_setting: str = user_preferences.setdefault("language", "en-US") # "language" not present, adds it
    print(f"5.1.2 Set 'language' with setdefault (new): {user_preferences} -> returned '{language_setting}'")
    # → 5.1.2 Set 'language' with setdefault (new): {'theme': 'light', 'notifications': True, 'language': 'en-US'} -> returned 'en-US'

    theme_setting: str = user_preferences.setdefault("theme", "dark") # "theme" is present, returns existing value
    print(f"5.1.3 Set 'theme' with setdefault (exists): {user_preferences} -> returned '{theme_setting}'")
    # → 5.1.3 Set 'theme' with setdefault (exists): {'theme': 'light', 'notifications': True, 'language': 'en-US'} -> returned 'light'

    # 5.2 Merging Dictionaries
    # Combining two or more dictionaries.

    dict1: Dict[str, int] = {"a": 1, "b": 2}
    dict2: Dict[str, int] = {"b": 3, "c": 4}
    print(f"\n5.2.1 dict1: {dict1}, dict2: {dict2}")
    # → 5.2.1 dict1: {'a': 1, 'b': 2}, dict2: {'b': 3, 'c': 4}

    # ⚠️ Naive way: Loop and update
    # merged_naive = dict1.copy()
    # for key, value in dict2.items():
    #     merged_naive[key] = value
    # print(f"Naive merge: {merged_naive}")

    # ✅ Pythonic way (Python 3.9+): Using the dictionary union operator `|`
    # The `|` operator creates a new dictionary. If keys overlap, the right-hand dictionary's value wins.
    merged_pythonic_union: Dict[str, int] = dict1 | dict2
    print(f"5.2.2 Pythonic merge (union operator): {merged_pythonic_union}")
    # → 5.2.2 Pythonic merge (union operator): {'a': 1, 'b': 3, 'c':