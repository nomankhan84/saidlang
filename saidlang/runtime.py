"""
SaidLang Runtime Environment & Standard Math/String/IO Library
"""

import sys
import time
import random
import math
import os
import json
import urllib.request
import statistics

def show(*args, sep=' ', end='\n'):
    """Print output to console nicely."""
    formatted = []
    for arg in args:
        if isinstance(arg, bool):
            formatted.append("true" if arg else "false")
        elif arg is None:
            formatted.append("nothing")
        else:
            formatted.append(str(arg))
    print(sep.join(formatted), end=end)

def ask(prompt=""):
    """Ask user for text input without trailing newline."""
    return input(str(prompt))

def ask_number(prompt=""):
    """Ask user for a numeric input (int or float)."""
    val = input(str(prompt)).strip()
    try:
        if '.' in val:
            return float(val)
        return int(val)
    except ValueError:
        return 0

def ask_boolean(prompt=""):
    """Ask user for a yes/no or true/false input."""
    val = input(str(prompt)).strip().lower()
    return val in ("yes", "y", "true", "t", "1")

# ----------------- Math Helpers -----------------

def calculate_percent(percent, total):
    """Calculate X percent of Y: (percent / 100) * total."""
    return (float(percent) / 100.0) * float(total)

def square_root(val):
    """Calculate square root."""
    return math.isqrt(int(val)) if (isinstance(val, int) and int(val) >= 0 and math.isqrt(int(val))**2 == int(val)) else math.sqrt(float(val))

def power_of(base, exp):
    """Calculate base to the power of exp."""
    return base ** exp

def round_number(val, decimals=0):
    """Round a number to given decimal places."""
    if decimals == 0:
        return round(float(val))
    return round(float(val), int(decimals))

def find_highest(collection):
    """Find maximum item in list or numbers."""
    if isinstance(collection, (int, float)):
        return collection
    return max(collection)

def find_lowest(collection):
    """Find minimum item in list or numbers."""
    if isinstance(collection, (int, float)):
        return collection
    return min(collection)

def find_average(collection):
    """Find arithmetic average/mean of list."""
    if not collection:
        return 0
    return statistics.mean(collection)

def random_number(minimum=1, maximum=100):
    """Generate random integer between min and max inclusive."""
    return random.randint(int(minimum), int(maximum))

def pick_random(collection):
    """Pick a random item from a list or collection."""
    if not collection:
        return None
    return random.choice(list(collection))

# ----------------- String Helpers -----------------

def to_uppercase(text):
    return str(text).upper()

def to_lowercase(text):
    return str(text).lower()

def trim_spaces(text):
    return str(text).strip()

def count_characters(text):
    return len(str(text))

def count_words(text):
    return len(str(text).split())

def replace_text(text, old_val, new_val):
    return str(text).replace(str(old_val), str(new_val))

def text_contains(text, sub):
    return str(sub) in str(text)

def text_starts_with(text, sub):
    return str(text).startswith(str(sub))

def text_ends_with(text, sub):
    return str(text).endswith(str(sub))

def split_text(text, sep=" "):
    return str(text).split(str(sep))

def length_of(item):
    return len(item)

def wait(seconds):
    time.sleep(float(seconds))

# ----------------- File & Web Helpers -----------------

def write_file(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(content))
    return True

def read_file(filepath):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def append_file(filepath, content):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(str(content))
    return True

def fetch_url(url):
    req = urllib.request.Request(url, headers={"User-Agent": "SaidLang/0.1"})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8")

def fetch_json(url):
    raw = fetch_url(url)
    return json.loads(raw)
