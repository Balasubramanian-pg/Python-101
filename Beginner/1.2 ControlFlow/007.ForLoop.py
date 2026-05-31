"""For Loop

This script introduces the fundamental concept of the 'for' loop in Python, demonstrating how to iterate over various data structures. It covers basic syntax, common patterns, potential pitfalls, and Pythonic approaches to repetitive tasks.

What you will learn:
* How to use a `for` loop to iterate over sequences like lists, tuples, and strings.
* The utility of the `range()` function for generating sequences of numbers.
* How to access both index and value simultaneously using `enumerate()`.
* How to iterate over multiple sequences in parallel using `zip()`.
* Best practices for iterating over dictionaries and avoiding common errors.
* Advanced loop control with `break`, `continue`, and the `else` clause.
* An introduction to generator functions for memory-efficient iteration.

Prerequisites:
* Basic understanding of Python data types (integers, strings, lists, tuples, dictionaries).
* Familiarity with variable assignment and basic operators.

Key Concepts Covered:
* Iteration
* Sequences (lists, tuples, strings, dictionaries, sets)
* `range()` function
* `enumerate()` function
* `zip()` function
* `break` statement
* `continue` statement
* `for-else` block
* Nested loops
* Generator functions
* List comprehensions (briefly)
* `all()` and `any()` functions
* `reversed()` and `sorted()` functions
* Time complexity (basic)
* Memory efficiency (basic)
"""

import time # Used for basic performance measurement in Section 7
from typing import Iterator, Any, List, Tuple, Dict, Set # Type hints for clarity and robustness

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: Iterating Over Sequences
# ═══════════════════════════════════════════════════════════════

def section_1_core_concept() -> None:
    """
    Demonstrates the absolute fundamentals of the for loop,
    iterating over basic sequence types.
    """
    print("SECTION 1: Core Concept: Iterating Over Sequences\n")

    # WHY: Loops are essential for repeating tasks without writing redundant code.
    #      A `for` loop iterates over items of any sequence (list, tuple, string, etc.)
    #      or other iterable objects.

    # Example 1.1: Iterating over a list of strings
    fruits: List[str] = ["apple", "banana", "cherry"] # Define a list of fruits
    print(f"Iterating over fruits: {fruits}")
    # → Iterating over fruits: ['apple', 'banana', 'cherry']
    for fruit in fruits: # Loop through each item in the 'fruits' list
        print(f"  I love {fruit}s!") # Print a message for each fruit
    # →   I love apples!
    # →   I love bananas!
    # →   I love cherrys!
    print("-" * 30)

    # Example 1.2: Iterating over a tuple of numbers
    numbers: Tuple[int, ...] = (10, 20, 30, 40) # Define a tuple of numbers
    total_sum: int = 0 # Initialize a variable to store the sum
    print(f"Calculating sum of numbers: {numbers}")
    # → Calculating sum of numbers: (10, 20, 30, 40)
    for num in numbers: # Loop through each number in the tuple
        total_sum += num # Add the current number to total_sum
    print(f"  The sum is: {total_sum}") # Print the final sum
    # →   The sum is: 100
    print("-" * 30)

    # Example 1.3: Iterating over a string (which is a sequence of characters)
    word: str = "Python" # Define a string
    print(f"Iterating over word: '{word}'")
    # → Iterating over word: 'Python'
    for char in word: # Loop through each character in the string
        print(f"  Character: {char}") # Print each character
    # →   Character: P
    # →   Character: y
    # →   Character: t
    # →   Character: h
    # →   Character: o
    # →   Character: n
    print("-" * 30)

    # Example 1.4: Using `range()` for a fixed number of iterations
    # WHY: `range()` generates a sequence of numbers, commonly used for loops
    #      when you need to repeat an action a specific number of times.
    print("Using range() for 3 iterations:")
    # → Using range() for 3 iterations:
    for i in range(3): # Loop 3 times (0, 1, 2)
        print(f"  Iteration number: {i + 1}") # Print the current iteration number (starting from 1)
    # →   Iteration number: 1
    # →   Iteration number: 2
    # →   Iteration number: 3
    print("-" * 30)

    # 🔑 Key insight: The `for` loop works with any "iterable" object.
    #    It fetches one item at a time until no more items are left.


# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns: `range()`, `enumerate()`, `zip()`
# ═══════════════════════════════════════════════════════════════

def section_2_syntax_common_patterns() -> None:
    """
    Explores common and powerful patterns for using for loops,
    including `range()`, `enumerate()`, and `zip()`.
    """
    print("SECTION 2: Syntax & Common Patterns: `range()`, `enumerate()`, `zip()`\n")

    # Example 2.1: `range()` with start, stop, and step
    # WHY: `range()` is versatile. `range(stop)` starts from 0.
    #      `range(start, stop)` starts from `start`.
    #      `range(start, stop, step)` increments by `step`.
    print("Counting from 5 to 9 (exclusive):")
    # → Counting from 5 to 9 (exclusive):
    for i in range(5, 10): # Loop from 5 up to (but not including) 10
        print(f"  Number: {i}") # Print each number
    # →   Number: 5
    # →   Number: 6
    # →   Number: 7
    # →   Number: 8
    # →   Number: 9
    print("-" * 30)

    print("Counting down from 10 to 1 (inclusive) with step -2:")
    # → Counting down from 10 to 1 (inclusive) with step -2:
    for i in range(10, 0, -2): # Loop from 10 down to (but not including) 0, decrementing by 2
        print(f"  Countdown: {i}") # Print each number
    # →   Countdown: 10
    # →   Countdown: 8
    # →   Countdown: 6
    # →   Countdown: 4
    # →   Countdown: 2
    print("-" * 30)

    # Example 2.2: `enumerate()` for index and value
    # WHY: When you need both the item's value AND its position (index) in a sequence,
    #      `enumerate()` is the Pythonic way.
    groceries: List[str] = ["milk", "bread", "eggs", "butter"] # List of groceries
    print(f"Grocery list: {groceries}")
    # → Grocery list: ['milk', 'bread', 'eggs', 'butter']
    for index, item in enumerate(groceries): # Loop with index and item value
        print(f"  Item {index + 1}: {item}") # Print item number (starting from 1) and item
    # →   Item 1: milk
    # →   Item 2: bread
    # →   Item 3: eggs
    # →   Item 4: butter
    print("-" * 30)

    # Example 2.3: `zip()` for parallel iteration
    # WHY: `zip()` combines multiple iterables into an iterator of tuples,
    #      where the i-th tuple contains the i-th element from each of the input iterables.
    names: List[str] = ["Alice", "Bob", "Charlie"] # List of names
    scores: List[int] = [85, 92, 78] # List of scores
    print(f"Matching names {names} with scores {scores}:")
    # → Matching names ['Alice', 'Bob', 'Charlie'] with scores [85, 92, 78]:
    for name, score in zip(names, scores): # Iterate over both lists simultaneously
        print(f"  {name} scored {score} points.") # Print combined information
    # →   Alice scored 85 points.
    # →   Bob scored 92 points.
    # →   Charlie scored 78 points.
    print("-" * 30)

    # Example 2.4: Iterating over dictionaries
    # WHY: Dictionaries can be iterated over in several ways: keys, values, or key-value pairs.
    student_grades: Dict[str, int] = {"Alice": 90, "Bob": 85, "Charlie": 92} # Dictionary of student grades

    print("Iterating over dictionary keys (default):")
    # → Iterating over dictionary keys (default):
    for student in student_grades: # By default, iterating over a dict yields its keys
        print(f"  Student: {student}") # Print each student name (key)
    # →   Student: Alice
    # →   Student: Bob
    # →   Student: Charlie
    print("-" * 30)

    print("Iterating over dictionary values:")
    # → Iterating over dictionary values:
    for grade in student_grades.values(): # Use .values() to iterate over values only
        print(f"  Grade: {grade}") # Print each grade (value)
    # →   Grade: 90
    # →   Grade: 85
    # →   Grade: 92
    print("-" * 30)

    print("Iterating over dictionary items (key-value pairs):")
    # → Iterating over dictionary items (key-value pairs):
    for student, grade in student_grades.items(): # Use .items() to get key-value pairs as tuples
        print(f"  {student}'s grade is {grade}.") # Print formatted key-value pair
    # →   Alice's grade is 90.
    # →   Bob's grade is 85.
    # →   Charlie's grade is 92.
    print("-" * 30)


# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas: Modifying Collections, `break`, `continue`, `else`
# ═══════════════════════════════════════════════════════════════

def section_3_edge_cases_gotchas() -> None:
    """
    Addresses common pitfalls and advanced control flow features
    within for loops.
    """
    print("SECTION 3: Edge Cases & Gotchas: Modifying Collections, `break`, `continue`, `else`\n")

    # ⚠️ Common mistake: Modifying a list while iterating over it
    # WHY: Iterating over a list while simultaneously adding or removing items
    #      can lead to unexpected behavior, skipping elements, or infinite loops.
    original_numbers: List[int] = [1, 2, 3, 4, 5] # Original list
    print(f"Original list for modification attempt: {original_numbers}")
    # → Original list for modification attempt: [1, 2, 3, 4, 5]

    # WRONG approach (commented out to avoid actual execution issues)
    # print("  Attempting to remove even numbers (WRONG WAY):")
    # for number in original_numbers:
    #     if number % 2 == 0:
    #         original_numbers.remove(number) # This modifies the list being iterated
    # print(f"  List after WRONG modification: {original_numbers}")
    # # → List after WRONG modification: [1, 3, 5] (Oops, 2 was removed, then 4 was skipped!)

    # ✅ Preferred/Pythonic: Iterate over a copy or build a new list
    # WHY: To safely modify a list, iterate over a copy or create a new list
    #      with the desired elements.
    numbers_to_filter: List[int] = [1, 2, 3, 4, 5, 6] # List to filter
    filtered_numbers: List[int] = [] # Initialize an empty list for filtered results
    print(f"List for safe filtering: {numbers_to_filter}")
    # → List for safe filtering: [1, 2, 3, 4, 5, 6]
    for number in numbers_to_filter: # Iterate over the original list
        if number % 2 != 0: # Check if the number is odd
            filtered_numbers.append(number) # Add odd numbers to the new list
    print(f"  List after SAFE modification (odd numbers): {filtered_numbers}")
    # →   List after SAFE modification (odd numbers): [1, 3, 5]
    print("-" * 30)

    # Example 3.1: `break` statement
    # WHY: `break` is used to exit a loop immediately, regardless of whether
    #      the loop's iterable has been exhausted.
    search_list: List[str] = ["apple", "banana", "grape", "orange", "kiwi"] # List to search
    target_fruit: str = "grape" # Fruit to find
    found: bool = False # Flag to track if target is found
    print(f"Searching for '{target_fruit}' in {search_list}:")
    # → Searching for 'grape' in ['apple', 'banana', 'grape', 'orange', 'kiwi']:
    for fruit in search_list: # Loop through the list
        if fruit == target_fruit: # Check if current fruit is the target
            print(f"  Found {target_fruit}!") # Indicate target found
            found = True # Set flag to True
            break # Exit the loop immediately
        print(f"  Checking {fruit}...") # Print fruits being checked
    # →   Checking apple...
    # →   Checking banana...
    # →   Found grape!
    if not found: # Check if target was not found after loop
        print(f"  {target_fruit} not found.") # Print message if not found
    print("-" * 30)

    # Example 3.2: `continue` statement
    # WHY: `continue` skips the rest of the current iteration and moves to the
    #      next item in the iterable.
    data_points: List[int | None] = [10, 5, None, 20, 0, 15] # List with potential None values
    processed_values: List[int] = [] # List to store processed values
    print(f"Processing data points: {data_points}")
    # → Processing data points: [10, 5, None, 20, 0, 15]
    for value in data_points: # Loop through data points
        if value is None: # Check for None (missing data)
            print("  Skipping missing data point (None).") # Indicate skipping
            continue # Skip to the next iteration
        if value == 0: # Check for zero (invalid for division, for example)
            print("  Skipping zero value.") # Indicate skipping
            continue # Skip to the next iteration
        processed_values.append(value * 2) # Process valid values (e.g., multiply by 2)
        print(f"  Processed {value}, result: {value * 2}") # Print processing result
    # →   Processed 10, result: 20
    # →   Processed 5, result: 10
    # →   Skipping missing data point (None).
    # →   Processed 20, result: 40
    # →   Skipping zero value.
    # →   Processed 15, result: 30
    print(f"  Final processed values: {processed_values}") # Print final list
    # →   Final processed values: [20, 10, 40, 30]
    print("-" * 30)

    # Example 3.3: `for-else` block
    # WHY: The `else` block after a `for` loop executes ONLY if the loop
    #      completes without encountering a `break` statement.
    #      It's useful for "search" operations to determine if an item was found.
    items_to_check: List[int] = [1, 2, 3, 4, 5] # List to check
    target_value_found: int = 6 # Value not in list
    target_value_not_found: int = 3 # Value in list

    print(f"Searching for {target_value_found} in {items_to_check} (not found):")
    # → Searching for 6 in [1, 2, 3, 4, 5] (not found):
    for item in items_to_check: # Loop through items
        if item == target_value_found: # Check if target is found
            print(f"  {target_value_found} was found!") # This won't print
            break # Exit loop if found
    else: # This 'else' executes because no 'break' was hit
        print(f"  {target_value_found} was NOT found in the list.") # Print not found message
    # →   6 was NOT found in the list.
    print("-" * 30)

    print(f"Searching for {target_value_not_found} in {items_to_check} (found):")
    # → Searching for 3 in [1, 2, 3, 4, 5] (found):
    for item in items_to_check: # Loop through items
        if item == target_value_not_found: # Check if target is found
            print(f"  {target_value_not_found} was found!") # Print found message
            break # Exit loop if found, preventing 'else' from executing
    else: # This 'else' will NOT execute because 'break' was hit
        print(f"  {target_value_not_found} was NOT found in the list.")
    # →   3 was found!
    print("-" * 30)


# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns: Nested Loops, List Comprehensions (briefly)
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """
    Covers more complex loop structures like nested loops and
    briefly introduces list comprehensions as an alternative.
    """
    print("SECTION 4: Intermediate Patterns: Nested Loops, List Comprehensions (briefly)\n")

    # Example 4.1: Nested for loops
    # WHY: Nested loops are used when you need to iterate over combinations
    #      of elements from multiple iterables, or over multi-dimensional structures.
    rows: List[str] = ["A", "B", "C"] # List representing rows
    cols: List[int] = [1, 2, 3] # List representing columns
    print(f"Generating coordinates from rows {rows} and columns {cols}:")
    # → Generating coordinates from rows ['A', 'B', 'C'] and columns [1, 2, 3]:
    for row in rows: # Outer loop iterates through rows
        for col in cols: # Inner loop iterates through columns for each row
            print(f"  Coordinate: ({row},{col})") # Print combined coordinate
    # →   Coordinate: (A,1)
    # →   Coordinate: (A,2)
    # →   Coordinate: (A,3)
    # →   Coordinate: (B,1)
    # →   Coordinate: (B,2)
    # →   Coordinate: (B,3)
    # →   Coordinate: (C,1)
    # →   Coordinate: (C,2)
    # →   Coordinate: (C,3)
    print("-" * 30)

    # Example 4.2: Nested loops for a multiplication table
    print("Generating a 3x3 multiplication table:")
    # → Generating a 3x3 multiplication table:
    for i in range(1, 4): # Outer loop for numbers 1, 2, 3
        for j in range(1, 4): # Inner loop for numbers 1, 2, 3
            print(f"  {i} * {j} = {i * j}") # Print multiplication result
        print("  ---") # Separator for each row
    # →   1 * 1 = 1
    # →   1 * 2 = 2
    # →   1 * 3 = 3
    # →   ---
    # →   2 * 1 = 2
    # →   2 * 2 = 4
    # →   2 * 3 = 6
    # →   ---
    # →   3 * 1 = 3
    # →   3 * 2 = 6
    # →   3 * 3 = 9
    # →   ---
    print("-" * 30)

    # ℹ️ Note: List Comprehensions
    # WHY: List comprehensions provide a concise way to create lists based on existing iterables.
    #      They are often more readable and efficient than explicit for loops for simple transformations/filters.
    original_list: List[int] = [1, 2, 3, 4, 5] # Original list
    print(f"Original list for squaring: {original_list}")
    # → Original list for squaring: [1, 2, 3, 4, 5]

    # Traditional for loop approach
    squared_numbers_loop: List[int] = [] # Initialize empty list
    for num in original_list: # Loop through original list
        squared_numbers_loop.append(num * num) # Append squared number
    print(f"  Squared numbers (loop): {squared_numbers_loop}")
    # →   Squared numbers (loop): [1, 4, 9, 16, 25]

    # List comprehension approach
    squared_numbers_comprehension: List[int] = [num * num for num in original_list] # Create list in one line
    print(f"  Squared numbers (comprehension): {squared_numbers_comprehension}")
    # →   Squared numbers (comprehension): [1, 4, 9, 16, 25]
    print("  (List comprehensions are powerful but are covered in more detail in another module.)")
    print("-" * 30)

    # Example 4.3: Iterating over sets
    # WHY: Sets are unordered collections of unique elements. Iterating over them
    #      is similar to lists/tuples, but the order is not guaranteed.
    unique_colors: Set[str] = {"red", "green", "blue", "red"} # Define a set (duplicates are removed)
    print(f"Iterating over unique colors: {unique_colors}")
    # → Iterating over unique colors: {'green', 'blue', 'red'} (Order may vary)
    for color in unique_colors: # Loop through each unique color
        print(f"  Color: {color}") # Print the color
    # →   Color: green
    # →   Color: blue
    # →   Color: red
    print("-" * 30)


