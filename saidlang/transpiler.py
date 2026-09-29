"""
SaidLang Transpiler
Translates ultra-friendly SaidLang syntax into valid Python code.
"""

import re

# Operators dictionary sorted by length of phrase descending (so longer phrases match first)
OPERATOR_MAP = [
    (r"\bis greater than or equal to\b", ">="),
    (r"\bis less than or equal to\b", "<="),
    (r"\bis greater than\b", ">"),
    (r"\bis less than\b", "<"),
    (r"\bis not equal to\b", "!="),
    (r"\bis equal to\b", "=="),
    (r"\bis exactly\b", "=="),
    (r"\bmultiplied by\b", "*"),
    (r"\bdivided by\b", "/"),
    (r"\bpower of\b", "**"),
    (r"\bplus\b", "+"),
    (r"\bminus\b", "-"),
    (r"\bmodulo\b", "%"),
    (r"\btrue\b", "True"),
    (r"\bfalse\b", "False"),
    (r"\bnothing\b", "None"),
    (r"\bnull\b", "None"),
]

def mask_string_literals(line):
    """
    Extract string literals to protect them from operator substitutions.
    Returns the masked line and a map of placeholders to original strings.
    """
    strings = {}
    counter = 0

    def replace_str(match):
        nonlocal counter
        key = f"__SAID_STR_{counter}__"
        strings[key] = match.group(0)
        counter += 1
        return key

    # Match single, double, and triple quoted strings
    pattern = r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')'
    masked_line = re.sub(pattern, replace_str, line)
    return masked_line, strings

def unmask_string_literals(line, strings):
    """Restore string literals from placeholders."""
    for key, val in strings.items():
        line = line.replace(key, val)
    return line

def translate_expressions(expr):
    """Translate human phrases in expressions to Python equivalents."""
    masked, strings = mask_string_literals(expr)

    for pattern, replacement in OPERATOR_MAP:
        masked = re.sub(pattern, replacement, masked, flags=re.IGNORECASE)

    return unmask_string_literals(masked, strings)

