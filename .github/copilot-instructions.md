# GitHub Copilot / AI agent guidance for simple_git_python

## Project intent (big picture)
- This repository is a small, educational Python project that provides simple example scripts under `examples/` for learning Python basics (math, tuples, dictionaries, formatting, doctests, etc.).
- Files in `examples/` are primarily learning examples: they include functions, doctest-style examples inside docstrings, and direct execution blocks (`if __name__ == "__main__":`). Avoid turning `examples/` into a production package — keep changes minimal and educational in scope.

## Important files and patterns to know
- `examples/` — all the example scripts. Key files:
  - `examples/fibonacci.py`, `examples/factorialnumber.py`, `examples/triangle.py`, `examples/imc.py`, `examples/dictionary.py`, `examples/tuples.py`
  - Each of these generally follows the same pattern: small helper/validator functions, a `main()` function used for demo output, `if __name__ == "__main__"` block, and doctests in the function docstrings.
- `doctest.txt` — short guide file describing how doctest works (useful for running local checks).
- `entry.py` — a placeholder entry file used when learning git and project structure.
- `requirements.txt` — list of third-party packages; project currently doesn't import most of them in the example scripts (this appears to be a general/global list used for learning).
- `Starting and GIT.txt` and `Starting from GIT.txt` — initial developer setup and workflow notes; follow those for environment and Git usage.

## Local dev workflow (commands)
- Setup a venv and install deps:
  - Windows PowerShell:
    .\venv\Scripts\activate
    pip install -r requirements.txt
- Run a single example file as a script:
  - python examples/fibonacci.py
- Run doctests for a specific file (used frequently in examples):
  - python -m doctest -v examples/fibonacci.py
- Run doctests for all example files (simple check):
  - python -m doctest -v examples/*.py

## Coding conventions in this repo
- Preserve educational focus: when editing examples prefer adding new examples rather than refactoring away readability.
- Docstrings: Use docstring-based doctests for examples and validations (see `examples/fibonacci.py` and `examples/triangle.py` for canonical samples).
- Type hints: Many functions include type hints (e.g., `-> int`, `-> float`); follow this style for new functions to keep consistent.
- `main()` + `__main__` pattern: Keep the `main()` demo function and the `if __name__ == "__main__"` guard to allow both CLI execution and import for doctest/pytest.
- Spanish comments: Many files use Spanish comments for clarifications. Keep the original language when editing unless asked to internationalize.
- Printing & I/O: Example scripts often print outputs to show results; do not remove demo prints unless converting a file to library-only code.

## Adding new code & tests (recommendations)
- Prefer adding small, self-contained functions with: type hints + docstring + doctest example(s).
- When adding a new example file, follow the file pattern: functions, doctest examples, `main()` execution demo, and `if __name__` block.
- If you add formal automated tests, place them under a new `tests/` directory (and include pytest in `requirements.txt`). Don’t modify existing doctests — if needed, add equivalent unit tests rather than replacing doctests.

## What not to change (unless requested)
- Do not remove or rewrite doctests provided in the docstrings — they serve as living documentation and quick validation points.
- Do not translate Spanish comments or messages unless requested — these are part of the educational content.
- Avoid introducing heavy application-level refactors that convert examples into a production library without user direction.

## Collaboration & pull request guidance
- Small, focused PRs are preferred: preserve the educational example intent.
- When adding library-like utilities, add `tests/` with coverage for the main logic, and update `requirements.txt` when you introduce dependencies.
- Add short examples in the docstrings to maintain the living documentation approach.

## Quick examples (copy/paste)
- Run fibonacci doctests:
  - python -m doctest -v examples/fibonacci.py
- Run a script interactively in PowerShell:
  - .\venv\Scripts\activate; python examples/triangle.py

## Notes for the AI agent
- This repository is not a production app; aim to preserve the educational content and the executable, simple examples.
- Use doctests as the canonical verification mechanism for small logic changes.
- If a requested change is larger (convert to a package, add CI, restructure), ask the user for explicit confirmation.

