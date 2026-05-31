"""Parameters

This module explores the fundamental concept of parameters in Python functions, explaining how they enable functions to accept and process external data. You will learn about the different types of parameters, their syntax, and best practices for using them effectively to create flexible and reusable code.

What you will learn:
*   The distinction between parameters (definition) and arguments (call).
*   How to define functions with positional and keyword parameters.
*   The use of default parameter values to make functions more versatile.
*   Common pitfalls like mutable default arguments and how to avoid them.
*   Advanced techniques using *args and **kwargs for flexible argument handling.
*   Pythonic approaches to designing readable and robust function signatures.
*   How Python handles parameter passing (pass by object reference).

Prerequisites:
*   Basic understanding of Python variables and data types (integers, strings, lists).
*   Familiarity with defining and calling simple functions without parameters.
*   Knowledge of control flow statements (if/else, for loops).

Key Concepts Covered:
*   Parameters vs. Arguments
*   Positional Arguments
*   Keyword Arguments
*   Default Parameter Values
*   Mutable Default Argument Trap
*   Arbitrary Positional Arguments (*args)
*   Arbitrary Keyword Arguments (**kwargs)
*   Argument Unpacking
*   Position-Only Parameters (/)
*   Keyword-Only Parameters (*)
*   Pass by Object Reference
*   Immutability and Mutability with Parameters
"""

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: Understanding Function Parameters
# ═══════════════════════════════════════════════════════════════

# Parameters are placeholders in a function definition that receive values
# when the function is called. These values are known as arguments.

def greet_user() -> None: # A function with no parameters
    """Greets a generic user."""
    print("Hello, Pythonista!") # Prints a fixed greeting
    # → Hello, Pythonista!

def greet_specific_user(name: str) -> None: # 'name' is a parameter
    """Greets a specific user by their name."""
    print(f"Hello, {name}!") # Uses the 'name' parameter in the greeting
    # → Hello, Alice!

def add_numbers(num1: int, num2: int) -> int: # 'num1' and 'num2' are parameters
    """Adds two integers and returns their sum."""
    return num1 + num2 # Returns the sum of the two numbers

print("SECTION 1: Core Concept: Understanding Function Parameters")
print("---------------------------------------------------------")

# Calling functions with arguments:
print("\n--- Calling functions ---")
greet_user() # Calling the function with no arguments
# → Hello, Pythonista!

greet_specific_user("Alice") # "Alice" is an argument passed to the 'name' parameter
# → Hello, Alice!

# When calling a function, the values provided are called arguments.
# The variables defined in the function signature are called parameters.
first_number: int = 10 # Define a variable for the first argument
second_number: int = 20 # Define a variable for the second argument
sum_result: int = add_numbers(first_number, second_number) # 10 and 20 are arguments
print(f"The sum of {first_number} and {second_number} is: {sum_result}")
# → The sum of 10 and 20 is: 30

# 🔑 Key insight: Parameters make functions reusable and dynamic,
# allowing them to operate on different data inputs without modification.

# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns: Positional and Keyword Arguments
# ═══════════════════════════════════════════════════════════════

# Python supports different ways to pass arguments to parameters.

def describe_animal(animal_type: str, name: str, age: int) -> None:
    """Describes an animal using its type, name, and age."""
    print(f"This is a {animal_type} named {name}, and it is {age} years old.")

print("\nSECTION 2: Syntax & Common Patterns: Positional and Keyword Arguments")
print("-------------------------------------------------------------------")

print("\n--- Positional Arguments ---")
# Arguments are matched to parameters by their position.
describe_animal("dog", "Buddy", 5) # "dog" -> animal_type, "Buddy" -> name, 5 -> age
# → This is a dog named Buddy, and it is 5 years old.

# ⚠️ Common mistake: Incorrect order will lead to logical errors or runtime errors.
# describe_animal("Buddy", "dog", 5) # This would assign "Buddy" to animal_type, which is wrong.

print("\n--- Keyword Arguments ---")
# Arguments are matched to parameters by their name, regardless of position.
describe_animal(animal_type="cat", name="Whiskers", age=3) # Explicitly naming parameters
# → This is a cat named Whiskers, and it is 3 years old.

# Keyword arguments allow for more readable code, especially with many parameters.
describe_animal(age=2, animal_type="bird", name="Chirpy") # Order doesn't matter for keyword args
# → This is a bird named Chirpy, and it is 2 years old.

print("\n--- Mixing Positional and Keyword Arguments ---")
# Positional arguments must always come before keyword arguments.
describe_animal("fish", name="Nemo", age=1) # "fish" is positional, others are keyword
# → This is a fish named Nemo, and it is 1 years old.

