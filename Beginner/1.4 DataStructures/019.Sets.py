"""Sets: Unordered Collections of Unique Elements

Sets are a fundamental data structure in Python, representing an unordered collection of unique, hashable elements. They are highly efficient for tasks like membership testing, removing duplicates, and performing mathematical set operations.

What you will learn:
* How to create and initialize sets using various methods.
* Basic set operations like adding, removing, and checking for element existence.
* The critical concept of hashability and why it matters for set elements.
* Advanced mathematical set operations: union, intersection, difference, and symmetric difference.
* Pythonic idioms for efficient data manipulation, such as deduplication.
* Real-world applications of sets in data analysis scenarios.
* Performance characteristics of sets, especially for membership testing.

Prerequisites:
* Basic understanding of Python syntax and data types (integers, strings, booleans).
* Familiarity with lists and their mutable, ordered nature.
* Concept of iteration and loops in Python.

Key Concepts Covered:
* Set creation (`{}` vs `set()`)
* Mutability of sets
* Hashability of set elements
* `add()`, `remove()`, `discard()`, `pop()`, `clear()` methods
* `in` operator for membership testing
* `len()` for set size
* `frozenset` (immutable sets)
* Set operations: `union()`, `intersection()`, `difference()`, `symmetric_difference()`
* Comparison operators: `issubset()`, `issuperset()`, `isdisjoint()`
* Set comprehensions
* Performance implications of using sets for unique element management
"""

import time # Used for basic performance measurement in Section 7
import collections # Not directly used but good to keep in mind for related concepts

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: What are Sets?
# ═══════════════════════════════════════════════════════════════

