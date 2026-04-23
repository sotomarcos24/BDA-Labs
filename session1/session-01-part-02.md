### Session 1 | part 2

> In BDA, we will gradually build our own small libraries. First, let's recap the basics.

#### 1. Goal

First, you will practice core Python loop logic using:

- counters
- indexes
- `for` loops
- nested loops (matrix traversal)

#### 2. Prerequisites

Before starting:

1. Open the `session1` folder in Visual Studio Code.
2. Activate your virtual environment.
3. Open (or create) your solution files in:

```txt
session1/solutions/
```

#### 3. Basics you should know

- `counter`: a variable that increases/decreases to track quantity.
- `index`: the position of an element in a list (starts at `0`).
- `pointer`: in this class, we use this word like a position tracker (usually an index counter).
- `range(len(data))`: common pattern to iterate through list indexes.
- `nested loop`: a loop inside another loop (used for matrices).
- `break`: stops the current loop immediately.

#### 4. Example 1: Count elements

Consider a list. Can you count all elements without using `len()`?

Create a file named `count_items.py` with this code:

File: `session1/solutions/count_items.py`

```python
data = [10, 20, 30, 40, 50]

count = 0
for item in data:
    count += 1

print(count)
```

Expected output:

```txt
5
```

Now wrap the same logic in a function:

File: `session1/solutions/loop_utils.py`

```python
def my_len(data):
    count = 0
    for item in data:
        count += 1
    return count
```

Save this function in a different file, for example `loop_utils.py` (same folder).

Then import and use it from `count_items.py`:

File: `session1/solutions/count_items.py`

```python
from loop_utils import my_len

print(my_len([10, 20, 30]))
```

Expected output:

```txt
3
```

> [!TIP]
>
> What are the time and space complexities of `my_len`?
>
> <details>
>   <summary>Show answer</summary>
> Time: O(n)
>
> Space: O(1)
>
> If you do not get it, talk to Stelios.
>
> </details>

#### 5. Example 2: Sum elements

Let's sum all elements using a `total` variable.

File: `session1/solutions/sum_items.py`

```python
data = [10, 20, 30, 40, 50]

total = 0
for item in data:
    total += item

print(total)
```

Expected output:

```txt
150
```

> `i += 1` increments by 1, while `total += element` accumulates values.

Good practice: wrap reusable logic into functions in `loop_utils.py` and call them from files like `sum_items.py`.

> [!TIP]
>
> What are the time and space complexities of the script above?
>
> <details>
>   <summary>Show answer</summary>
>
> Time: O(n)
>
> Space: O(1)
>
> </details>

#### 6. Example 3: Find position of a target value

Let's find the position of a target value.

File: `session1/solutions/find_position.py`

```python
data = [10, 20, 30, 40, 50]

pointer = 0
for item in data:
    if item == 30:
        print(pointer)
        break
    pointer += 1
```

Expected output:

```txt
2
```

Another common way to work with positions is:

File: `session1/solutions/find_position.py`

```python
data = [10, 20, 30, 40, 50]

for i in range(len(data)):
    print(i)
```

#### 7. Example 4: Traverse a matrix with nested loops

Run this and explore the output.

File: `session1/solutions/matrix_positions.py`

```python
matrix = [
    [10, 20],
    [30, 40]
]

for row in matrix:
    print(row)
    for value in row:
        print(value)
```

Now track row and column indexes explicitly:

File: `session1/solutions/matrix_positions.py`

```python
matrix = [
    [10, 20],
    [30, 40]
]

row_index = 0
col_index = 0

for row in matrix:
    print("row:", row_index)
    for value in row:
        print("col:", col_index, "value:", value)
        col_index += 1
    col_index = 0
    row_index += 1
```

Expected output:

```txt
row: 0
col: 0 value: 10
col: 1 value: 20
row: 1
col: 0 value: 30
col: 1 value: 40
```

> [!NOTE]
>
> Why do we set `col_index = 0` after each row?
>
> <details>
> <summary>Show answer</summary>
>
> - Because each new row starts from the first column again.
> - If you do not reset it, column indexes continue from the previous row and become incorrect.
>
> </details>
>
> What are the time and space complexities of the script above?
>
> <details>
> <summary>Show answer</summary>
>
>
> Time: O(r * c) where `r` is the number of rows and `c` is the number of columns.
>
> Space: O(1)
>
> </details>

### TEST

<details> <summary>Show code</summary>

Time: O(r * c) where `r` is the number of rows and `c` is the number of columns.

```
python
matrix = [
    [10, 20],
    [30, 40]
]

row_index = 0
col_index = 0

for row in matrix:
    print("row:", row_index)
    for value in row:
        print("col:", col_index, "value:", value)
        col_index += 1
    col_index = 0
    row_index += 1
```

</details> 

#### 8. Call Stelios 🥊

Call Stelios to challenge you with a question before moving to the exercise.

#### 9. Exercise

Add your answers to:

```txt
session1/solutions/
```

Tasks:

1. In `count_items.py`, write a function to count elements between `1` and `10` (inclusive) in `data = [30, 6, 9, 12, 15, 8]`.
2. In `sum_items.py`, write a function to sum all even numbers in the same list.
3. In `find_position.py`, write a function that returns the position of the first value equal to `12` in the same list. If the value is not found, return `-1`.
4. In `matrix_positions.py`, for the matrix below, print the position of `25` as user-friendly coordinates `[2, 2]` (use 1-based indexing for rows and columns).

File: `session1/solutions/matrix_positions.py`

```python
matrix = [
    [5, 10, 15],
    [20, 25, 30]
]
```

5. In one short comment, explain why resetting the column index is important in nested loops.
6. What are the time and space complexities of your script(s)?

#### 10. Quiz

Complete the following quiz.

```shell
quizmd quizzes/python-loops-and-indexing-quiz.md
```

If you want to choose a theme:

```bash
quizmd --theme light quizzes/python-loops-and-indexing-quiz.md
quizmd --theme dark quizzes/python-loops-and-indexing-quiz.md
```

- Use `--theme light` if your terminal has a white/light background.
- Use `--theme dark` if your terminal has a dark background.

> For accessibility use this: `quizmd --no-color quizzes/python-loops-and-indexing-quiz.md`
