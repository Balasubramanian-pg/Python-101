"""
If Else: Controlling Program Flow

This module introduces the fundamental 'if-else' conditional statements in Python,
essential for making decisions and directing the execution path of your programs.
You'll learn how to execute different blocks of code based on whether a condition is true or false.

What you will learn:
• How to use the basic `if` statement for conditional execution.
• The role of `else` to provide an alternative execution path.
• Employing `elif` for handling multiple distinct conditions efficiently.
• Understanding Python's concept of "truthiness" and "falsiness".
• Writing clear and maintainable conditional logic using Pythonic idioms.
• Applying `if-else` in a practical, mini-program scenario.

Prerequisites:
• Basic understanding of Python syntax (variables, data types).
• Knowledge of comparison operators (==, !=, <, >, <=, >=).
• Familiarity with boolean values (True, False).

Key Concepts Covered:
• `if` statement
• `else` statement
• `elif` statement
• Conditional expressions (ternary operator)
• Boolean expressions
• Truthiness and Falsiness
• Indentation (code blocks)
• Logical operators (`and`, `or`, `not`)
• Guard clauses
• Short-circuiting
"""

import sys # Used for accessing Python version and exiting gracefully in examples

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept - The `if` Statement
# ═══════════════════════════════════════════════════════════════

def section_1_core_concept() -> None:
    """
    Demonstrates the fundamental `if` statement and its role in conditional execution.
    Introduces boolean expressions and the importance of indentation.
    """
    print("\nSECTION 1: Core Concept - The `if` Statement")
    print("--------------------------------------------------")

    # 🔑 Key insight: The `if` statement executes a block of code only if its condition is True.
    # The condition must evaluate to a boolean (True or False).

    temperature: int = 25 # Define a variable for temperature
    print(f"Current temperature: {temperature}°C")

    # Example 1.1: Basic `if` statement
    # Checks if the temperature is greater than 20.
    if temperature > 20: # Condition: temperature > 20. This is True (25 > 20).
        print("It's a warm day!") # This line will execute because the condition is True.
    # → It's a warm day!

    # Example 1.2: `if` statement with a False condition
    # Checks if the temperature is less than 10.
    if temperature < 10: # Condition: temperature < 10. This is False (25 < 10).
        print("It's quite cold.") # This line will NOT execute because the condition is False.
    print("Moving on from temperature check.") # This line executes regardless of the `if` condition.
    # → Moving on from temperature check.

    # ℹ️ Note: Indentation defines the code block. All lines at the same indentation level
    # after the `if` statement belong to that `if` block.
    # The standard indentation is 4 spaces.

    is_raining: bool = True # A boolean variable directly used as a condition
    if is_raining: # Condition: is_raining. This is True.
        print("Remember to take an umbrella.") # This line executes.
        print("Stay dry!") # This line also executes as it's part of the same `if` block.
    # → Remember to take an umbrella.
    # → Stay dry!

    # Example 1.3: Using comparison operators
    age: int = 18 # Define an age variable
    required_age: int = 18 # Define a required age

    # Checks if the age is greater than or equal to the required age.
    if age >= required_age: # Condition: age >= required_age. This is True (18 >= 18).
        print(f"You are {age} years old. You are old enough to vote.") # Executes.
    # → You are 18 years old. You are old enough to vote.

    # 🐛 Bug source: Incorrect indentation breaks the code block.
    # The following would cause an IndentationError if uncommented:
    # if True:
    # print("This would be an error!") # Incorrectly indented

# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns - `if-else` and `if-elif-else`
# ═══════════════════════════════════════════════════════════════

