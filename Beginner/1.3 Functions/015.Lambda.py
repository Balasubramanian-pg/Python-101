"""Lambda: Anonymous, Single-Expression Functions

This module explores Python's `lambda` keyword, which allows the creation of small, anonymous functions. Lambdas are best used for simple, one-off operations where a full `def` function would be overkill and reduce readability.

What you will learn:
*   How to define a basic `lambda` function.
*   The key differences between `lambda` functions and regular `def` functions.
*   Common use cases for `lambda` with built-in functions like `map()`, `filter()`, and `sorted()`.
*   Potential pitfalls and limitations of using `lambda` expressions.
*   When to prefer `lambda` for conciseness versus when `def` is more appropriate.
*   How `lambda` functions interact with closures and scope.

Prerequisites:
*   Basic understanding of Python functions (`def`).
*   Familiarity with higher-order functions (functions that take other functions as arguments).
*   Knowledge of basic data structures like lists and dictionaries.

Key Concepts Covered:
*   `lambda` keyword
*   Anonymous functions
*   Single-expression functions
*   Higher-order functions (`map`, `filter`, `sorted`)
*   Function arguments
*   Closures and scope
*   Readability vs. conciseness
*   `functools.reduce`
*   `operator` module alternatives
"""

import functools
import timeit
import operator

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept - Understanding Anonymous Functions
# ═══════════════════════════════════════════════════════════════

def section_1_core_concept() -> None:
    """
    Demonstrates the fundamental nature of lambda functions.
    Explains what they are and their basic syntax, comparing them to regular functions.
    """
    print("SECTION 1: Core Concept - Understanding Anonymous Functions")
    print("-------------------------------------------------------")

    # ℹ️ What is a lambda function?
    # A lambda function is a small anonymous function.
    # An anonymous function is a function without a name.
    # Lambda functions can take any number of arguments, but can only have one expression.

    # 1.1 Basic Lambda Syntax
    print("\n1.1 Basic Lambda Syntax: `lambda arguments: expression`")

    # A simple lambda that adds two numbers
    add_lambda = lambda a, b: a + b  # Defines an anonymous function and assigns it to `add_lambda`
    print(f"Lambda `add_lambda(5, 3)`: {add_lambda(5, 3)}")
    # → Lambda `add_lambda(5, 3)`: 8

    # A lambda that squares a number
    square_lambda = lambda x: x * x  # Takes one argument `x` and returns `x * x`
    print(f"Lambda `square_lambda(7)`: {square_lambda(7)}")
    # → Lambda `square_lambda(7)`: 49

    # A lambda with no arguments (returns a constant value)
    greet_lambda = lambda: "Hello from lambda!" # No arguments, returns a fixed string
    print(f"Lambda `greet_lambda()`: {greet_lambda()}")
    # → Lambda `greet_lambda()`: Hello from lambda!

    # 1.2 Comparison with Regular Functions (def)
    print("\n1.2 Comparison with Regular Functions (def)")

    # Define the same functionality using a regular `def` function
    def add_def(a: int, b: int) -> int:
        """Adds two numbers."""  # Regular functions can have docstrings
        return a + b             # Explicit return statement

    print(f"Regular function `add_def(5, 3)`: {add_def(5, 3)}")
    # → Regular function `add_def(5, 3)`: 8

    def square_def(x: int) -> int:
        """Squares a number."""
        return x * x

    print(f"Regular function `square_def(7)`: {square_def(7)}")
    # → Regular function `square_def(7)`: 49

    # 🔑 Key Insight:
    # Lambdas are syntactically restricted to a single expression.
    # They implicitly return the result of that expression.
    # Regular functions (`def`) can contain multiple statements, have docstrings,
    # and require an explicit `return` statement (or they return `None` implicitly).

    print(f"\nType of `add_lambda`: {type(add_lambda)}")
    # → Type of `add_lambda`: <class 'function'>
    print(f"Type of `add_def`: {type(add_def)}")
    # → Type of `add_def`: <class 'function'>
    # Both are function objects, but lambdas are often used for their conciseness
    # when passed as arguments to other functions.

# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns - Everyday Lambda Usage
# ═══════════════════════════════════════════════════════════════

def section_2_syntax_common_patterns() -> None:
    """
    Demonstrates common practical applications of lambda functions
    with built-in higher-order functions like map, filter, and sorted.
    """
    print("\nSECTION 2: Syntax & Common Patterns - Everyday Lambda Usage")
    print("---------------------------------------------------------")

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Sample list for transformations
    names = ["Alice", "bob", "Charlie", "david"] # Sample list for sorting/mapping

    # 2.1 Lambdas with `map()`
    # `map()` applies a given function to all items in an input list (or other iterable)
    # and returns an iterator.

    print("\n2.1 Lambdas with `map()`")
    # Goal: Square each number in the `data` list.

    # ✅ Using lambda with map
    squared_numbers = list(map(lambda x: x * x, data)) # `lambda x: x*x` is applied to each element
    print(f"Original data: {data}")
    print(f"Squared numbers (map + lambda): {squared_numbers}")
    # → Squared numbers (map + lambda): [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # Equivalent using a regular function (more verbose for a simple operation)
    def square_func(x: int) -> int:
        return x * x
    squared_numbers_def = list(map(square_func, data))
    print(f"Squared numbers (map + def): {squared_numbers_def}")
    # → Squared numbers (map + def): [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # 2.2 Lambdas with `filter()`
    # `filter()` constructs an iterator from elements of an iterable for which
    # a function returns true.

    print("\n2.2 Lambdas with `filter()`")
    # Goal: Get only even numbers from the `data` list.

    # ✅ Using lambda with filter
    even_numbers = list(filter(lambda x: x % 2 == 0, data)) # `lambda x: x % 2 == 0` filters even numbers
    print(f"Original data: {data}")
    print(f"Even numbers (filter + lambda): {even_numbers}")
    # → Even numbers (filter + lambda): [2, 4, 6, 8, 10]

    # Equivalent using a regular function
    def is_even(x: int) -> bool:
        return x % 2 == 0
    even_numbers_def = list(filter(is_even, data))
    print(f"Even numbers (filter + def): {even_numbers_def}")
    # → Even numbers (filter + def): [2, 4, 6, 8, 10]

    # 2.3 Lambdas with `sorted()`
    # `sorted()` returns a new sorted list from the items in an iterable.
    # It takes an optional `key` argument, which is a function to extract a comparison key.

    print("\n2.3 Lambdas with `sorted()`")
    # Goal: Sort names ignoring case.

    print(f"Original names: {names}")
    # ✅ Using lambda as a key for sorted()
    sorted_names_case_insensitive = sorted(names, key=lambda name: name.lower()) # Converts each name to lowercase for comparison
    print(f"Sorted names (case-insensitive): {sorted_names_case_insensitive}")
    # → Sorted names (case-insensitive): ['Alice', 'bob', 'Charlie', 'david']

    # Goal: Sort a list of tuples by the second element.
    pairs = [(1, 'apple'), (3, 'banana'), (2, 'cherry'), (4, 'date')]
    print(f"Original pairs: {pairs}")
    sorted_pairs_by_second = sorted(pairs, key=lambda pair: pair[1]) # Sorts by the string element of the tuple
    print(f"Sorted pairs by second element: {sorted_pairs_by_second}")
    # → Sorted pairs by second element: [(1, 'apple'), (3, 'banana'), (2, 'cherry'), (4, 'date')]

    # 2.4 Lambdas as arguments to custom higher-order functions
    print("\n2.4 Lambdas as arguments to custom higher-order functions")

    def apply_operation(value: int, operation_func) -> int:
        """Applies an operation function to a given value."""
        return operation_func(value)

    # Use a lambda to multiply by 10
    result_multiply = apply_operation(15, lambda x: x * 10) # Pass lambda directly as argument
    print(f"Applying `lambda x: x * 10` to 15: {result_multiply}")
    # → Applying `lambda x: x * 10` to 15: 150

    # Use a lambda to check if a number is positive
    result_positive = apply_operation(-5, lambda x: x > 0)
    print(f"Applying `lambda x: x > 0` to -5: {result_positive}")
    # → Applying `lambda x: x > 0` to -5: False

# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas - What Beginners Always Get Wrong
# ═══════════════════════════════════════════════════════════════

def section_3_edge_cases_gotchas() -> None:
    """
    Highlights common mistakes and limitations when using lambda functions,
    such as single-expression restriction and closure issues.
    """
    print("\nSECTION 3: Edge Cases & Gotchas - What Beginners Always Get Wrong")
    print("---------------------------------------------------------------")

    # 3.1 Lambda can only contain a single expression, not statements
    print("\n3.1 Lambda can only contain a single expression, not statements")
    # ⚠️ Common mistake: Trying to put multiple statements or complex logic.
    # Lambdas are not meant for multi-line code blocks or explicit statements like `if`, `for`, `while`.

    # 🐛 Bug source: Trying to assign a variable inside a lambda
    # try:
    #     invalid_lambda_assign = lambda x: y = x * 2 # SyntaxError: invalid syntax
    #     print(invalid_lambda_assign(5))
    # except SyntaxError as e:
    #     print(f"Error trying to assign in lambda: {e}")

    # 🐛 Bug source: Trying to use an if/else *statement*
    # (Note: `if/else` *expression* is fine, see below)
    # try:
    #     invalid_lambda_if = lambda x: if x > 0: x else: 0 # SyntaxError: invalid syntax
    #     print(invalid_lambda_if(5))
    # except SyntaxError as e:
    #     print(f"Error trying to use if statement in lambda: {e}")

    # ✅ Correct way: Use a conditional expression (ternary operator)
    conditional_lambda = lambda x: "Positive" if x > 0 else "Non-positive" # This is a single expression
    print(f"Conditional lambda for 10: {conditional_lambda(10)}")
    # → Conditional lambda for 10: Positive
    print(f"Conditional lambda for -3: {conditional_lambda(-3)}")
    # → Conditional lambda for -3: Non-positive

    # 3.2 Late Binding Closures (a classic Python gotcha!)
    print("\n3.2 Late Binding Closures")
    # This is a common source of confusion when lambdas (or any function) are created in a loop.
    # The lambda's closure 'remembers' the *variable* (not its value at creation time)
    # from the enclosing scope.

    actions_wrong = []
    for i in range(5):
        # ⚠️ Common mistake: `i` is evaluated when the lambda is *called*, not when it's *defined*.
        # By the time these lambdas are called, `i` will have already reached its final value (4).
        actions_wrong.append(lambda: i * 2)

    print("Wrong closure example (all functions return 8):")
    for action in actions_wrong:
        print(f"  {action()}")
    # →   8
    # →   8
    # →   8
    # →   8
    # →   8
    # Explanation: When the loop finishes, `i` is 4. All lambdas refer to this *same* `i`.

    # ✅ Correct way: Capture the current value of `i` using a default argument.
    # The default argument is evaluated at the time the function is *defined*.
    actions_correct = []
    for i in range(5):
        actions_correct.append(lambda x=i: x * 2) # `x=i` captures the value of `i` for each lambda

    print("Correct closure example (functions return 0, 2, 4, 6, 8):")
    for action in actions_correct:
        print(f"  {action()}")
    # →   0
    # →   2
    # →   4
    # →   6
    # →   8

    # 3.3 No Docstrings or Annotations
    print("\n3.3 No Docstrings or Annotations")
    # Lambdas are simple and don't support docstrings or type annotations in their definition.
    # While type checkers can infer types in some cases, explicit annotations are not possible.

    simple_add = lambda a, b: a + b
    print(f"Lambda function name: {simple_add.__name__}")
    # → Lambda function name: <lambda>
    print(f"Lambda has docstring? {simple_add.__doc__ is not None}")
    # → Lambda has docstring? False

    def regular_add(a: int, b: int) -> int:
        """Adds two integers."""
        return a + b
    print(f"Regular function name: {regular_add.__name__}")
    # → Regular function name: regular_add
    print(f"Regular function docstring: {regular_add.__doc__}")
    # → Regular function docstring: Adds two integers.

    # 🔑 Key Insight:
    # Use lambdas for very simple, single-expression logic where a full `def` would add clutter.
    # For anything more complex, with multiple statements, docstrings, or clear type hints,
    # a regular `def` function is always the better choice for readability and maintainability.

# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns - Lambdas in More Advanced Contexts
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """
    Explores slightly more advanced uses of lambdas, such as with `functools.reduce`
    and in dynamic function creation scenarios.
    """
    print("\nSECTION 4: Intermediate Patterns - Lambdas in More Advanced Contexts")
    print("------------------------------------------------------------------")

    numbers = [1, 2, 3, 4, 5] # Sample data for reduction
    employees = [
        {"name": "Alice", "salary": 60000},
        {"name": "Bob", "salary": 75000},
        {"name": "Charlie", "salary": 50000}
    ]

    # 4.1 Lambdas with `functools.reduce()`
    # `reduce()` applies a function of two arguments cumulatively to the items of an iterable,
    # from left to right, so as to reduce the iterable to a single value.

    print("\n4.1 Lambdas with `functools.reduce()`")
    # Goal: Calculate the sum of all numbers in the list.

    # ✅ Using lambda with reduce for sum
    sum_of_numbers = functools.reduce(lambda acc, x: acc + x, numbers) # `acc` is accumulator, `x` is current item
    print(f"Numbers: {numbers}")
    print(f"Sum of numbers (reduce + lambda): {sum_of_numbers}")
    # → Sum of numbers (reduce + lambda): 15

    # Goal: Find the maximum number in the list.
    max_number = functools.reduce(lambda a, b: a if a > b else b, numbers)
    print(f"Max number (reduce + lambda): {max_number}")
    # → Max number (reduce + lambda): 5

    # 4.2 Lambdas in dictionary/list comprehensions (as values)
    print("\n4.2 Lambdas in dictionary/list comprehensions (as values)")

    # Goal: Create a dictionary where keys are operations and values are lambda functions.
    operation_funcs = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y
    }
    print(f"Operations dictionary: {operation_funcs}")
    # → Operations dictionary: {'add': <function <lambda> at ...>, 'subtract': <function <lambda> at ...>, 'multiply': <function <lambda> at ...>}

    print(f"Using 'add': {operation_funcs['add'](10, 5)}")
    # → Using 'add': 15
    print(f"Using 'multiply': {operation_funcs['multiply'](10, 5)}")
    # → Using 'multiply': 50

    # 4.3 Lambdas for creating simple factory functions (currying/partial application)
    print("\n4.3 Lambdas for creating simple factory functions")
    # You can create functions that return other functions using lambdas.
    # This is a form of currying or partial application.

    def make_multiplier(factor: int) -> callable:
        """Returns a lambda function that multiplies its input by `factor`."""
        return lambda x: x * factor # `factor` is enclosed in the lambda's scope

    multiply_by_5 = make_multiplier(5) # `factor` is captured as 5
    multiply_by_10 = make_multiplier(10) # `factor` is captured as 10

    print(f"Multiply 7 by 5: {multiply_by_5(7)}")
    # → Multiply 7 by 5: 35
    print(f"Multiply 7 by 10: {multiply_by_10(7)}")
    # → Multiply 7 by 10: 70

    # 🔑 Key Insight:
    # Lambdas are powerful when used in functional programming constructs or
    # to create specialized functions on the fly. Their conciseness shines here.

