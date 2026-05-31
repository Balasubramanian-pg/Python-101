"""Nested Loops: Iterating with multiple loops for multi-dimensional data processing.
This module explores how to use one loop structure inside another to handle complex iteration patterns.

What you will learn:
*   The fundamental concept and syntax of nested `for` and `while` loops.
*   How to control the flow of execution within nested loops using `break` and `continue`.
*   Common applications such as processing grids, matrices, and generating combinations.
*   Understanding the performance implications and time complexity of nested loops.
*   Pythonic alternatives like nested list comprehensions and `itertools.product`.
*   Strategies for efficiently exiting from deeply nested loop structures.

Prerequisites:
*   Basic understanding of `for` loops and `while` loops.
*   Familiarity with Python's iterable types (lists, tuples, strings, ranges).
*   Knowledge of conditional statements (`if`, `elif`, `else`).

Key Concepts Covered:
*   Outer loop, inner loop
*   Iteration order
*   `break` statement behavior in nested loops
*   `continue` statement behavior in nested loops
*   Early exit strategies (flags, functions)
*   Nested list comprehensions
*   Nested generator expressions
*   `itertools.product` for Cartesian products
*   Time complexity (O(N^2), O(N^3))
*   Matrix processing
*   Coordinate generation
*   Class definition for structured data iteration
*   Generator function for efficient iteration
"""

import time # For performance measurement in Section 7
import itertools # For Pythonic alternatives in Section 5

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: Understanding Nested Loop Fundamentals
# ═══════════════════════════════════════════════════════════════

def section_1_core_concept() -> None:
    """
    Demonstrates the absolute fundamentals of nested loops.
    Explains the concept of an outer loop and an inner loop, and their execution order.
    """
    print("SECTION 1: Core Concept: Understanding Nested Loop Fundamentals")
    print("------------------------------------------------------------")

    # A nested loop is a loop inside another loop.
    # The inner loop completes all its iterations for each single iteration of the outer loop.

    print("\nExample 1.1: Basic 2x2 Grid Iteration")
    # This example shows how to iterate through a simple 2x2 grid structure.
    # The outer loop handles rows, and the inner loop handles columns.
    for row_index in range(2): # Outer loop: iterates twice (for row 0, then row 1)
        for col_index in range(2): # Inner loop: iterates twice for *each* outer loop iteration
            print(f"  Processing coordinate: ({row_index}, {col_index})") # Print current coordinate
            # → Processing coordinate: (0, 0)
            # → Processing coordinate: (0, 1)
            # → Processing coordinate: (1, 0)
            # → Processing coordinate: (1, 1)

    print("\nKey insight: The inner loop runs to completion for every single iteration of the outer loop.")
    print("Example 1.2: Visualizing Iteration Order with Different Iterables")
    # Using different iterables to better visualize the nested execution.
    colors = ["Red", "Green"] # Outer loop iterable
    shapes = ["Circle", "Square"] # Inner loop iterable

    # Iterate through each color, and for each color, iterate through each shape.
    for color in colors: # Outer loop starts with "Red"
        print(f"  Outer loop: Current color is '{color}'") # Indicate outer loop progress
        for shape in shapes: # Inner loop runs for "Circle", then "Square"
            print(f"    Inner loop: Current shape is '{shape}' associated with '{color}'") # Show association
            # → Outer loop: Current color is 'Red'
            # →   Inner loop: Current shape is 'Circle' associated with 'Red'
            # →   Inner loop: Current shape is 'Square' associated with 'Red'
            # → Outer loop: Current color is 'Green'
            # →   Inner loop: Current shape is 'Circle' associated with 'Green'
            # →   Inner loop: Current shape is 'Square' associated with 'Green'

    print("\nNested loops are fundamental for processing multi-dimensional data like matrices or tables.")
    print("This pattern effectively creates a Cartesian product of the elements from the iterables.")

# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns: Practical Nested Loop Applications
# ═══════════════════════════════════════════════════════════════

