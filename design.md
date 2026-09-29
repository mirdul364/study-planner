# Design Document

## 1. Problem Statement
Students find it hard to organise study hours and practise basic algorithms in one place. See `statement.md`.

## 2. Objectives
1. Let a student build and manage a study plan.
2. Show progress through a simple report.
3. Provide an Algorithm Lab that applies the fundamental algorithms of the course.
4. Keep the program modular, validated and tested.

## 3. Functional Requirements
| ID | Requirement |
|---|---|
| FR1 | Add a subject with study hours (no duplicates). |
| FR2 | View, mark completed, remove, search and sort the plan. |
| FR3 | Generate a report (counts, hours, percentage). |
| FR4 | Run 9 algorithms from the Algorithm Lab on user input. |
| FR5 | Show clear menus and messages for every action. |

The three major modules are **Study Plan Management**, **Report** and **Algorithm Lab**.

## 4. Non-Functional Requirements
| Type | Requirement |
|---|---|
| Usability | Numbered menus and clear prompts stating the allowed range. |
| Reliability | Every input is validated and re-asked; the program never crashes on bad input. |
| Maintainability | One responsibility per module; comments on every function. |
| Performance / resource efficiency | Trial division stops at the square root (time trade-off); input limits keep run time short. |
| Error handling | Invalid choices and item numbers give a message and the menu continues. |

## 5. System Architecture
```mermaid
flowchart TD
    U[User] --> M[main.py - menus]
    M --> V[validation.py]
    M --> P[planner.py]
    M --> R[report.py]
    M --> B[basic_algorithms.py]
    M --> N[number_algorithms.py]
    P --> D[(In-memory list of dictionaries)]
    R --> D
    N -. reuses .-> N
```

## 6. Workflow Diagram
```mermaid
flowchart TD
    A([Start]) --> B[Show main menu]
    B --> C{Choice}
    C -->|1-6| D[Plan action]
    C -->|7| E[Show report]
    C -->|8| F[Algorithm Lab]
    C -->|9| G([Exit])
    C -->|other| H[Invalid choice]
    D --> B
    E --> B
    F --> B
    H --> B
```

## 7. Use Case Diagram
```mermaid
flowchart LR
    S((Student)) --> UC1[Add subject]
    S --> UC2[View plan]
    S --> UC3[Mark completed]
    S --> UC4[Remove item]
    S --> UC5[Search subject]
    S --> UC6[Sort plan]
    S --> UC7[View report]
    S --> UC8[Use Algorithm Lab]
```

## 8. Sequence Diagram (Add Subject)
```mermaid
sequenceDiagram
    participant U as Student
    participant M as main.py
    participant V as validation.py
    participant P as planner.py
    U->>M: choose 1
    M->>V: get_text
    V-->>M: name
    M->>V: get_integer(hours)
    V-->>M: hours
    M->>P: add_subject(subjects, name, hours)
    P-->>M: True / False
    M-->>U: Added / Already exists
```

## 9. Component Diagram
```mermaid
flowchart LR
    main --> validation
    main --> planner
    main --> report
    main --> basic_algorithms
    main --> number_algorithms
    test_project --> planner
    test_project --> report
    test_project --> basic_algorithms
    test_project --> number_algorithms
```

## 10. Storage Design
No database is used. The plan is kept in memory as a list of dictionaries:
```
subjects = [ {'name': 'Maths', 'hours': 3, 'done': False}, ... ]
```
An ER diagram is therefore not applicable.

## 11. Design Decisions
- **List of dictionaries:** each subject has named fields, and the list keeps the order shown to the user.
- **Functions in separate modules:** easier to test and explain.
- **Loop-based validation:** `isdecimal()` check with a `while` loop instead of exceptions.
- **Newton's method for square root:** converges in a few steps; the loop stops when two guesses are almost equal.
- **Divisors only up to the square root:** cuts the work from n steps to about the square root of n.