# ═══════════════════════════════════════════════════════════════
# SECTION 5: Pythonic Idioms - The Right Way vs the Naive Way
# ═══════════════════════════════════════════════════════════════

def section_5_pythonic_idioms() -> None:
    """
    Compares common lambda usage patterns with more Pythonic alternatives,
    especially involving the `operator` module.
    """
    print("\nSECTION 5: Pythonic Idioms - The Right Way vs the Naive Way")
    print("---------------------------------------------------------")

    data_dicts = [
        {"name": "apple", "price": 1.50, "stock": 100},
        {"name": "banana", "price": 0.75, "stock": 200},
        {"name": "cherry", "price": 3.00, "stock": 50}
    ]

    # 5.1 When `def` is clearer than `lambda`
    print("\n5.1 When `def` is clearer than `lambda`")
    # If the logic is even slightly complex or needs multiple steps, use `def`.

    # ⚠️ Less readable lambda for complex logic
    # complex_filter_lambda = lambda item: item['stock'] > 100 and item['price'] < 2.00 and len(item['name']) > 5
    # print(f"Filtered (complex lambda): {list(filter(complex_filter_lambda, data_dicts))}")

    # ✅ Preferred: Use a regular `def` function for clarity
    def is_affordable_and_plentiful(item: dict) -> bool:
        """Checks if an item is affordable, plentiful, and has a long name."""
        has_enough_stock = item['stock'] > 100
        is_cheap_enough = item['price'] < 2.00
        has_long_name = len(item['name']) > 5
        return has_enough_stock and is_cheap_enough and has_long_name

    filtered_data = list(filter(is_affordable_and_plentiful, data_dicts))
    print(f"Original data: {data_dicts}")
    print(f"Filtered (clear def function): {filtered_data}")
    # → Filtered (clear def function): [{'name': 'banana', 'price': 0.75, 'stock': 200}]

    # 5.2 Using `operator` module instead of lambda for common operations
    print("\n5.2 Using `operator` module instead of lambda for common operations")
    # The `operator` module provides functions that correspond to Python's operators.
    # These are often more efficient and readable than equivalent lambdas for simple operations.

    # 5.2.1 `operator.itemgetter` for dictionary/list access
    print("\n  5.2.1 `operator.itemgetter`")
    # Goal: Sort `data_dicts` by price.

    # ⚠️ Naive way: lambda for key access
    sorted_by_price_lambda = sorted(data_dicts, key=lambda item: item['price'])
    print(f"Sorted by price (lambda): {sorted_by_price_lambda}")
    # → Sorted by price (lambda): [{'name': 'banana', 'price': 0.75, 'stock': 200}, {'name': 'apple', 'price': 1.5, 'stock': 100}, {'name': 'cherry', 'price': 3.0, 'stock': 50}]

    # ✅ Pythonic way: `operator.itemgetter`
    # `itemgetter` returns a callable object that fetches the item(s) from its operand.
    sorted_by_price_itemgetter = sorted(data_dicts, key=operator.itemgetter('price'))
    print(f"Sorted by price (itemgetter): {sorted_by_price_itemgetter}")
    # → Sorted by price (itemgetter): [{'name': 'banana', 'price': 0.75, 'stock': 200}, {'name': 'apple', 'price': 1.5, 'stock': 100}, {'name': 'cherry', 'price': 3.0, 'stock': 50}]

    # 5.2.2 `operator.attrgetter` for object attributes (if we had a class)
    print("\n  5.2.2 `operator.attrgetter` (conceptual)")
    # If `data_dicts` were a list of objects like `[Product('apple', 1.50), ...]`,
    # then `operator.attrgetter('price')` would be used.
    class Product:
        def __init__(self, name: str, price: float, stock: int):
            self.name = name
            self.price = price
            self.stock = stock
        def __repr__(self) -> str:
            return f"Product('{self.name}', {self.price})"

    products = [
        Product("apple", 1.50, 100),
        Product("banana", 0.75, 200),
        Product("cherry", 3.00, 50)
    ]
    # ⚠️ Naive way: lambda for attribute access
    sorted_products_lambda = sorted(products, key=lambda p: p.price)
    print(f"Sorted products by price (lambda): {sorted_products_lambda}")
    # → Sorted products by price (lambda): [Product('banana', 0.75), Product('apple', 1.5), Product('cherry', 3.0)]

    # ✅ Pythonic way: `operator.attrgetter`
    sorted_products_attrgetter = sorted(products, key=operator.attrgetter('price'))
    print(f"Sorted products by price (attrgetter): {sorted_products_attrgetter}")
    # → Sorted products by price (attrgetter): [Product('banana', 0.75), Product('apple', 1.5), Product('cherry', 3.0)]

    # 5.2.3 Other `operator` functions (e.g., `add`, `mul`)
    print("\n  5.2.3 Other `operator` functions (e.g., `add`, `mul`)")
    # Instead of `lambda x, y: x + y` for `reduce`
    numbers = [1, 2, 3, 4, 5]
    sum_with_lambda = functools.reduce(lambda x, y: x + y, numbers)
    sum_with_operator = functools.reduce(operator.add, numbers)
    print(f"Sum with lambda: {sum_with_lambda}, Sum with operator.add: {sum_with_operator}")
    # → Sum with lambda: 15, Sum with operator.add: 15

    # 🔑 Key Insight:
    # While lambdas are concise, the `operator` module often provides more readable
    # and sometimes more performant alternatives for common operations, especially
    # when accessing elements of sequences or attributes of objects.
    # Always prioritize readability. If a lambda becomes hard to parse, switch to `def`.