def section_1_core_concept() -> None:
    """
    Introduces the absolute fundamentals of sets: creation, uniqueness, and mutability.
    """
    print("SECTION 1: Core Concept: What are Sets?\n")

    # 1.1 Creating Sets
    # Sets can be created using curly braces {} or the set() constructor.
    # An empty set MUST be created with set(), as {} creates an empty dictionary.
    empty_set: set[int] = set() # Creates an empty set, specifying expected element type
    print(f"1.1.1 Empty set created with set(): {empty_set}")
    # → 1.1.1 Empty set created with set(): set()

    # ⚠️ Common mistake: Using {} to create an empty set results in a dictionary.
    # empty_dict = {}
    # print(type(empty_dict)) # <class 'dict'>

    # Creating a set with elements using curly braces
    fruits_set: set[str] = {"apple", "banana", "cherry"} # Set of strings
    print(f"1.1.2 Set created with {{}}: {fruits_set}")
    # → 1.1.2 Set created with {}: {'cherry', 'apple', 'banana'} (order may vary)

    # Creating a set from an iterable (like a list or tuple) using the set() constructor
    numbers_list: list[int] = [1, 2, 3, 2, 4, 1] # A list with duplicate numbers
    unique_numbers_set: set[int] = set(numbers_list) # Convert list to set, duplicates are automatically removed
    print(f"1.1.3 Set created from a list: {unique_numbers_set}")
    # → 1.1.3 Set created from a list: {1, 2, 3, 4} (order may vary)

    # 1.2 Uniqueness Property
    # Sets automatically ensure that all elements are unique.
    # If duplicate elements are provided during creation, only one instance is kept.
    colors_with_duplicates: set[str] = {"red", "green", "blue", "red", "green"} # 'red' and 'green' are repeated
    print(f"1.2.1 Set with duplicates removed: {colors_with_duplicates}")
    # → 1.2.1 Set with duplicates removed: {'red', 'blue', 'green'} (order may vary)

    # 🔑 Key insight: Sets are inherently designed for unique element storage.

    # 1.3 Unordered Nature
    # Sets do not maintain any specific order of elements.
    # The order of elements when printed or iterated over is not guaranteed.
    my_set: set[int] = {10, 20, 30, 40}
    print(f"1.3.1 Set elements (order not guaranteed): {my_set}")
    # → 1.3.1 Set elements (order not guaranteed): {40, 10, 20, 30} (example output, actual order varies)

    # 1.4 Mutability of Sets
    # Sets are mutable, meaning you can add or remove elements after creation.
    mutable_set: set[str] = {"alpha", "beta"}
    print(f"1.4.1 Original mutable set: {mutable_set}")
    # → 1.4.1 Original mutable set: {'alpha', 'beta'}

    mutable_set.add("gamma") # Add a new element
    print(f"1.4.2 Set after adding 'gamma': {mutable_set}")
    # → 1.4.2 Set after adding 'gamma': {'alpha', 'beta', 'gamma'}

    mutable_set.remove("beta") # Remove an existing element
    print(f"1.4.3 Set after removing 'beta': {mutable_set}")
    # → 1.4.3 Set after removing 'beta': {'alpha', 'gamma'}

    # 1.5 Hashability Requirement for Set Elements
    # Elements stored in a set must be "hashable".
    # Hashable objects have a hash value that never changes during their lifetime.
    # Immutable types (numbers, strings, tuples, frozensets) are hashable.
    # Mutable types (lists, dictionaries, sets) are NOT hashable.

    hashable_elements: set[int | str | tuple[int, int]] = {1, "hello", (1, 2)} # Valid elements
    print(f"1.5.1 Set with hashable elements: {hashable_elements}")
    # → 1.5.1 Set with hashable elements: {1, 'hello', (1, 2)} (order may vary)

    # ⚠️ Common mistake: Trying to add an unhashable type (like a list) to a set.
    # This will raise a TypeError.
    try:
        # my_set_with_list = {1, [2, 3]} # This line would cause a TypeError
        pass # Commented out to prevent script termination
    except TypeError as e:
        print(f"1.5.2 Attempting to add a list to a set raises: {e}")
        # → 1.5.2 Attempting to add a list to a set raises: unhashable type: 'list'

    # 1.6 Frozenset: Immutable Sets
    # A frozenset is an immutable version of a set.
    # Once created, elements cannot be added or removed.
    # Frozensets ARE hashable and can therefore be elements of other sets or keys in dictionaries.
    frozen_items: frozenset[str] = frozenset(["cat", "dog", "mouse"])
    print(f"1.6.1 Frozenset: {frozen_items}")
    # → 1.6.1 Frozenset: frozenset({'mouse', 'dog', 'cat'})

    # ℹ️ Note: Attempting to modify a frozenset will raise an AttributeError.
    try:
        # frozen_items.add("bird") # This line would cause an AttributeError
        pass # Commented out to prevent script termination
    except AttributeError as e:
        print(f"1.6.2 Attempting to modify a frozenset raises: {e}")
        # → 1.6.2 Attempting to modify a frozenset raises: 'frozenset' object has no attribute 'add'

    # Example of a frozenset as an element in another set:
    set_of_frozensets: set[frozenset[int]] = {frozenset({1, 2}), frozenset({3, 4})}
    print(f"1.6.3 Set containing frozensets: {set_of_frozensets}")
    # → 1.6.3 Set containing frozensets: {frozenset({1, 2}), frozenset({3, 4})}
    print("-" * 40 + "\n")


# ═══════════════════════════════════════════════════════════════
# SECTION 2: Syntax & Common Patterns: Basic Operations
# ═══════════════════════════════════════════════════════════════