def section_2_syntax_common_patterns() -> None:
    """
    Explores common use cases and typical syntax for nested loops.
    Includes examples like multiplication tables, grid creation, and finding pairs.
    """
    print("\nSECTION 2: Syntax & Common Patterns: Practical Nested Loop Applications")
    print("---------------------------------------------------------------------")

    print("\nExample 2.1: Generating a Multiplication Table")
    # A classic use case for nested loops is generating tables.
    # The outer loop iterates through the multiplicands, the inner loop through multipliers.
    table_size = 3 # Define the size of the multiplication table

    print(f"  Multiplication Table (up to {table_size}x{table_size}):")
    # Iterate through rows (multiplicands)
    for i in range(1, table_size + 1): # i will be 1, 2, 3
        row_output = [] # Initialize list to store results for the current row
        # Iterate through columns (multipliers)
        for j in range(1, table_size + 1): # j will be 1, 2, 3 for each i
            product = i * j # Calculate the product
            row_output.append(f"{product:2d}") # Add formatted product to the row list (e.g., ' 1', ' 2', ' 3')
        print(f"  {' '.join(row_output)}") # Join and print the row elements
        # →   1  2  3
        # →   2  4  6
        # →   3  6  9

    print("\nExample 2.2: Creating a Simple Text-Based Grid/Board")
    # Nested loops are ideal for drawing grid-like structures.
    grid_rows = 4 # Number of rows for the grid
    grid_cols = 5 # Number of columns for the grid
    grid_symbol = "*" # Symbol to use for each cell

    print(f"  {grid_rows}x{grid_cols} Grid:")
    # Iterate for each row
    for row in range(grid_rows): # Outer loop: controls vertical position
        current_row_str = "" # String to build the current row
        # Iterate for each column in the current row
        for col in range(grid_cols): # Inner loop: controls horizontal position
            current_row_str += grid_symbol + " " # Add symbol and space to the row string
        print(f"  {current_row_str.strip()}") # Print the completed row, removing trailing space
        # →   * * * * *
        # →   * * * * *
        # →   * * * * *
        # →   * * * * *

    print("\nExample 2.3: Finding All Unique Pairs in a List")
    # Nested loops can be used to compare every element with every other element.
    numbers = [1, 2, 3, 4] # List of numbers to find pairs from
    print(f"  List of numbers: {numbers}")
    print("  Unique pairs (order matters):")
    # Iterate through each element as the first element of a pair
    for i, num1 in enumerate(numbers): # Outer loop gets index and value
        # Iterate through each element as the second element of a pair
        # Starting from i+1 ensures unique pairs and avoids self-pairing (e.g., (1,1))
        # and duplicate pairs (e.g., (1,2) and (2,1) if order doesn't matter)
        for j, num2 in enumerate(numbers): # Inner loop gets index and value
            if i < j: # Condition to ensure unique pairs and avoid self-pairing/duplicates
                print(f"    Pair: ({num1}, {num2})") # Print the unique pair
                # →   Pair: (1, 2)
                # →   Pair: (1, 3)
                # →   Pair: (1, 4)
                # →   Pair: (2, 3)
                # →   Pair: (2, 4)
                # →   Pair: (3, 4)

    print("\nExample 2.4: Basic Matrix Summation")
    # Nested loops are fundamental for processing 2D data structures like matrices.
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ] # A 3x3 matrix
    total_sum = 0 # Initialize sum accumulator

    print(f"  Matrix: {matrix}")
    print("  Calculating sum of all elements:")
    # Iterate through each row in the matrix
    for row in matrix: # Outer loop processes each list (row)
        # Iterate through each element within the current row
        for element in row: # Inner loop processes each number in the row
            total_sum += element # Add the element to the total sum
    print(f"  Total sum of matrix elements: {total_sum}")
    # → Total sum of matrix elements: 45

# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas: Pitfalls and Control Flow in Nested Loops
# ═══════════════════════════════════════════════════════════════

