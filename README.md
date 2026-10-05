# SaidLang 🚀

<p align="center">
  <img src="./assets/logo.png" alt="SaidLang Logo" width="160" />
</p>

<p align="center">
  <b>A conversational, human-first programming language transpiled directly into Python.</b><br/>
  Write clean, expressive programs using plain English phrasing with zero syntax clutter.
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python 3.8+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></a>
  <a href="https://github.com/nomankhan84/saidlang/issues"><img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg" alt="Contributions Welcome"></a>
  <a href="SYNTAX_GUIDE.md"><img src="https://img.shields.io/badge/Docs-Syntax%20Guide-orange.svg" alt="Documentation"></a>
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Installation](#-installation)
- [CLI Reference](#-cli-reference)
- [Documentation & Syntax Guide](#-documentation--syntax-guide)
- [Project Architecture](#-project-architecture)
- [Development & Testing](#-development--testing)
- [Contributing](#-contributing)
- [Repository Structure](#-repository-structure)
- [License](#-license)

---

## 🌟 Overview

**SaidLang** bridges the gap between human thought and executable code. Designed with a conversational syntax grammar, SaidLang transpiles natural, declarative English sentences directly into high-performance, idiomatic Python code.

It eliminates common syntax friction—such as mandatory quotation marks, trailing semicolons, and strict symbol delimiters—while retaining full compatibility with Python's runtime, data structures, and ecosystem.

---

## ⚡ Key Features

- **🗣️ Natural English Grammar**: Write expressive logic, declarations, and string interpolation without quotes or boilerplate symbols.
- **📦 Full Data Type System**: Native support for strings, integers, floats, booleans, lists, dictionaries, tuples, and sets.
- **🧮 Conversational Computations**: Built-in keywords for percentages, powers, square roots, rounding, and arithmetic expressions.
- **🔤 Built-in Text Operations**: First-class support for text transformation, trimming, word counting, and substring operations.
- **🔄 Declarative Control Flow**: Expressive conditionals, loops, range iterators, and function definitions.
- **🛠️ Cross-Platform CLI & REPL**: Interactive REPL console, transpilation preview, and build tools available globally in your terminal.
- **🎨 IDE Syntax Highlighting**: Official extension support for VS Code and Antigravity IDE with dedicated token coloring and file icons.

---

## 📦 Installation

### Prerequisites
- **Python 3.8** or higher
- **Git**

### 1. Install SaidLang CLI
Clone the repository and install it in editable mode:

```bash
git clone https://github.com/nomankhan84/saidlang.git
cd saidlang
pip install -e .
```

Verify that the CLI is installed and available in your path:

```bash
said --help
```

### 2. Install IDE Extension (VS Code / Antigravity IDE)
Install the syntax highlighting package automatically:

```bash
python install_extension.py
```

*Alternatively, manually install the packaged extension:*
```bash
code --install-extension vscode-extension/saidlang-0.1.0.vsix
```

---

## 💻 CLI Reference

SaidLang includes a unified command-line interface:

| Command | Action | Example |
| :--- | :--- | :--- |
| `said <file.said>` | Execute a SaidLang program directly | `said examples/hello.said` |
| `said repl` *(or `said`)* | Launch the interactive live REPL shell | `said repl` |
| `said preview <file.said>` | Transpile and view the generated Python code | `said preview script.said` |
| `said build <file.said> -o <out.py>` | Compile a `.said` source file into a standalone `.py` script | `said build app.said -o app.py` |

---

## 📖 Documentation & Syntax Guide

All language specifications, token rules, keyword references, and syntax examples are documented in the official guide:

👉 **[Read the Full SaidLang Syntax Guide (SYNTAX_GUIDE.md)](SYNTAX_GUIDE.md)**

You can also explore runnable program files in the **[`examples/`](examples/)** directory:
- [`examples/hello.said`](examples/hello.said) — Basic outputs and variable assignment
- [`examples/pure_english.said`](examples/pure_english.said) — Natural English statements and queries
- [`examples/math_and_strings.said`](examples/math_and_strings.said) — Arithmetic calculations and text operations
- [`examples/loops_and_lists.said`](examples/loops_and_lists.said) — Iteration, arrays, and collections
- [`examples/functions_and_math.said`](examples/functions_and_math.said) — Function definitions and logic
- [`examples/files_and_web.said`](examples/files_and_web.said) — File I/O and HTTP operations

---

## 🏗️ Project Architecture

SaidLang operates via a multi-stage transpilation pipeline:

```
┌─────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐      ┌─────────────────┐
│   .said Source  │ ───► │  SaidLang Transpiler    │ ───► │    Standard Python      │ ───► │  Python Runtime │
│   (Plain Text)  │      │  (Pattern & Grammar AST)│      │    Generated Code       │      │   (Execution)   │
└─────────────────┘      └─────────────────────────┘      └─────────────────────────┘      └─────────────────┘
```

1. **Parser & Normalizer**: Cleans indentation, identifies conversational patterns, and maps keywords.
2. **Grammar Transpiler**: Converts declarative English statements into corresponding Python AST structures and expressions.
3. **Runtime & Execution**: Executes the resulting Python code or emits standalone Python artifacts.

---

## 🧪 Development & Testing

Run the test suite using Python's built-in `unittest` runner:

```bash
python -m unittest test_saidlang.py
```

To run with verbose output:

```bash
python -m unittest test_saidlang.py -v
```

---

## 🤝 Contributing

We welcome contributions from the open-source community! Whether you are fixing bugs, proposing new conversational keywords, improving documentation, or adding tests, your help is appreciated.

### How to Contribute

1. **Fork the Repository**
   Click the **Fork** button at the top right of the GitHub repository.

2. **Clone your Fork**
   ```bash
   git clone https://github.com/<your-username>/saidlang.git
   cd saidlang
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Set Up the Environment**
   ```bash
   pip install -e ".[dev]"
   ```

5. **Implement Changes & Add Tests**
   - Follow clean Python formatting conventions (PEP 8).
   - Add new test cases in `tests/` for any new syntax features or bug fixes.
   - Run the test suite:
     ```bash
     pytest tests/ -v
     ```

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "feat: add conversational keyword for XYZ"
   git push origin feature/your-feature-name
   ```

7. **Submit a Pull Request**
   Open a Pull Request on the main repository describing your changes and referencing any related issues.

---

## 📂 Repository Structure

```plaintext
saidlang/
├── .github/                       # GitHub Actions CI/CD and issue templates
│   ├── workflows/
│   │   ├── ci.yml                 # Cross-platform multi-Python CI matrix
│   │   └── release.yml            # Automated PyPI & VS Code release pipeline
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                          # In-depth architectural & syntax docs
│   ├── ARCHITECTURE.md            # Transpiler engine pipeline details
│   └── SPECIFICATION.md           # Formal syntax and keyword dictionary
├── examples/                      # Canonical, progressive tutorial programs
│   ├── 01_hello_world.said
│   ├── 02_variables_and_math.said
│   ├── 03_control_flow.said
│   ├── 04_loops_and_lists.said
│   ├── 05_functions.said
│   ├── 06_file_and_web.said
│   └── 07_natural_english.said
├── saidlang/                      # Core engine package
│   ├── __init__.py                # Package exports & version
│   ├── cli.py                     # CLI entrypoint (said run, build, repl)
│   ├── hook.py                    # Native Python import hook (.said modules)
│   ├── runtime.py                 # Standard library runtime helpers
│   └── transpiler.py              # Parsing & code generation engine
├── tests/                         # Comprehensive test suite
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_examples.py
│   ├── test_pure_english.py
│   ├── test_runtime.py
│   └── test_transpiler.py
├── vscode-extension/              # Editor tooling & syntax highlighting
├── .gitignore                     # Production Python & editor ignore rules
├── CHANGELOG.md                   # Version tracking & release notes
├── CODE_OF_CONDUCT.md             # Contributor Covenant standard
├── CONTRIBUTING.md                # Development, test running, & PR guidelines
├── pyproject.toml                 # PEP 517/621 packaging metadata
├── README.md                      # Project documentation
├── SECURITY.md                    # Security vulnerability policy
└── SYNTAX_GUIDE.md                # Language syntax reference
```

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).

---

## 👤 Maintainer

**Noman Khan**  
- GitHub: [@nomankhan84](https://github.com/nomankhan84)