def section_2_syntax_common_patterns() -> None:
    """
    Covers the everyday usage of sets, including adding, removing, checking
    membership, and iterating.
    """
    print("SECTION 2: Syntax & Common Patterns: Basic Operations\n")

    my_elements: set[str] = {"alpha", "beta", "gamma"}
    print(f"2.1 Initial set: {my_elements}")
    # → 2.1 Initial set: {'alpha', 'beta', 'gamma'}

    # 2.1 Adding Elements
    # .add(element) adds a single element to the set.
    # If the element already exists, nothing happens (due to uniqueness).
    my_elements.add("delta") # Add a new element
    print(f"2.1.1 After adding 'delta': {my_elements}")
    # → 2.1.1 After adding 'delta': {'alpha', 'beta', 'gamma', 'delta'}

    my_elements.add("alpha") # Adding an existing element has no effect
    print(f"2.1.2 After adding 'alpha' again: {my_elements}")
    # → 2.1.2 After adding 'alpha' again: {'alpha', 'beta', 'gamma', 'delta'}

    # .update(iterable) adds all elements from an iterable to the set.
    my_elements.update(["epsilon", "zeta", "alpha"]) # Add multiple elements, duplicates ignored
    print(f"2.1.3 After updating with list: {my_elements}")
    # → 2.1.3 After updating with list: {'epsilon', 'zeta', 'alpha', 'beta', 'gamma', 'delta'}

    # 2.2 Removing Elements
    # .remove(element) removes a specified element. Raises KeyError if element not found.
    try:
        my_elements.remove("beta") # Remove an existing element
        print(f"2.2.1 After removing 'beta': {my_elements}")
        # → 2.2.1 After removing 'beta': {'epsilon', 'zeta', 'alpha', 'gamma', 'delta'}
    except KeyError as e:
        print(f"2.2.1 Error removing 'beta': {e}")

    try:
        my_elements.remove("lambda") # Try to remove a non-existent element
    except KeyError as e:
        print(f"2.2.2 Attempting to remove non-existent element raises: {e}")
        # → 2.2.2 Attempting to remove non-existent element raises: 'lambda'

    # .discard(element) removes a specified element. Does nothing if element not found (no error).
    my_elements.discard("gamma") # Remove an existing element
    print(f"2.2.3 After discarding 'gamma': {my_elements}")
    # → 2.2.3 After discarding 'gamma': {'epsilon', 'zeta', 'alpha', 'delta'}

    my_elements.discard("lambda") # Discard a non-existent element, no error
    print(f"2.2.4 After discarding non-existent 'lambda': {my_elements}")
    # → 2.2.4 After discarding non-existent 'lambda': {'epsilon', 'zeta', 'alpha', 'delta'}

    # .pop() removes and returns an arbitrary element from the set. Raises KeyError if set is empty.
    popped_element: str = my_elements.pop() # Remove and get an arbitrary element
    print(f"2.2.5 Popped element: '{popped_element}', Set now: {my_elements}")
    # → 2.2.5 Popped element: 'epsilon', Set now: {'zeta', 'alpha', 'delta'} (element popped varies)

    # .clear() removes all elements from the set.
    my_elements.clear() # Empty the set
    print(f"2.2.6 After clearing the set: {my_elements}")
    # → 2.2.6 After clearing the set: set()

    # 2.3 Membership Testing (using 'in' and 'not in' operators)
    # Checks if an element exists in the set. Very fast for sets.
    present_set: set[str] = {"apple", "orange", "grape"}
    print(f"2.3.1 Is 'apple' in {present_set}? {'apple' in present_set}")
    # → 2.3.1 Is 'apple' in {'apple', 'orange', 'grape'}? True
    print(f"2.3.2 Is 'kiwi' in {present_set}? {'kiwi' in present_set}")
    # → 2.3.2 Is 'kiwi' in {'apple', 'orange', 'grape'}? False

    # 2.4 Length of a Set (using len())
    # Returns the number of unique elements in the set.
    print(f"2.4.1 Length of {present_set}: {len(present_set)}")
    # → 2.4.1 Length of {'apple', 'orange', 'grape'}: 3

    # 2.5 Iterating Over Sets
    # You can loop through elements of a set. Order is not guaranteed.
    print("2.5.1 Iterating through a set:")
    for item in present_set: # Loop through each element
        print(f"  - {item}")
    # → 2.5.1 Iterating through a set:
    #   - apple
    #   - orange
    #   - grape (order may vary)

    # 2.6 Converting Other Iterables to Sets
    # Sets are often used to quickly get unique elements from lists, tuples, or strings.
    data_list: list[int] = [1, 5, 2, 5, 3, 1, 4]
    unique_data: set[int] = set(data_list) # Convert list to set
    print(f"2.6.1 Unique elements from list {data_list}: {unique_data}")
    # → 2.6.1 Unique elements from list [1, 5, 2, 5, 3, 1, 4]: {1, 2, 3, 4, 5}

    text_string: str = "hello world"
    unique_chars: set[str] = set(text_string) # Convert string to set of unique characters
    print(f"2.6.2 Unique characters from string '{text_string}': {unique_chars}")
    # → 2.6.2 Unique characters from string 'hello world': {'r', 'e', 'w', 'l', ' ', 'd', 'h', 'o'} (order may vary)
    print("-" * 40 + "\n")


# ═══════════════════════════════════════════════════════════════
# SECTION 3: Edge Cases & Gotchas: Hashability
# ═══════════════════════════════════════════════════════════════