def section_3_edge_cases_gotchas() -> None:
    """
    Addresses common mistakes and advanced control flow techniques within nested loops,
    such as `break` and `continue` statements and early exit strategies.
    """
    print("\nSECTION 3: Edge Cases & Gotchas: Pitfalls and Control Flow in Nested Loops")
    print("------------------------------------------------------------------------")

    print("\nExample 3.1: Understanding `break` in Nested Loops")
    # The `break` statement only exits the *innermost* loop it is contained within.
    search_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    target_value = 5 # Value to search for

    print(f"  Searching for {target_value} in matrix: {search_matrix}")
    # Iterate through rows
    for r_idx, row in enumerate(search_matrix): # Outer loop
        # Iterate through columns
        for c_idx, value in enumerate(row): # Inner loop
            if value == target_value: # Check if current value matches target
                print(f"    Found {target_value} at ({r_idx}, {c_idx})") # Indicate finding
                break # 🔑 Key insight: This 'break' only exits the INNER loop (over 'value')
        print(f"  Outer loop continues after inner loop break (or completion) for row {r_idx}.")
        # →   Outer loop continues after inner loop break (or completion) for row 0.
        # →     Found 5 at (1, 1)
        # →   Outer loop continues after inner loop break (or completion) for row 1.
        # →   Outer loop continues after inner loop break (or completion) for row 2.

    print("\nExample 3.2: Early Exit from Both Loops (Using a Flag)")
    # To exit *all* nested loops, a common pattern is to use a flag variable.
    search_found = False # Flag to indicate if the target was found
    target_value_double_break = 5 # Value to search for

    print(f"  Searching for {target_value_double_break} with early exit via flag.")
    # Iterate through rows
    for r_idx, row in enumerate(search_matrix): # Outer loop
        if search_found: # Check flag before starting inner loop
            break # If found, break the outer loop as well
        # Iterate through columns
        for c_idx, value in enumerate(row): # Inner loop
            if value == target_value_double_break: # Check if target found
                print(f"    Found {target_value_double_break} at ({r_idx}, {c_idx})")
                search_found = True # Set flag to True
                break # Break the inner loop
    if not search_found: # Check if target was found after loops
        print(f"  {target_value_double_break} not found.")
    # →     Found 5 at (1, 1)

    print("\nExample 3.3: Early Exit from Both Loops (Using a Function)")
    # Encapsulating nested loops in a function allows using `return` for early exit.
    def find_target_in_matrix(matrix: list[list[int]], target: int) -> tuple[int, int] | None:
        """Searches for a target value in a matrix and returns its coordinates or None."""
        # Iterate through rows
        for r_idx, row in enumerate(matrix): # Outer loop
            # Iterate through columns
            for c_idx, value in enumerate(row): # Inner loop
                if value == target: # Target found
                    return r_idx, c_idx # ✅ Preferred: Return immediately, exiting all loops
        return None # If loops complete without finding, return None

    target_value_func_break = 8 # Value to search for
    print(f"  Searching for {target_value_func_break} with early exit via function return.")
    coords = find_target_in_matrix(search_matrix, target_value_func_break) # Call the search function
    if coords:
        print(f"    Found {target_value_func_break} at {coords}")
        # →     Found 8 at (2, 1)
    else:
        print(f"    {target_value_func_break} not found.")

    target_value_not_found = 99 # Value not in matrix
    coords_not_found = find_target_in_matrix(search_matrix, target_value_not_found)
    if coords_not_found:
        print(f"    Found {target_value_not_found} at {coords_not_found}")
    else:
        print(f"    {target_value_not_found} not found.")
        # →     99 not found.

    print("\nExample 3.4: Understanding `continue` in Nested Loops")
    # The `continue` statement skips the rest of the current inner loop iteration
    # but continues with the next iteration of the *inner* loop.
    data_list = [(1, 'a'), (2, 'b'), (3, 'c')] # Sample data
    skip_value = 2 # Value to skip

    print(f"  Iterating through {data_list}, skipping processing for outer loop values of {skip_value}.")
    # Iterate through outer list
    for item_outer_val, item_outer_char in data_list:
        if item_outer_val == skip_value: # Condition to skip processing for a specific outer value
            print(f"    ⚠️  Outer loop: Skipping all inner loop processing for value {item_outer_val}.")
            continue # This 'continue' skips to the NEXT iteration of the OUTER loop
        print(f"  Outer loop: Processing value {item_outer_val}.")
        # Iterate through inner list (same list for demonstration)
        for item_inner_val, item_inner_char in data_list:
            if item_inner_val == skip_value: # Condition to skip a specific inner value
                print(f"      Inner loop: Skipping inner processing for value {item_inner_val}.")
                continue # This 'continue' skips to the NEXT iteration of the INNER loop
            print(f"      Inner loop: Pair ({item_outer_val}, {item_inner_val})")
            # →   Outer loop: Processing value 1.
            # →     Inner loop: Pair (1, 1)
            # →     Inner loop: Skipping inner processing for value 2.
            # →     Inner loop: Pair (1, 3)
            # →     Outer loop: Skipping all inner loop processing for value 2.
            # →   Outer loop: Processing value 3.
            # →     Inner loop: Pair (3, 1)
            # →     Inner loop: Skipping inner processing for value 2.
            # →     Inner loop: Pair (3, 3)

# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns: Beyond Basic Two-Level Nesting
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """
    Explores more complex nested loop structures, including three or more levels,
    mixing `for` and `while` loops, and conditional nesting.
    """
    print("\nSECTION 4: Intermediate Patterns: Beyond Basic Two-Level Nesting")
    print("---------------------------------------------------------------")

    print("\nExample 4.1: Three-Level Nested Loops (3D Coordinates)")
    # Nested loops can extend to any depth, useful for N-dimensional data.
    # This example generates all points in a 2x2x2 cube.
    cube_size = 2 # Each dimension goes from 0 to cube_size-1

    print(f"  Generating 3D coordinates for a {cube_size}x{cube_size}x{cube_size} cube:")
    # Outer loop for X-axis
    for x in range(cube_size):
        # Middle loop for Y-axis
        for y in range(cube_size):
            # Inner loop for Z-axis
            for z in range(cube_size):
                print(f"    Coordinate: ({x}, {y}, {z})")
                # →     Coordinate: (0, 0, 0)
                # →     Coordinate: (0, 0, 1)
                # →     Coordinate: (0, 1, 0)
                # →     Coordinate: (0, 1, 1)
                # →     Coordinate: (1, 0, 0)
                # →     Coordinate: (1, 0, 1)
                # →     Coordinate: (1, 1, 0)
                # →     Coordinate: (1, 1, 1)

    print("\nExample 4.2: Mixing `for` and `while` Loops")
    # It's possible to combine different loop types in a nested structure.
    # This example uses a `for` loop for outer iteration and a `while` loop for inner.
    outer_items = ["A", "B", "C"] # Items for the outer `for` loop
    inner_limit = 2 # Limit for the inner `while` loop

    print(f"  Mixing `for` (outer) and `while` (inner) loops:")
    # Iterate through outer_items
    for item in outer_items:
        print(f"  Outer loop: Processing item '{item}'")
        count = 0 # Initialize counter for inner `while` loop
        # Inner `while` loop runs up to inner_limit times
        while count < inner_limit:
            print(f"    Inner loop: Iteration {count + 1} for '{item}'")
            count += 1 # Increment inner loop counter
            # →   Outer loop: Processing item 'A'
            # →     Inner loop: Iteration 1 for 'A'
            # →     Inner loop: Iteration 2 for 'A'
            # →   Outer loop: Processing item 'B'
            # →     Inner loop: Iteration 1 for 'B'
            # →     Inner loop: Iteration 2 for 'B'
            # →   Outer loop: Processing item 'C'
            # →     Inner loop: Iteration 1 for 'C'
            # →     Inner loop: Iteration 2 for 'C'

    print("\nExample 4.3: Conditional Nesting (Inner loop runs based on outer condition)")
    # Sometimes, the inner loop should only execute if a certain condition is met
    # in the outer loop's current iteration.
    tasks = [
        {"name": "Task A", "subtasks": ["A1", "A2"]},
        {"name": "Task B", "subtasks": []}, # No subtasks
        {"name": "Task C", "subtasks": ["C1"]},
    ]

    print("  Processing tasks with conditional subtasks:")
    # Iterate through each task
    for task in tasks:
        print(f"  Processing main task: {task['name']}")
        # Check if the current task has subtasks
        if task["subtasks"]: # Condition: only proceed if 'subtasks' list is not empty
            print(f"    Subtasks found for {task['name']}:")
            # Iterate through subtasks if they exist
            for subtask in task["subtasks"]:
                print(f"      - {subtask}")
        else:
            print(f"    No subtasks for {task['name']}.")
            # →   Processing main task: Task A
            # →     Subtasks found for Task A:
            # →       - A1
            # →       - A2
            # →   Processing main task: Task B
            # →     No subtasks for Task B.
            # →   Processing main task: Task C
            # →     Subtasks found for Task C:
            # →       - C1

# ═══════════════════════════════════════════════════════════════
# SECTION 5: Pythonic Idioms: Efficient and Readable Alternatives
# ═══════════════════════════════════════════════════════════════

