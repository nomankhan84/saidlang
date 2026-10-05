# SaidLang Formal Specification

## 1. Output & Console
| SaidLang Syntax | Target Python |
| :--- | :--- |
| `show "Hello World"` | `show("Hello World")` |
| `say "Hello"` | `show("Hello")` |
| `say @name` | `show(name)` |
| `say my score is @score` | `show(f"my score is {score}")` |

## 2. Variables & Assignment
| SaidLang Syntax | Target Python |
| :--- | :--- |
| `save name as noman as string` | `name = "noman"` |
| `save age as 25 as integer` | `age = int(25)` |
| `set score to 100` | `score = 100` |
| `let x be 42` | `x = 42` |
| `make ready = true` | `ready = True` |
| `increase count by 1` | `count += 1` |
| `decrease lives by 1` | `lives -= 1` |

## 3. Comparison Operators
| SaidLang Phrase | Operator |
| :--- | :--- |
| `is equal to`, `is the same as` | `==` |
| `is not equal to`, `is different from` | `!=` |
| `is greater than`, `is bigger than`, `is more than` | `>` |
| `is less than`, `is smaller than` | `<` |
| `is at least`, `is greater than or equal to` | `>=` |
| `is at most`, `is less than or equal to` | `<=` |

## 4. Control Flow
| SaidLang Syntax | Target Python |
| :--- | :--- |
| `if condition:` | `if condition:` |
| `otherwise if condition:` | `elif condition:` |
| `otherwise:` | `else:` |
| `if <cond> then say <A> else say <B>` | `if <cond>:\n    show(<A>)\nelse:\n    show(<B>)` |

## 5. Loops
| SaidLang Syntax | Target Python |
| :--- | :--- |
| `repeat 5 times:` | `for _ in range(5):` |
| `repeat 5 times with i:` | `for i in range(5):` |
| `count from 1 to 10 as num:` | `for num in range(1, (10) + 1):` |
| `for each item in basket:` | `for item in basket:` |
| `while condition:` | `while condition:` |
| `repeat <message> <N> times` | `for _ in range(N):\n    show("<message>")` |

## 6. Functions & Procedures
| SaidLang Syntax | Target Python |
| :--- | :--- |
| `to greet with name:` | `def greet(name):` |
| `give back result` | `return result` |