def section_2_syntax_and_patterns() -> None:
    """
    Explores the `if-else` and `if-elif-else` constructs for more comprehensive conditional logic.
    Provides examples for different scenarios.
    """
    print("\nSECTION 2: Syntax & Common Patterns - `if-else` and `if-elif-else`")
    print("--------------------------------------------------------------------")

    # 🔑 Key insight: `if-else` provides an alternative path when the `if` condition is False.
    # `if-elif-else` handles multiple exclusive conditions sequentially.

    # Example 2.1: `if-else` statement
    # Use `if-else` when you have exactly two possible outcomes.
    score: int = 75 # Student's score
    passing_score: int = 60 # Minimum score to pass

    if score >= passing_score: # Condition: score >= passing_score. True (75 >= 60).
        print(f"Score: {score}. Congratulations, you passed!") # Executes.
    else: # This block executes if the `if` condition is False.
        print(f"Score: {score}. Unfortunately, you did not pass.") # Does not execute.
    # → Score: 75. Congratulations, you passed!

    score = 55 # Change score for the next run
    if score >= passing_score: # Condition: score >= passing_score. False (55 >= 60).
        print(f"Score: {score}. Congratulations, you passed!") # Does not execute.
    else: # This block executes.
        print(f"Score: {score}. Unfortunately, you did not pass.") # Executes.
    # → Score: 55. Unfortunately, you did not pass.

    # Example 2.2: `if-elif-else` statement
    # Use `if-elif-else` when you have several possible outcomes and only one should be chosen.
    # Python checks conditions from top to bottom. The first True condition's block is executed,
    # and the rest of the `elif` and `else` blocks are skipped.

    grade_percentage: int = 88 # Student's grade percentage
    print(f"\nEvaluating grade for {grade_percentage}%:")

    if grade_percentage >= 90: # Is 88 >= 90? False.
        print("Grade: A")
    elif grade_percentage >= 80: # Is 88 >= 80? True. This block executes.
        print("Grade: B")
    elif grade_percentage >= 70: # This block is skipped.
        print("Grade: C")
    elif grade_percentage >= 60: # This block is skipped.
        print("Grade: D")
    else: # This block is skipped.
        print("Grade: F")
    # → Evaluating grade for 88%:
    # → Grade: B

    grade_percentage = 45 # Another grade for testing
    print(f"\nEvaluating grade for {grade_percentage}%:")
    if grade_percentage >= 90: # False
        print("Grade: A")
    elif grade_percentage >= 80: # False
        print("Grade: B")
    elif grade_percentage >= 70: # False
        print("Grade: C")
    elif grade_percentage >= 60: # False
        print("Grade: D")
    else: # All `if` and `elif` conditions were False, so `else` executes.
        print("Grade: F")
    # → Evaluating grade for 45%:
    # → Grade: F

    # Example 2.3: Order matters in `if-elif-else`
    # ⚠️ Common mistake: Incorrect order of conditions can lead to unexpected results.
    # Conditions should be ordered from most specific to least specific, or in a clear logical sequence.
    age_group: int = 15

    # WRONG APPROACH (if you want to catch specific age first):
    # if age_group >= 10:
    #     print("Eligible for general admission.") # This would catch 15-year-olds, preventing them from being seen as teens.
    # elif age_group >= 13:
    #     print("Eligible for teen discount.")
    # else:
    #     print("Child ticket.")

    # ✅ Preferred/Pythonic: Order conditions from highest to lowest or specific to general.
    print(f"\nDetermining ticket price for age {age_group}:")
    if age_group >= 18: # Is 15 >= 18? False.
        print("Adult ticket price.")
    elif age_group >= 13: # Is 15 >= 13? True. This executes.
        print("Teen discount ticket price.")
    elif age_group >= 5: # This is skipped.
        print("Child ticket price.")
    else: # This is skipped.
        print("Infant free admission.")
    # → Determining ticket price for age 15:
    # → Teen discount ticket price.

# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas - Truthiness, Falsiness, and Indentation
# ═══════════════════════════════════════════════════════════════

