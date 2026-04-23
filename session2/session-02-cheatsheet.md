### Session 2 | cheatsheet

> Quick reference for common time complexities and the code patterns behind them.

#### 1. Common complexities

From best growth to worst growth:

```text
O(1)       -> constant
O(log n)   -> logarithmic
O(n)       -> linear
O(n log n) -> linearithmic
O(n^2)     -> quadratic
O(2^n)     -> exponential
O(n!)      -> factorial
```

#### 2. Intuition

| Complexity | Intuition |
| --- | --- |
| `O(1)` | Same time no matter input size |
| `O(log n)` | Cut the problem in half each step |
| `O(n)` | Check everything once |
| `O(n log n)` | Process all elements across logarithmic levels |
| `O(n^2)` | Compare everything with everything |
| `O(2^n)` | Explore all include/exclude combinations |
| `O(n!)` | Explore all possible orders |

#### 3. Real-world examples

| Complexity | Example |
| --- | --- |
| `O(1)` | Read first item in a list |
| `O(log n)` | Higher/lower guessing on sorted data |
| `O(n)` | Search a name in an unsorted list |
| `O(n log n)` | Sorting a very large leaderboard by repeatedly splitting players into smaller groups and merging them back in order |
| `O(n^2)` | Compare every candidate with every other candidate |
| `O(2^n)` | Trying every possible combination of items in a bag |
| `O(n!)` | Arranging people in every possible order |

#### 4. Code patterns

`O(1)`:

```python
x = arr[0]
```

`O(log n)`:

```python
while n > 1:
    n //= 2
```

`O(n)`:

```python
for x in arr:
    print(x)
```

`O(n log n)`:

```python
def merge_sort(arr):
    # split into halves and merge sorted halves
    ...
```

`O(n^2)`:

```python
for i in arr:
    for j in arr:
        print(i, j)
```

`O(2^n)`:

```python
def count_subsets(items):
    ...
```

`O(n!)`:

```python
def count_permutations(items):
    ...
```

#### 5. Common mistakes

- Nested loops are not always `O(n^2)`; bounds matter.
- Starting inner loop at `j = i + 1` is still `O(n^2)`.
- Binary search requires sorted input.

#### 6. Growth comparison

For `n = 10`:

```text
log n     ~ 3
n         = 10
n log n   ~ 30
n^2       = 100
2^n       = 1024
n!        = 3,628,800
```

This is why high-complexity algorithms become infeasible quickly.

#### 7. Quick model

```text
O(n)       -> scales
O(n^2)     -> starts exploding
O(2^n)     -> explodes fast
O(n!)      -> becomes infeasible very quickly
```
