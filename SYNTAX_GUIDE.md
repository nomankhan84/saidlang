# 📘 SaidLang - The Complete Official Documentation & Syntax Reference

<p align="center">
  <img src="./assets/logo.png" alt="SaidLang Logo" width="160" />
</p>

<p align="center">
  <b>SaidLang</b> is a pure conversational, ultra human-friendly programming language transpiled directly into Python.<br/>
  Write code that reads and writes like everyday plain English — <b>no mandatory quotes, no semicolons, no colons required</b>.
</p>

---

## 📑 Table of Contents
1. [Installation & Setup](#1-installation--setup)
2. [CLI Commands](#2-cli-commands)
3. [Variables & Data Types](#3-variables--data-types)
4. [User Inputs](#4-user-inputs)
5. [Printing & String Interpolation](#5-printing--string-interpolation)
6. [Conversational Math & Calculations](#6-conversational-math--calculations)
7. [String & Text Manipulation](#7-string--text-manipulation)
8. [Conditionals & Logic](#8-conditionals--logic)
9. [Loops & Iteration](#9-loops--iteration)
10. [Functions & Actions](#10-functions--actions)
11. [File & Web Operations](#11-file--web-operations)
12. [Error Handling](#12-error-handling)
13. [Python Import Integration](#13-python-import-integration)

---

## 1. Installation & Setup

### Install SaidLang CLI globally
In your project directory:
```bash
pip install -e .
```
This registers the global `said` command in your terminal (`cmd.exe`, PowerShell, Bash, Git Bash).

### Install the VS Code / Antigravity IDE Extension
Run the automated installer:
```bash
python install_extension.py
```
*(Or install the `.vsix` package: `antigravity-ide.cmd --install-extension vscode-extension/saidlang-0.1.0.vsix`)*

---

## 2. CLI Commands

| Command | Description | Example |
|---|---|---|
| `said <file.said>` | Run a SaidLang script | `said main.said` |
| `said repl` / `said` | Open the interactive live console | `said repl` |
| `said preview <file.said>` | Preview generated Python code | `said preview script.said` |
| `said build <file.said> -o <out.py>` | Compile `.said` file to `.py` | `said build app.said -o app.py` |

---

## 3. Variables & Data Types

SaidLang supports all native Python data types declared in plain English sentences.

### Single Variable Declarations (`save <name> as <value> as <type>`)
```saidlang
save user_name as Noman as string
save age as 21 as integer
save price as 49.99 as float
save is_active as yes as boolean
save skills as ["Python", "JavaScript", "PHP"] as list
save profile as {"role": "Engineer", "level": "Senior"} as dictionary
save coordinates as (10, 20) as tuple
save unique_ids as {101, 102, 103} as set
```

### Multiple Declarations in One Sentence
You can chain multiple assignments together using `and`:
```saidlang
save rohan's age as 15 as integer and mohan's age as 16 as integer and role as Admin as string
```

### Supported Data Type Keywords:
- **String / Text**: `string`, `text`, `str`
- **Integer**: `integer`, `int`
- **Decimal / Float**: `float`, `decimal`, `number`
- **Boolean**: `boolean`, `bool` (`true`/`false` or `yes`/`no`)
- **List / Array**: `list`, `array`
- **Dictionary / Object**: `dictionary`, `dict`, `object`
- **Tuple**: `tuple`
- **Set**: `set`

---

## 4. User Inputs

Prompt the user for input with automatic type-casting:

```saidlang
// String Input
ask what is your name and save as username as string

// Integer / Number Input
ask enter your age and save as userage as integer

// Float / Decimal Input
ask enter your hourly rate and save as rate as float

// Boolean (Yes/No) Input
ask are you currently working and save as is_employed as boolean
```

---

## 5. Printing & String Interpolation

You can output text and reference variables directly with `@variable_name` without quotes or string concatenation (`+`):

```saidlang
save name as Noman as string
save age as 21 as integer

// Interpolate variables directly in plain text:
say my name is @name and my age is @age

// Output single variable value:
say @name

// Output plain phrases:
say Hello World!
say welcome to SaidLang
```

---

## 6. Conversational Math & Calculations

### Percentages & Expressions
```saidlang
calculate 15 percent of 500 into discount
calculate 10 plus 20 multiplied by 3 into total
```

### Basic Arithmetic Triggers
```saidlang
add 100 and 50 into sum_total          // sum_total = 100 + 50
subtract 30 from 100 into diff_total   // diff_total = 100 - 30
multiply 8 by 9 into product_total     // product_total = 8 * 9
divide 100 by 4 into div_total         // div_total = 100 / 4
```

### Advanced Math
```saidlang
find square root of 144 into root_val            // root_val = 12
find power of 2 to 8 into power_val              // power_val = 256
round 49.8765 to 2 decimals into rounded_val    // rounded_val = 49.88
round 49.8765 into whole_val                    // whole_val = 50
```

### Statistical Analysis
```saidlang
save scores as [85, 92, 78, 96, 88] as list

find highest in @scores into top_score           // top_score = 96
find lowest in @scores into min_score            // min_score = 78
find average of @scores into avg_score           // avg_score = 87.8
```

---

## 7. String & Text Manipulation

### Case & Whitespace Transformations
```saidlang
save raw_input as "  Hello SaidLang World  " as string

trim spaces from @raw_input into clean_text       // "Hello SaidLang World"
change @clean_text to uppercase into upper_text   // "HELLO SAIDLANG WORLD"
change @clean_text to lowercase into lower_text   // "hello saidlang world"
```

### Find, Replace & Metrics
```saidlang
count characters in @clean_text into char_count
count words in @clean_text into word_count
replace "World" with "Universe" in @clean_text into replaced_text
```

### Substring & Content Checks
```saidlang
check if @clean_text contains "SaidLang" then say Found keyword! else say Not found
check if @clean_text starts with "Hello" then say Starts with Hello! else say Does not start with Hello
```

---

## 8. Conditionals & Logic

### Inline One-Line Conditionals (Pure English)
```saidlang
save rohan's age as 15 as integer and mohan's age as 16 as integer

if rohan's age is bigger than mohan's age then say rohan is bigger else say mohan is bigger
```

### Multi-Line Structured Conditions
```saidlang
if age is greater than or equal to 18:
    say Welcome, adult user!
otherwise if age is greater than 13:
    say Welcome, teenager!
otherwise:
    say Welcome, kid!
```

### Inverse Condition (`unless`)
```saidlang
unless score is 0:
    say Game is still active!
```

### Comparison Operator Keywords:
| SaidLang Phrase | Python Operator |
|---|---|
| `is bigger than` / `is greater than` | `>` |
| `is smaller than` / `is less than` | `<` |
| `is bigger than or equal to` / `is greater than or equal to` | `>=` |
| `is smaller than or equal to` / `is less than or equal to` | `<=` |
| `is equal to` / `is same as` / `is exactly` | `==` |
| `is not equal to` / `is different from` / `is not same as` | `!=` |
| `and` | `and` |
| `or` | `or` |
| `not` | `not` |

---

## 9. Loops & Iteration

### Pure Conversational Repeat
```saidlang
repeat i have a boyfriend 3 times
repeat say hello @name 5 times
```

### Structured Repeat Blocks
```saidlang
repeat 3 times:
    say Repeating block!

repeat 5 times with i:
    say Index is @i
```

### Counting Range Loops
```saidlang
count from 1 to 5 as n:
    say Step: @n

// With custom step:
count from 0 to 20 step 5 as n:
    say Step by 5: @n
```

### For Each (Lists & Collections)
```saidlang
save fruits as ["Apple", "Mango", "Banana"] as list

for each fruit in @fruits:
    say I love eating @fruit
```

### While Loops
```saidlang
save count as 1 as integer
repeat while @count <= 5:
    say Count: @count
    increase count by 1
```

---

## 10. Functions & Actions

Define reusable functions using natural syntax:

```saidlang
to calculate_total with price and tax_rate:
    calculate price plus (price multiplied by tax_rate) into total
    give back total

to greet with name:
    say Welcome back, @name!

// Calling actions:
greet("Noman")
set final_bill to calculate_total(100, 0.18)
say Total bill: @final_bill
```

---

## 11. File & Web Operations

### File Operations
```saidlang
// Writing to a file
write "SaidLang wrote this message!" into file "output.txt"

// Reading from a file
read file "output.txt" into saved_data
say Read data: @saved_data

// Appending to a file
append "\nAppended line" to file "output.txt"
```

### Web & API Fetching
```saidlang
// Fetch JSON directly:
fetch json "https://api.github.com/users/nomankhan84" into user_data
say GitHub Bio: @user_data["bio"]

// Fetch raw URL content:
fetch url "https://example.com" into webpage_html
```

---

## 12. Error Handling

Safely catch and recover from errors:

```saidlang
attempt:
    calculate 100 divided by 0 into bad_math
on error as err:
    say Handled error gracefully: @err
```

---

## 13. Python Import Integration

You can import any `.said` file directly into a Python application using the built-in import hook:

```python
import saidlang.hook
import my_script  # Automatically transpiles and runs my_script.said!
```

---

<p align="center">
  <b>Built with ❤️ by Noman Khan</b>
</p>