def section_3_edge_cases_and_gotchas() -> None:
    """
    Explains Python's truthiness and falsiness concept, common indentation errors,
    and pitfalls like floating-point comparisons.
    """
    print("\nSECTION 3: Edge Cases & Gotchas - Truthiness, Falsiness, and Indentation")
    print("------------------------------------------------------------------------")

    # 🔑 Key insight: In Python, many non-boolean values are treated as either True or False
    # when used in a boolean context (like an `if` condition). This is called "truthiness" and "falsiness".

    # Falsy values:
    # • None
    # • False
    # • Numeric zero of all types (0, 0.0, 0j)
    # • Empty sequences ('', [], ())
    # • Empty mappings ({})
    # • Empty sets (set())
    # • Empty ranges (range(0))

    # All other values are considered Truthy.

    # Example 3.1: Truthiness and Falsiness
    my_string: str = "Hello" # A non-empty string is truthy
    if my_string: # Condition: "Hello". This evaluates to True.
        print(f"String '{my_string}' is truthy.") # Executes.
    # → String 'Hello' is truthy.

    empty_string: str = "" # An empty string is falsy
    if not empty_string: # Condition: not "". This evaluates to not False, which is True.
        print(f"String '{empty_string}' is falsy (empty).") # Executes.
    # → String '' is falsy (empty).

    my_list: list[int] = [1, 2, 3] # A non-empty list is truthy
    if my_list: # Condition: [1, 2, 3]. This evaluates to True.
        print(f"List {my_list} is truthy.") # Executes.
    # → List [1, 2, 3] is truthy.

    empty_list: list[int] = [] # An empty list is falsy
    if not empty_list: # Condition: not []. This evaluates to not False, which is True.
        print(f"List {empty_list} is falsy (empty).") # Executes.
    # → List [] is falsy (empty).

    zero_value: int = 0 # Zero is falsy
    if not zero_value: # Condition: not 0. This evaluates to not False, which is True.
        print(f"Integer {zero_value} is falsy.") # Executes.
    # → Integer 0 is falsy.

    none_value: None = None # None is falsy
    if none_value is None: # ✅ Preferred/Pythonic: Use `is None` or `is not None` for None checks.
        print(f"Value {none_value} is None and therefore falsy.") # Executes.
    # → Value None is None and therefore falsy.

    # Example 3.2: Indentation Gotchas
    # Python uses indentation to define code blocks. Incorrect indentation leads to errors or logical bugs.
    x_val: int = 10
    if x_val > 5:
        print("x is greater than 5.") # This line is part of the `if` block.
        # This print statement is also part of the `if` block.
        print("This is still inside the if block.")
    print("This line is outside the if block.") # This line always executes.
    # → x is greater than 5.
    # → This is still inside the if block.
    # → This line is outside the if block.

    # ⚠️ Common mistake: Mixing tabs and spaces can cause `IndentationError`.
    # Always use 4 spaces for indentation (PEP 8 standard).
    # If you copy-paste code with mixed indentation, Python might complain.

    # Example 3.3: Floating-point comparison issues
    # Due to how floating-point numbers are represented in binary, direct equality
    # comparisons (`==`) can sometimes yield unexpected results.
    price_a: float = 0.1 + 0.2 # This might not be exactly 0.3
    price_b: float = 0.3

    print(f"\nFloating point comparison: {price_a} == {price_b}?")
    if price_a == price_b: # This might evaluate to False, even if mathematically they should be equal.
        print("Prices are exactly equal.")
    else:
        print(f"Prices are NOT exactly equal. price_a={price_a}, price_b={price_b}")
    # → Floating point comparison: 0.30000000000000004 == 0.3?
    # → Prices are NOT exactly equal. price_a=0.30000000000000004, price_b=0.3

    # ✅ Preferred/Pythonic: Compare floats within a tolerance (epsilon).
    epsilon: float = 1e-9 # A small tolerance value
    if abs(price_a - price_b) < epsilon: # Check if the absolute difference is very small.
        print("Prices are approximately equal.")
    else:
        print("Prices are not approximately equal.")
    # → Prices are approximately equal.

# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns - Nested Ifs and Logical Operators
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """
    Explores more complex conditional structures using nested `if` statements
    and logical operators (`and`, `or`, `not`).
    """
    print("\nSECTION 4: Intermediate Patterns - Nested Ifs and Logical Operators")
    print("-------------------------------------------------------------------")

    # 🔑 Key insight: Nested `if` statements allow for conditions within conditions.
    # Logical operators combine multiple conditions into a single boolean expression.

    # Example 4.1: Nested `if` statements
    # Used when a secondary condition only makes sense if a primary condition is met.
    user_status: str = "active" # User's account status
    has_premium: bool = True # Does the user have premium subscription?

    print(f"User status: {user_status}, Premium: {has_premium}")

    if user_status == "active": # Primary condition: Is the user active?
        print("User account is active.")
        if has_premium: # Secondary condition: Does the active user have premium?
            print("Granting access to premium features.") # Executes.
        else:
            print("Accessing standard features.") # Does not execute.
    else:
        print("User account is inactive. Access denied.") # Does not execute.
    # → User status: active, Premium: True
    # → User account is active.
    # → Granting access to premium features.

    user_status = "inactive" # Change status
    if user_status == "active": # False
        print("User account is active.")
        if has_premium:
            print("Granting access to premium features.")
        else:
            print("Accessing standard features.")
    else: # Executes.
        print("User account is inactive. Access denied.")
    # → User account is inactive. Access denied.

    # ℹ️ Note: While nesting is sometimes necessary, deeply nested `if` statements
    # can reduce readability. Consider refactoring with logical operators or functions.

    # Example 4.2: Using `and` logical operator
    # The `and` operator returns True if BOTH conditions are True.
    current_hour: int = 14 # Current hour (24-hour format)
    is_weekend: bool = False # Is it a weekend?

    # Check if it's working hours (9-17) AND not a weekend.
    if current_hour >= 9 and current_hour <= 17 and not is_weekend: # True and True and True -> True
        print(f"\nIt's {current_hour}:00. Business hours: Office is open.") # Executes.
    else:
        print(f"\nIt's {current_hour}:00. Outside business hours or weekend: Office is closed.") # Does not execute.
    # → It's 14:00. Business hours: Office is open.

    current_hour = 20 # Change hour
    if current_hour >= 9 and current_hour <= 17 and not is_weekend: # False (20 not <= 17)
        print(f"\nIt's {current_hour}:00. Business hours: Office is open.")
    else: # Executes.
        print(f"\nIt's {current_hour}:00. Outside business hours or weekend: Office is closed.")
    # → It's 20:00. Outside business hours or weekend: Office is closed.

    # Example 4.3: Using `or` logical operator
    # The `or` operator returns True if AT LEAST ONE condition is True.
    weather: str = "sunny" # Current weather
    is_holiday: bool = True # Is today a holiday?

    # Check if it's good for a picnic (sunny OR holiday).
    if weather == "sunny" or is_holiday: # True or True -> True
        print(f"\nWeather is {weather}, holiday status: {is_holiday}. Let's go for a picnic!") # Executes.
    else:
        print(f"\nWeather is {weather}, holiday status: {is_holiday}. Maybe another day for a picnic.")
    # → Weather is sunny, holiday status: True. Let's go for a picnic!

    weather = "rainy" # Change weather
    is_holiday = False # Change holiday status
    if weather == "sunny" or is_holiday: # False or False -> False
        print(f"\nWeather is {weather}, holiday status: {is_holiday}. Let's go for a picnic!")
    else: # Executes.
        print(f"\nWeather is {weather}, holiday status: {is_holiday}. Maybe another day for a picnic.")
    # → Weather is rainy, holiday status: False. Maybe another day for a picnic.

    # Example 4.4: Combining `and`, `or`, `not`
    # Parentheses can be used to control the order of evaluation (like in math).
    # `not` has highest precedence, then `and`, then `or`.
    has_ticket: bool = True
    has_id: bool = True
    is_vip: bool = False

    # Allow entry if (has ticket AND has ID) OR is VIP.
    if (has_ticket and has_id) or is_vip: # (True and True) or False -> True or False -> True
        print("\nEntry granted!") # Executes.
    else:
        print("\nEntry denied.")
    # → Entry granted!

    has_ticket = False
    if (has_ticket and has_id) or is_vip: # (False and True) or False -> False or False -> False
        print("\nEntry granted!")
    else: # Executes.
        print("\nEntry denied.")
    # → Entry denied.

# ═══════════════════════════════════════════════════════════════
# SECTION 5: Pythonic Idioms - Ternary Operator and Guard Clauses
# ═══════════════════════════════════════════════════════════════

