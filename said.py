#!/usr/bin/env python3
"""
SaidLang Root Entrypoint
Usage:
    python said.py run examples/hello.said
    python said.py build examples/hello.said -o hello.py
    python said.py preview examples/hello.said
    python said.py repl
"""

import os
import sys

# Ensure local directory is on python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from saidlang.cli import main

if __name__ == "__main__":
    main()