def section_3_edge_cases_gotchas() -> None:
    """
    Focuses on common pitfalls related to sets, particularly the hashability
    requirement for elements.
    """
    print("SECTION 3: Edge Cases & Gotchas: Hashability\n")

    # 3.1 Understanding Hashability
    # 🔑 Key insight: Set elements must be hashable. This means they must have a constant hash value
    # throughout their lifetime (i.e., they must be immutable).
    # Python's built-in immutable types: int, float, str, tuple, frozenset.
    # Python's built-in mutable types: list, dict, set.

    # ✅ Valid: Set of integers, strings, tuples, and frozensets
    valid_elements_set: set[int | str | tuple[int, str] | frozenset[int]] = {
        10,
        "Python",
        (1, "tuple"),
        frozenset({1, 2, 3})
    }
    print(f"3.1.1 Set with valid (hashable) elements: {valid_elements_set}")
    # → 3.1.1 Set with valid (hashable) elements: {10, 'Python', (1, 'tuple'), frozenset({1, 2, 3})} (order may vary)

    # ⚠️ Common mistake: Attempting to add mutable objects (lists, dictionaries, sets)
    # directly as elements to a set will result in a TypeError.

    # 🐛 Bug source: Unhashable types
    unhashable_list: list[int] = [1, 2, 3]
    unhashable_dict: dict[str, int] = {"a": 1, "b": 2}
    unhashable_set: set[int] = {4, 5, 6}

    try:
        # my_problem_set = {1, "hello", unhashable_list} # This line would cause a TypeError
        pass # Commented out to prevent script termination
    except TypeError as e:
        print(f"3.1.2 Error trying to add a list to a set: {e}")
        # → 3.1.2 Error trying to add a list to a set: unhashable type: 'list'

    try:
        # my_problem_set = {1, "hello", unhashable_dict} # This line would cause a TypeError
        pass # Commented out to prevent script termination
    except TypeError as e:
        print(f"3.1.3 Error trying to add a dict to a set: {e}")
        # → 3.1.3 Error trying to add a dict to a set: unhashable type: 'dict'

    try:
        # my_problem_set = {1, "hello", unhashable_set} # This line would cause a TypeError
        pass # Commented out to prevent script termination
    except TypeError as e:
        print(f"3.1.4 Error trying to add another set to a set: {e}")
        # → 3.1.4 Error trying to add another set to a set: unhashable type: 'set'

    # 3.2 Using Frozenset for Nested Sets
    # If you need to store a collection of unique collections, and those inner collections
    # need to be mutable-like but hashable, frozenset is the solution.
    # It allows you to create a "set of sets" (where the inner sets are frozensets).
    set_of_frozensets_example: set[frozenset[int]] = {
        frozenset({1, 2}),
        frozenset({3, 4, 5}),
        frozenset({1, 2}) # Duplicate frozenset, will be ignored
    }
    print(f"3.2.1 Set of frozensets: {set_of_frozensets_example}")
    # → 3.2.1 Set of frozensets: {frozenset({1, 2}), frozenset({3, 4, 5})} (order may vary)

    # 3.3 Implications of Unordered Nature
    # While not directly a "gotcha" for functionality, beginners sometimes expect
    # sets to maintain insertion order, which they do not.
    # This means you cannot rely on indexing or slicing.
    unordered_example: set[int] = {5, 1, 4, 2, 3}
    print(f"3.3.1 Set: {unordered_example}")
    # → 3.3.1 Set: {1, 2, 3, 4, 5} (Python 3.7+ may show insertion order for small sets, but not guaranteed)
    # ℹ️ Note: Python 3.7+ implements insertion-order preservation for dictionaries and sets,
    # but this is an implementation detail and not part of the language specification for sets.
    # Relying on it is non-portable and generally discouraged.

    try:
        # print(unordered_example[0]) # This line would cause a TypeError
        pass # Commented out to prevent script termination
    except TypeError as e:
        print(f"3.3.2 Attempting to index a set raises: {e}")
        # → 3.3.2 Attempting to index a set raises: 'set' object is not subscriptable
    print("-" * 40 + "\n")


# ═══════════════════════════════════════════════════════════════
# SECTION 4: Intermediate Patterns: Mathematical Set Operations
# ═══════════════════════════════════════════════════════════════

