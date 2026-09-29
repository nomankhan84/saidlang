# SaidLang 🚀
> An ultra human-friendly, plain-English programming language powered by Python.

**SaidLang** is designed so anyone can read and write code as easily as writing simple English sentences. It maps friendly human phrases into clean Python code and runs them instantly.

---

## 🌟 Syntax Mapping Reference

| SaidLang (Human-Friendly) | Python Equivalent | Purpose |
|---|---|---|
| `show "Hello!"` / `say "Hello!"` | `print("Hello!")` | Output text / values |
| `set score to 100` | `score = 100` | Assign variable |
| `let name be "Ali"` | `name = "Ali"` | Assign variable |
| `increase score by 10` | `score += 10` | Increment variable |
| `decrease lives by 1` | `lives -= 1` | Decrement variable |
| `ask "Your name: " into name` | `name = input("Your name: ")` | Read string input |
| `ask number "Age: " into age` | `age = ask_number("Age: ")` | Read numeric input |
| `if age is greater than 18:` | `if age > 18:` | Condition |
| `otherwise if score is equal to 100:` | `elif score == 100:` | Else-if condition |
| `otherwise:` | `else:` | Else condition |
| `repeat 5 times:` | `for _ in range(5):` | Simple repeat loop |
| `count from 1 to 10 as i:` | `for i in range(1, 11):` | Counting loop |
| `for each item in basket:` | `for item in basket:` | Iterate list |
| `repeat while count < 10:` | `while count < 10:` | While loop |
| `to greet with name:` | `def greet(name):` | Define a function |
| `give back result` | `return result` | Return from function |
| `create list fruits` | `fruits = []` | Create new list |
| `add "Apple" to fruits` | `fruits.append("Apple")` | Add item to list |
| `remove "Apple" from fruits` | `fruits.remove("Apple")` | Remove item from list |

---

## 🚀 How to Run and Use

### 1. Run a SaidLang script directly
```bash
python said.py run examples/hello.said
```

### 2. Preview the transpiled Python code
```bash
python said.py preview examples/hello.said
```

### 3. Build/Compile to a `.py` file
```bash
python said.py build examples/hello.said -o output.py
```

### 4. Interactive REPL (Live SaidLang Shell)
```bash
python said.py repl
```

---

## 📝 Example SaidLang Program

```saidlang
// Simple greeting and logic
say "Welcome to SaidLang!"

set score to 10
increase score by 5

if score is greater than 10:
    show "You scored high!"
otherwise:
    show "Keep trying!"

// Loops are easy!
count from 1 to 3 as round:
    show "Round: " + str(round)
```
