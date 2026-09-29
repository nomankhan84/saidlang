"""
SaidLang Python Import Hook
Allows direct importing of .said files in standard Python code.

Usage in Python:
    import saidlang.hook
    import my_said_script  # Loads my_said_script.said automatically!
"""

import sys
import os
import importlib.abc
import importlib.machinery
from saidlang.transpiler import SaidLangTranspiler

class SaidLangLoader(importlib.abc.Loader):
    def __init__(self, filename):
        self.filename = filename
        self.transpiler = SaidLangTranspiler(include_runtime=True)

    def exec_module(self, module):
        with open(self.filename, 'r', encoding='utf-8') as f:
            source = f.read()

        py_code = self.transpiler.transpile(source)
        compiled = compile(py_code, self.filename, 'exec')
        exec(compiled, module.__dict__)

class SaidLangFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if path is None:
            path = sys.path

        name = fullname.rsplit('.', 1)[-1]
        for p in path:
            candidate = os.path.join(p, f"{name}.said")
            if os.path.isfile(candidate):
                return importlib.machinery.ModuleSpec(
                    fullname,
                    SaidLangLoader(candidate),
                    origin=candidate
                )
        return None

# Auto-install the import hook upon import
if not any(isinstance(finder, SaidLangFinder) for finder in sys.meta_path):
    sys.meta_path.insert(0, SaidLangFinder())
