"""Scope: Understanding Variable Visibility and Lifetime

This module explores the fundamental concept of 'scope' in Python, which dictates where
variables can be accessed and for how long they exist. You will learn how Python
manages namespaces and resolves variable names using the LEGB rule.

What you will learn:
•  The definition of scope and why it's crucial in programming.
•  The four main types of scope in Python: Local, Enclosing, Global, and Built-in (LEGB rule).
•  How to define and access variables within different scopes.
•  The use cases and implications of the `global` and `nonlocal` keywords.
•  How scope enables advanced Python patterns like closures and decorators.
•  Best practices for managing variable scope to write cleaner, more maintainable code.
•  Briefly, the performance implications of scope lookup.

Prerequisites:
•  Basic understanding of Python variables and data types.
•  Familiarity with defining and calling functions.
•  Knowledge of basic control flow (if/else, loops).

Key Concepts Covered:
•  Local Scope
•  Enclosing Function Local Scope
•  Global (Module) Scope
•  Built-in Scope
•  LEGB Rule
•  Variable Shadowing
•  `global` keyword
•  `nonlocal` keyword
•  Closures
•  Decorators
•  Minimizing Global State
"""

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept - The LEGB Rule
# ═══════════════════════════════════════════════════════════════

# Python uses the LEGB rule to resolve names (variables, functions, classes, etc.).
# It checks scopes in this specific order:
# 1.  Local (L): Inside the current function.
# 2.  Enclosing (E): From outer functions (for nested functions).
# 3.  Global (G): At the top level of the module (the current .py file).
# 4.  Built-in (B): Names pre-defined in Python (e.g., `print`, `len`, `str`).

# Global scope variable: Defined at the module level.
global_message: str = "Hello from the Global Scope!" # This variable is accessible throughout the entire module.

def section_1_core_concept() -> None:
    """Demonstrates the fundamental LEGB rule with simple examples."""
    print("SECTION 1: Core Concept - The LEGB Rule")
    print("---------------------------------------")

    # 🔑 Key insight: Python looks for names in a specific order (LEGB).

    # Example 1.1: Global vs. Local Scope
    # ----------------------------------

    def local_scope_example() -> None:
        """A function demonstrating local scope."""
        local_variable: str = "I am a local variable inside local_scope_example." # This is a local variable.
        print(f"Inside local_scope_example: {local_variable}") # Accessing the local variable.
        # → Inside local_scope_example: I am a local variable inside local_scope_example.
        print(f"Inside local_scope_example, accessing global_message: {global_message}") # Accessing the global variable.
        # → Inside local_scope_example, accessing global_message: Hello from the Global Scope!

    # Call the function to execute its code and demonstrate local scope.
    local_scope_example()
    print(f"Outside function, accessing global_message: {global_message}") # Global variable is accessible here.
    # → Outside function, accessing global_message: Hello from the Global Scope!

    # ⚠️ Common mistake: Trying to access a local variable from outside its function.
    try:
        # print(local_variable) # This would raise a NameError.
        print("Attempting to access 'local_variable' outside its function (expected NameError)...")
        # Accessing `local_variable` here would fail because it's out of scope.
        # It was defined only within `local_scope_example`.
        # The interpreter cannot find 'local_variable' in the global scope.
        # `local_variable` ceases to exist once `local_scope_example` finishes execution.
    except NameError as e:
        print(f"  Caught expected error: {e}") # Confirms the variable is not found.
        # →   Caught expected error: name 'local_variable' is not defined

    print("\n" + "─" * 40 + "\n") # Separator for clarity


# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns - Variables in Different Scopes
# ═══════════════════════════════════════════════════════════════

# Global variable for this section.
module_level_setting: str = "Default Module Setting" # This variable is in the global scope.

