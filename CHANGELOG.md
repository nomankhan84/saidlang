# Changelog

All notable changes to **SaidLang** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2026-09-30

### Added
- **Natural English Syntax Engine**:
  - `save <var> as <val> as <type>` and compound assignments with `and`.
  - `@variable` string interpolation and expression evaluation.
  - Inline natural conditionals (`if ... then say ... else say ...`).
  - Natural repeat phrasing (`repeat <message> <N> times`).
- **Core Transpiler**:
  - Full variable assignments (`set ... to ...`, `let ... be ...`, `make ... = ...`).
  - Conditionals (`if`, `otherwise if`, `otherwise`).
  - Loops (`repeat N times`, `count from A to B`, `for each item in list`).
  - Functions (`to func with a and b:`, `give back result`).
  - Error handling (`attempt:`, `on error:`).
  - Built-in file I/O and web request primitives.
- **Developer Tooling**:
  - Unified CLI: `said run`, `said build`, `said repl`, `said new`, `said info`.
  - Native Python import hook support via `saidlang.hook`.
  - Official Visual Studio Code extension with syntax highlighting and snippets.
- **Open Source Infrastructure**:
  - Cross-platform CI/CD GitHub Actions matrix test suite across Python 3.8 - 3.12.
  - Standardized documentation and contributing guides.