def section_5_pythonic_idioms() -> None:
    """
    Introduces Pythonic ways to handle conditionals, including the ternary operator
    for concise assignments and guard clauses for early exits.
    """
    print("\nSECTION 5: Pythonic Idioms - Ternary Operator and Guard Clauses")
    print("---------------------------------------------------------------")

    # 🔑 Key insight: Python offers concise ways to express conditional logic.
    # The ternary operator simplifies conditional assignments, and guard clauses
    # improve function readability by handling invalid cases early.

    # Example 5.1: Conditional Expressions (Ternary Operator)
    # Syntax: `value_if_true if condition else value_if_false`
    # Used for assigning a value to a variable based on a condition in a single line.

    is_logged_in: bool = True # User login status
    status_message: str

    # Traditional `if-else` for assignment:
    # if is_logged_in:
    #     status_message = "Welcome back!"
    # else:
    #     status_message = "Please log in."

    # ✅ Preferred/Pythonic: Using a conditional expression for assignment.
    status_message = "Welcome back!" if is_logged_in else "Please log in."
    print(f"Login status: {status_message}")
    # → Login status: Welcome back!

    is_logged_in = False
    status_message = "Welcome back!" if is_logged_in else "Please log in."
    print(f"Login status: {status_message}")
    # → Login status: Please log in.

    # Another example: determining parity
    number: int = 7
    parity: str = "even" if number % 2 == 0 else "odd"
    print(f"The number {number} is {parity}.")
    # → The number 7 is odd.

    number = 10
    parity = "even" if number % 2 == 0 else "odd"
    print(f"The number {number} is {parity}.")
    # → The number 10 is even.

    # ℹ️ Note: While powerful, avoid overly complex conditional expressions
    # as they can hurt readability. Keep them simple and clear.

    # Example 5.2: Guard Clauses (Early Exit)
    # A guard clause is an `if` statement that checks for a condition and, if met,
    # exits the function (or loop) early, typically to handle invalid inputs or edge cases.
    # This reduces nesting and makes the main logic clearer.

    def calculate_discount(price: float, discount_percentage: float | None) -> float:
        """
        Calculates the final price after applying a discount.
        Uses a guard clause to handle invalid discount percentages.
        """
        # WHY: Validate input early to prevent errors and simplify main logic.
        # This is a guard clause: if the condition is met, we exit immediately.
        if discount_percentage is None or not (0 <= discount_percentage <= 100):
            print(f"⚠️ Invalid discount percentage provided ({discount_percentage}). Applying no discount.")
            return price # Exit early, return original price

        # If we reach here, the discount_percentage is valid.
        discount_amount: float = price * (discount_percentage / 100)
        final_price: float = price - discount_amount
        print(f"Original price: ${price:.2f}, Discount: {discount_percentage:.0f}%, Final price: ${final_price:.2f}")
        return final_price

    print("\n--- Discount Calculation Examples ---")
    calculate_discount(100.0, 10.0)
    # → Original price: $100.00, Discount: 10%, Final price: $90.00
    calculate_discount(50.0, None)
    # → ⚠️ Invalid discount percentage provided (None). Applying no discount.
    # → $50.00
    calculate_discount(200.0, 120.0) # Invalid discount
    # → ⚠️ Invalid discount percentage provided (120.0). Applying no discount.
    # → $200.00
    calculate_discount(75.0, 0.0) # Zero discount
    # → Original price: $75.00, Discount: 0%, Final price: $75.00

# ═══════════════════════════════════════════════════════════════
# SECTION 6: Real-World Mini-Program - Simple User Authentication System
# ═══════════════════════════════════════════════════════════════

# This section demonstrates `if-elif-else` in a more cohesive application.
# It uses a class definition for better organization.

class User:
    """Represents a user in the system with a username, password, and role."""
    def __init__(self, username: str, password: str, role: str) -> None:
        self.username: str = username
        self.password: str = password
        self.role: str = role # e.g., "admin", "editor", "viewer"

class AuthSystem:
    """Manages user authentication and authorization."""
    def __init__(self) -> None:
        # WHY: Initialize with some predefined users for demonstration.
        self.users: list[User] = [
            User("admin_user", "admin123", "admin"),
            User("editor_user", "editor456", "editor"),
            User("viewer_user", "viewer789", "viewer"),
        ]

    def authenticate_user(self, username: str, password: str) -> User | None:
        """
        Attempts to authenticate a user.
        Returns the User object if successful