def section_5_pythonic_idioms() -> None:
    """
    Introduces more Pythonic and often more concise ways to achieve results
    typically obtained with nested loops, focusing on list comprehensions
    and the `itertools` module.
    """
    print("\nSECTION 5: Pythonic Idioms: Efficient and Readable Alternatives")
    print("-------------------------------------------------------------")

    print("\nExample 5.1: Nested List Comprehensions for Grid Generation")
    # List comprehensions provide a concise way to create lists.
    # They can be nested to create lists of lists (e.g., matrices).
    rows = 3
    cols = 4
    # ⚠️  Naive way using nested loops:
    # grid_naive = []
    # for r in range(rows):
    #     row_list = []
    #     for c in range(cols):
    #         row_list.append(f"({r},{c})")
    #     grid_naive.append(row_list)

    # ✅  Pythonic way using nested list comprehension:
    # The outer comprehension creates the list of rows.
    # The inner comprehension creates each individual row.
    grid_comprehension: list[list[str]] = [[f"({r},{c})" for c in range(cols)] for r in range(rows)]
    print(f"  Generated {rows}x{cols} grid using nested list comprehension:")
    for row in grid_comprehension: # Print each row for clear output
        print(f"  {row}")
        # →   ['(0,0)', '(0,1)', '(0,2)', '(0,3)']
        # →   ['(1,0)', '(1,1)', '(1,2)', '(1,3)']
        # →   ['(2,0)', '(2,1)', '(2,2)', '(2,3)']

    print("\nExample 5.2: Nested Generator Expressions for Memory Efficiency")
    # Similar to list comprehensions, but use parentheses instead of square brackets.
    # They produce an iterator, yielding values one by one, saving memory for large datasets.
    max_x = 3
    max_y = 2
    # This creates a generator that yields generator objects for each 'x'.
    # Each inner generator yields 'y' values for its 'x'.
    coords_generator = ((x, y) for x in range(max_x) for y in range(max_y)) # Single line generator expression

    print(f"  Generating (x, y) coordinates up to ({max_x-1},{max_y-1}) using nested generator expression:")
    count = 0 # Counter for demonstration limit
    for coord in coords_generator: # Iterate through the outer generator
        print(f"  Yielded coordinate: {coord}")
        count += 1
        if count >= 6: # Limit output for brevity
            print("  ... (truncated for brevity)")
            break
        # →   Yielded coordinate: (0, 0)
        # →   Yielded coordinate: (0, 1)
        # →   Yielded coordinate: (1, 0)
        # →   Yielded coordinate: (1, 1)
        # →   Yielded coordinate: (2, 0)
        # →   Yielded coordinate: (2, 1)
        # →   ... (truncated for brevity)

    print("\nExample 5.3: Using `itertools.product` for Cartesian Products")
    # The `itertools.product` function is specifically designed to compute
    # the Cartesian product of input iterables, often replacing nested loops.
    colors = ["Red", "Blue"]
    sizes = ["S", "M", "L"]

    # ⚠️  Naive way using nested loops:
    # all_combinations_naive = []
    # for color in colors:
    #     for size in sizes:
    #         all_combinations_naive.append((color, size))

    # ✅  Pythonic way using itertools.product:
    all_combinations_itertools: list[tuple[str, str]] = list(itertools.product(colors, sizes))
    print(f"  All combinations of colors {colors} and sizes {sizes} using `itertools.product`:")
    for combo in all_combinations_itertools:
        print(f"  Combination: {combo}")
        # →   Combination: ('Red', 'S')
        # →   Combination: ('Red', 'M')
        # →   Combination: ('Red', 'L')
        # →   Combination: ('Blue', 'S')
        # →   Combination: ('Blue', 'M')
        # →   Combination: ('Blue', 'L')

    print("\nKey insight: `itertools.product` is highly optimized in C and generally faster and more memory efficient")
    print("             than manual nested loops for generating Cartesian products, especially for many iterables.")

# ═══════════════════════════════════════════════════════════════
# SECTION 6: Real-World Mini-Program: Building a Simple Game Board
# ═══════════════════════════════════════════════════════════════

class GameBoard:
    """
    A simple class representing a game board, demonstrating nested loops
    for initialization, display, and interaction.
    """
    def __init__(self, rows: int, cols: int, empty_char: str = '.') -> None:
        """
        Initializes the game board with specified dimensions and an empty character.
        Uses a nested list comprehension for efficient board creation.
        """
        if rows <= 0 or cols <= 0: # Input validation
            raise ValueError("Board dimensions must be positive.")
        self.rows = rows # Store number of rows
        self.cols = cols # Store number of columns
        self.empty_char = empty_char # Character for empty cells
        # ✅  Use nested list comprehension for board initialization
        self.board: list[list[str]] = [[empty_char for _ in range(cols)] for _ in range(rows)]
        print(f"  Board initialized: {self.rows}x{self.cols} with '{self.empty_char}' as empty cells.")

    def display(self) -> None:
        """
        Prints the current state of the game board to the console.
        Uses nested loops to iterate through rows and columns.
        """
        print("\n  Current Board:")
        # Iterate through each row of the board
        for r_idx, row in enumerate(self.board):
            row_str = f"{r_idx} | " # Start row string with row index
            # Iterate through each cell in the current row
            for cell in row:
                row_str += f"{cell} " # Add cell content to the row string
            print(row_str) # Print the complete row
        print("    " + "-" * (self.cols * 2 + 1)) # Separator line
        print("    " + " ".join(str(c) for c in range(self.cols))) # Column headers
        print("-" * 30) # Footer

    def place_piece(self, row: int, col: int, piece: str) -> bool:
        """
        Places a