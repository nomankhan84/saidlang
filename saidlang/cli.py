"""
SaidLang Command Line Interface (CLI)
Provides commands to run, build, preview, and interactively evaluate SaidLang code.
"""

import sys
import os
import argparse
from saidlang.transpiler import SaidLangTranspiler
from saidlang import runtime

def run_code(source_code, filename="<string>"):
    """Transpile and execute SaidLang code in Python runtime."""
    transpiler = SaidLangTranspiler(include_runtime=False)
    py_code = transpiler.transpile(source_code)

    # Prepare execution environment with runtime helpers and builtins
    env = {name: getattr(runtime, name) for name in dir(runtime) if not name.startswith("_")}
    env["__name__"] = "__main__"
    env["__file__"] = filename

    try:
        compiled = compile(py_code, filename, "exec")
        exec(compiled, env)
    except Exception as e:
        print(f"\n[SaidLang Execution Error]: {e}", file=sys.stderr)
        raise

def run_file(filepath):
    """Read a SaidLang file and run it."""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        source_code = f.read()

    run_code(source_code, filename=filepath)

def build_file(filepath, output_path=None):
    """Compile SaidLang file to a standalone Python script."""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)

    if not output_path:
        base, _ = os.path.splitext(filepath)
        output_path = base + ".py"

    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    transpiler = SaidLangTranspiler(include_runtime=True)
    py_code = transpiler.transpile(source)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(py_code)

    print(f"Compiled '{filepath}' -> '{output_path}'")

def preview_file(filepath):
    """Show the generated Python code for a SaidLang file."""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    transpiler = SaidLangTranspiler(include_runtime=True)
    py_code = transpiler.transpile(source)

    print("=" * 50)
    print(f" Python Equivalent for {filepath}")
    print("=" * 50)
    print(py_code)
    print("=" * 50)

def repl():
    """Interactive SaidLang shell."""
    print("Welcome to SaidLang Interactive Console! (Type 'exit' to quit)")
    print("-" * 55)
    transpiler = SaidLangTranspiler(include_runtime=False)
    env = {name: getattr(runtime, name) for name in dir(runtime) if not name.startswith("_")}
    env["__name__"] = "__repl__"

    while True:
        try:
            line = input("said > ")
            if not line.strip():
                continue
            if line.strip().lower() in ("exit", "quit"):
                print("Goodbye!")
                break

            py_line = transpiler.transpile_line(line)
            # Try eval first (for expressions), then exec (for statements)
            try:
                res = eval(py_line, env)
                if res is not None:
                    print(res)
            except SyntaxError:
                exec(py_line, env)
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break
        except Exception as err:
            print(f"Error: {err}")

def main():
    parser = argparse.ArgumentParser(
        description="SaidLang - Ultra human-friendly programming language transpiled to Python."
    )
    parser.add_argument("--version", "-v", action="version", version="SaidLang v0.1.0")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Run command
    run_parser = subparsers.add_parser("run", help="Run a .said source file")
    run_parser.add_argument("file", help="Path to .said file")

    # Build command
    build_parser = subparsers.add_parser("build", help="Compile .said to .py file")
    build_parser.add_argument("file", help="Path to .said file")
    build_parser.add_argument("-o", "--output", help="Output .py file path")

    # Preview command
    preview_parser = subparsers.add_parser("preview", help="Preview generated Python code")
    preview_parser.add_argument("file", help="Path to .said file")

    # REPL command
    subparsers.add_parser("repl", help="Start interactive SaidLang REPL")

    # Shortcut: if first argument is a file with .said extension
    if len(sys.argv) > 1 and sys.argv[1].endswith(".said") and not sys.argv[1].startswith("-"):
        run_file(sys.argv[1])
        return

    args = parser.parse_args()

    if args.command == "run":
        run_file(args.file)
    elif args.command == "build":
        build_file(args.file, args.output)
    elif args.command == "preview":
        preview_file(args.file)
    elif args.command == "repl" or args.command is None:
        repl()

if __name__ == "__main__":
    main()
