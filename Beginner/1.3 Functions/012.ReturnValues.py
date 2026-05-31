"""
Return Values
This module explores how functions in Python send results back to the caller using the `return` keyword.
Understanding return values is fundamental for writing modular, reusable, and effective Python code.

What you will learn:
•  The core purpose and syntax of the `return` keyword.
•  How Python functions implicitly return `None` if `return` is not explicitly used.
•  Returning various data types: numbers, strings, collections, and booleans.
•  The mechanism of returning multiple values using tuples and tuple unpacking.
•  Advanced patterns like early exit, chained function calls, and returning functions.
•  Memory-efficient data processing using generator functions and the `yield` keyword.

Prerequisites:
•  Basic understanding of Python syntax and program flow.
•  Familiarity with defining and calling functions.
•  Knowledge of fundamental data types (integers, strings, lists, dictionaries, booleans).

Key Concepts Covered:
`return` keyword, `None` type, function signature, type hints, tuple unpacking, early exit,
generator functions, `yield` keyword, function composition, memory efficiency, `time` module, `sys.getsizeof`.
"""

import time # For performance measurement in Section 7
import sys  # For sys.getsizeof in Section 7

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: The Purpose of `return`
# ════════════════