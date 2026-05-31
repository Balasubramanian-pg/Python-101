"""
Lists
Python lists are ordered, mutable collections of items. They are one of the most versatile and widely used data structures, capable of holding elements of different data types.

What you will learn:
* How to create and initialize lists.
* How to access, add, modify, and remove elements from lists.
* The difference between shallow and deep copies, and list mutability.
* Efficiently iterate and transform lists using comprehensions and built-in functions.
* Pythonic idioms for common list operations.
* Basic performance characteristics of list operations.

Prerequisites:
* Basic understanding of variables and data types (integers, strings, booleans).
* Familiarity with `for` loops.
* Knowledge of basic function definitions.

Key Concepts Covered:
* List creation and literals
* Indexing and slicing
* List methods (`append`, `insert`, `remove`, `pop`, `sort`, `reverse`, `count`, `index`)
* List concatenation and repetition
* Iteration over lists
* List comprehensions
* Shallow vs. Deep copy
* Mutability
* `enumerate()`, `zip()`, `sorted()`
* Time complexity for common list operations
"""

import sys # Used for sys.getsizeof in performance section

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: Introduction to Python Lists
# ═══════════════════════════════════════════════════════════════

def section_1_core_concept() -> None:
    """
    Demonstrates the absolute fundamentals of Python lists,
    including creation, basic access, modification, and length.
    """
    print("\n--- SECTION 1: Core Concept: Introduction to Python Lists ---")

    # 1.1 Creating Lists
    # Lists are defined using square brackets [] and elements separated by commas.
    empty_list: list[int] = [] # An empty list, explicitly typed for integers but can hold anything
    print(f"1.1 Empty list: {empty_list}")
    # → 1.1 Empty list: []

    # Lists can contain items of different data types (heterogeneous).
    mixed_list: list[int | str | bool] = [1, "hello", True, 3.14] # A list with mixed data types
    print(f"1.1 Mixed list: {mixed_list}")
    # → 1.1 Mixed list: [1, 'hello', True, 3.14]

    # Lists are ordered collections. The order of elements is preserved.
    fruits: list[str] = ["apple", "banana", "cherry", "date"] # A list of strings
    print(f"1.1 Fruits list: {fruits}")
    # → 1.1 Fruits list: ['apple', 'banana', 'cherry', 'date']

    # 1.2 Accessing Elements by Index
    # Elements in a list are accessed using their index, starting from 0 for the first element.
    first_fruit: str = fruits[0] # Accessing the first element
    print(f"1.2 First fruit: {first_fruit}")
    # → 1.2 First fruit: apple

    second_fruit: str = fruits[1] # Accessing the second element
    print(f"1.2 Second fruit: {second_fruit}")
    # → 1.2 Second fruit: banana

    # Negative indices count from the end of the list.
    # -1 refers to the last element, -2 to the second to last, and so on.
    last_fruit: str = fruits[-1] # Accessing the last element
    print(f"1.2 Last fruit: {last_fruit}")
    # → 1.2 Last fruit: date

    second_to_last_fruit: str = fruits[-2] # Accessing the second to last element
    print(f"1.2 Second to last fruit: {second_to_last_fruit}")
    # → 1.2 Second to last fruit: cherry

    # ⚠️ Common mistake: Trying to access an index out of bounds will raise an IndexError.
    try:
        # out_of_bounds = fruits[10] # This line would cause an IndexError
        pass # Commenting out to prevent script crash
    except IndexError:
        print("1.2 Caught an IndexError: List index out of range.")

    # 1.3 Modifying Elements
    # Lists are mutable, meaning their elements can be changed after creation.
    print(f"1.3 Original fruits: {fruits}")
    # → 1.3 Original fruits: ['apple', 'banana', 'cherry', 'date']

    fruits[1] = "blueberry" # Change the element at index 1
    print(f"1.3 Modified fruits (index 1): {fruits}")
    # → 1.3 Modified fruits (index 1): ['apple', 'blueberry', 'cherry', 'date']

    fruits[-1] = "grape" # Change the last element
    print(f"1.3 Modified fruits (last element): {fruits}")
    # → 1.3 Modified fruits (last element): ['apple', 'blueberry', 'cherry', 'grape']

    # 1.4 Getting the Length of a List
    # The built-in `len()` function returns the number of elements in a list.
    num_fruits: int = len(fruits) # Get the count of elements
    print(f"1.4 Number of fruits: {num_fruits}")
    # → 1.4 Number of fruits: 4

    empty_list_length: int = len(empty_list) # Length of an empty list
    print(f"1.4 Length of empty list: {empty_list_length}")
    # → 1.4 Length of empty list: 0

# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns: Essential List Operations
# ═══════════════════════════════════════════════════════════════

def section_2_syntax_common_patterns() -> None:
    """
    Covers everyday usage patterns for lists, including adding, removing,
    checking membership, slicing, and basic iteration.
    """
    print("\n--- SECTION 2: Syntax & Common Patterns: Essential List Operations ---")

    my_numbers: list[int] = [10, 20, 30, 40, 50] # Initial list for demonstrations
    print(f"2.0 Initial numbers: {my_numbers}")
    # → 2.0 Initial numbers: [10, 20, 30, 40, 50]

    # 2.1 Adding Elements
    # 2.1.1 `append()`: Adds an element to the end of the list. Modifies the list in-place.
    my_numbers.append(60) # Add 60 to the end
    print(f"2.1.1 After append(60): {my_numbers}")
    # → 2.1.1 After append(60): [10, 20, 30, 40, 50, 60]

    # 2.1.2 `insert()`: Adds an element at a specified index.
    my_numbers.insert(0, 5) # Insert 5 at the beginning (index 0)
    print(f"2.1.2 After insert(0, 5): {my_numbers}")
    # → 2.1.2 After insert(0, 5): [5, 10, 20, 30, 40, 50, 60]

    my_numbers.insert(3, 25) # Insert 25 at index 3
    print(f"2.1.2 After insert(3, 25): {my_numbers}")
    # → 2.1.2 After insert(3, 25): [5, 10, 20, 25, 30, 40, 50, 60]

    # 2.1.3 List Concatenation (`+` operator): Creates a new list by joining two lists.
    more_numbers: list[int] = [70, 80] # Another list
    combined_numbers: list[int] = my_numbers + more_numbers # Concatenate lists
    print(f"2.1.3 Combined with [70, 80]: {combined_numbers}")
    # → 2.1.3 Combined with [70, 80]: [5, 10, 20, 25, 30, 40, 50, 60, 70, 80]

    # 2.1.4 `extend()`: Adds elements from an iterable (like another list) to the end of the current list.
    # It modifies the list in-place, similar to `append`, but for multiple items.
    my_numbers.extend([90, 100]) # Add multiple elements from another list
    print(f"2.1.4 After extend([90, 100]): {my_numbers}")
    # → 2.1.4 After extend([90, 100]): [5, 10, 20, 25, 30, 40, 50, 60, 90, 100]

    # 2.2 Removing Elements
    # 2.2.1 `del` statement: Removes an element at a specific index or a slice.
    del my_numbers[0] # Remove the first element
    print(f"2.2.1 After del my_numbers[0]: {my_numbers}")
    # → 2.2.1 After del my_numbers[0]: [10, 20, 25, 30, 40, 50, 60, 90, 100]

    del my_numbers[6:] # Remove elements from index 6 to the end (slicing)
    print(f"2.2.1 After del my_numbers[6:] (slice): {my_numbers}")
    # → 2.2.1 After del my_numbers[6:] (slice): [10, 20, 25, 30, 40, 50]

    # 2.2.2 `remove()`: Removes the *first occurrence* of a specified value. Raises ValueError if not found.
    my_numbers.remove(25) # Remove the value 25
    print(f"2.2.2 After remove(25): {my_numbers}")
    # → 2.2.2 After remove(25): [10, 20, 30, 40, 50]

    try:
        # my_numbers.remove(99) # This would raise a ValueError
        pass # Commenting out to prevent script crash
    except ValueError:
        print("2.2.2 Caught a ValueError: List.remove(x): x not in list.")

    # 2.2.3 `pop()`: Removes and returns the element at a specified index (or the last element if no index is given).
    popped_element_last: int = my_numbers.pop() # Remove and return the last element
    print(f"2.2.3 Popped last element: {popped_element_last}, List: {my_numbers}")
    # → 2.2.3 Popped last element: 50, List: [10, 20, 30, 40]

    popped_element_index: int = my_numbers.pop(1) # Remove and return element at index 1
    print(f"2.2.3 Popped element at index 1: {popped_element_index}, List: {my_numbers}")
    # → 2.2.3 Popped element at index 1: 20, List: [10, 30, 40]

    # 2.3 Checking for Element Existence (`in` operator)
    # The `in` operator returns True if an item is found in the list, False otherwise.
    is_30_in: bool = 30 in my_numbers # Check if 30 is in the list
    print(f"2.3 Is 30 in my_numbers? {is_30_in}")
    # → 2.3 Is 30 in my_numbers? True

    is_99_in: bool = 99 in my_numbers # Check if 99 is in the list
    print(f"2.3 Is 99 in my_numbers? {is_99_in}")
    # → 2.3 Is 99 in my_numbers? False

    # 2.4 Slicing Lists
    # Slicing allows you to get a sub-list (a "slice") from a list.
    # Syntax: `list[start:end:step]`
    # `start` is inclusive, `end` is exclusive.
    numbers_full: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"2.4 Original list for slicing: {numbers_full}")
    # → 2.4 Original list for slicing: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    slice_middle: list[int] = numbers_full[2:7] # Elements from index 2 up to (but not including) 7
    print(f"2.4 Slice [2:7]: {slice_middle}")
    # → 2.4 Slice [2:7]: [3, 4, 5, 6, 7]

    slice_from_start: list[int] = numbers_full[:5] # Elements from the beginning up to (but not including) 5
    print(f"2.4 Slice [:5]: {slice_from_start}")
    # → 2.4 Slice [:5]: [1, 2, 3, 4, 5]

    slice_to_end: list[int] = numbers_full[6:] # Elements from index 6 to the end
    print(f"2.4 Slice [6:]: {slice_to_end}")
    # → 2.4 Slice [6:]: [7, 8, 9, 10]

    slice_copy: list[int] = numbers_full[:] # A full copy of the list
    print(f"2.4 Slice [:]: {slice_copy}")
    # → 2.4 Slice [:]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    slice_step: list[int] = numbers_full[::2] # Every second element, starting from the first
    print(f"2.4 Slice [::2] (every other): {slice_step}")
    # → 2.4 Slice [::2] (every other): [1, 3, 5, 7, 9]

    slice_reverse: list[int] = numbers_full[::-1] # Reverse the list
    print(f"2.4 Slice [::-1] (reversed): {slice_reverse}")
    # → 2.4 Slice [::-1] (reversed): [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # 2.5 Iterating Through a List
    # The most common way to process each item in a list is with a `for` loop.
    print("2.5 Iterating through my_numbers:")
    for num in my_numbers: # Iterate directly over elements
        print(f"  Current number: {num}")
    # →   Current number: 10
    # →   Current number: 30
    # →   Current number: 40

    # 2.6 Nested Lists (Lists of Lists)
    # Lists can contain other lists, creating multi-dimensional structures.
    matrix: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ] # A 3x3 matrix represented as a list of lists
    print(f"2.6 Matrix: {matrix}")
    # → 2.6 Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Accessing elements in nested lists requires multiple indices.
    element_row1_col2: int = matrix[0][1] # Access element at row 0, column 1 (value 2)
    print(f"2.6 Element at [0][1]: {element_row1_col2}")
    # → 2.6 Element at [0][1]: 2

    # Modifying an element in a nested list
    matrix[1][2] = 99 # Change element at row 1, column 2 (value 6 to 99)
    print(f"2.6 Matrix after modification: {matrix}")
    # → 2.6 Matrix after modification: [[1, 2, 3], [4, 5, 99], [7, 8, 9]]


# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas: Immutability vs. Mutability & Copying
# ═══════════════════════════════════════════════════════════════

def section_3_edge_cases_gotchas() -> None:
    """
    Explores the implications of lists being mutable, particularly regarding
    aliasing and the crucial distinction between shallow and deep copies.
    """
    print("\n--- SECTION 3: Edge Cases & Gotchas: Immutability vs. Mutability & Copying ---")

    # 3.1 Mutability: Lists can be changed after creation.
    # This is a fundamental property that distinguishes them from immutable types like tuples or strings.
    original_list: list[int] = [1, 2, 3] # Define an initial list
    print(f"3.1 Original list: {original_list}")
    # → 3.1 Original list: [1, 2, 3]

    original_list.append(4) # Modify the list in-place
    print(f"3.1 Modified list: {original_list}")
    # → 3.1 Modified list: [1, 2, 3, 4]

    # 3.2 Aliasing: Multiple References to the Same List Object
    # When you assign one list variable to another, you're not creating a new list.
    # Instead, both variables point to the *same* list object in memory.
    list_a: list[int] = [10, 20, 30] # First list
    list_b: list[int] = list_a # list_b now refers to the same object as list_a
    print(f"3.2 Initial list_a: {list_a}, list_b: {list_b}")
    # → 3.2 Initial list_a: [10, 20, 30], list_b: [10, 20, 30]

    list_b.append(40) # Modify list_b
    print(f"3.2 After list_b.append(40), list_a: {list_a}, list_b: {list_b}")
    # → 3.2 After list_b.append(40), list_a: [10, 20, 30, 40], list_b: [10, 20, 30, 40]
    # 🔑 Key insight: Both lists changed because they are the same object.

    # You can check if two variables refer to the exact same object using `is`.
    are_same_object: bool = list_a is list_b
    print(f"3.2 Are list_a and list_b the same object? {are_same_object}")
    # → 3.2 Are list_a and list_b the same object? True

    # 3.3 Shallow Copy vs. Deep Copy
    # When you need an independent copy of a list, you must explicitly create one.

    # 3.3.1 Shallow Copy Methods
    # A shallow copy creates a new list object, but it does NOT create copies of the
    # *elements* within the list. If elements are mutable (like other lists),
    # changes to those nested mutable elements will affect both the original and the copy.

    # Method 1: Slicing `[:]`
    list_original: list[int | list[int]] = [1, 2, [3, 4]] # List with a nested mutable element
    list_shallow_slice: list[int | list[int]] = list_original[:] # Create a shallow copy using slicing
    print(f"3.3.1 Original: {list_original}, Shallow Slice: {list_shallow_slice}")
    # → 3.3.1 Original: [1, 2, [3, 4]], Shallow Slice: [1, 2, [3, 4]]
    print(f"3.3.1 Are list_original and list_shallow_slice the same object? {list_original is list_shallow_slice}")
    # → 3.3.1 Are list_original and list_shallow_slice the same object? False

    # Modify a top-level element in the shallow copy. Original is unaffected.
    list_shallow_slice[0] = 99 # Modify a simple integer element
    print(f"3.3.1 After modifying top-level: Original: {list_original}, Shallow Slice: {list_shallow_slice}")
    # → 3.3.1 After modifying top-level: Original: [1, 2, [3, 4]], Shallow Slice: [99, 2, [3, 4]]

    # Modify a nested mutable element in the shallow copy. Original *is* affected.
    # 🐛 Bug source: Beginners often expect this not to happen.
    # This is because the nested list [3, 4] is still the *same object* in both lists.
    list_shallow_slice[2].append(5) # Modify the nested list
    print(f"3.3.1 After modifying nested: Original: {list_original}, Shallow Slice: {list_shallow_slice}")
    # → 3.3.1 After modifying nested: Original: [1, 2, [3, 4, 5]], Shallow Slice: [99, 2, [3, 4, 5]]
    # 🔑 Key insight: The nested list `[3, 4]` is shared between `list_original` and `list_shallow_slice`.

    # Method 2: `list()` constructor
    list_shallow_constructor: list[int | list[int]] = list(list_original) # Create a shallow copy using list()
    print(f"3.3.1 Original: {list_original}, Shallow Constructor: {list_shallow_constructor}")
    # → 3.3.1 Original: [1, 2, [3, 4, 5]], Shallow Constructor: [1, 2, [3, 4, 5]]
    list_shallow_constructor[2].append(6) # Further modify the nested list
    print(f"3.3.1 After modifying nested via constructor copy: Original: {list_original}, Constructor Copy: {list_shallow_constructor}")
    # → 3.3.1 After modifying nested via constructor copy: Original: [1, 2, [3, 4, 5, 6]], Constructor Copy: [1, 2, [3, 4, 5, 6]]
    # 🔑 Key insight: `list()` constructor behaves identically to slicing `[:]` for shallow copies.

    # 3.3.2 Deep Copy
    # A deep copy creates a new list object AND recursively creates copies of all elements,
    # including nested mutable objects. This ensures complete independence.
    # To perform a deep copy, you typically use the `copy.deepcopy()` function from the `copy` module.
    # For this beginner-level file, we'll explain the concept but avoid importing `copy` to keep it lean.

    # ℹ️ Note: While `copy.deepcopy` is the standard for deep copying,
    # for lists containing only immutable elements (numbers, strings, tuples of immutables)
    # or other lists of only immutable elements, a shallow copy is effectively a deep copy.
    simple_list_for_copy: list[int] = [100, 200, 300]
    shallow_copy_simple: list[int] = simple_list_for_copy[:]
    shallow_copy_simple[0] = 500
    print(f"3.3.2 Simple list copy: Original: {simple_list_for_copy}, Shallow Copy: {shallow_copy_simple}")
    # → 3.3.2 Simple list copy: Original: [100, 200, 300], Shallow Copy: [500, 200, 300]
    # Here, a shallow copy works like a deep copy because elements are immutable integers.

    # 🔑 Key insight: Be mindful of mutability and copying when dealing with nested lists or
    # when passing lists to functions, to avoid unintended side effects.

# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns: List Comprehensions and Sorting
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """
    Introduces more advanced list manipulation techniques like list comprehensions
    for concise list creation and various sorting methods.
    """
    print("\n--- SECTION 4: Intermediate Patterns: List Comprehensions and Sorting ---")

    # 4.1 List Comprehensions
    # A concise way to create lists. They consist of an expression followed by a `for` clause,
    # and then zero or more `for` or `if` clauses.

    # 4.1.1 Basic List Comprehension: Squaring numbers
    # WHY: Instead of a multi-line loop, create a new list by applying an operation to each item.
    numbers_to_square: list[int] = [1, 2, 3, 4, 5]
    print(f"4.1.1 Original numbers: {numbers_to_square}")
    # → 4.1.1 Original numbers: [1, 2, 3, 4, 5]

    # 👎 Wrong/Naive way: Using a for loop and append
    # squared_numbers_naive = []
    # for num in numbers_to_square:
    #     squared_numbers_naive.append(num * num)

    # ✅ Preferred/Pythonic: Using a list comprehension
    squared_numbers_lc: list[int] = [num * num for num in numbers_to_square] # Create a new list with squared values
    print(f"4.1.1 Squared numbers (LC): {squared_numbers_lc}")
    # → 4.1.1 Squared numbers (LC): [1, 4, 9, 16, 25]

    # 4.1.2 List Comprehension with a Condition: Filtering even numbers
    # WHY: Combine transformation and filtering into a single, readable line.
    numbers_to_filter: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"4.1.2 Numbers to filter: {numbers_to_filter}")
    # → 4.1.2 Numbers to filter: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 👎 Wrong/Naive way: Using a for loop with an if statement
    # even_numbers_naive = []
    # for num in numbers_to_filter:
    #     if num % 2 == 0:
    #         even_numbers_naive.append(num)

    # ✅ Preferred/Pythonic: Using a list comprehension with an `if` clause
    even_numbers_lc: list[int] = [num for num in numbers_to_filter if num % 2 == 0] # Filter for even numbers
    print(f"4.1.2 Even numbers (LC): {even_numbers_lc}")
    # → 4.1.2 Even numbers (LC): [2, 4, 6, 8, 10]

    # 4.1.3 List Comprehension with `if/else` expression
    # WHY: Apply different transformations based on a condition within the list creation.
    numbers_if_else: list[int] = [1, 2, 3, 4, 5]
    transformed_numbers: list[str] = ["Even" if x % 2 == 0 else "Odd" for x in numbers_if_else] # Transform based on condition
    print(f"4.1.3 Transformed (if/else LC): {transformed_numbers}")
    # → 4.1.3 Transformed (if/else LC): ['Odd', 'Even', 'Odd', 'Even', 'Odd']

    # 4.2 Sorting Lists