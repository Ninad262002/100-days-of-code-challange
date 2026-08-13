# Loops in Python

Loops are used to **repeat a block of code multiple times**.

Python mainly has two types of loops:

- `for` loop
- `while` loop

## `for` Loop

A `for` loop is used to **iterate over a sequence** such as:

- String
- List
- Tuple
- Set
- Dictionary

### Example: String

```python
name = "Abhishek"

for i in name:
    print(i)
```

**Output:**

```text
A
b
h
i
s
h
e
k
```

The loop takes **one character at a time** from the string.

### Example: List

```python
colors = ["Red", "Green", "Blue", "Yellow"]

for color in colors:
    print(color)
```

**Output:**

```text
Red
Green
Blue
Yellow
```

## `range()` Function

`range()` is used when you want to repeat a loop for a **specific number or range of times**.

### Example

```python
for i in range(5):
    print(i)
```

**Output:**

```text
0
1
2
3
4
```

`range(5)` starts from **0** and stops **before 5**.

### Specific Range

```python
for i in range(4, 9):
    print(i)
```

**Output:**

```text
4
5
6
7
8
```

### Remember

```text
range(start, stop)
```

- `start` → where the loop starts
- `stop` → where the loop stops (**not included**)

**Example:** `range(4, 9)` → `4, 5, 6, 7, 8`




## How `range(1, 10, 2)` Works

Python calculates `range(1, 10, 2)` step-by-step:

1. **Start at 1**
   - First number: `1`

2. **Add 2**
   - `1 + 2 = 3`

3. **Add 2**
   - `3 + 2 = 5`

4. **Add 2**
   - `5 + 2 = 7`

5. **Add 2**
   - `7 + 2 = 9`

6. **Stop**
   - Next number: `9 + 2 = 11`
   - `11` is greater than `10`, so the loop stops.

### Result

```text
1, 3, 5, 7, 9


| Syntax | Example | Result Sequence | Notes |
|---|---|---|---|
| `range(start, stop)` | `range(1, 5)` | `1, 2, 3, 4` | Step defaults to `1` |
| `range(start, stop, positive_step)` | `range(2, 9, 3)` | `2, 5, 8` | Stops before reaching or exceeding `9` |
| `range(start, stop, negative_step)` | `range(5, 1, -1)` | `5, 4, 3, 2` | Counts backwards |

