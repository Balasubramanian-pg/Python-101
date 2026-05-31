"""
Tuples: Immutable Sequences in Python

This module explores tuples, an ordered, immutable collection type in Python. You'll learn
how to create, access, and effectively use tuples for various programming tasks.

What you will learn:
• The fundamental concept of tuples as immutable data structures.
• Various syntax for creating tuples, including single-element tuples.
• How to access elements using indexing and slice notation.
• Practical applications of tuple unpacking and extended unpacking.
• The implications of immutability, especially with nested mutable objects.
• Pythonic idioms and performance considerations when using tuples.

Prerequisites:
• Basic understanding of Python variables and data types (integers, strings).
• Familiarity with lists and their mutable nature.
• Knowledge of basic control flow (if/else, for loops).

Key Concepts Covered:
• Tuple creation (literals, constructor)
• Immutability
• Indexing and Slicing
• Tuple Unpacking
• Single-element tuple syntax
• Tuples as function return values
• Nested Tuples
• `collections.namedtuple`
• Generator Expressions (tuple-like behavior)
• Extended Unpacking
• Tuples as dictionary keys
• Performance and Memory comparison with Lists
"""

import sys # Used for sys.getsizeof in Section 7
import time # Used for basic timing in Section 7
from collections import namedtuple # Used for namedtuple in Section 4

# ════════════════════════════════════════════════════════