def section_2_syntax_patterns() -> None:
    """Explores variable definition and access across different scopes."""
    print("SECTION 2: Syntax & Common Patterns - Variables in Different Scopes")
    print("-----------------------------------------------------------------")

    # Example 2.1: Local Scope
    # ------------------------

    # WHY: Demonstrate that variables defined inside a function are local to that function.
    def calculate_sum(a: int, b: int) -> int:
        """Calculates the sum of two numbers."""
        total: int = a + b # 'total', 'a', 'b' are local to calculate_sum.
        print(f"  Inside calculate_sum: a={a}, b={b}, total={total}")
        return total

    result: int = calculate_sum(10, 20) # Call the function.
    # →   Inside calculate_sum: a=10, b=20, total=30
    print(f"  Result from calculate_sum: {result}")
    # →   Result from calculate_sum: 30

    # Example 2.2: Enclosing (Nonlocal) Scope
    # ---------------------------------------

    # WHY: Illustrate how nested functions can access variables from their outer (enclosing) function.
    def outer_function(greeting_prefix: str) -> None:
        """An outer function defining a variable for its inner function."""
        # 'greeting_prefix' is local to outer_function, but enclosing to inner_function.
        message_suffix: str = "World!" # This is local to outer_function.

        def inner_function(name: str) -> None:
            """An inner (nested) function accessing variables from its enclosing scope."""
            # 'name' is local to inner_function.
            # 'greeting_prefix' and 'message_suffix' are in the enclosing scope.
            print(f"  Inside inner_function: {greeting_prefix} {name}, {message_suffix}")

        print(f"  Inside outer_function: Initializing inner_function.")
        inner_function("Python") # Call the inner function.
        # →   Inside inner_function: Hello Python, World!

    outer_function("Hello") # Call the outer function.
    # →   Inside outer_function: Initializing inner_function.

    # Example 2.3: Built-in Scope
    # ---------------------------

    # WHY: Show that built-in functions and types are always available without explicit import.
    list_of_numbers: list[int] = [1, 2, 3, 4, 5] # A local list.
    print(f"  Length of list_of_numbers: {len(list_of_numbers)}") # `len` is a built-in function.
    # →   Length of list_of_numbers: 5
    print(f"  Type of list_of_numbers: {type(list_of_numbers)}") # `type` is a built-in function.
    # →   Type of list_of_numbers: <class 'list'>

    # Example 2.4: Variable Shadowing
    # -------------------------------

    # WHY: Explain how a local variable with the same name as a global variable
    #      will "shadow" the global one within its local scope.
    print(f"  Global module_level_setting before shadowing: {module_level_setting}")
    # →   Global module_level_setting before shadowing: Default Module Setting

    def shadow_example() -> None:
        """Demonstrates variable shadowing."""
        # This 'module_level_setting' is a NEW LOCAL variable, not the global one.
        module_level_setting: str = "Overridden Local Setting" # Shadows the global variable.
        print(f"  Inside shadow_example (local): {module_level_setting}")
        # →   Inside shadow_example (local): Overridden Local Setting

    shadow_example() # Call the function to demonstrate shadowing.
    print(f"  Global module_level_setting after shadowing: {module_level_setting}") # Global variable remains unchanged.
    # →   Global module_level_setting after shadowing: Default Module Setting

    print("\n" + "─" * 40 + "\n")


# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas - `global` and `nonlocal` Keywords
# ═══════════════════════════════════════════════════════════════

# Global variable for this section.
global_counter: int = 0 # Initial value for a global counter.
enclosing_message: str = "Original Enclosing Message" # Initial value for an enclosing message.

