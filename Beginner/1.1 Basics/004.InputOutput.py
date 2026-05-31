"""Input Output in Python

Learn how Python programs interact with users and files. Master reading data from the console and writing results to the screen and persistent storage.

What you will learn:
* How to get user input using the `input()` function.
* How to display output using the `print()` function.
* Controlling `print()` behavior with `sep` and `end` arguments.
* Performing essential type conversions for user input data.
* Reading from and writing to text files using `open()`.
* Efficiently handling file operations with context managers and generators.

Prerequisites:
* Basic Python syntax (variables, data types, control flow).
* Understanding of strings, integers, and floats.
* Familiarity with calling functions and basic data structures like lists.

Key Concepts Covered:
* `input()` function
* `print()` function
* `str()`, `int()`, `float()` type conversion
* `open()` function (file modes: 'w', 'r', 'a', 'x')
* `write()`, `read()`, `readline()`, `readlines()` file methods
* `close()` file method
* `with` statement (context manager for files)
* File object iteration
* `try-except` for error handling
* Generator functions for efficient file processing
"""

import os # Used for file cleanup in some sections

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept - Basic User & Program Interaction
# ═══════════════════════════════════════════════════════════════

def section_1_core_concept() -> None:
    """
    Demonstrates the absolute fundamentals of input and output:
    getting user input with `input()` and displaying output with `print()`.
    """
    print("SECTION 1: Core Concept - Basic User & Program Interaction\n")

    # 1.1 Using print() to display information
    # The print() function displays values to the console.
    print("Hello, Python learners!") # Prints a simple string literal
    # → Hello, Python learners!

    # print() can display multiple items, separated by spaces by default.
    name: str = "Alice" # Define a string variable
    age: int = 30 # Define an integer variable
    print("Name:", name, "Age:", age) # Prints string literals and variable values
    # → Name: Alice Age: 30

    # 1.2 Using input() to get information from the user
    # The input() function pauses program execution and waits for the user
    # to type something and press Enter. It always returns a string.
    user_name: str = input("Please enter your name: ") # Prompts user and stores their input
    # User types "Bob" and presses Enter
    print(f"Welcome, {user_name}!") # Prints a personalized welcome message using an f-string
    # → Welcome, Bob!

    # 1.3 Combining input and print for a simple interaction
    # This example asks for a city and then confirms it.
    city: str = input("What city do you live in? ") # Asks for the user's city
    print(f"You live in {city}.") # Confirms the entered city
    # User types "New York" and presses Enter
    # → You live in New York.

    print("\nEnd of Section 1.\n")

# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns - Formatting Output and Handling Inputs
# ═══════════════════════════════════════════════════════════════

def section_2_syntax_common_patterns() -> None:
    """
    Explores common `print()` arguments (`sep`, `end`) and how to
    convert user input (which is always a string) to other data types.
    """
    print("SECTION 2: Syntax & Common Patterns - Formatting Output and Handling Inputs\n")

    # 2.1 Customizing print() behavior with 'sep' and 'end'
    # The 'sep' (separator) argument changes what separates multiple items.
    print("Apple", "Banana", "Cherry", sep=" | ") # Items separated by " | " instead of space
    # → Apple | Banana | Cherry

    # The 'end' argument changes what character is printed at the end of the line.
    # By default, 'end' is '\n' (newline).
    print("This is the first part.", end=" ") # Prints text, ends with a space instead of newline
    print("This is the second part.") # Prints on the same line because the previous print didn't add a newline
    # → This is the first part. This is the second part.

    # 2.2 Getting multiple inputs and type conversion
    # input() always returns a string. For numerical operations, it must be converted.
    # We use int() for integers and float() for floating-point numbers.

    # 🔑 Key insight: Always convert input to the desired type immediately.
    num1_str: str = input("Enter the first number: ") # User enters "10"
    num2_str: str = input("Enter the second number: ") # User enters "5"

    # ⚠️ Common mistake: Trying to perform arithmetic on strings.
    # print(f"String sum: {num1_str + num2_str}") # This would concatenate "10" and "5" to "105"

    # ✅ Preferred/Pythonic: Convert to appropriate numeric types.
    num1: int = int(num1_str) # Converts "10" to integer 10
    num2: int = int(num2_str) # Converts "5" to integer 5
    total: int = num1 + num2 # Performs arithmetic on integers
    print(f"The sum of {num1} and {num2} is: {total}") # Prints the correct sum
    # → The sum of 10 and 5 is: 15

    # Example with float conversion
    price_str: str = input("Enter an item's price: ") # User enters "19.99"
    quantity_str: str = input("Enter the quantity: ") # User enters "2"

    price: float = float(price_str) # Converts "19.99" to float 19.99
    quantity: int = int(quantity_str) # Converts "2" to integer 2
    total_cost: float = price * quantity # Calculates total cost
    print(f"Total cost: ${total_cost:.2f}") # Prints total cost, formatted to 2 decimal places
    # → Total cost: $39.98

    print("\nEnd of Section 2.\n")

# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas - What Beginners Always Get Wrong
# ═══════════════════════════════════════════════════════════════

def section_3_edge_cases_gotchas() -> None:
    """
    Highlights common mistakes and how to handle them, especially
    regarding `input()` returning strings and potential `ValueError`
    during type conversion.
    """
    print("SECTION 3: Edge Cases & Gotchas - What Beginners Always Get Wrong\n")

    # 3.1 `input()` always returns a string, even if it looks like a number.
    user_age_str: str = input("How old are you? ") # User enters "25"
    print(f"Type of user_age_str: {type(user_age_str)}") # Shows it's a string
    # → Type of user_age_str: <class 'str'>

    # If you need to treat it as a number, explicit conversion is required.
    user_age: int = int(user_age_str) # Converts "25" to integer 25
    print(f"In 5 years, you will be {user_age + 5} years old.") # Correct arithmetic
    # → In 5 years, you will be 30 years old.

    # 3.2 Handling invalid input with `try-except`
    # Attempting to convert a non-numeric string to `int` or `float` raises a `ValueError`.
    print("\nLet's try converting some input:")
    try:
        # This block attempts to convert user input to an integer.
        # 🐛 Bug source: If the user enters non-numeric text, int() will fail.
        user_number_str: str = input("Enter a whole number: ") # User enters "hello"
        converted_number: int = int(user_number_str) # This line will raise a ValueError
        print(f"You entered: {converted_number}")
    except ValueError:
        # This block catches the ValueError and handles it gracefully.
        print(f"⚠️ Error: '{user_number_str}' is not a valid whole number. Please enter digits only.")
    # User types "hello" and presses Enter
    # → ⚠️ Error: 'hello' is not a valid whole number. Please enter digits only.

    # Another example with float conversion
    print("\nLet's try converting a decimal number:")
    try:
        user_decimal_str: str = input("Enter a decimal number: ") # User enters "3.14" or "abc"
        converted_decimal: float = float(user_decimal_str)
        print(f"You entered: {converted_decimal}")
    except ValueError:
        print(f"⚠️ Error: '{user_decimal_str}' is not a valid decimal number.")
    # User types "3.14" and presses Enter
    # → You entered: 3.14
    # User types "abc" and presses Enter
    # → ⚠️ Error: 'abc' is not a valid decimal number.

    # 3.3 Handling empty input
    # An empty string is returned if the user just presses Enter.
    favorite_color: str = input("What's your favorite color? (Press Enter for none) ") # User presses Enter
    if not favorite_color: # Checks if the string is empty
        print("You didn't specify a favorite color.")
    else:
        print(f"Your favorite color is {favorite_color}.")
    # User presses Enter
    # → You didn't specify a favorite color.

    print("\nEnd of Section 3.\n")

# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns - Basic File I/O
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """
    Introduces basic file input/output operations: opening files,
    writing content to them, and reading content back.
    """
    print("SECTION 4: Intermediate Patterns - Basic File I/O\n")

    # Define a filename for this section's examples
    filename: str = "my_notes.txt"

    # 4.1 Writing to a file (mode 'w')
    # The 'w' mode opens a file for writing. If the file exists, it truncates (empties) it.
    # If the file does not exist, it creates a new one.
    print(f"1. Writing to '{filename}'...")
    file_writer = open(filename, 'w') # Open the file in write mode
    file_writer.write("This is the first line of my note.\n") # Write a string to the file
    file_writer.write("Remember to buy groceries.\n") # Write another string
    file_writer.write("Call Mom on Sunday.\n") # And another
    file_writer.close() # It's crucial to close the file to save changes and release resources
    print("   Content written and file closed.")

    # 4.2 Reading from a file (mode 'r')
    # The 'r' mode opens a file for reading. If the file does not exist, it raises a FileNotFoundError.
    print(f"\n2. Reading entire content from '{filename}'...")
    file_reader = open(filename, 'r') # Open the file in read mode
    content: str = file_reader.read() # Read the entire content of the file as a single string
    print("   File Content:\n")
    print(content) # Display the content
    # → File Content:
    # → This is the first line of my note.
    # → Remember to buy groceries.
    # → Call Mom on Sunday.
    file_reader.close() # Always close the file after reading

    # 4.3 Appending to a file (mode 'a')
    # The 'a' mode opens a file for appending. It adds new content to the end of the file
    # without truncating existing content. If the file doesn't exist, it creates it.
    print(f"\n3. Appending to '{filename}'...")
    file_appender = open(filename, 'a') # Open in append mode
    file_appender.write("Added a new task: Learn Python I/O.\n") # Add a new line
    file_appender.close()
    print("   Appended new content and file closed.")

    # Verify append by reading again
    print(f"\n4. Reading updated content from '{filename}'...")
    file_reader_again = open(filename, 'r')
    updated_content: str = file_reader_again.read()
    print("   Updated File Content:\n")
    print(updated_content)
    # → Updated File Content:
    # → This is the first line of my note.
    # → Remember to buy groceries.
    # → Call Mom on Sunday.
    # → Added a new task: Learn Python I/O.
    file_reader_again.close()

    # 4.4 Reading line by line (`readline()` and `readlines()`)
    print(f"\n5. Reading line by line from '{filename}'...")
    file_lines_reader = open(filename, 'r')

    # readline() reads one line at a time
    first_line: str = file_lines_reader.readline() # Reads the first line
    print(f"   First line (readline): {first_line.strip()}") # .strip() removes trailing newline
    # → First line (readline): This is the first line of my note.

    # readlines() reads all lines into a list of strings
    all_lines: list[str] = file_lines_reader.readlines() # Reads remaining lines from current position
    print("   Remaining lines (readlines):")
    for line in all_lines: # Iterate through the list of lines
        print(f"   - {line.strip()}") # Print each line, stripped
    # → Remaining lines (readlines):
    # → - Remember to buy groceries.
    # → - Call Mom on Sunday.
    # → - Added a new task: Learn Python I/O.
    file_lines_reader.close()

    # Clean up the created file
    if os.path.exists(filename): # Check if the file exists
        os.remove(filename) # Delete the file
        print(f"\nCleaned up: '{filename}' deleted.")

    print("\nEnd of Section 4.\n")

# ═══════════════════════════════════════════════════════════════
# SECTION 5: Pythonic Idioms - The Right Way vs. The Naive Way
# ═══════════════════════════════════════════════════════════════

