"""
SaidLang Transpiler - Pure Natural Conversational English Engine
"""

import re

# Operators dictionary sorted by length descending
OPERATOR_MAP = [
    (r"\bis greater than or equal to\b", ">="),
    (r"\bis less than or equal to\b", "<="),
    (r"\bis bigger than or equal to\b", ">="),
    (r"\bis smaller than or equal to\b", "<="),
    (r"\bis bigger than\b", ">"),
    (r"\bis smaller than\b", "<"),
    (r"\bis greater than\b", ">"),
    (r"\bis less than\b", "<"),
    (r"\bis not equal to\b", "!="),
    (r"\bis not same as\b", "!="),
    (r"\bis different from\b", "!="),
    (r"\bis equal to\b", "=="),
    (r"\bis same as\b", "=="),
    (r"\bis exactly\b", "=="),
    (r"\bmultiplied by\b", "*"),
    (r"\btimes\b", "*"),
    (r"\bdivided by\b", "/"),
    (r"\bpower of\b", "**"),
    (r"\bplus\b", "+"),
    (r"\bminus\b", "-"),
    (r"\bmodulo\b", "%"),
    (r"\btrue\b", "True"),
    (r"\bfalse\b", "False"),
    (r"\byes\b", "True"),
    (r"\bno\b", "False"),
    (r"\bnothing\b", "None"),
    (r"\bnull\b", "None"),
]

def sanitize_var_name(raw_name):
    """Normalize plain English variable names like `rohan's age` -> `rohan_s_age`."""
    name = raw_name.strip()
    if name.startswith("@"):
        name = name[1:]
    name = re.sub(r"['’]s\b", "_s", name)
    name = re.sub(r"['’]", "", name)
    name = re.sub(r"[^\w]", "_", name)
    name = re.sub(r"_+", "_", name)
    return name.strip("_")

def mask_string_literals(line):
    strings = {}
    counter = 0

    def replace_str(match):
        nonlocal counter
        key = f"__SAID_STR_{counter}__"
        strings[key] = match.group(0)
        counter += 1
        return key

    pattern = r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')'
    masked_line = re.sub(pattern, replace_str, line)
    return masked_line, strings

def unmask_string_literals(line, strings):
    for key, val in strings.items():
        line = line.replace(key, val)
    return line

def clean_expr_tokens(expr):
    """Clean and normalize math/logical expression tokens."""
    expr = expr.strip()
    for pattern, replacement in OPERATOR_MAP:
        expr = re.sub(pattern, replacement, expr, flags=re.IGNORECASE)
    # Convert @var to var
    expr = re.sub(r'@([a-zA-Z_][\w\'’]*)', lambda m: sanitize_var_name(m.group(1)), expr)
    return expr

def parse_natural_say(content):
    """
    Parse content for 'say' / 'show'.
    Examples:
      say @name -> show(name)
      say 42 -> show(42)
      say hello @name, you are @age years old -> show(f"hello {name}, you are {age} years old")
      say "quoted string" -> show("quoted string")
    """
    content = content.strip()
    if not content:
        return "show()"

    # Single @var reference without extra words
    if re.match(r'^@[\w\'’]+$', content):
        var = sanitize_var_name(content)
        return f"show({var})"

    # Numeric constant
    if re.match(r'^-?\d+(?:\.\d+)?$', content):
        return f"show({content})"

    # Already quoted string literal
    if (content.startswith('"') and content.endswith('"')) or (content.startswith("'") and content.endswith("'")):
        return f"show({content})"

    # Format into Python f-string or string
    def replace_var(m):
        v = sanitize_var_name(m.group(1))
        return "{" + v + "}"

    fstring_body = re.sub(r'@([a-zA-Z_][\w\'’]*)', replace_var, content)
    fstring_body = fstring_body.replace('"', '\\"')

    if "{" in fstring_body:
        return f'show(f"{fstring_body}")'
    return f'show("{fstring_body}")'