def section_4_intermediate_patterns() -> None:
    """
    Explores the powerful mathematical operations available for sets,
    which are analogous to set theory concepts.
    """
    print("SECTION 4: Intermediate Patterns: Mathematical Set Operations\n")

    set_a: set[int] = {1, 2, 3, 4, 5}
    set_b: set[int] = {4, 5, 6, 7, 8}
    set_c: set[int] = {1, 2}
    set_d: set[int] = {9, 10}

    print(f"Initial Set A: {set_a}")
    print(f"Initial Set B: {set_b}")
    print(f"Initial Set C: {set_c}")
    print(f"Initial Set D: {set_d}\n")

    # 4.1 Union: Elements in either set (or both)
    # Operator: `|`
    # Method: `union()`
    union_set_op: set[int] = set_a | set_b # Using the | operator
    union_set_method: set[int] = set_a.union(set_b) # Using the union() method
    print(f"4.1.1 Union of A and B (A | B): {union_set_op}")
    # → 4.1.1 Union of A and B (A | B): {1, 2, 3, 4, 5, 6, 7, 8}
    print(f"4.1.2 Union of A and B (A.union(B)): {union_set_method}")
    # → 4.1.2 Union of A and B (A.union(B)): {1, 2, 3, 4, 5, 6, 7, 8}

    # 4.2 Intersection: Elements common to both sets
    # Operator: `&`
    # Method: `intersection()`
    intersection_set_op: set[int] = set_a & set_b # Using the & operator
    intersection_set_method: set[int] = set_a.intersection(set_b) # Using the intersection() method
    print(f"4.2.1 Intersection of A and B (A & B): {intersection_set_op}")
    # → 4.2.1 Intersection of A and B (A & B): {4, 5}
    print(f"4.2.2 Intersection of A and B (A.intersection(B)): {intersection_set_method}")
    # → 4.2.2 Intersection of A and B (A.intersection(B)): {4, 5}

    # 4.3 Difference: Elements in the first set but NOT in the second
    # Operator: `-`
    # Method: `difference()`
    difference_set_op: set[int] = set_a - set_b # Elements in A but not in B
    difference_set_method: set[int] = set_a.difference(set_b) # Elements in A but not in B
    print(f"4.3.1 Difference of A and B (A - B): {difference_set_op}")
    # → 4.3.1 Difference of A and B (A - B): {1, 2, 3}
    print(f"4.3.2 Difference of A and B (A.difference(B)): {difference_set_method}")
    # → 4.3.2 Difference of A and B (A.difference(B)): {1, 2, 3}

    difference_set_b_a: set[int] = set_b - set_a # Elements in B but not in A
    print(f"4.3.3 Difference of B and A (B - A): {difference_set_b_a}")
    # → 4.3.3 Difference of B and A (B - A): {8, 6, 7}

    # 4.4 Symmetric Difference: Elements in either set, but NOT in both
    # Operator: `^`
    # Method: `symmetric_difference()`
    symmetric_difference_set_op: set[int] = set_a ^ set_b # Elements unique to A or B
    symmetric_difference_set_method: set[int] = set_a.symmetric_difference(set_b)
    print(f"4.4.1 Symmetric Difference of A and B (A ^ B): {symmetric_difference_set_op}")
    # → 4.4.1 Symmetric Difference of A and B (A ^ B): {1, 2, 3, 6, 7, 8}
    print(f"4.4.2 Symmetric Difference of A and B (A.symmetric_difference(B)): {symmetric_difference_set_method}")
    # → 4.4.2 Symmetric Difference of A and B (A.symmetric_difference(B)): {1, 2, 3, 6, 7, 8}

    # 4.5 Subset and Superset: Relationship between sets
    # `issubset()` or `<=` : Checks if all elements of one set are in another.
    # `issuperset()` or `>=` : Checks if one set contains all elements of another.
    print(f"4.5.1 Is C a subset of A ({set_c} <= {set_a})? {set_c <= set_a}")
    # → 4.5.1 Is C a subset of A ({1, 2} <= {1, 2, 3, 4, 5})? True
    print(f"4.5.2 Is A a superset of C ({set_a} >= {set_c})? {set_a >= set_c}")
    # → 4.5.2 Is A a superset of C ({1, 2, 3, 4, 5} >= {1, 2})? True
    print(f"4.5.3 Is B a subset of A ({set_b} <= {set_a})? {set_b <= set_a}")
    # → 4.5.3 Is B a subset of A ({4, 5, 6, 7, 8} <= {1, 2, 3, 4, 5})? False