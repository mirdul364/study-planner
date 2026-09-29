# Student Study Planner

## Overview
A console-based Python project that helps students plan study hours and practise fundamental algorithms. It was built for the *Problem Solving and Python Programming* course and uses only the concepts from that syllabus (functions, modules, control flow, lists, dictionaries, tuple assignment).

## Features
- **Study Plan Management:** add, view, mark completed, remove, search and sort subjects.
- **Report:** counts and sums study hours, and shows completion percentage.
- **Algorithm Lab:** factorial, Fibonacci, reverse text, base conversion (2-16), GCD, prime numbers up to N, prime factors, smallest divisor, square root (Newton's method).
- **Input validation:** invalid input is rejected and asked again, so the program does not crash.

## Technologies Used
- Python 3.8 or later (no external libraries)
- Git and GitHub for version control

## Project Structure
```
study-planner/
├── main.py                 # entry point, menus
├── validation.py           # input validation helpers
├── planner.py              # study plan management
├── report.py               # report generation
├── basic_algorithms.py     # factorial, Fibonacci, reverse, base conversion
├── number_algorithms.py    # square root, divisor, GCD, primes, prime factors
├── test_project.py         # validation tests
├── statement.md            # problem statement
└── docs/design.md          # requirements and design diagrams
```

## Install and Run
1. Install Python 3 from https://www.python.org
2. Clone the repository:
   ```
   git clone <your-repository-url>
   cd study-planner
   ```
3. Run the program:
   ```
   python main.py
   ```

## Testing
Run the validation tests:
```
python test_project.py
```
Expected output: `All tests passed.`

Manual tests: enter letters, 0, negative numbers or empty text at any prompt. The program should show a message and ask again.

## Syllabus Mapping
| Syllabus topic | Where it is used |
|---|---|
| Modules and functions | Every file; `main.py` imports the others |
| Conditionals, iteration, break/continue | Menus, validation, `smallest_divisor` |
| Tuple assignment / exchange values | `sort_by_hours`, `fibonacci`, `gcd` |
| Counting and summation | `report.py` |
| Factorial, Fibonacci, reverse, base conversion | `basic_algorithms.py` |
| Square root, smallest divisor, GCD, primes, prime factors | `number_algorithms.py` |
| Lists and dictionaries | Study plan (list of dictionaries) |
| Time trade-off | `smallest_divisor` tries divisors only up to the square root |

## Screenshots
Add screenshots of the menus and sample runs here (e.g. `docs/screenshot1.png`).
