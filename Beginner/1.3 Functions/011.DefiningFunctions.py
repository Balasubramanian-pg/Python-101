"""
Defining Functions: The Building Blocks of Reusable Code

This module introduces the fundamental concepts of defining and using functions in Python. Functions are
essential for organizing code, promoting reusability, and making programs more modular and readable.

What you will learn:
• How to define a function using the `def` keyword.
• The role of parameters and arguments in functions.
• How to return values from a function.
• Understanding variable scope (local vs. global) within functions.
• Applying type hints for better code readability and maintainability.
• Writing effective docstrings to document function purpose and usage.

Prerequisites:
• Basic understanding of Python syntax (variables, data types, operators).
• Familiarity with control flow statements (if/else, loops).

Key Concepts Covered:
• Function definition (`def`)
• Function call
• Parameters and arguments (positional, keyword, default)
• Return statement
• Docstrings (PEP 257)
• Type hinting (PEP 484, PEP 585)
• Local and global scope
• The `nonlocal` keyword
• Side effects
• Mutable default arguments (and how to avoid issues)
• Arbitrary positional arguments (`*args`)
• Arbitrary keyword arguments (`**kwargs`)
• Nested functions (closures)
• First-class functions
• Generator functions (`yield`)
• Function overhead (basic understanding)
• Memory efficiency with generators
"""

import time # For measuring performance in Section 7
import sys