# ═══════════════════════════════════════════════════════════════
# SECTION 5: Pythonic Idioms: Generators, `all()`, `any()`
# ═══════════════════════════════════════════════════════════════

def section_5_pythonic_idioms() -> None:
    """
    Introduces more advanced and Pythonic ways to handle iteration,
    including generator functions and built-in functions for checking conditions.
    """
    print("SECTION 5: Pythonic Idioms: Generators, `all()`, `any()`\n")

    # Example 5.1: Using a generator function with a for loop
    # WHY: Generator functions (`yield` keyword) create iterators. They generate values
    #      on-the-fly, one at a time, which is memory-efficient for large sequences.
    def fibonacci_sequence(limit: int) -> Iterator[int]: # Define a generator function
        """Generates Fibonacci numbers up to a given limit."""
        a, b = 0, 1 # Initialize first two Fibonacci numbers
        while a < limit: # Loop until 'a' exceeds the limit
            yield a # Yield the current Fibonacci number
            a, b = b, a + b # Update 'a' and 'b' for the next number

    print("Generating Fibonacci numbers up to 50:")
    # → Generating Fibonacci numbers up to 50:
    for num in fibonacci_sequence(50): # Iterate over the generator object
        print(f"  {num}", end=" ") # Print each number, separated by space
    # →   0 1 1 2 3 5 8 13 21 34
    print("\n" + "-" * 30)

    # Example 5.2: `all()` and `any()` as alternatives to manual flag loops
    # WHY: `all()` returns True if all elements of an iterable are true (or if the iterable is empty).
    #      `any()` returns True if any element of an iterable is true.
    #      These are more concise and often more readable than writing explicit loops with flags.

    # Manual loop for `all()`
    numbers_all: List[int] = [2, 4, 6, 8] # All even numbers
    all_even_manual: bool = True # Flag to check if all are even
    print(f"Checking if all numbers in {numbers_all} are even (manual loop):")
    # → Checking if all numbers in [2, 4, 6, 8] are even (manual loop):
    for n in numbers_all: # Loop through numbers
        if n % 2 != 0: # If any number is odd
            all_even_manual = False # Set flag to False
            break # Exit loop early
    print(f"  All even (manual): {all_even_manual}")
    # →   All even (manual): True

    # Pythonic `all()` approach
    all_even_pythonic: bool = all(n % 2 == 0 for n in numbers_all) # Generator expression with all()
    print(f"  All even (Pythonic all()): {all_even_pythonic}")
    # →   All even (Pythonic all()): True
    print("-" * 30)

    # Manual loop for `any()`
    mixed_numbers: List[int] = [1, 3, 4, 7] # Contains one even number
    any_even_manual: bool = False # Flag to check if any are even
    print(f"Checking if any numbers in {mixed_numbers} are even (manual loop):")
    # → Checking if any numbers in [1, 3, 4, 7] are even (manual loop):
    for n in mixed_numbers: # Loop through numbers
        if n % 2 == 0: # If any number is even
            any_even_manual = True # Set flag to True
            break # Exit loop early
    print(f"  Any even (manual): {any_even_manual}")
    # →   Any even (manual): True

    # Pythonic `any()` approach
    any_even_pythonic: bool = any(n % 2 == 0 for n in mixed_numbers) # Generator expression with any()
    print(f"  Any even (Pythonic any()): {any_even_pythonic}")
    # →   Any even (Pythonic any()): True
    print("-" * 30)

    # Example 5.3: Using `reversed()` and `sorted()` with loops
    # WHY: These built-in functions provide convenient ways to iterate over
    #      sequences in a specific order without modifying the original.
    original_data: List[int] = [3, 1, 4, 1, 5, 9, 2] # Original list
    print(f"Original data: {original_data}")
    # → Original data: [3, 1, 4, 1, 5, 9, 2]

    print("Iterating in reverse order:")
    # → Iterating in reverse order:
    for item in reversed(original_data): # Iterate over the reversed view of the list
        print(f"  Reverse item: {item}") # Print each item
    # →   Reverse item: 2
    # →   Reverse item: 9
    # →   Reverse item: 5
    # →   Reverse item: 1
    # →   Reverse item: 4
    # →   Reverse item: 1
    # →   Reverse item: 3
    print("-" * 30)

    print("Iterating in sorted order:")
    # → Iterating in sorted order:
    for item in sorted(original_data): # Iterate over a new sorted list (original is unchanged)
        print(f"  Sorted item: {item}") # Print each item
    # →   Sorted item: 1
    # →   Sorted item: 1
    # →   Sorted item: 2
    # →   Sorted item: 3
    # →   Sorted item: 4
    # →   Sorted item: 5
    # →   Sorted item: 9
    print("-" * 30)


# ═══════════════════════════════════════════════════════════════
# SECTION 6: Real-World Mini-Program: Simple Data Processing
# ═══════════════════════════════════════════════════════════════

def section_6_real_world_mini_program() -> None:
    """
    A small, cohesive program demonstrating the practical application of for loops
    in data processing and simple reporting.
    """
    print("SECTION 6: Real-World Mini-Program: Simple Data Processing\n")

    # WHY: This mini-program simulates processing student quiz scores to calculate
    #      averages, assign grades, and identify top performers using various
    #      for loop patterns.

    class Student: # Define a simple class to