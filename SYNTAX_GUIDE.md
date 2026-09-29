# 📘 SaidLang - Complete Conversational Language Manual

SaidLang is a **pure conversational programming language** designed to run anywhere with no mandatory quotes, semicolons, or colons required.

---

## 🗂️ 1. Variables & All Data Types

### Standard Variable Declarations
```saidlang
save name as Noman as string
save age as 21 as integer
save price as 49.99 as float
save is_active as yes as boolean
save skills as ["Python", "JavaScript", "PHP"] as list
save profile as {"role": "Engineer", "level": "Senior"} as dictionary
save coordinates as (10, 20) as tuple
save unique_ids as {101, 102, 103} as set
```

### Multiple Declarations in One Sentence
```saidlang
save rohan's age as 15 as integer and mohan's age as 16 as integer and role as Admin as string
```

---

## 📥 2. User Input Commands

```saidlang
// String / Text Input
ask what is your name and save as user_name as string

// Integer / Number Input
ask enter your age and save as user_age as integer

// Decimal / Float Input
ask enter your hourly rate and save as rate as float

// Boolean (Yes/No) Input
ask are you currently working and save as is_employed as boolean
```

---

## 🧮 3. Conversational Math & Arithmetic Operations

### Percentage & Expressions
```saidlang
calculate 15 percent of 500 into discount
calculate 10 plus 20 multiplied by 3 into total
```

### Basic Arithmetic Triggers
```saidlang
add 100 and 50 into sum_total
subtract 30 from 100 into diff_total
multiply 8 by 9 into product_total
divide 100 by 4 into div_total
```

### Advanced Math
```saidlang
find square root of 144 into root_val
find power of 2 to 8 into power_val
round 49.8765 to 2 decimals into rounded_val
round 49.8765 into whole_val
```

### Statistical Analysis
```saidlang
save scores as [85, 92, 78, 96, 88] as list
find highest in @scores into top_score
find lowest in @scores into min_score
find average of @scores into avg_score
```

---

## 🔤 4. Conversational String & Text Operations

### Text Transformations
```saidlang
save raw_input as "  Hello SaidLang World  " as string

trim spaces from @raw_input into clean_text
change @clean_text to uppercase into upper_text
change @clean_text to lowercase into lower_text
replace "World" with "Universe" in @clean_text into replaced_text
```

### Text Analysis & Metrics
```saidlang
count characters in @clean_text into total_characters
count words in @clean_text into total_words
```

### Substring & Content Checks
```saidlang
check if @clean_text contains "SaidLang" then say Found keyword! else say Not found
check if @clean_text starts with "Hello" then say Starts with Hello! else say Does not start with Hello
```

---

## 💬 5. Output & Printing

```saidlang
// Direct @variable interpolation (no quotes needed):
say my name is @name and I am @age years old

// Direct values:
say Hello World!
say 42
say @scores
```

---

## 🔁 6. Loops & Conditionals

### Repeat Loops
```saidlang
repeat i have a boyfriend 3 times
repeat say hello @name 5 times
```

### Conversational If / Else
```saidlang
if rohan's age is bigger than mohan's age then say rohan is bigger else say mohan is bigger
```

---

## 🚀 Running Any Script

```bash
# In CMD / PowerShell / Terminal:
said script.said

# Preview generated Python code:
said preview script.said

# Interactive REPL:
said repl
```