# ═══════════════════════════════════════════════════════════════
# SECTION 6: Real-World Mini-Program - Data Transformation Example
# ═══════════════════════════════════════════════════════════════

def section_6_real_world_mini_program() -> None:
    """
    A practical example demonstrating how lambdas can be used in a cohesive
    data processing pipeline, especially with lists of objects or dictionaries.
    """
    print("\nSECTION 6: Real-World Mini-Program - Data Transformation Example")
    print("--------------------------------------------------------------")

    # Define a simple class to represent sensor readings
    class SensorReading:
        def __init__(self, sensor_id: str, temperature: float, humidity: float, timestamp: int):
            self.sensor_id = sensor_id
            self.temperature = temperature
            self.humidity = humidity
            self.timestamp = timestamp # Unix timestamp

        def __repr__(self) -> str:
            return (f"SensorReading(id='{self.sensor_id}', temp={self.temperature}°C, "
                    f"hum={self.humidity}%, ts={self.timestamp})")

    # Simulate a generator for sensor data (to meet requirement)
    def generate_sensor_data(count: int) -> list[SensorReading]:
        """Generates a list of synthetic sensor readings."""
        readings = []
        import random
        import time
        for i in range(count):
            sensor_id = f"sensor_{random.randint(1, 3)}"
            temperature = round(random.uniform(20.0, 30.0), 1)
            humidity = round(random.uniform(40.0, 70.0), 1)
            timestamp = int(time.time()) - (count - 1 - i) * 60 # simulate time passing
            readings.append(SensorReading(sensor_id, temperature, humidity, timestamp))
        return readings

    # Generate some sample data
    all_readings = generate_sensor_data(10)
    print("1. Original Sensor Readings:")
    for reading in all_readings:
        print(f"   {reading}")
    # Expected output: A list of 10 SensorReading objects with varying data.

    print("\n2. Filtering: Get readings from 'sensor_1' with temperature >