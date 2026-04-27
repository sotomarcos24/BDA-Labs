### Session 1 | Part 2

> In BDA, we will gradually build our own small libraries. First, let's recap the basics.

#### 1. Goal

In this tutorial, you will practice core Python loop logic using:

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

Create a file in your `solutions/` folder with this code:

File: `session1/solutions/exercise-01-02.py`

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

File: `session1/solutions/exercise-01-02.py`

```python
def my_len(data):
    count = 0
    for item in data:
        count += 1
    return count
```

Save this function in a different file in the same folder, for example `exercise_01_02_lib.py`.

Then import and use it from your main script:

File: `session1/solutions/exercise-01-02.py`

```python
from exercise_01_02_lib import my_len

print(my_len([10, 20, 30]))
```

Expected output:

```txt
3
```

> [!NOTE]
>
> What are the time and space complexities of `my_len`?
>
> <details>
>   <summary>Show answer</summary>
>
> Time: O(n)
>
> Space: O(1)
>
> If you do not get it, talk to Stelios.
>
> </details>

#### 5. Example 2: Sum elements

Let's sum all elements using a `total` variable.  
File: `session1/solutions/exercise-01-02.py`. Fill in the missing code.

```python
data = [10, 20, 30, 40, 50]

total = 0
...
print(total)
```

Expected output:

```txt
150
```

> Solution
>
> <details>
> <summary>Show answer</summary>
>
> `count += 1` increments a counter, while `total += item` accumulates values.
>
> ```python
> data = [10, 20, 30, 40, 50]
> 
> total = 0
> for item in data:
>     total += item
> 
> print(total)
> ```
>
> </details>

Good practice: wrap reusable logic into helper functions (for example `exercise_01_02_lib.py`) and import them into your main script.

> [!NOTE]
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

File: `session1/solutions/exercise-01-02.py`. Fill up the missing code.

```python
data = [10, 20, 30, 40, 50]

# We use `pointer` as an index counter (starting at 0).
pointer = 0
...
```

Expected output (0-based index, counting starts from 0):

```txt
2
```

> Solution
>
> <details>
> <summary>Show answer</summary>
>
> We use a position counter (`pointer`) and stop at the first match using `break`.
>
> ```python
> data = [10, 20, 30, 40, 50]
> 
> pointer = 0
> for item in data:
>     if item == 30:
>         print(pointer)
>         break
>     pointer += 1
> ```
>
> </details>

Another common way to work with positions is:

File: `session1/solutions/exercise-01-02.py`

```python
data = [10, 20, 30, 40, 50]

for i in range(len(data)):
    print(i)
```

#### 7. Example 4: Traverse a matrix with nested loops

Run this and explore the output.

File: `session1/solutions/exercise-01-02.py`

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

File: `session1/solutions/exercise-01-02.py`

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
    # Reset col_index for each new row.
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
> Time: O(r * c) where `r` is the number of rows and `c` is the number of columns.
>
> Space: O(1)
>
> </details>

#### 8. Call Stelios for a quick challenge 🔥

Call Stelios for a quick challenge question before moving to the exercise.

#### 9. Exercise

Add your answers to:

```txt
session1/solutions/
```

Tasks:

1. Write a function to count elements between `1` and `10` (inclusive) in `data = [30, 6, 9, 12, 15, 8]`.
2. Write a function to sum all even numbers in the same list.
3. Write a function that returns the position of the first value equal to `12` in the same list. If the value is not found, return `-1`.
4. For the matrix below, print the position of `25` as coordinates [2, 2] in the matrix (row, column), using 1-based indexing.
   
File: `session1/solutions/exercise-01-02.py`

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

```bash
quizmd quizzes/python-loops-and-indexing-quiz.md
```

If you want to choose a theme:

```bash
quizmd --theme light quizzes/python-loops-and-indexing-quiz.md
quizmd --theme dark quizzes/python-loops-and-indexing-quiz.md
```