def parse_save_assignment_chunk(chunk):
    """
    Parses assignment expressions like:
      'name as noman as string'
      'age as 17 as integer'
      'price as 19.99 as float'
      'is_active as true as boolean'
      'scores as [10, 20, 30] as list'
      'profile as {"role": "dev"} as dict'
    """
    chunk = chunk.strip()
    match = re.match(r'^(?:save|store|set)?\s*(.+?)\s+as\s+(.+?)(?:\s+as\s+(string|text|str|integer|int|number|float|decimal|boolean|bool|list|array|dict|dictionary|object|tuple|set))?$', chunk, re.IGNORECASE)
    if match:
        raw_var = match.group(1).strip()
        val = match.group(2).strip()
        cast = (match.group(3) or "").lower()

        var = sanitize_var_name(raw_var)

        # Type casting & normalization
        if cast in ("string", "text", "str"):
            if not (val.startswith('"') or val.startswith("'")):
                val = f'"{val}"'
        elif cast in ("integer", "int"):
            val = f"int({clean_expr_tokens(val)})"
        elif cast in ("float", "decimal", "number"):
            val = f"float({clean_expr_tokens(val)})"
        elif cast in ("boolean", "bool"):
            if val.lower() in ("true", "yes"):
                val = "True"
            elif val.lower() in ("false", "no"):
                val = "False"
            else:
                val = f"bool({clean_expr_tokens(val)})"
        elif cast in ("list", "array"):
            if not (val.startswith("[") and val.endswith("]")):
                val = f"[{val}]"
        elif cast in ("dict", "dictionary", "object"):
            if not (val.startswith("{") and val.endswith("}")):
                val = f"{{{val}}}"
        elif cast == "tuple":
            if not (val.startswith("(") and val.endswith(")")):
                val = f"({val})"
        elif cast == "set":
            if not (val.startswith("{") and val.endswith("}")):
                val = f"set([{val}])"

        return f"{var} = {val}"
    return None