class SaidLangTranspiler:
    def __init__(self, include_runtime=True):
        self.include_runtime = include_runtime

    def transpile_line(self, raw_line):
        """Transpile a single SaidLang line into Python."""
        # Preserve indentation
        indent = ""
        lstripped = raw_line.lstrip()
        indent_len = len(raw_line) - len(lstripped)
        indent = raw_line[:indent_len]

        line = lstripped.rstrip()

        # Handle empty lines
        if not line:
            return ""

        # Handle comments: // or note: or #
        if line.startswith("//"):
            return indent + "#" + line[2:]
        if line.lower().startswith("note:"):
            return indent + "#" + line[5:]
        if line.startswith("#"):
            return indent + line

        # 1. Output statements:
        # show "hello", say "hello", display "hello", print "hello"
        match = re.match(r'^(?:show|say|display|print)\s+(.+)$', line, re.IGNORECASE)
        if match:
            expr = translate_expressions(match.group(1).strip())
            return f"{indent}show({expr})"

        if re.match(r'^(?:show|say|display|print)\s*$', line, re.IGNORECASE):
            return f"{indent}show()"

        # 2. Variable assignments:
        # set <var> to <val>
        # set <var> = <val>
        # make <var> = <val>
        # let <var> be <val>
        # remember <var> as <val>
        match = re.match(r'^(?:set|make|let|remember)\s+([a-zA-Z_]\w*)\s+(?:to|=|be|as)\s+(.+)$', line, re.IGNORECASE)
        if match:
            var_name = match.group(1)
            expr = translate_expressions(match.group(2).strip())
            return f"{indent}{var_name} = {expr}"

        # 3. Increase / Decrease / Math on variables
        # increase x by 5
        match = re.match(r'^increase\s+([a-zA-Z_]\w*)\s+by\s+(.+)$', line, re.IGNORECASE)
        if match:
            var = match.group(1)
            expr = translate_expressions(match.group(2).strip())
            return f"{indent}{var} += {expr}"

        # decrease x by 5
        match = re.match(r'^decrease\s+([a-zA-Z_]\w*)\s+by\s+(.+)$', line, re.IGNORECASE)
        if match:
            var = match.group(1)
            expr = translate_expressions(match.group(2).strip())
            return f"{indent}{var} -= {expr}"

        # multiply x by 5
        match = re.match(r'^multiply\s+([a-zA-Z_]\w*)\s+by\s+(.+)$', line, re.IGNORECASE)
        if match:
            var = match.group(1)
            expr = translate_expressions(match.group(2).strip())
            return f"{indent}{var} *= {expr}"

        # divide x by 5
        match = re.match(r'^divide\s+([a-zA-Z_]\w*)\s+by\s+(.+)$', line, re.IGNORECASE)
        if match:
            var = match.group(1)
            expr = translate_expressions(match.group(2).strip())
            return f"{indent}{var} /= {expr}"

        # 4. User input:
        # ask number "prompt" into <var>
        match = re.match(r'^ask\s+number\s+(.+?)\s+into\s+([a-zA-Z_]\w*)$', line, re.IGNORECASE)
        if match:
            prompt = translate_expressions(match.group(1).strip())
            var = match.group(2)
            return f"{indent}{var} = ask_number({prompt})"

        # ask [user] "prompt" into <var>
        match = re.match(r'^ask(?:\s+user)?\s+(.+?)\s+into\s+([a-zA-Z_]\w*)$', line, re.IGNORECASE)
        if match:
            prompt = translate_expressions(match.group(1).strip())
            var = match.group(2)
            return f"{indent}{var} = ask({prompt})"

        # 5. List operations:
        # add <item> to <list>
        match = re.match(r'^add\s+(.+?)\s+to\s+([a-zA-Z_]\w*)$', line, re.IGNORECASE)
        if match:
            item = translate_expressions(match.group(1).strip())
            target_list = match.group(2)
            return f"{indent}{target_list}.append({item})"

        # remove <item> from <list>
        match = re.match(r'^remove\s+(.+?)\s+from\s+([a-zA-Z_]\w*)$', line, re.IGNORECASE)
        if match:
            item = translate_expressions(match.group(1).strip())
            target_list = match.group(2)
            return f"{indent}{target_list}.remove({item})"

        # create empty list <name> / create list <name>
        match = re.match(r'^create\s+(?:empty\s+)?list\s+([a-zA-Z_]\w*)$', line, re.IGNORECASE)
        if match:
            return f"{indent}{match.group(1)} = []"

        # 6. Conditionals:
        # otherwise if / else if / or if <cond>:
        match = re.match(r'^(?:otherwise\s+if|else\s+if|or\s+if)\s+(.+?):?$', line, re.IGNORECASE)
        if match:
            cond = translate_expressions(match.group(1).strip())
            return f"{indent}elif {cond}:"

        # otherwise: / else:
        match = re.match(r'^(?:otherwise|else):?$', line, re.IGNORECASE)
        if match:
            return f"{indent}else:"

        # unless <cond>: (meaning: if not (...):)
        match = re.match(r'^unless\s+(.+?):?$', line, re.IGNORECASE)
        if match:
            cond = translate_expressions(match.group(1).strip())
            return f"{indent}if not ({cond}):"

        # if <cond>:
        match = re.match(r'^if\s+(.+?):?$', line, re.IGNORECASE)
        if match:
            cond = translate_expressions(match.group(1).strip())
            return f"{indent}if {cond}:"

        # 7. Loops:
        # repeat <N> times with <var>:
        match = re.match(r'^repeat\s+(.+?)\s+times\s+with\s+([a-zA-Z_]\w*):?$', line, re.IGNORECASE)
        if match:
            times = translate_expressions(match.group(1).strip())
            var = match.group(2)
            return f"{indent}for {var} in range({times}):"

        # repeat <N> times:
        match = re.match(r'^repeat\s+(.+?)\s+times:?$', line, re.IGNORECASE)
        if match:
            times = translate_expressions(match.group(1).strip())
            return f"{indent}for _ in range({times}):"

        # count from <start> to <end> step <step> as <var>:
        match = re.match(r'^count\s+from\s+(.+?)\s+to\s+(.+?)\s+step\s+(.+?)\s+as\s+([a-zA-Z_]\w*):?$', line, re.IGNORECASE)
        if match:
            start = translate_expressions(match.group(1).strip())
            end = translate_expressions(match.group(2).strip())
            step = translate_expressions(match.group(3).strip())
            var = match.group(4)
            return f"{indent}for {var} in range({start}, ({end}) + 1, {step}):"

        # count from <start> to <end> as <var>:
        match = re.match(r'^count\s+from\s+(.+?)\s+to\s+(.+?)\s+as\s+([a-zA-Z_]\w*):?$', line, re.IGNORECASE)
        if match:
            start = translate_expressions(match.group(1).strip())
            end = translate_expressions(match.group(2).strip())
            var = match.group(3)
            return f"{indent}for {var} in range({start}, ({end}) + 1):"

        # for each <item> in <collection>:
        match = re.match(r'^for\s+each\s+([a-zA-Z_]\w*)\s+in\s+(.+?):?$', line, re.IGNORECASE)
        if match:
            item = match.group(1)
            collection = translate_expressions(match.group(2).strip())
            return f"{indent}for {item} in {collection}:"

        # repeat while <cond>:
        match = re.match(r'^repeat\s+while\s+(.+?):?$', line, re.IGNORECASE)
        if match:
            cond = translate_expressions(match.group(1).strip())
            return f"{indent}while {cond}:"

        # while <cond>:
        match = re.match(r'^while\s+(.+?):?$', line, re.IGNORECASE)
        if match:
            cond = translate_expressions(match.group(1).strip())
            return f"{indent}while {cond}:"

        # stop loop / break
        if re.match(r'^(?:stop\s+loop|break)$', line, re.IGNORECASE):
            return f"{indent}break"

        # skip to next / continue
        if re.match(r'^(?:skip\s+to\s+next|continue)$', line, re.IGNORECASE):
            return f"{indent}continue"

        # 8. Functions / Actions:
        # define / action / to <name> with <args>:
        match = re.match(r'^(?:define|action|to)\s+([a-zA-Z_]\w*)\s+with\s+(.+?):?$', line, re.IGNORECASE)
        if match:
            func_name = match.group(1)
            raw_args = match.group(2).strip()
            # support comma or "and" separated args
            args = [a.strip() for a in re.split(r',|\band\b', raw_args) if a.strip()]
            return f"{indent}def {func_name}({', '.join(args)}):"

        # define / action / to <name>:
        match = re.match(r'^(?:define|action|to)\s+([a-zA-Z_]\w*)\s*(?:\(\))?:?$', line, re.IGNORECASE)
        if match:
            func_name = match.group(1)
            return f"{indent}def {func_name}():"

        # give back <expr> / return <expr>
        match = re.match(r'^(?:give\s+back|return)\s+(.+)$', line, re.IGNORECASE)
        if match:
            expr = translate_expressions(match.group(1).strip())
            return f"{indent}return {expr}"

        # give back / return
        if re.match(r'^(?:give\s+back|return)$', line, re.IGNORECASE):
            return f"{indent}return"

        # 9. Wait:
        # wait <N> seconds / wait <N>
        match = re.match(r'^wait\s+(.+?)(?:\s+seconds?)?$', line, re.IGNORECASE)
        if match:
            sec = translate_expressions(match.group(1).strip())
            return f"{indent}wait({sec})"

        # Fallback: Translate any remaining expressions and keep structure
        return indent + translate_expressions(line)

    def transpile(self, source_code):
        """Transpile full SaidLang source code into Python."""
        lines = source_code.splitlines()
        py_lines = []

        if self.include_runtime:
            py_lines.append("# --- Auto-generated by SaidLang Transpiler ---")
            py_lines.append("from saidlang.runtime import *")
            py_lines.append("")

        for line in lines:
            py_lines.append(self.transpile_line(line))

        return "\n".join(py_lines)