# 🐛 Bug source: Keyword arguments before positional arguments will raise a TypeError.
# describe_animal(name="Goldie", "fish", age=1) # This line would cause a SyntaxError or TypeError.

print("\n--- Default Parameter Values ---")
# Parameters can have default values, making them optional during function calls.
def send_message(message: str, recipient: str = "Friend", sender: str = "Anonymous") -> None:
    """Sends a message to a recipient from a sender."""
    print(f"From {sender} to {recipient}: {message}")

send_message("Hello there!") # Only required argument 'message' is provided
# → From Anonymous to Friend: Hello there!

send_message("See you soon!", recipient="Alice") # Override recipient, sender uses default
# → From Anonymous to Alice: See you soon!

send_message("Meeting at 5 PM", recipient="Bob", sender="Charlie") # Override all defaults
# → From Charlie to Bob: Meeting at 5 PM

send_message(sender="Eve", message="Good morning!", recipient="David") # Order of keyword args doesn't matter
# → From Eve to David: Good morning!

# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas: What Beginners Always Get Wrong
# ═══════════════════════════════════════════════════════════════

print("\nSECTION 3: Edge Cases & Gotchas: What Beginners Always Get Wrong")
print("----------------------------------------------------------------")

print("\n--- Gotcha 1: Mutable Default Argument Trap ---")
# ⚠️ Common mistake: Using mutable objects (like lists, dictionaries, sets)
# as default arguments can lead to unexpected behavior.
# The default object is created only once when the function is defined,
# not each time the function is called.

def add_item_wrong(item: str, item_list: list[str] = []) -> list[str]: # Default list created ONCE
    """Adds an item to a list (WRONG way with mutable default)."""
    item_list.append(item) # Modifies the same list object
    return item_list

print("\n--- Demonstrating the mutable default trap (WRONG) ---")
shopping_list1: list[str] = add_item_wrong("Apples")
print(f"Shopping list 1: {shopping_list1}")
# → Shopping list 1: ['Apples']

shopping_list2: list[str] = add_item_wrong("Bananas") # Expected: ['Bananas'], Actual: ['Apples', 'Bananas']
print(f"Shopping list 2: {shopping_list2}")
# → Shopping list 2: ['Apples', 'Bananas']

shopping_list3: list[str] = add_item_wrong("Oranges") # Expected: ['Oranges'], Actual: ['Apples', 'Bananas', 'Oranges']
print(f"Shopping list 3: {shopping_list3}")
# → Shopping list 3: ['Apples', 'Bananas', 'Oranges']

# ✅ Preferred/Pythonic: Use None as a default, and initialize the mutable object inside the function.
def add_item_correct(item: str, item_list: list[str] | None = None) -> list[str]:
    """Adds an item to a list (CORRECT way using None default)."""
    if item_list is None: # Check if a list was provided
        item_list = [] # Create a new list if none was provided
    item_list.append(item) # Append to the provided or new list
    return item_list

print("\n--- Demonstrating the correct way with None default ---")
shopping_list_a: list[str] = add_item_correct("Milk")
print(f"Shopping list A: {shopping_list_a}")
# → Shopping list A: ['Milk']

shopping_list_b: list[str] = add_item_correct("Bread")
print(f"Shopping list B: {shopping_list_b}")
# → Shopping list B: ['Bread']

my_custom_list: list[str] = ["Eggs"]
shopping_list_c: list[str] = add_item_correct("Cheese", my_custom_list) # Using an explicit list
print(f"Shopping list C (custom): {shopping_list_c}")
# → Shopping list C (custom): ['Eggs', 'Cheese']
print(f"Original custom list: {my_custom_list}") # Original list is modified as expected
# → Original custom list: ['Eggs', 'Cheese']

print("\n--- Gotcha 2: Argument Count Mismatch ---")
# Python enforces the correct number of arguments unless defaults are provided.

