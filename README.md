# SaidLang 🚀
<p align="center">
  <img src="./assets/logo.png" alt="SaidLang Logo" width="160" />
</p>

> An ultra human-friendly, plain-English programming language powered by Python.

**SaidLang** is designed so anyone can read and write code as easily as writing simple English sentences. It maps friendly human phrases into clean Python code and runs them instantly.

---

## 🌟 Full Syntax Reference Table

| SaidLang (Ultra-Friendly) | Python Transpilation | Description |
|---|---|---|
| `show "Hello!"` / `say "Hello!"` | `show("Hello!")` | Print text / values |
| `set score to 100` | `score = 100` | Assign variable |
| `let name be "Ali"` | `name = "Ali"` | Assign variable |
| `increase score by 10` | `score += 10` | Increment variable |
| `decrease lives by 1` | `lives -= 1` | Decrement variable |
| `ask "Your name: " into name` | `name = ask("Your name: ")` | Read string input |
| `ask number "Age: " into age` | `age = ask_number("Age: ")` | Read numeric input |
| `if age is greater than 18:` | `if age > 18:` | Conditional check |
| `otherwise if score is equal to 100:` | `elif score == 100:` | Else-if check |
| `otherwise:` | `else:` | Else block |
| `unless score is 0:` | `if not (score == 0):` | Negative condition |
| `repeat 5 times:` | `for _ in range(5):` | Repeat loop |
| `count from 1 to 10 as i:` | `for i in range(1, 11):` | Counting range loop |
| `for each item in basket:` | `for item in basket:` | Loop over items |
| `repeat while count < 10:` | `while count < 10:` | While loop |
| `create list fruits` | `fruits = []` | Create empty list |
| `add "Apple" to fruits` | `fruits.append("Apple")` | Add item to list |
| `remove "Apple" from fruits` | `fruits.remove("Apple")` | Remove item |
| `pick random from fruits into pick` | `pick = pick_random(fruits)` | Pick random element |
| `random number between 1 and 10 into n` | `n = random_number(1, 10)` | Random integer |
| `write "content" into file "a.txt"` | `write_file("a.txt", "content")` | Write file |
| `read file "a.txt" into text` | `text = read_file("a.txt")` | Read file |
| `append "line" to file "a.txt"` | `append_file("a.txt", "line")` | Append to file |
| `fetch json "url" into data` | `data = fetch_json("url")` | Fetch JSON API |
| `split text by "," into parts` | `parts = text.split(",")` | Split string |
| `attempt:` ... `on error as err:` | `try:` ... `except Exception as err:` | Safe error handling |
| `to greet with name:` | `def greet(name):` | Define action / function |
| `give back result` | `return result` | Return statement |
| `wait 2 seconds` | `wait(2)` | Sleep / pause execution |

---

## 📦 Install as a Global CLI SDK

To use the `said` command from anywhere in your terminal:

```bash
pip install -e .
```

Now you can run any file simply with:
```bash
said examples/hello.said
said preview examples/hello.said
said repl
```

---

## 🐍 Import `.said` Scripts in Normal Python

You can directly import `.said` files inside any Python program:

```python
import saidlang.hook
import examples.functions_and_math  # Loads and runs functions_and_math.said!
```

---

## 🚀 Running Examples

```bash
# Run Hello World
python said.py run examples/hello.said

# Run Loops & Lists
python said.py run examples/loops_and_lists.said

# Run Functions & Math
python said.py run examples/functions_and_math.said

# Run File I/O & Random
python said.py run examples/files_and_web.said
```

