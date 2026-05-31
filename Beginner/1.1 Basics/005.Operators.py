"""Operators
Operators are special symbols or keywords that perform operations on one or more operands (values or variables). They are fundamental building blocks for all computation and logic in Python, enabling everything from simple arithmetic to complex data manipulations and control flow.

What you will learn:
*   The core categories of operators: arithmetic, comparison, and logical.
*   How assignment operators provide concise ways to update variable values.
*   The distinction and usage of identity (`is`) and membership (`in`) operators.
*   Fundamentals of bitwise operators for low-level data manipulation.
*   Understanding operator precedence and associativity to predict evaluation order.
*   Common operator-related pitfalls and Pythonic idioms for elegant code.

Prerequisites:
*   Basic understanding of Python variables and data types (numbers, strings, booleans, lists).
*   Familiarity with simple control flow structures like `if/else` statements.

Key Concepts Covered:
*   Arithmetic Operators (+, -, *, /, //, %, **)
*   Comparison Operators (==, !=, <, >, <=, >=)
*   Logical Operators (and, or, not)
*   Assignment Operators (=, +=, -=, *=, /=, //=, %=, **=)
*   Identity Operators (is, is not)
*   Membership Operators (in, not in)
*   Bitwise Operators (&, |, ^, ~, <<, >>)
*   Ternary Operator (Conditional Expression)
*   Operator Precedence and Associativity
*   Short-Circuiting
*   Chained Comparisons
*   Augmented Assignment
*   Object Identity vs. Value Equality
"""

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: The Building Blocks of Computation
# ═══════════════════════════════════════════════════════════════

def section_1_core_concept() -> None:
    """
    Introduces the fundamental types of operators in Python, focusing on
    arithmetic operations as the most basic form of computation.
    """
    print("\nSECTION 1: Core Concept: The Building Blocks of Computation")
    print("----------------------------------------------------------")

    # ℹ️ Operators are symbols that perform operations on values.
    #    Operands are the values the operators act upon.

    # 🔑 Key insight: Python categorizes operators for different purposes.

    # Example 1.1: Arithmetic Operators
    # These operators perform mathematical calculations.
    print("\n--- Arithmetic Operators ---")

    operand_a: int = 10  # Define the first integer operand
    operand_b: int = 3   # Define the second integer operand
    operand_c: float = 2.5 # Define a float operand

    # Addition: Adds two operands
    sum_result: int = operand_a + operand_b
    print(f"Addition ({operand_a} + {operand_b}): {sum_result}")
    # → Addition (10 + 3): 13

    # Subtraction: Subtracts the second operand from the first
    diff_result: int = operand_a - operand_b
    print(f"Subtraction ({operand_a} - {operand_b}): {diff_result}")
    # → Subtraction (10 - 3): 7

    # Multiplication: Multiplies two operands
    prod_result: int = operand_a * operand_b
    print(f"Multiplication ({operand_a} * {operand_b}): {prod_result}")
    # → Multiplication (10 * 3): 30

    # Division: Divides the first operand by the second, always returns a float
    div_result: float = operand_a / operand_b
    print(f"Division ({operand_a} / {operand_b}): {div_result}")
    # → Division (10 / 3): 3.3333333333333335

    # Floor Division: Divides and returns the integer part of the quotient
    # It rounds down to the nearest whole number.
    floor_div_result: int = operand_a // operand_b
    print(f"Floor Division ({operand_a} // {operand_b}): {floor_div_result}")
    # → Floor Division (10 // 3): 3

    negative_floor_div: int = -10 // 3 # Example with negative numbers
    print(f"Floor Division (-10 // 3): {negative_floor_div}")
    # → Floor Division (-10 // 3): -4 (rounds down to -4, not -3)

    # Modulus: Returns the remainder of the division
    mod_result: int = operand_a % operand_b
    print(f"Modulus ({operand_a} % {operand_b}): {mod_result}")
    # → Modulus (10 % 3): 1 (10 divided by 3 is 3 with a remainder of 1)

    # Exponentiation: Raises the first operand to the power of the second
    exp_result: int = operand_a ** operand_b
    print(f"Exponentiation ({operand_a} ** {operand_b}): {exp_result}")
    # → Exponentiation (10 ** 3): 1000

    # Mixing integer and float operands
    mixed_sum: float = operand_a + operand_c
    print(f"Mixed Addition ({operand_a} + {operand_c}): {mixed_sum}")
    # → Mixed Addition (10 + 2.5): 12.5
    # ℹ️ Result type promotion: If any operand is a float, the result is typically a float.

    # Unary operators: act on a single operand
    positive_num: int = 5
    negative_num: int = -positive_num # Unary negation
    print(f"Unary Negation (-{positive_num}): {negative_num}")
    # → Unary Negation (-5): -5

    positive_explicit: int = +negative_num # Unary positive (rarely used, usually implied)
    print(f"Unary Positive (+{negative_num}): {positive_explicit}")
    # → Unary Positive (-5): -5


# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns: Everyday Operator Usage
# ═══════════════════════════════════════════════════════════════

def section_2_syntax_common_patterns() -> None:
    """
    Explores common operator categories like comparison, logical, and assignment
    operators, which are used daily for decision-making and variable updates.
    """
    print("\nSECTION 2: Syntax & Common Patterns: Everyday Operator Usage")
    print("-----------------------------------------------------------")

    # Example 2.1: Comparison Operators
    # These operators compare two values and return a boolean (True or False).
    print("\n--- Comparison Operators ---")

    value_x: int = 15
    value_y: int = 20
    value_z: int = 15

    # Equality (==): Checks if two values are equal
    print(f"{value_x} == {value_y}: {value_x == value_y}") # Is 15 equal to 20?
    # → 15 == 20: False
    print(f"{value_x} == {value_z}: {value_x == value_z}") # Is 15 equal to 15?
    # → 15 == 15: True

    # Inequality (!=): Checks if two values are not equal
    print(f"{value_x} != {value_y}: {value_x != value_y}") # Is 15 not equal to 20?
    # → 15 != 20: True

    # Greater than (>): Checks if the left operand is greater than the right
    print(f"{value_x} > {value_y}: {value_x > value_y}")   # Is 15 greater than 20?
    # → 15 > 20: False

    # Less than (<): Checks if the left operand is less than the right
    print(f"{value_x} < {value_y}: {value_x < value_y}")   # Is 15 less than 20?
    # → 15 < 20: True

    # Greater than or equal to (>=):
    print(f"{value_x} >= {value_z}: {value_x >= value_z}") # Is 15 greater than or equal to 15?
    # → 15 >= 15: True

    # Less than or equal to (<=):
    print(f"{value_x} <= {value_y}: {value_x <= value_y}") # Is 15 less than or equal to 20?
    # → 15 <= 20: True

    # Example 2.2: Logical Operators
    # Combine conditional statements and return a boolean.
    print("\n--- Logical Operators (and, or, not) ---")

    is_student: bool = True
    has_discount_card: bool = False
    is_senior: bool = True
    age: int = 65

    # 'and': Returns True if both operands are True
    eligible_for_student_discount: bool = is_student and has_discount_card
    print(f"Eligible for student discount (is_student and has_discount_card): {eligible_for_student_discount}")
    # → Eligible for student discount (is_student and has_discount_card): False

    # 'or': Returns True if at least one operand is True
    eligible_for_special_rate: bool = is_student or is_senior
    print(f"Eligible for special rate (is_student or is_senior): {eligible_for_special_rate}")
    # → Eligible for special rate (is_student or is_senior): True

    # 'not': Inverts the boolean value of the operand
    not_a_student: bool = not is_student
    print(f"Not a student (not is_student): {not_a_student}")
    # → Not a student (not is_student): False

    # Combining multiple logical operations
    can_vote: bool = age >= 18 and not is_senior # Assuming seniors can also vote
    print(f"Can vote (age >= 18 and not is_senior for condition): {can_vote}")
    # → Can vote (age >= 18 and not is_senior for condition): False (because not is_senior is False when is_senior is True)
    # ⚠️ Let's fix this logic for "can vote" to be more realistic:
    can_vote_realistic: bool = age >= 18
    print(f"Can vote (age >= 18): {can_vote_realistic}")
    # → Can vote (age >= 18): True

    # Example 2.3: Assignment Operators
    # Assigns a value to a variable. Augmented assignment operators perform
    # an operation and then assign the result.
    print("\n--- Assignment Operators ---")

    current_score: int = 100 # Simple assignment (=)
    print(f"Initial score: {current_score}")
    # → Initial score: 100

    # Add and assign (+=)
    current_score += 50 # Equivalent to: current_score = current_score + 50
    print(f"Score after += 50: {current_score}")
    # → Score after += 50: 150

    # Subtract and assign (-=)
    current_score -= 20 # Equivalent to: current_score = current_score - 20
    print(f"Score after -= 20: {current_score}")
    # → Score after -= 20: 130

    # Multiply and assign (*=)
    current_score *= 2  # Equivalent to: current_score = current_score * 2
    print(f"Score after *= 2: {current_score}")
    # → Score after *= 2: 260

    # Divide and assign (/=)
    current_score /= 4  # Equivalent to: current_score = current_score / 4
    print(f"Score after /= 4: {current_score}")
    # → Score after /= 4: 65.0

    # Floor divide and assign (//=)
    item_count: int = 17
    batch_size: int = 5
    batches_needed: int = 0
    batches_needed //= batch_size # This would be 0 // 5 = 0
    # ⚠️ Common mistake: For a new calculation, don't use augmented assignment like this.
    # ✅ Preferred/Correct: Calculate directly or assign after an operation.
    batches_needed = item_count // batch_size # Calculate new value
    print(f"Batches needed ({item_count} // {batch_size}): {batches_needed}")
    # → Batches needed (17 // 5): 3

    # Modulus and assign (%=)
    remainder_value: int = 25
    remainder_value %= 7 # Equivalent to: remainder_value = remainder_value % 7
    print(f"Remainder after %= 7: {remainder_value}")
    # → Remainder after %= 7: 4

    # Exponentiate and assign (**=)
    base_value: int = 2
    base_value **= 3 # Equivalent to: base_value = base_value ** 3
    print(f"Base value after **= 3: {base_value}")
    # → Base value after **= 3: 8

    # Example 2.4: Ternary Operator (Conditional Expression)
    # A concise way to assign a value based on a condition.
    print("\n--- Ternary Operator (Conditional Expression) ---")

    temperature: int = 28
    weather_status: str = "Hot" if temperature > 25 else "Pleasant"
    print(f"Weather status for {temperature}°C: {weather_status}")
    # → Weather status for 28°C: Hot

    temperature = 20
    weather_status = "Hot" if temperature > 25 else "Pleasant"
    print(f"Weather status for {temperature}°C: {weather_status}")
    # → Weather status for 20°C: Pleasant

    # ℹ️ This is equivalent to:
    # if temperature > 25:
    #     weather_status = "Hot"
    # else:
    #     weather_status = "Pleasant"


# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas: Operator Quirks and Common Mistakes
# ═══════════════════════════════════════════════════════════════

def section_3_edge_cases_gotchas() -> None:
    """
    Highlights common pitfalls and tricky behaviors of operators,
    especially concerning floating-point arithmetic, object identity,
    and operator precedence.
    """
    print("\nSECTION 3: Edge Cases & Gotchas: Operator Quirks and Common Mistakes")
    print("------------------------------------------------------------------")

    # Example 3.1: Floating-Point Precision Issues with Equality (==)
    print("\n--- Floating-Point Precision Issues ---")
    # Due to the way computers represent floating-point numbers, direct equality
    # comparisons can be unreliable for floats.

    # Calculate 0.1 + 0.2
    sum_floats: float = 0.1 + 0.2
    print(f"0.1 + 0.2 = {sum_floats}")
    # → 0.1 + 0.2 = 0.30000000000000004

    # Compare with 0.3
    is_equal: bool = sum_floats == 0.3
    print(f"(0.1 + 0.2) == 0.3: {is_equal}")
    # → (0.1 + 0.2) == 0.3: False

    # ✅ Preferred/Pythonic: Compare floats within a tolerance (epsilon)
    epsilon: float = 1e-9 # A small tolerance value
    is_approximately_equal: bool = abs(sum_floats - 0.3) < epsilon
    print(f"abs((0.1 + 0.2) - 0.3) < {epsilon}: {is_approximately_equal}")
    # → abs((0.1 + 0.2) - 0.3) < 1e-09: True

    # Example 3.2: Identity vs. Equality (`is` vs `==`)
    print("\n--- Identity vs. Equality ---")
    # `==` checks if two objects have the same value.
    # `is` checks if two variables refer to the *exact same object* in memory.

    list_a: list[int] = [1, 2, 3]
    list_b: list[int] = [1, 2, 3]
    list_c: list[int] = list_a # list_c now refers to the same object as list_a

    print(f"list_a: {list_a}, list_b: {list_b}, list_c: {list_c}")
    # → list_a: [1, 2, 3], list_b: [1, 2, 3], list_c: [1, 2, 3]

    # Equality check (values are the same)
    print(f"list_a == list_b: {list_a == list_b}") # Do they have the same content?
    # → list_a == list_b: True
    print(f"list_a == list_c: {list_a == list_c}") # Do they have the same content?
    # → list_a == list_c: True

    # Identity check (are they the same object in memory?)
    print(f"list_a is list_b: {list_a is list_b}") # Are they the same object?
    # → list_a is list_b: False (They are distinct objects with same content)
    print(f"list_a is list_c: {list_a is list_c}") # Are they the same object?
    # → list_a is list_c: True (list_c is an alias for list_a)

    # 🔑 Key insight: Use `is` primarily for singletons like `None`, `True`, `False`.
    #    For other objects, use `==` for value comparison.
    my_variable: str | None = None
    print(f"my_variable is None: {my_variable is None}") # Correct way to check for None
    # → my_variable is None: True

    # ⚠️ Common mistake: Don't use `== None` for checking `None` as it can be less performant
    # and might behave unexpectedly if an object overloads `__eq__`.
    print(f"my_variable == None: {my_variable == None}") # This usually works, but `is None` is preferred.
    # → my_variable == None: True


    # Example 3.3: Operator Precedence and Associativity
    print("\n--- Operator Precedence ---")
    # Operators have different priorities (precedence). Parentheses can override this.
    # Higher precedence operators are evaluated first.

    # Multiplication has higher precedence than addition
    result_precedence_1: int = 5 + 3 * 2
    print(f"5 + 3 * 2 = {result_precedence_1}") # Evaluates as 5 + (3 * 2) = 5 + 6 = 11
    # → 5 + 3 * 2 = 11

    # Use parentheses to change the order of operations
    result_precedence_2: int = (5 + 3) * 2
    print(f"(5 + 3) * 2 = {result_precedence_2}") # Evaluates as (5 + 3) * 2 = 8 * 2 = 16
    # → (5 + 3) * 2 = 16

    # Associativity: When operators have the same precedence, associativity (left-to-right or right-to-left)
    # determines the order. Most Python operators are left-to-right associative.
    # Exception: Exponentiation (**) is right-to-left associative.
    exp_associativity_1: int = 2 ** 3 ** 2 # Evaluates as 2 ** (3 ** 2) = 2 ** 9 = 512
    print(f"2 ** 3 ** 2 = {exp_associativity_1}")
    # → 2 ** 3 ** 2 = 512

    exp_associativity_2: int = (2 ** 3) ** 2 # Explicit left-to-right
    print(f"(2 ** 3) ** 2 = {exp_associativity_2}") # Evaluates as (2 ** 3) ** 2 = 8 ** 2 = 64
    # → (2 ** 3) ** 2 = 64

    # Example 3.4: Short-Circuiting in Logical Operators (`and`, `or`)
    print("\n--- Short-Circuiting ---")
    # Logical operators evaluate operands from left to right and stop as soon as
    # the result can be determined.

    def check_true() -> bool:
        """A function that returns True and prints a message."""
        print("  (check_true() called)")
        return True

    def check_false() -> bool:
        """A function that returns False and prints a message."""
        print("  (check_false() called)")
        return False

    # 'and' short-circuits if the first operand is False
    print("Evaluating False and check_true():")
    result_and: bool = check_false() and check_true()
    print(f"Result: {result_and}")
    # → Evaluating False and check_true():
    # →   (check_false() called)
    # → Result: False
    # ℹ️ check_true() was never called because check_false() was already False.

    # 'or' short-circuits if the first operand is True
    print("\nEvaluating True or check_false():")
    result_or: bool = check_true() or check_false()
    print(f"Result: {result_or}")
    # → Evaluating True or check_false():
    # →   (check_true() called)
    # → Result: True
    # ℹ️ check_false() was never called because check_true() was already True.


# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns: Beyond the Basics
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """
    Delves into more specialized operators like membership and identity,
    and introduces bitwise operators for low-level data manipulation.
    """
    print("\nSECTION 4: Intermediate Patterns: Beyond the Basics")
    print("---------------------------------------------------")

    # Example 4.1: Membership Operators (`in`, `not in`)
    # Check if a value is present in a sequence (string, list, tuple, set, dict keys).
    print("\n--- Membership Operators ---")

    my_list: list[str] = ["apple", "banana", "cherry"]
    my_string: str = "hello world"
    my_dictionary: dict[str, int] = {"name": 1, "age": 2}

    # 'in': Checks if an element is present
    print(f"'banana' in my_list: {'banana' in my_list}")
    # → 'banana' in my_list: True
    print(f"'grape' in my_list: {'grape' in my_list}")
    # → 'grape' in my_list: False

    print(f"'world' in my_string: {'world' in my_string}") # Substring check
    # → 'world' in my_string: True
    print(f"'xyz' in my_string: {'xyz' in my_string}")
    # → 'xyz' in my_string: False

    print(f"'name' in my_dictionary: {'name' in my_dictionary}") # Checks keys
    # → 'name' in my_dictionary: True
    print(f"1 in my_dictionary.values(): {1 in my_dictionary.values()}") # Checks values explicitly
    # → 1 in my_dictionary.values(): True

    # 'not in': Checks if an element is not present
    print(f"'grape' not in my_list: {'grape' not in my_list}")
    # → 'grape' not in my_list: True

    # Example 4.2: Identity Operators (`is`, `is not`) - Revisited with more types
    print("\n--- Identity Operators (Revisited) ---")
    # As discussed, `is` checks if two variables refer to the same object.
    # This is particularly relevant for mutable objects and singletons.

    num1: int = 1000
    num2: int = 1000
    # Python often interns small integers (typically -5 to 256) for optimization,
    # making `is` True for them. For larger integers, new objects are created.
    print(f"{num1} is {num2}: {num1 is num2}")
    # → 1000 is 1000: False (for larger integers, new objects are usually created)

    small_num1: int = 50
    small_num2: int = 50
    print(f"{small_num1} is {small_num2}: {small_num1 is small_num2}")
    # → 50 is 50: True (small integers are often interned)

    text1: str = "hello"
    text2: str = "hello"
    # Python also interns some strings for optimization.
    print(f"'{text1}' is '{text2}': {text1 is text2}")
    # → 'hello' is 'hello': True

    text3: str = "hello world"
    text4: str = "hello world"
    print(f"'{text3}' is '{text4}': {text3 is text4}")
    # → 'hello world' is 'hello world': True (Even multi-word strings can be interned if literal)

    # Example 4.3: Bitwise Operators
    # Perform operations on individual bits of integers. Used in low-level
    # programming, flag management, encryption, etc.
    print("\n--- Bitwise Operators ---")

    num_a_bits: int = 0b1100 # Binary: 12 (Decimal)
    num_b_bits: int = 0b1010 # Binary: 10 (Decimal)
    print(f"num_a_bits (12): {bin(num_a_bits)}") # Display binary representation
    # → num_a_bits (12): 0b1100
    print(f"num_b_bits (10): {bin(num_b_bits)}")
    # → num_b_bits (10): 0b1010

    # Bitwise AND (&): Sets each bit to 1 if both bits are 1
    # 0b1100 (12)
    # 0b1010 (10)
    # --------
    # 0b1000 (8)
    and_result: int = num_a_bits & num_b_bits
    print(f"AND ({bin(num_a_bits)} & {bin(num_b_bits)}): {bin(and_result)} ({and_result})")
    # → AND (0b1100 & 0b1010): 0b1000 (8)

    # Bitwise OR (|): Sets each bit to 1 if at least one of the bits is 1
    # 0b1100 (12)
    # 0b1010 (10)
    # --------
    # 0b1110 (14)
    or_result: int = num_a_bits | num_b_bits
    print(f"OR ({bin(num_a_bits)} | {bin(num_b_bits)}): {bin(or_result)} ({or_result})")
    # → OR (0b1100 | 0b1010): 0b1110 (14)

    # Bitwise XOR (^): Sets each bit to 1 if only one of the bits is 1 (exclusive OR)
    # 0b1100 (12)
    # 0b1010 (10)
    # --------
    # 0b0110 (6)
    xor_result: int = num_a_bits ^ num_b_bits
    print(f"XOR ({bin(num_a_bits)} ^ {bin(num_b_bits)}): {bin(xor_result)} ({xor_result})")
    # → XOR (0b1100 ^ 0b1010): 0b110 (6)

    # Bitwise NOT (~): Inverts all bits (unary operator)
    # For positive integers, it's