def section_3_edge_cases() -> None:
    """Demonstrates `global` and `nonlocal` keywords to modify outer scope variables."""
    print("SECTION 3: Edge Cases & Gotchas - `global` and `nonlocal` Keywords")
    print("----------------------------------------------------------------")

    # Example 3.1: Modifying Global Variables with `global`
    # ----------------------------------------------------

    # WHY: Show that without `global`, assignment inside a function creates a new local variable.
    #      Then, demonstrate how `global` allows modification of the module-level variable.
    print(f"  Initial global_counter: {global_counter}")
    # →   Initial global_counter: 0

    def increment_global_wrong() -> None:
        """Incorrectly attempts to modify global_counter without 'global'."""
        # ⚠️ Common mistake: This creates a NEW LOCAL variable named 'global_counter'.
        #    It does NOT modify the module-level 'global_counter'.
        global_counter: int = 100 # This is a local variable shadowing the global one.
        print(f"  Inside increment_global_wrong (local): {global_counter}")
        # →   Inside increment_global_wrong (local): 100

    increment_global_wrong()
    print(f"  global_counter after wrong increment: {global_counter}") # Global variable is still 0.
    # →   global_counter after wrong increment: 0

    def increment_global_correct() -> None:
        """Correctly modifies global_counter using the 'global' keyword."""
        global global_counter # Declare intent to modify the global variable.
        global_counter += 1 # This now modifies the module-level global_counter.
        print(f"  Inside increment_global_correct (global): {global_counter}")
        # →   Inside increment_global_correct (global): 1

    increment_global_correct()
    print(f"  global_counter after correct increment: {global_counter}") # Global variable is now 1.
    # →   global_counter after correct increment: 1

    # Example 3.2: Modifying Enclosing Variables with `nonlocal`
    # ---------------------------------------------------------

    # WHY: Show that `nonlocal` is used for modifying variables in an enclosing scope,
    #      but not the global scope.
    print(f"  Initial enclosing_message: {enclosing_message}")
    # →   Initial enclosing_message: Original Enclosing Message

    def outer_scope_modifier() -> None:
        """Outer function for demonstrating nonlocal."""
        # This 'enclosing_message' is in the enclosing scope for 'inner_scope_modifier'.
        enclosing_message: str = "Outer Function's Message" # This is local to outer_scope_modifier.
        print(f"  Outer function before inner call: {enclosing_message}")
        # →   Outer function before inner call: Outer Function's Message

        def inner_scope_modifier() -> None:
            """Inner function modifying the enclosing scope variable."""
            # ⚠️ Common mistake: Without 'nonlocal', this would create a new local variable.
            #    `global` would try to modify the module-level variable, not the enclosing one.
            nonlocal enclosing_message # Declare intent to modify the enclosing variable.
            enclosing_message = "Modified by Inner Function (nonlocal)" # Modifies the 'enclosing_message' in outer_scope_modifier.
            print(f"  Inside inner_scope_modifier: {enclosing_message}")
            # →   Inside inner_scope_modifier: Modified by Inner Function (nonlocal)

        inner_scope_modifier()
        print(f"  Outer function after inner call: {enclosing_message}") # Reflects the change from inner_scope_modifier.
        # →   Outer function after inner call: Modified by Inner Function (nonlocal)

    outer_scope_modifier()
    print(f"  enclosing_message at global level (unchanged): {enclosing_message}") # Global variable is still "Original Enclosing Message".
    # →   enclosing_message at global level (unchanged): Original Enclosing Message

    print("\n" + "─" * 40 + "\n")


# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns - Closures and Decorators
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """Demonstrates closures and a simple decorator, both relying on scope."""
    print("SECTION 4: Intermediate Patterns - Closures and Decorators")
    print("--------------------------------------------------------")

    # Example 4.1: Closures
    # ---------------------

    # WHY: A closure is a function object that remembers values in its enclosing scope
    #      even if the enclosing function is no longer running.
    def make_multiplier(factor: int) -> callable[[int], int]:
        """Returns a function that multiplies its input by 'factor'."""
        # 'factor' is in the enclosing scope of 'multiplier_function'.
        def multiplier_function(number: int) -> int:
            """Inner function that performs the multiplication."""
            return number * factor # 'factor' is remembered from make_multiplier's scope.
        return multiplier_function # Return the inner function.

    # Create two different multiplier functions.
    multiply_by_2: callable[[int], int] = make_multiplier(2) # 'factor' is 2 for this closure.
    multiply_by_5: callable[[int], int] = make_multiplier(5) # 'factor' is 5 for this closure.

    print(f"  Multiply 10 by 2: {multiply_by_2(10)}")
    # →   Multiply 10 by 2: 20
    print(f"  Multiply 10 by 5: {multiply_by_5(10)}")
    # →   Multiply 10 by 5: 50
    print(f"  Multiply 7 by 2: {multiply_by_2(7)}")
    # →   Multiply 7 by 2: 14

    # Example 4.2: Simple Decorator (using closures and scope)
    # -------------------------------------------------------

    # WHY: Decorators are functions that wrap other functions, adding functionality.
    #      They rely heavily on closures to maintain state or reference the decorated function.

    def simple_timer(func: callable[..., int | float]) -> callable[..., int | float]:
        """A decorator that prints the execution time of a function."""
        import time # `time` module is part of the standard library.

        def wrapper(*args: object, **kwargs: object) -> int | float:
            """The wrapper function returned by the decorator."""
            start_time: float = time.perf_counter() # Local variable for start time.
            result: int | float = func(*args, **kwargs) # Call the original function.
            end_time: float = time.perf_counter() # Local variable for end time.
            elapsed_time: float = end_time - start_time # Calculate elapsed time.
            print(f"  Function '{func.__name__}' took {elapsed_time:.4f} seconds.")
            return result # Return the original function's result.
        return wrapper # Return the wrapper function (a closure).

    @simple_timer # Apply the decorator to the function below.
    def calculate_power(base: int, exponent: int) -> int:
        """Calculates base raised to the power of exponent."""
        # Simulate some work.
        import time
        time.sleep(0.01) # Sleep for a short duration.
        return base ** exponent

    print(f"  Calculating 2^10: {calculate_power(2, 10)}")
    # →   Function 'calculate_power' took 0.01... seconds.
    # →   Calculating 2^10: 1024

    print(f"  Calculating 3^5: {calculate_power(3, 5)}")
    # →   Function 'calculate_power' took 0.01... seconds.
    # →   Calculating 3^5: 243

    print("\n" + "─" * 40 + "\n")


# ═══════════════════════════════════════════════════════════════
# SECTION 5: Pythonic Idioms - Minimizing Global State
# ═══════════════════════════════════════════════════════════════

# A global variable, often considered "state".
DEBUG_MODE: bool = False # Global flag for debugging.