def section_5_pythonic_idioms() -> None:
    """
    Demonstrates Pythonic ways to handle file I/O, primarily using
    the `with` statement for automatic resource management and
    iterating directly over file objects.
    """
    print("SECTION 5: Pythonic Idioms - The Right Way vs. The Naive Way\n")

    filename: str = "pythonic_example.txt"

    # 5.1 Using the 'with' statement (context manager) for file handling
    # WHY: The 'with' statement ensures that files are properly closed
    #      even if errors occur, preventing resource leaks.
    # It's the standard and recommended way for file I/O.

    # 🐛 Bug source: Manually opening and closing files can lead to forgotten .close() calls.
    # file = open(filename, 'w')
    # file.write("Hello\n")
    # # If an error occurs here, file.close() might never be called.
    # file.close()

    # ✅ Preferred/Pythonic: Use 'with' statement.
    print(f"1. Writing to '{filename}' using 'with' statement...")
    with open(filename, 'w') as f: # 'f' is the file object, automatically closed when exiting 'with' block
        f.write("This line is written using a context manager.\n")
        f.write("Context managers ensure resources are properly handled.\n")
        f.write("No need to call f.close() explicitly!\n")
    print("   Content written. File automatically closed.")

    # 5.2 Reading a file line by line using iteration
    # WHY: Iterating directly over a file object is memory-efficient for large files
    #      as it reads one line at a time, without loading the entire file into memory.

    print(f"\n2. Reading '{filename}' line by line using file object iteration:")
    print("   File Content:")
    with open(filename, 'r') as f: # Open in read mode with context manager
        for line_num, line in enumerate(f, 1): # Iterate directly over the file object
            print(f"   Line {line_num}: {line.strip()}") # Process each line, stripping newline
    # → File Content:
    # → Line 1: This line is written using a context manager.
    # → Line 2: Context managers ensure resources are properly handled.
    # → Line 3: No need to call f.close() explicitly!
    print("   Finished reading line by line.")

    # 5.3 Using 'x' mode for exclusive file creation
    # The 'x' mode creates a new file for writing. If the file already exists, it raises a FileExistsError.
    # This is useful when you want to ensure you don't accidentally overwrite an existing file.
    new_exclusive_file: str = "unique_data.txt"
    print(f"\n3. Trying to create '{new_exclusive_file}' with 'x' mode...")
    try:
        with open(new_exclusive_file, 'x') as f: # This will succeed the first time
            f.write("This file was created exclusively.\n")
        print(f"   Successfully created and wrote to '{new_exclusive_file}'.")

        # Attempt to create it again – this should fail
        print(f"\n4. Attempting to create '{new_exclusive_file}' again with 'x' mode...")
        with open(new_exclusive_file, 'x') as f: # This will raise FileExistsError
            f.write("This line should not be written.\n")
        print("   This message should not appear.") # Should not reach here
    except FileExistsError:
        print(f"⚠️ Error: '{new_exclusive_file}' already exists. Cannot create in 'x' mode.")
    # → Successfully created and wrote to 'unique_data.txt'.
    # → ⚠️ Error: 'unique_data.txt' already exists. Cannot create in 'x' mode.

    # Clean up created files
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\nCleaned up: '{filename}' deleted.")
    if os.path.exists(new_exclusive_file):
        os.remove(new_exclusive_file)
        print(f"Cleaned up: '{new_exclusive_file}' deleted.")

    print("\nEnd of Section 5.\n")

# ═══════════════════════════════════════════════════════════════
# SECTION 6: Real-World Mini-Program - Simple Note Taker
# ═══════════════════════════════════════════════════════════════

class NoteManager:
    """
    A simple class to manage notes, including adding, viewing, and
    persisting them to a file. Demonstrates practical application
    of input/output and file handling.
    """
    def __init__(self, filename: str = "notes.txt") -> None:
        """Initializes the NoteManager with a default filename."""
        self.filename: str = filename # Store the filename
        self.notes: list[str] = [] # Initialize an empty list to hold notes
        self._load_notes() # Load existing notes when the manager is created

    def _load_notes(self) -> None:
        """
        Loads notes from the file into the `notes` list.
        Handles cases where the file might not exist.
        """
        if not os.path.exists(self.filename): # Check if the file exists
            print(f"ℹ️ Note file '{self.filename}' not found. Starting with empty notes.")
            return # If not, no notes to load

        try:
            with open(self.filename, 'r') as f: # Open the file in read mode
                self.notes = [line.strip() for line in f] # Read all lines and strip newlines
            print(f"Loaded {len(self.notes)} notes from '{self.filename}'.")
        except IOError as e: # Catch potential I/O errors (e.g., permission issues)
            print(f"⚠️ Error loading notes from '{self.filename}': {e}")
            self.notes = [] # Reset notes if loading fails

    def _save_notes(self) -> None:
        """Saves the current `notes` list to the file."""
        try:
            with open(self.filename, 'w') as f: # Open in write mode (overwrites existing content)
                for note in self.notes: # Iterate through each note
                    f.write(note + "\n") # Write each note followed by a newline
            print(f"Saved {len(self.notes)} notes to '{self.filename}'.")
        except IOError as e:
            print(f"⚠️ Error saving notes to '{self.filename}': {e}")

    def add_note(self, note_content: str) -> None:
        """Adds a new note to the list and saves it to the file."""
        if note_content.strip(): # Only add if the note is not empty or just whitespace
            self.notes.append(note_content.strip()) # Add the stripped note
            self._save_notes() # Save changes to the file
            print("Note added successfully.")
        else:
            print("Cannot add an empty note.")

    def view_notes(self) -> None:
        """Displays all current notes to the console."""
        if not self.notes: # Check if the notes list is empty
            print("No notes available.")
            return

        print("\n--- Your Notes ---")
        for i, note in enumerate(self.notes, 1): # Iterate with index
            print(f"{i}. {note}") # Print note with a numbered prefix
        print("------------------")

