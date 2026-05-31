"""Break Continue

This script explores the fundamental control flow statements `break` and `continue` in Python.
It demonstrates how these statements alter the normal execution flow within loops, offering
powerful ways to manage iteration based on specific conditions.

What you will learn:
• The core purpose and behavior of the `break` statement.
• The core purpose and behavior of the `continue` statement.
• How `break` and `continue` affect `for` loops and `while` loops.
• The impact of `break` and `continue` in nested loop structures.
• Common pitfalls and best practices when using these control flow statements.
• Pythonic alternatives and when to prefer them over explicit `break`/`continue`.

Prerequisites:
• Basic understanding of Python `for` and `while` loops.
• Familiarity with conditional statements (`if`, `elif`, `else`).
• Knowledge of basic data structures like lists and ranges.

Key Concepts Covered:
- `break` statement
- `continue` statement
- `for` loops
- `while` loops
- Nested loops
- Loop `else` clause
- Generator functions
- Pythonic filtering
- Early exit optimization
"""

import time # For performance measurement in Section 7
import sys  # For sys.getsizeof in Section 7 (though not strictly memory, useful for object size)

# ═══════════════════════════════════════════════════════════════
# SECTION 1: Core Concept: Understanding `