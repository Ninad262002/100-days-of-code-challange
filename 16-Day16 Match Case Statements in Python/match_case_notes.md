# Match-Case Statements in Python

## What is Match-Case?

`match-case` is Python's way of doing something similar to a **switch-case** statement in languages like C, C++, and Java.

It checks a value against different `case` patterns and runs the code for the **first matching case**.

## Syntax

```python
match variable:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default case
```

- `match` → value we want to check
- `case` → possible value/pattern
- `_` → default case, similar to `else`

## Example

```python
x = 4

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _:
        print("Other value")
```

### Output

```text
x is 4
```

## Match-Case with a Condition

You can also add an `if` condition to a case:

```python
x = 4

match x:
    case 4 if x % 2 == 0:
        print("4 is even")
    case _:
        print("Other value")
```

### Output

```text
4 is even
```

### Key Point

`match-case` checks cases **from top to bottom** and executes the **first matching case**.