def section_5_pythonic_idioms() -> None:
    """Discusses and demonstrates minimizing reliance on global variables."""
    print("SECTION 5: Pythonic Idioms - Minimizing Global State")
    print("--------------------------------------------------")

    # WHY: Excessive use of global variables can lead to code that is hard to
    #      understand, test, and maintain. Changes in one part of the code
    #      can have unforeseen side effects in other parts.

    # Example 5.1: The "Less Pythonic" Way (relying on global state)
    # -------------------------------------------------------------

    # WHY: Show how functions become implicitly coupled to global variables.
    def process_data_global(data_item: str) -> str:
        """Processes a data item, relying on a global DEBUG_MODE."""
        if DEBUG_MODE: # Directly accesses the global DEBUG_MODE.
            print(f"  [DEBUG] Processing: {data_item}")
        return data_item.upper() + " (processed)"

    print("  --- Processing with global DEBUG_MODE = False ---")
    processed_1: str = process_data_global("item_a")
    # No debug print expected here.
    print(f"  Result 1: {processed_1}")
    # →   Result 1: ITEM_A (processed)

    global DEBUG_MODE # Need to use 'global' to change the module-level variable.
    DEBUG_MODE = True # Modify the global state.
    print("  --- Processing with global DEBUG_MODE = True ---")
    processed_2: str = process_data_global("item_b")
    # →   [DEBUG] Processing: item_b
    print(f"  Result 2: {processed_2}")
    # →   Result 2: ITEM_B (processed)
    DEBUG_MODE = False # Reset for other sections.

    # ✅ Preferred/Pythonic: Passing arguments (explicit dependencies)
    # -------------------------------------------------------------

    # WHY: Passing configuration as arguments makes functions more independent,
    #      testable, and easier to understand. Their dependencies are explicit.
    def process_data_explicit(data_item: str, debug: bool) -> str:
        """Processes a data item, with debug mode passed as an argument."""
        if debug: # Debug mode is now an explicit parameter.
            print(f"  [DEBUG] Processing: {data_item}")
        return data_item.upper() + " (processed)"

    print("  --- Processing with explicit debug=False ---")
    processed_3: str = process_data_explicit("item_c", False) # Pass False directly.
    # No debug print expected here.
    print(f"  Result 3: {processed_3}")
    # →   Result 3: ITEM_C (processed)

    print("  --- Processing with explicit debug=True ---")
    processed_4: str = process_data_explicit("item_d", True) # Pass True directly.
    # →   [DEBUG] Processing: item_d
    print(f"  Result 4: {processed_4}")
    # →   Result 4: ITEM_D (processed)

    # ✅ Preferred/Pythonic: Using classes for shared state
    # ----------------------------------------------------

    # WHY: Classes encapsulate related data (state) and behavior.
    #      Instance variables provide a clear way to manage state without globals.
    class DataProcessor:
        """A class to process data with configurable debug mode."""
        def __init__(self, debug_mode: bool = False) -> None:
            self.debug_mode: bool = debug_mode # Instance variable for debug mode.

        def process(self, data_item: str) -> str:
            """Processes a data item using the instance's debug mode."""
            if self.debug_mode:
                print(f"  [DEBUG] Processing (class): {data_item}")
            return data_item.upper() + " (class processed)"

    processor_debug_off: DataProcessor = DataProcessor(debug_mode=False) # Instance 1 with debug off.
    processor_debug_on: DataProcessor = DataProcessor(debug_mode=True)   # Instance 2 with debug on.

    print("  --- Processing with DataProcessor (debug off) ---")
    class_processed_1: str = processor_debug_off.process("item_e")
    print(f"  Result 5: {class_processed_1}")
    # →   Result 5: ITEM_E (class processed)

    print("  --- Processing with DataProcessor (debug on) ---")
    class_processed_2: str = processor_debug_on.process("item_f")
    # →   [DEBUG] Processing (class): item_f
    print(f"  Result 6: {class_processed_2}")
    # →   Result 6: ITEM_F (class processed)

    print("\n" + "─" * 40 + "\n")


# ═══════════════════════════════════════════════════════════════
# SECTION 6: Real-World Mini-Program - Simple Configuration Manager
# ═══════════════════════════════════════════════════════════════

# Global configuration dictionary (module-level state).
# ⚠️ While this is global, it's used as a demonstration of a central config.
#    In larger apps, this might be loaded from a file or managed by a ConfigManager class.
GLOBAL_APP_CONFIG: dict[str, str | int | bool] = {
    "log_level": "INFO",
    "max_retries": 3,
    "feature_enabled": True,
    "api_key": "some_default_key"
}

class ConfigManager:
    """
    A simple configuration manager demonstrating different scopes.
    It allows setting default configurations and overriding them locally.
    """
    def __init__(self, default_config: dict[str, str | int | bool]) -> None:
        self._config: dict[str, str | int | bool] = default_config.copy() # Instance variable for configuration.
        print(f"  ConfigManager initialized with: {self._config['log_level']} log level.")

    def get_setting(self, key: str) -> str | int | bool | None:
        """Retrieves a configuration setting."""
        # Accessing instance variable _config.
        return self._config.get(key)

    def set_setting(self, key: str, value: str | int | bool) -> None:
        """Sets or updates a configuration setting."""
        # Modifying instance variable _config.
        self._config[key] = value
        print(f"  ConfigManager: Set '{key}' to '{value}'.")

    def _internal_process(self, data: str) -> str:
        """An internal method demonstrating local access to config."""
        # 'data' is local to this method.
        # 'self._config' is an instance variable.
        current_log_level: str | int | bool | None = self.get_setting("log_level") # Accessing instance method.
        if current_log_level == "DEBUG":
            print(f"  [DEBUG] Internal process for: {data}")
        return f"{data.upper()} (processed with log_level={current_log_level})"

