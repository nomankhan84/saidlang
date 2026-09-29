"""
SaidLang Runtime Environment & Built-in Helper Functions.
Provides friendly natural-language standard library functions.
"""

import sys
import time
import random

def show(*args, sep=' ', end='\n'):
    """Print output to console nicely."""
    formatted = []
    for arg in args:
        if isinstance(arg, bool):
            formatted.append("true" if arg else "false")
        else:
            formatted.append(str(arg))
    print(sep.join(formatted), end=end)

def ask(prompt=""):
    """Ask user for text input."""
    return input(str(prompt))

def ask_number(prompt=""):
    """Ask user for a numeric input (int or float)."""
    val = input(str(prompt)).strip()
    try:
        if '.' in val:
            return float(val)
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return 0

def length_of(item):
    """Return the length/size of a list, string, or dictionary."""
    return len(item)

def random_number(minimum=1, maximum=100):
    """Generate a random number between minimum and maximum inclusive."""
    return random.randint(int(minimum), int(maximum))

def wait(seconds):
    """Pause execution for given seconds."""
    time.sleep(float(seconds))

def uppercase(text):
    """Convert text to UPPERCASE."""
    return str(text).upper()

def lowercase(text):
    """Convert text to lowercase."""
    return str(text).lower()

def capitalize_text(text):
    """Capitalize first letter."""
    return str(text).capitalize()

def join_words(words, separator=" "):
    """Join words with a separator."""
    return separator.join(str(w) for w in words)
