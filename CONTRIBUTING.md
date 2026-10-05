# Contributing to SaidLang

Thank you for your interest in contributing to SaidLang! We welcome contributions from developers, educators, and language enthusiasts of all skill levels.

---

## 🛠️ Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nomankhan84/saidlang.git
   cd saidlang
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install in editable development mode with test dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

---

## 🧪 Running Tests

Before submitting any code changes, ensure the test suite passes:

```bash
# Run all tests
pytest tests/ -v

# Run with test coverage
pytest --cov=saidlang tests/

# Run example verification
python -m tests.test_examples
```

---

## 📂 Project Architecture

- **`saidlang/transpiler.py`**: The core parser and transpiler engine. Converts `.said` source code into clean Python code.
- **`saidlang/runtime.py`**: The standard library and built-in helper functions (e.g., `show`, `ask`, `read_file`, `write_file`).
- **`saidlang/cli.py`**: The Command Line Interface (`said run`, `said build`, `said repl`).
- **`saidlang/hook.py`**: Python import hook enabling native `import my_module` for `.said` files.
- **`tests/`**: Unit, integration, and example verification tests.
- **`examples/`**: Canonical code samples demonstrating features.
- **`vscode-extension/`**: Syntax highlighting and snippet bundle for Visual Studio Code.

---

## 💡 How to Add New Syntax

1. Add parsing/transpilation rules to `SaidLangTranspiler.transpile_line()` in `saidlang/transpiler.py`.
2. If runtime helpers are required, implement them in `saidlang/runtime.py`.
3. Add comprehensive test cases in `tests/test_transpiler.py` or `tests/test_pure_english.py`.
4. Update `SYNTAX_GUIDE.md` and `docs/SPECIFICATION.md`.
5. Update syntax highlighting in `vscode-extension/syntaxes/saidlang.tmLanguage.json` if new keywords are introduced.

---

## 🚀 Pull Request Guidelines

1. Create a feature branch (`git checkout -b feature/natural-loops`).
2. Follow clean code and PEP 8 conventions.
3. Write test cases for all new syntax and edge cases.
4. Ensure all tests pass.
5. Submit a Pull Request describing your changes.