def section_6_real_world_mini_program() -> None:
    """
    A mini-program that acts as a simple note-taker, demonstrating
    how to combine user input, output, and file I/O in a practical scenario.
    """
    print("SECTION 6: Real-World Mini-Program - Simple Note Taker\n")

    notes_file: str = "my_daily_notes.txt"
    # Clean up previous notes file if it exists, for a fresh start
    if os.path.exists(notes_file):
        os.remove(notes_file)
        print(f"Cleaned up previous '{notes_file}' for fresh start.")

    manager = NoteManager(notes_file) # Create an instance of the NoteManager

    while True: # Loop indefinitely until user decides to exit
        print("\nNote Taker Menu:")
        print("1. Add a note")
        print("2. View notes")
        print("3. Exit")

        choice_str: str = input("Enter your choice (1-3): ") # Get user's menu choice

        try:
            choice: int = int(choice_str) # Convert choice to integer
            if choice == 1:
                note_text: str = input("Enter your note: ") # Get the note content
                manager.add_note(note_text) # Call the add_note method
            elif choice == 2:
                manager.view_notes() # Call the view_notes method
            elif choice == 3:
                print("Exiting Note Taker. Goodbye!")
                break # Exit the loop
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")
        except Exception as e: # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

    # Clean up the notes file created by the program
    if os.path.exists(notes_file):
        os.remove(notes_file)
        print(f"\nCleaned up: '{notes_file}' deleted.")

    print("\nEnd of Section 6.\n")

# ═══════════════════════════════════════════════════════════════
# SECTION 7: Performance & Memory - When it Matters, How to Measure
# ═══════════════════════════════════════════════════════════════

def generate_large_file(filename: str, num_lines: int) -> None:
    """Helper function to create a large text file for testing."""
    print(f"Generating a large file: '{filename}' with {num_lines} lines...")
    with open(filename, 'w') as f:
        for i in range(num_lines):
            f.write(f"This is line number {i+1} in the large file.\n")
    print("File generation complete.")

def read_large_file_generator(filename: str) -> None:
    """
    Reads a large file line by line using a generator.
    This is memory-efficient as it yields one line at a time.
    """
    print(f"\nReading '{filename}' using a generator (memory efficient):")
    line_count: int = 0
    try:
        with open(filename, 'r') as f:
            for line in f: # File objects are naturally iterable (generators)
                line_count += 1
                # print(f"Processing line: {line.strip()}") # Uncomment to see lines being processed
                pass # Simulate processing without printing all lines to avoid huge output
        print(f"Processed {line_count} lines efficiently.")
    except FileNotFoundError:
        print(f"⚠️ Error: File '{filename}' not found.")
    except IOError as e:
        print(f"⚠️ Error reading file '{filename}': {e}")


def section_7_performance_memory() -> None:
    """
    Discusses performance and memory considerations for file I/O,
    especially when dealing with large files, and introduces generator
    functions for efficient line-by-line processing.
    """
    print("SECTION 7: Performance & Memory - When it Matters, How to Measure\n")

    large_filename: str = "large_data.txt"
    num_lines_in_file: int = 100_000 # A moderately large number of lines

    # Create a large file for demonstration
    generate_large_file(large_filename, num_lines_in_file)

    # 7.1 The problem with `readlines()` for large files
    # WHY: `readlines()` reads the entire file content into a list of strings
    #      in memory. For very large files (GBs), this can exhaust available RAM.
    print(f"\n1. Demonstrating `readlines()` (potential memory issue for huge files):")
    try:
        with open(large_filename, 'r') as f:
            # 🐛 Bug source: For extremely large files, this loads everything into RAM.
            #   If num_lines_