def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle."""
    return length * width

# 🐛 Bug source: Calling with too few arguments
try:
    # calculate_area(10) # This would raise a TypeError: missing 1 required positional argument: 'width'
    print("Attempting to call calculate_area(10)...")
    calculate_area(10)
except TypeError as e:
    print(f"Caught expected error: {e}")
    # → Caught expected error: calculate_area() missing 1 required positional argument: 'width'

# 🐛 Bug source: Calling with too many arguments
try:
    # calculate_area(10, 5, 2) # This would raise a TypeError: calculate_area() takes 2 positional arguments but 3 were given
    print("Attempting to call calculate_area(10, 5, 2)...")
    calculate_area(10, 5, 2)
except TypeError as e:
    print(f"Caught expected error: {e}")
    # → Caught expected error: calculate_area() takes 2 positional arguments but 3 were given

print(f"Correct call: Area of 10x5 rectangle is {calculate_area(10, 5)}")
# → Correct call: Area of 10x5 rectangle is 50.0

# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns: Arbitrary Arguments (*args and **kwargs)
# ═══════════════════════════════════════════════════════════════

print("\nSECTION 4: Intermediate Patterns: Arbitrary Arguments (*args and **kwargs)")
print("-----------------------------------------------------------------------")

print("\n--- *args (Arbitrary Positional Arguments) ---")
# The `*args` syntax allows a function to accept any number of positional arguments.
# These arguments are collected into a tuple inside the function.

def sum_all_numbers(*numbers: int) -> int: # 'numbers' will be a tuple of integers
    """Sums an arbitrary number of integer arguments."""
    total: int = 0 # Initialize sum
    for num in numbers: # Iterate through the collected tuple
        total += num # Add each number to the total
    return total

print(f"Sum of (1, 2, 3): {sum_all_numbers(1, 2, 3)}")
# → Sum of (1, 2, 3): 6

print(f"Sum of (10, 20, 30, 40, 50): {sum_all_numbers(10, 20, 30, 40, 50)}")
# → Sum of (10, 20, 30, 40, 50): 150

print(f"Sum of no numbers: {sum_all_numbers()}") # Can be called with no arguments
# → Sum of no numbers: 0

print("\n--- **kwargs (Arbitrary Keyword Arguments) ---")
# The `**kwargs` syntax allows a function to accept any number of keyword arguments.
# These arguments are collected into a dictionary inside the function.

def display_user_info(**info: str) -> None: # 'info' will be a dictionary of strings
    """Displays user information provided as keyword arguments."""
    print("User Info:") # Header for user information
    if not info: # Check if the dictionary is empty
        print("  No information provided.") # Message if no info
        return # Exit function

    for key, value in info.items(): # Iterate through key-value pairs in the dictionary
        print(f"  {key.replace('_', ' ').title()}: {value}") # Format and print each item

display_user_info(name="Alice", age="30", city="New York")
# → User Info:
# →   Name: Alice
# →   Age: 30
# →   City: New York

display_user_info(product_id="P123", price="99.99", in_stock="True")
# → User Info:
# →   Product Id: P123
# →   Price: 99.99
# →   In Stock: True

display_user_info() # Can be called with no keyword arguments
# → User Info:
# →   No information provided.

print("\n--- Combining Regular, *args, and **kwargs Parameters ---")
# The order matters: regular parameters -> *args -> **kwargs.

def configure_settings(
    config_name: str,
    *options: str,
    verbose: bool = False,
    **extra_settings: str
) -> None:
    """
    Configures settings, demonstrating all parameter types.
    config_name: A required string.
    *options: Optional positional arguments (tuple).
    verbose: A keyword argument with a default value.
    **extra_settings: Optional keyword arguments (dictionary).
    """
    print(f"\nConfiguration for: {config_name}") # Print the required config name
    if options: # Check if any options were provided
        print(f"  Options: {', '.join(options)}") # Join and print options
    else:
        print("  No specific options provided.") # Message if no options
    print(f"  Verbose mode: {verbose}") # Print verbose status

    if extra_settings: # Check if extra settings were provided
        print("  Additional Settings:") # Header for additional settings
        for key, value in extra_settings.items(): # Iterate and print extra settings
            print(f"    {key}: {value}")
    else:
        print("  No additional settings.") # Message if no extra settings

configure_settings("System Startup")
# → Configuration for: System Startup
# →   No specific options provided.
# →   Verbose mode: False
# →   No additional settings.

configure_settings("Network Setup", "enable_firewall", "set_ip_range", verbose=True, protocol="TCP", port="8080")
# → Configuration for: Network Setup
# →   Options: enable_firewall, set_ip_range
# →   Verbose mode: True
# →   Additional Settings:
# →     protocol: TCP
# →     port: 8080

print("\n--- Argument Unpacking (using * and **) ---")
# You can use `*` and `**` when calling a function to unpack iterables
# and dictionaries into positional and keyword arguments, respectively.

def display_coordinates(x: int, y: int, z: int) -> None:
    """Displays 3D coordinates."""
    print(f"Coordinates: ({x}, {y}, {z})")

coordinates_list: list[int] = [10, 20, 30] # A list of coordinates
display_coordinates(*coordinates_list) # Unpacks the list into x, y, z
# → Coordinates: (10, 20, 30)

coordinates_tuple: tuple[int, int, int] = (1, 2, 3) # A tuple of coordinates
display_coordinates(*coordinates_tuple) # Unpacks the tuple
# → Coordinates: (1, 2, 3)

def create_profile(name: str, age: int, **kwargs: str) -> None:
    """Creates a user profile with base info and additional details."""
    print(f"\nProfile for {name} (Age: {age}):")
    for key, value in kwargs.items():
        print(f"  {key.title()}: {value}")

user_data: dict[str, str] = {"city": "London", "occupation": "Engineer"}
create_profile("Jane Doe", 28, **user_data) # Unpacks the dictionary into keyword arguments
# → Profile for Jane Doe (Age: 28):
# →   City: London
# →   Occupation: Engineer

# ═══════════════════════════════════════════════════════════════
# SECTION 5: Pythonic Idioms: Parameter Best Practices and Readability
# ═══════════════════════════════════════════════════════════════

print("\nSECTION 5: Pythonic Idioms: Parameter Best Practices and Readability")
print("------------------------------------------------------------------")

print("\n--- Position-Only Parameters (/) ---")
# Introduced in Python 3.8, parameters before `/` can only be passed positionally.
# This forces callers to use positional arguments for certain parameters,
# which can be useful for enforcing API stability or clarity.

def calculate_distance(x1: float, y1: float, /, x2: float, y2: float) -> float:
    """
    Calculates Euclidean distance between two points (x1, y1) and (x2, y2).
    x1, y1 must be positional-only. x2, y2 can be positional or keyword.
    """
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("\n--- Positional-only example ---")
# ✅ Preferred/Pythonic: x1, y1 must be positional
distance1: float = calculate_distance(0, 0, 3, 4) # All positional
print(f"Distance from (0,0) to (3,4): {distance1}")
# → Distance from (0,0) to (3,4): 5.0

distance2: float = calculate_distance(0, 0, x2=3, y2=4) # x1, y1 positional; x2, y2 keyword
print(f"Distance from (0,0) to (3,4) with keywords: {distance2}")
# → Distance from (0,0) to (3,4) with keywords: 5.0

# 🐛 Bug source: Passing x1 or y1 as keyword arguments will raise a TypeError.
try:
    # calculate_distance(x1=0, y1=0, x2=3, y2=4) # This would raise a TypeError
    print("Attempting to call calculate_distance with x1=0 (keyword)...")
    calculate_distance(x1=0, y1=0, x2=3, y2=4)
except TypeError as e:
    print(f"Caught expected error: {e}")
    # → Caught expected error: calculate_distance() got some positional-only arguments passed as keyword arguments: 'x1, y1'

print("\n--- Keyword-Only Parameters (*) ---")
# Parameters after `*` (or after `*args`) must be passed as keyword arguments.
# This improves readability and prevents accidental argument order mix-ups.

def create_report(title: str, *, author: str, date: str) -> None:
    """
    Creates a report header. Title is positional, author and date are keyword-only.
    """
    print(f"\nReport Title: {title}")
    print(f"  Author: {author}")
    print(f"  Date: {date}")

print("\n--- Keyword-only example ---")
create_report("Project Status", author="John Doe", date="2023-10-27")
# → Report Title: Project Status
# →   Author: John Doe
# →   Date: 2023-10-27

# 🐛 Bug source: Passing author or date as positional arguments will raise a TypeError.
try:
    # create_report("Project Status", "John Doe", "2023-10-27") # This would raise a TypeError
    print("Attempting to call create_report with author/date as positional...")
    create_report("Project Status", "John Doe", "2023-10-27")
except TypeError as e:
    print(f"Caught expected error: {e}")
    # → Caught expected error: create_report() takes 1 positional argument but 3 were given

print("\n--- Good Naming Conventions ---")
# Use descriptive names for parameters to enhance code readability.
# ✅ Preferred/Pythonic:
def calculate_total_price(unit_price: float, quantity: int, discount_percentage: float = 0.0) -> float:
    """Calculates total price after applying discount."""
    base_price: float = unit_price * quantity
    final_price: float = base_price * (1 - discount_percentage)
    return final_price

# ⚠️ Common mistake: Avoid single-letter or overly generic names if they don't add clarity.
# def calc(up, qty, disc=0.0): # Less readable
#     pass

print(f"Total price for 5 items at $10 each: ${calculate_total_price(10.0, 5)}")
# → Total price for 5 items at $10 each: $50.0
print(f"Total price with 10% discount: ${calculate_total_price(10.0, 5, 0.1)}")
# → Total price with 10% discount: $45.0

# ═══════════════════════════════════════════════════════════════
# SECTION 6: Real-World Mini-Program: A Simple Inventory System Class
# ═══════════════════════════════════════════════════════════════

# Demonstrating parameters within a class context, specifically in __init__
# and other methods, showcasing various parameter types.

class InventoryItem:
    """
    Represents an item in an inventory system.
    Uses various parameter types in its methods.
    """
    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        """
        Initializes an InventoryItem with essential details.
        item_id: Unique identifier (positional).
        name: Name of the item (positional).
        quantity: Current stock quantity (positional).
        price: Price per unit (positional).
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def display_info(self, detailed: bool = False) -> None:
        """
        Displays item information.
        detailed: If True, includes price and ID. Uses default parameter.
        """
        print(f"\n--- Item: {self.name} ---")
        print(f"  Quantity: {self.quantity}")
        if detailed: # Conditionally display more details
            print(f"  ID: {self.item_id}")
            print(f"  Price: ${self.price:.2f}")
            print(f"  Total Value: ${self.get_total_value():.2f}")

    def update_stock(self, *, amount: int, operation: str = "add") -> None:
        """
        Updates the item's stock quantity.
        amount: Quantity to add or remove (keyword-only).
        operation: "add" or "remove" (keyword-only with default).
        """
        if operation == "add":
            self.quantity += amount # Increase quantity
            print(f"  Added {amount} units to {self.name}. New quantity: {self.quantity}")
        elif operation == "remove":
            if self.quantity >= amount: # Ensure enough stock to remove
                self.quantity -= amount # Decrease quantity
                print(f"  Removed {amount} units from {self.name}. New quantity: {self.quantity}")
            else:
                print(f"  ⚠️  Not enough {self.name} to remove {amount} units. Current: {self.quantity}")
        else:
            print(f"  ⚠️  Invalid operation: '{operation}'. Use 'add' or 'remove'.")

    def get_total_value(self) -> float:
        """Calculates the total monetary value of the current stock."""
        return self.quantity * self.price

    def apply_discount(self, *discounts: float) -> None:
        """
        Applies multiple percentage discounts to the item's price.
        *discounts: Arbitrary number of discount percentages (e.g., 0.10 for 10%).
        """
        original_price: float = self.price # Store original price for calculation
        for discount_rate in discounts: # Iterate through each discount
            self.price *= (1 - discount_rate) # Apply the discount
        print(f"  Applied {len(discounts)} discounts. Price changed from ${original_price:.2f} to ${self.price:.2f}")