class SaidLangTranspiler:
    def __init__(self, include_runtime=True):
        self.include_runtime = include_runtime

    def transpile_line(self, raw_line):
        indent = ""
        lstripped = raw_line.lstrip()
        indent_len = len(raw_line) - len(lstripped)
        indent = raw_line[:indent_len]

        line = lstripped.rstrip()

        if not line:
            return ""

        # Comments
        if line.startswith("//"):
            return indent + "#" + line[2:]
        if line.lower().startswith("note:"):
            return indent + "#" + line[5:]
        if line.startswith("#"):
            return indent + line

        # -------------------------------------------------------------
        # 1. Variable Assignments (save ... as ... as type [and ...])
        # -------------------------------------------------------------
        if re.match(r'^(?:save|store)\s+', line, re.IGNORECASE):
            body = re.sub(r'^(?:save|store)\s+', '', line, flags=re.IGNORECASE)
            chunks = re.split(r'\s+and\s+', body)
            py_assignments = []
            for chunk in chunks:
                parsed = parse_save_assignment_chunk(chunk)
                if parsed:
                    py_assignments.append(parsed)
            if py_assignments:
                return "\n".join(f"{indent}{a}" for a in py_assignments)

        # -------------------------------------------------------------
        # 2. User Input Commands (ask ... and save as <var> as <type>)
        # -------------------------------------------------------------
        match = re.match(r'^ask\s+(.+?)\s+and\s+save\s+as\s+(.+?)(?:\s+as\s+(string|text|str|integer|int|number|float|decimal|boolean|bool))?$', line, re.IGNORECASE)
        if match:
            prompt = match.group(1).strip()
            raw_var = match.group(2).strip()
            cast = (match.group(3) or "string").lower()
            var = sanitize_var_name(raw_var)
            if cast in ("integer", "int"):
                return f'{indent}{var} = int(ask_number("{prompt}: "))'
            elif cast in ("float", "decimal", "number"):
                return f'{indent}{var} = float(ask_number("{prompt}: "))'
            elif cast in ("boolean", "bool"):
                return f'{indent}{var} = ask_boolean("{prompt}: ")'
            return f'{indent}{var} = ask("{prompt}: ")'

        # -------------------------------------------------------------
        # 3. Math & Calculations Trigger Rules:
        # -------------------------------------------------------------
        # calculate <percent> percent of <total> into <var>
        match = re.match(r'^calculate\s+(.+?)\s+percent\s+of\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            pct = clean_expr_tokens(match.group(1).strip())
            total = clean_expr_tokens(match.group(2).strip())
            var = sanitize_var_name(match.group(3))
            return f"{indent}{var} = calculate_percent({pct}, {total})"

        # calculate <math expression> into <var>
        match = re.match(r'^calculate\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            expr = clean_expr_tokens(match.group(1).strip())
            var = sanitize_var_name(match.group(2))
            return f"{indent}{var} = {expr}"

        # add <a> and <b> into <var>
        match = re.match(r'^add\s+(.+?)\s+and\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            a = clean_expr_tokens(match.group(1).strip())
            b = clean_expr_tokens(match.group(2).strip())
            var = sanitize_var_name(match.group(3))
            return f"{indent}{var} = ({a}) + ({b})"

        # subtract <a> from <b> into <var>
        match = re.match(r'^subtract\s+(.+?)\s+from\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            a = clean_expr_tokens(match.group(1).strip())
            b = clean_expr_tokens(match.group(2).strip())
            var = sanitize_var_name(match.group(3))
            return f"{indent}{var} = ({b}) - ({a})"

        # multiply <a> by <b> into <var>
        match = re.match(r'^multiply\s+(.+?)\s+by\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            a = clean_expr_tokens(match.group(1).strip())
            b = clean_expr_tokens(match.group(2).strip())
            var = sanitize_var_name(match.group(3))
            return f"{indent}{var} = ({a}) * ({b})"

        # divide <a> by <b> into <var>
        match = re.match(r'^divide\s+(.+?)\s+by\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            a = clean_expr_tokens(match.group(1).strip())
            b = clean_expr_tokens(match.group(2).strip())
            var = sanitize_var_name(match.group(3))
            return f"{indent}{var} = ({a}) / ({b})"

        # find square root of <val> into <var>
        match = re.match(r'^find\s+square\s+root\s+of\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            val = clean_expr_tokens(match.group(1).strip())
            var = sanitize_var_name(match.group(2))
            return f"{indent}{var} = square_root({val})"

        # find power of <base> to <exp> into <var>
        match = re.match(r'^find\s+power\s+of\s+(.+?)\s+to\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            base = clean_expr_tokens(match.group(1).strip())
            exp = clean_expr_tokens(match.group(2).strip())
            var = sanitize_var_name(match.group(3))
            return f"{indent}{var} = power_of({base}, {exp})"

        # round <val> to <N> decimals into <var>
        match = re.match(r'^round\s+(.+?)\s+to\s+(\d+)\s+decimals?\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            val = clean_expr_tokens(match.group(1).strip())
            dec = match.group(2).strip()
            var = sanitize_var_name(match.group(3))
            return f"{indent}{var} = round_number({val}, {dec})"

        # round <val> into <var>
        match = re.match(r'^round\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            val = clean_expr_tokens(match.group(1).strip())
            var = sanitize_var_name(match.group(2))
            return f"{indent}{var} = round_number({val})"

        # find highest/max in <col> into <var>
        match = re.match(r'^find\s+(?:highest|max|maximum)\s+(?:number\s+)?in\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            col = clean_expr_tokens(match.group(1).strip())
            var = sanitize_var_name(match.group(2))
            return f"{indent}{var} = find_highest({col})"

        # find lowest/min in <col> into <var>
        match = re.match(r'^find\s+(?:lowest|min|minimum)\s+(?:number\s+)?in\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            col = clean_expr_tokens(match.group(1).strip())
            var = sanitize_var_name(match.group(2))
            return f"{indent}{var} = find_lowest({col})"

        # find average of <col> into <var>
        match = re.match(r'^find\s+average\s+of\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            col = clean_expr_tokens(match.group(1).strip())
            var = sanitize_var_name(match.group(2))
            return f"{indent}{var} = find_average({col})"

        # -------------------------------------------------------------
        # 4. String & Text Trigger Rules:
        # -------------------------------------------------------------
        # change/convert <text> to uppercase into <var>
        match = re.match(r'^(?:change|convert)\s+(.+?)\s+to\s+uppercase\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            text = clean_expr_tokens(match.group(1).strip())
            var = sanitize_var_name(match.group(2))
            return f"{indent}{var} = to_uppercase({text})"

        # change/convert <text> to lowercase into <var>
        match = re.match(r'^(?:change|convert)\s+(.+?)\s+to\s+lowercase\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            text = clean_expr_tokens(match.group(1).strip())
            var = sanitize_var_name(match.group(2))
            return f"{indent}{var} = to_lowercase({text})"

        # trim spaces from <text> into <var>
        match = re.match(r'^trim\s+spaces\s+from\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            text = clean_expr_tokens(match.group(1).strip())
            var = sanitize_var_name(match.group(2))
            return f"{indent}{var} = trim_spaces({text})"

        # count characters in <text> into <var>
        match = re.match(r'^count\s+characters\s+in\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            text = clean_expr_tokens(match.group(1).strip())
            var = sanitize_var_name(match.group(2))
            return f"{indent}{var} = count_characters({text})"

        # count words in <text> into <var>
        match = re.match(r'^count\s+words\s+in\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            text = clean_expr_tokens(match.group(1).strip())
            var = sanitize_var_name(match.group(2))
            return f"{indent}{var} = count_words({text})"

        # replace <old> with <new> in <text> into <var>
        match = re.match(r'^replace\s+(.+?)\s+with\s+(.+?)\s+in\s+(.+?)\s+into\s+(.+)$', line, re.IGNORECASE)
        if match:
            old_val = clean_expr_tokens(match.group(1).strip())
            new_val = clean_expr_tokens(match.group(2).strip())
            text = clean_expr_tokens(match.group(3).strip())
            var = sanitize_var_name(match.group(4))
            return f"{indent}{var} = replace_text({text}, {old_val}, {new_val})"

        # -------------------------------------------------------------
        # 5. Conditionals & Inline Checks:
        # -------------------------------------------------------------
        # check if <text> contains <subtext> then <action> [else <action>]
        match = re.match(r'^check\s+if\s+(.+?)\s+contains\s+(.+?)\s+then\s+(.+?)(?:\s+else\s+(.+))?$', line, re.IGNORECASE)
        if match:
            text = clean_expr_tokens(match.group(1).strip())
            sub = clean_expr_tokens(match.group(2).strip())
            then_act = parse_natural_say(re.sub(r'^(?:say|show)\s+', '', match.group(3).strip(), flags=re.IGNORECASE))
            else_raw = match.group(4)
            if else_raw:
                else_act = parse_natural_say(re.sub(r'^(?:say|show)\s+', '', else_raw.strip(), flags=re.IGNORECASE))
                return f"{indent}if text_contains({text}, {sub}):\n{indent}    {then_act}\n{indent}else:\n{indent}    {else_act}"
            return f"{indent}if text_contains({text}, {sub}):\n{indent}    {then_act}"

        # check if <text> starts with <subtext> then <action> [else <action>]
        match = re.match(r'^check\s+if\s+(.+?)\s+starts\s+with\s+(.+?)\s+then\s+(.+?)(?:\s+else\s+(.+))?$', line, re.IGNORECASE)
        if match:
            text = clean_expr_tokens(match.group(1).strip())
            sub = clean_expr_tokens(match.group(2).strip())
            then_act = parse_natural_say(re.sub(r'^(?:say|show)\s+', '', match.group(3).strip(), flags=re.IGNORECASE))
            else_raw = match.group(4)
            if else_raw:
                else_act = parse_natural_say(re.sub(r'^(?:say|show)\s+', '', else_raw.strip(), flags=re.IGNORECASE))
                return f"{indent}if text_starts_with({text}, {sub}):\n{indent}    {then_act}\n{indent}else:\n{indent}    {else_act}"
            return f"{indent}if text_starts_with({text}, {sub}):\n{indent}    {then_act}"

        # Pure Natural Inline IF-THEN-ELSE
        match = re.match(r'^if\s+(.+?)\s+then\s+(.+?)\s+else\s+(.+)$', line, re.IGNORECASE)
        if match:
            cond_raw = match.group(1).strip()
            then_raw = match.group(2).strip()
            else_raw = match.group(3).strip()

            cond = cond_raw
            for pattern, replacement in OPERATOR_MAP:
                cond = re.sub(pattern, replacement, cond, flags=re.IGNORECASE)

            comp_match = re.split(r'(\s*(?:>=|<=|==|!=|>|<)\s*)', cond)
            if len(comp_match) == 3:
                left = sanitize_var_name(comp_match[0])
                op = comp_match[1].strip()
                right = sanitize_var_name(comp_match[2])
                cond = f"{left} {op} {right}"

            if then_raw.lower().startswith("say ") or then_raw.lower().startswith("show "):
                then_code = parse_natural_say(re.sub(r'^(?:say|show)\s+', '', then_raw, flags=re.IGNORECASE))
            else:
                then_code = parse_natural_say(then_raw)

            if else_raw.lower().startswith("say ") or else_raw.lower().startswith("show "):
                else_code = parse_natural_say(re.sub(r'^(?:say|show)\s+', '', else_raw, flags=re.IGNORECASE))
            else:
                else_code = parse_natural_say(else_raw)

            return f"{indent}if {cond}:\n{indent}    {then_code}\n{indent}else:\n{indent}    {else_code}"

        # -------------------------------------------------------------
        # 6. Natural Inline Repeat:
        # -------------------------------------------------------------
        match = re.match(r'^repeat\s+(.+?)\s+(\d+)\s+times$', line, re.IGNORECASE)
        if match:
            action_text = match.group(1).strip()
            count = match.group(2).strip()

            if action_text.lower().startswith("say ") or action_text.lower().startswith("show "):
                content = re.sub(r'^(?:say|show)\s+', '', action_text, flags=re.IGNORECASE)
                sub_code = parse_natural_say(content)
            else:
                sub_code = parse_natural_say(action_text)

            return f"{indent}for _ in range({count}):\n{indent}    {sub_code}"

        # -------------------------------------------------------------
        # 7. Output Statements:
        # -------------------------------------------------------------
        masked_line, strings = mask_string_literals(line)

        def finalize(code):
            for pattern, replacement in OPERATOR_MAP:
                code = re.sub(pattern, replacement, code, flags=re.IGNORECASE)
            return indent + unmask_string_literals(code, strings)

        match = re.match(r'^(?:say|show|display|print)\s+(.+)$', masked_line, re.IGNORECASE)
        if match:
            raw_arg = unmask_string_literals(match.group(1).strip(), strings)
            return indent + parse_natural_say(raw_arg)

        if re.match(r'^(?:say|show|display|print)\s*$', masked_line, re.IGNORECASE):
            return f"{indent}show()"

        # 8. Collection & File operations:
        # split <text> by <sep> into <var>
        match = re.match(r'^split\s+(.+?)\s+by\s+(.+?)\s+into\s+([a-zA-Z_]\w*)$', masked_line, re.IGNORECASE)
        if match:
            text = clean_expr_tokens(match.group(1).strip())
            sep = clean_expr_tokens(match.group(2).strip())
            var = match.group(3)
            return finalize(f"{var} = {text}.split({sep})")

        # attempt: / on error:
        if re.match(r'^(?:attempt|try):?$', masked_line, re.IGNORECASE):
            return f"{indent}try:"

        match = re.match(r'^(?:on\s+error|catch)\s+as\s+([a-zA-Z_]\w*):?$', masked_line, re.IGNORECASE)
        if match:
            err_var = match.group(1)
            return f"{indent}except Exception as {err_var}:"

        if re.match(r'^(?:on\s+error|catch):?$', masked_line, re.IGNORECASE):
            return f"{indent}except Exception:"

        # Standard set / make / let <var> to <val>
        match = re.match(r'^(?:set|make|let|remember)\s+([a-zA-Z_][\w\'’]*)\s+(?:to|=|be|as)\s+(.+)$', masked_line, re.IGNORECASE)
        if match:
            var_name = sanitize_var_name(match.group(1))
            expr = clean_expr_tokens(match.group(2).strip())
            return finalize(f"{var_name} = {expr}")

        # increase / decrease by
        match = re.match(r'^increase\s+([a-zA-Z_][\w\'’]*)\s+by\s+(.+)$', masked_line, re.IGNORECASE)
        if match:
            var = sanitize_var_name(match.group(1))
            expr = clean_expr_tokens(match.group(2).strip())
            return finalize(f"{var} += {expr}")

        match = re.match(r'^decrease\s+([a-zA-Z_][\w\'’]*)\s+by\s+(.+)$', masked_line, re.IGNORECASE)
        if match:
            var = sanitize_var_name(match.group(1))
            expr = clean_expr_tokens(match.group(2).strip())
            return finalize(f"{var} -= {expr}")

        match = re.match(r'^create\s+(?:empty\s+)?list\s+([a-zA-Z_]\w*)$', masked_line, re.IGNORECASE)
        if match:
            return f"{indent}{match.group(1)} = []"

        match = re.match(r'^create\s+(?:empty\s+)?(?:object|dictionary)\s+([a-zA-Z_]\w*)$', masked_line, re.IGNORECASE)
        if match:
            return f"{indent}{match.group(1)} = {{}}"

        match = re.match(r'^pick\s+random\s+from\s+(.+?)\s+into\s+([a-zA-Z_]\w*)$', masked_line, re.IGNORECASE)
        if match:
            col = clean_expr_tokens(match.group(1).strip())
            var = match.group(2)
            return finalize(f"{var} = pick_random({col})")

        match = re.match(r'^random\s+number\s+between\s+(.+?)\s+and\s+(.+?)\s+into\s+([a-zA-Z_]\w*)$', masked_line, re.IGNORECASE)
        if match:
            min_val = clean_expr_tokens(match.group(1).strip())
            max_val = clean_expr_tokens(match.group(2).strip())
            var = match.group(3)
            return finalize(f"{var} = random_number({min_val}, {max_val})")

        match = re.match(r'^add\s+(.+?)\s+to\s+([a-zA-Z_]\w*)$', masked_line, re.IGNORECASE)
        if match:
            item = clean_expr_tokens(match.group(1).strip())
            target_list = match.group(2)
            return finalize(f"{target_list}.append({item})")

        match = re.match(r'^remove\s+(.+?)\s+from\s+([a-zA-Z_]\w*)$', masked_line, re.IGNORECASE)
        if match:
            item = clean_expr_tokens(match.group(1).strip())
            target_list = match.group(2)
            return finalize(f"{target_list}.remove({item})")

        match = re.match(r'^write\s+(.+?)\s+into(?:\s+file)?\s+(.+)$', masked_line, re.IGNORECASE)
        if match:
            content = clean_expr_tokens(match.group(1).strip())
            filepath = clean_expr_tokens(match.group(2).strip())
            return finalize(f"write_file({filepath}, {content})")

        match = re.match(r'^append\s+(.+?)\s+to(?:\s+file)?\s+(.+)$', masked_line, re.IGNORECASE)
        if match:
            content = clean_expr_tokens(match.group(1).strip())
            filepath = clean_expr_tokens(match.group(2).strip())
            return finalize(f"append_file({filepath}, {content})")

        match = re.match(r'^read(?:\s+file)?\s+(.+?)\s+into\s+([a-zA-Z_]\w*)$', masked_line, re.IGNORECASE)
        if match:
            filepath = clean_expr_tokens(match.group(1).strip())
            var = match.group(2)
            return finalize(f"{var} = read_file({filepath})")

        # -------------------------------------------------------------
        # 9. Structured Control Flow (if/else/loops/functions):
        # -------------------------------------------------------------
        match = re.match(r'^(?:otherwise\s+if|else\s+if|or\s+if)\s+(.+?):?$', masked_line, re.IGNORECASE)
        if match:
            cond = clean_expr_tokens(match.group(1).strip())
            return finalize(f"elif {cond}:")

        if re.match(r'^(?:otherwise|else):?$', masked_line, re.IGNORECASE):
            return f"{indent}else:"

        match = re.match(r'^unless\s+(.+?):?$', masked_line, re.IGNORECASE)
        if match:
            cond = clean_expr_tokens(match.group(1).strip())
            return finalize(f"if not ({cond}):")

        match = re.match(r'^if\s+(.+?):?$', masked_line, re.IGNORECASE)
        if match:
            cond = clean_expr_tokens(match.group(1).strip())
            return finalize(f"if {cond}:")

        match = re.match(r'^repeat\s+(.+?)\s+times\s+with\s+([a-zA-Z_]\w*):?$', masked_line, re.IGNORECASE)
        if match:
            times = clean_expr_tokens(match.group(1).strip())
            var = match.group(2)
            return finalize(f"for {var} in range({times}):")

        match = re.match(r'^repeat\s+(.+?)\s+times:?$', masked_line, re.IGNORECASE)
        if match:
            times = clean_expr_tokens(match.group(1).strip())
            return finalize(f"for _ in range({times}):")

        match = re.match(r'^count\s+from\s+(.+?)\s+to\s+(.+?)\s+step\s+(.+?)\s+as\s+([a-zA-Z_]\w*):?$', masked_line, re.IGNORECASE)
        if match:
            start = clean_expr_tokens(match.group(1).strip())
            end = clean_expr_tokens(match.group(2).strip())
            step = clean_expr_tokens(match.group(3).strip())
            var = match.group(4)
            return finalize(f"for {var} in range({start}, ({end}) + 1, {step}):")

        match = re.match(r'^count\s+from\s+(.+?)\s+to\s+(.+?)\s+as\s+([a-zA-Z_]\w*):?$', masked_line, re.IGNORECASE)
        if match:
            start = clean_expr_tokens(match.group(1).strip())
            end = clean_expr_tokens(match.group(2).strip())
            var = match.group(3)
            return finalize(f"for {var} in range({start}, ({end}) + 1):")

        match = re.match(r'^for\s+each\s+([a-zA-Z_]\w*)\s+in\s+(.+?):?$', masked_line, re.IGNORECASE)
        if match:
            item = match.group(1)
            collection = clean_expr_tokens(match.group(2).strip())
            return finalize(f"for {item} in {collection}:")

        match = re.match(r'^repeat\s+while\s+(.+?):?$', masked_line, re.IGNORECASE)
        if match:
            cond = clean_expr_tokens(match.group(1).strip())
            return finalize(f"while {cond}:")

        match = re.match(r'^(?:define|action|to)\s+([a-zA-Z_]\w*)\s+with\s+(.+?):?$', masked_line, re.IGNORECASE)
        if match:
            func_name = match.group(1)
            raw_args = match.group(2).strip()
            args = [a.strip() for a in re.split(r',|\band\b', raw_args) if a.strip()]
            return f"{indent}def {func_name}({', '.join(args)}):"

        match = re.match(r'^(?:define|action|to)\s+([a-zA-Z_]\w*)\s*(?:\(\))?:?$', masked_line, re.IGNORECASE)
        if match:
            func_name = match.group(1)
            return f"{indent}def {func_name}():"

        match = re.match(r'^(?:give\s+back|return)\s+(.+)$', masked_line, re.IGNORECASE)
        if match:
            expr = clean_expr_tokens(match.group(1).strip())
            return finalize(f"return {expr}")

        if re.match(r'^(?:give\s+back|return)$', masked_line, re.IGNORECASE):
            return f"{indent}return"

        match = re.match(r'^wait\s+(.+?)(?:\s+seconds?)?$', masked_line, re.IGNORECASE)
        if match:
            sec = clean_expr_tokens(match.group(1).strip())
            return finalize(f"wait({sec})")

        return finalize(masked_line)

    def transpile(self, source_code):
        lines = source_code.splitlines()
        py_lines = []

        if self.include_runtime:
            py_lines.append("# --- Auto-generated by SaidLang Transpiler ---")
            py_lines.append("from saidlang.runtime import *")
            py_lines.append("")

        for line in lines:
            res = self.transpile_line(line)
            if res:
                py_lines.append(res)

        return "\n".join(py_lines)