def process_data_with_config(data: str, config_mgr: ConfigManager) -> str:
    """
    Processes data using a provided ConfigManager instance.
    Demonstrates local function scope interacting with an object's instance scope.
    """
    # 'data' and 'config_mgr' are local to this function.
    log_level: str | int | bool | None = config_mgr.get_setting("log_level") # Accessing instance method.
    max_retries: str | int | bool | None = config_mgr.get_setting("max_retries")

    if log_level == "INFO":
        print(f"  INFO: Processing '{data}' with {max_retries} retries.")

    # Simulate some processing, potentially using internal methods.
    processed_output: str = config_mgr._internal_process(data)
    return processed_output

def section_6_real_world_mini_program() -> None:
    """
    Demonstrates scope management in a simple configuration scenario using a class.
    """
    print("SECTION 6: Real-World Mini-Program - Simple Configuration Manager")
    print("---------------------------------------------------------------")

    print(f"  Global app config log_level: {GLOBAL_APP_CONFIG['log_level']}")
    # →   Global app config log_level: INFO

    # Create a ConfigManager instance based on the global config.
    app_config_manager: ConfigManager = ConfigManager(GLOBAL_APP_CONFIG)

    # Process some data using the default configuration.
    output_1: str = process_data_with_config("report_A", app_config_manager)
    # →   ConfigManager initialized with: INFO log level.
    # →   INFO: Processing 'report_A' with 3 retries.
    print(f"  Output 1: {output_1}\n")
    # →   Output 1: REPORT_A (processed with log_level=INFO)

    # Locally override a setting within the ConfigManager instance.
    app_config_manager.set_setting("log_level", "DEBUG")
    # →   ConfigManager: Set 'log_level' to 'DEBUG'.

    # Process more data with the updated configuration.
    output_2: str = process_data_with_config("report_B", app_config_manager)
    # →   [DEBUG] Internal process for: report_B
    print(f"  Output 2: {output_2}\n")
    # →   Output 2: REPORT_B (processed with log_level=DEBUG)

    # Demonstrate creating another manager with different settings.
    # This config is local to this section, not global.
    temp_config_for_task: dict[str, str | int | bool] = {
        "log_level": "WARNING",
        "max_retries": 1,
        "feature_enabled": False
    }
    task_config_manager: ConfigManager = ConfigManager(temp_config_for_task)
    # →   ConfigManager initialized with: WARNING log level.

    output_3: str = process_data_with_config("task_X", task_config_manager)
    # No INFO/DEBUG print expected here, as log_level is WARNING.
    print(f"  Output 3: {output_3}\n")
    # →   Output 3: TASK_X (processed with log_level=WARNING)

    # The original GLOBAL_APP_CONFIG remains unchanged.
    print(f"  Global app config log_level (still original): {GLOBAL_APP_CONFIG['log_level']}")
    # →   Global app config log_level (still original): INFO

    print("\n" + "─" * 40 + "\n")


# ═══════════════════════════════════════════════════════════════
# SECTION 7: Performance & Memory - Scope Lookup Overhead
# ═══════════════════════════════════════════════════════════════

# Global variable for performance test.
GLOBAL_VALUE: int = 100

def section_7_performance_memory() -> None:
    """Briefly discusses the minor performance implications of scope lookup."""
    print("SECTION 7: Performance & Memory - Scope Lookup Overhead")
    print("-----------------------------------------------------")

    # WHY: While scope lookup is highly optimized in Python