print("\nSECTION 6: Real-World Mini-Program: A Simple Inventory System Class")
print("------------------------------------------------------------------")

# Create inventory items using positional arguments for __init__
item1: InventoryItem = InventoryItem("SKU001", "Laptop", 10, 1200.00)
item2: InventoryItem = InventoryItem("SKU002", "Mouse", 50, 25.50)
item3: InventoryItem = InventoryItem("SKU003", "Keyboard", 30, 75.00)

item1.display_info() # Display basic info (detailed=False by default)
# → --- Item: Laptop ---
# →   Quantity: 10

item2.display_info(detailed=True) # Display detailed info using keyword argument
# → --- Item: Mouse ---
# →   Quantity: 50
# →   ID: SKU002
# →   Price: $25.50
# →   Total Value: $1275.00

# Update stock using keyword-only parameters
item1.update_stock(amount=5) # Uses default operation="add"
# →   Added 5 units to Laptop. New quantity: 15
item1.display_info()
# → --- Item: Laptop ---
# →   Quantity: 15

item3.update_stock(amount=10, operation="remove") # Explicitly remove
# →   Removed 10 units from Keyboard. New quantity: 20
item3.display_info()
# → --- Item: Keyboard ---
# →   Quantity: 20

item3.update_stock(amount=30, operation="remove") # Attempt to remove more than available
# →   ⚠️  Not enough Keyboard to remove 30 units. Current: 20

# Apply multiple discounts using *args
item2.display_info(detailed=True)
# → --- Item: Mouse ---
# →   Quantity: 50
# →   ID: SKU002
# →   Price: $25.50
# →   Total Value: $1275.00
item2.apply_discount(0.10, 0.05) # Apply 10% then 5% discount
# →   Applied 2 discounts. Price changed from $25.50 to $21.80
item2.display_info(detailed=True)
# → --- Item: Mouse ---
# →   Quantity: 50
# →   ID: SKU002
# →   Price: $21.80
# →   Total Value: $1091.25

print("\n--- Inventory Summary ---")
inventory_value: float = item1.get_total_value() + item2.get_total_value() + item3.get_total_value()
print(f"Total inventory value: ${inventory_value:.2f}")
# → Total inventory value: $20916.25 (Value will depend on previous operations)

# ════════════════