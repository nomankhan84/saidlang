# SaidLang 🚀
<p align="center">
  <img src="./assets/logo.png" alt="SaidLang Logo" width="160" />
</p>

<p align="center">
  <b>SaidLang</b> is a pure conversational, ultra human-friendly programming language transpiled into Python.<br/>
  Write code that reads like everyday plain English — <b>no mandatory quotes, no semicolons, no colons required</b>.
</p>

<p align="center">
  <a href="#-quick-tour">Quick Tour</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-cli-usage">CLI Usage</a> •
  <a href="SYNTAX_GUIDE.md">Full Syntax Manual</a> •
  <a href="#-license">License</a>
</p>

---

## ✨ Why SaidLang?

- **💬 Conversational English**: Write `say my name is @name and I am @age years old` without string concatenations or quotation marks.
- **🗂️ Rich Typing**: Full support for `string`, `integer`, `float`, `boolean`, `list`, `dict`, `tuple`, `set`.
- **🧮 Natural Math**: Plain-English calculations (`calculate 15 percent of 500 into discount`, `find square root of 144 into root`).
- **🔤 Text Utilities**: Built-in string actions (`change text to uppercase`, `trim spaces`, `count words`, `replace`).
- **🔁 Conversational Loops**: `repeat i have a boyfriend 3 times`.
- **💻 Global CLI & REPL**: Run `.said` scripts anywhere from your terminal (`cmd.exe`, PowerShell, Bash).
- **🎨 Custom IDE Syntax Theme**: Official VS Code / Antigravity extension with custom syntax highlighting and file icons.

---

## ⚡ Quick Tour

```saidlang
// 1. Storing Variables
save name as Noman as string
save age as 21 as integer
save hourly_rate as 45.50 as float
save is_available as yes as boolean

// 2. Printing & Direct @variable Interpolation
say my name is @name and I am @age years old

// 3. Conversational Calculations
calculate 15 percent of 500 into discount_price
say 15 percent of 500 is: @discount_price

find square root of 144 into root_val
say Square root of 144 is: @root_val

// 4. Conversational Conditionals
save rohan's age as 15 as integer and mohan's age as 16 as integer

if rohan's age is bigger than mohan's age then say rohan is bigger else say mohan is bigger

// 5. Conversational Loops
repeat i have a boyfriend 3 times

// 6. User Inputs
ask enter your lucky number and save as lucky_num as integer
say Your lucky number is @lucky_num!
```

---

## 📦 Installation

### 1. Install SaidLang globally via Python
```bash
git clone https://github.com/nomankhan84/saidlang.git
cd saidlang
pip install -e .
```

### 2. Install IDE Syntax Highlighting
```bash
python install_extension.py
```

---

## 🚀 CLI Usage

```bash
# Run any script:
said examples/pure_english.said
said examples/math_and_strings.said

# Launch the interactive live REPL console:
said repl

# Preview transpiled Python code:
said preview examples/pure_english.said

# Compile .said file to standalone .py:
said build examples/pure_english.said -o output.py
```

---

## 📖 Comprehensive Documentation

For the full detailed syntax reference, check out:
👉 **[Official SaidLang Syntax Manual (SYNTAX_GUIDE.md)](SYNTAX_GUIDE.md)**

---

## 👨‍💻 Author

Developed by **Noman Khan**  
- **GitHub**: [@nomankhan84](https://github.com/nomankhan84)
- **Portfolio**: [Noman Khan Portfolio](index.html)
