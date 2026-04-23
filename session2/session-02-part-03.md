### Session 2 | part 3

> In this part, you will explore common algorithmic complexities with short, pure-Python examples.

#### 1. Goal

In this tutorial, you will:

- practice reading small algorithms
- connect code patterns to time complexity
- compare `O(log n)`, `O(n log n)`, `O(n^2)`, `O(2^n)`, and `O(n!)`
- answer quick complexity questions with reasoning

#### 2. Prerequisites

Before starting:

1. Open the `session2` folder in Visual Studio Code.
2. Activate your virtual environment:

```bash
source .venv/bin/activate
```

On Windows (VS Code terminal):

- PowerShell: `.venv\Scripts\Activate.ps1` (may be blocked by execution policy on some machines)
- Command Prompt: `.venv\Scripts\activate.bat`
- If activation is blocked, run scripts directly with: `.venv\Scripts\python.exe your_script.py`
- Optional temporary PowerShell bypass (current session only):
  `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
  Then run: `.venv\Scripts\Activate.ps1`

3. Create (or open) your solution file:

```txt
session2/session_solutions/session-02-part-03.py
```

#### 3. Basics you should know

- `O(log n)`: input is reduced by a constant factor each step (for example, half).
- `O(n log n)`: often appears in efficient divide-and-conquer sorting.
- `O(n^2)`: often appears with two nested loops over the same input.
- `O(2^n)`: branching recursion where each level doubles work.
- `O(n!)`: explores all permutations/orderings.

#### 4. Example 1: Binary search (`O(log n)`)

Binary search works on **sorted** data.

```python
def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


nums = [2, 5, 8, 12, 16, 23, 38, 56, 72]
print(binary_search(nums, 23))  # 5
```

> [!TIP]
>
> Why is binary search `O(log n)`?
>
> <details>
>   <summary>Show answer</summary>
>
> At each step, it removes half of the remaining search space.
> Repeated halving gives logarithmic growth.
>
> </details>

> [!TIP]
>
> What happens if the list is not sorted?
>
> <details>
>   <summary>Show answer</summary>
>
> Binary search can return wrong results because its left/right decisions
> assume sorted order.
>
> </details>

#### 5. Example 2: Merge sort shape (`O(n log n)`)

```python
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


print(merge_sort([7, 2, 9, 1, 5, 3]))
```

> [!TIP]
>
> Why is merge sort `O(n log n)`?
>
> <details>
>   <summary>Show answer</summary>
>
> The recursion depth is about `log n`, and each level processes about `n`
> total elements during merge steps.
>
> </details>

#### 6. Example 3: Nested loop count (`O(n^2)`)

```python
def count_pairs(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                count += 1
    return count


print(count_pairs([10, 20, 30, 40]))
```

> [!TIP]
>
> Why is this `O(n^2)`?
>
> <details>
>   <summary>Show answer</summary>
>
> For each outer-loop item (`n` choices), the inner loop also scans about `n`
> items.
>
> </details>

#### 7. Example 4: Fibonacci recursion (`O(2^n)`)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(6))
```

> [!TIP]
>
> Why does this grow close to `O(2^n)`?
>
> <details>
>   <summary>Show answer</summary>
>
> Most calls branch into two more calls, creating an exponential recursion tree.
>
> </details>

#### 8. Example 5: Permutation count (`O(n!)`)

```python
def permute_count(data):
    if len(data) <= 1:
        return 1

    total = 0
    for i in range(len(data)):
        rest = data[:i] + data[i + 1:]
        total += permute_count(rest)
    return total


print(permute_count([1, 2, 3, 4]))  # 24
```

> [!TIP]
>
> Why is this `O(n!)`?
>
> <details>
>   <summary>Show answer</summary>
>
> It explores every possible ordering (permutation), and there are `n!`
> permutations.
>
> </details>

#### 9. Exercise

Add your answers to:

```txt
session2/session_solutions/session-02-part-03.py
```

Tasks:

1. Run each example with a small input and note the output.
2. For each example, write one sentence explaining the complexity.
3. Modify `binary_search` to count how many loop iterations it performs.
4. Modify `count_pairs` so the inner loop starts from `i + 1`; explain the effect.
5. In a short note, rank these growth rates from smallest to largest:
   `O(log n)`, `O(n log n)`, `O(n^2)`, `O(2^n)`, `O(n!)`.

#### 10. Quiz

Before starting the quiz, please review the [computational complexity cheatsheet](./session-02-cheatsheet.md).

Complete the following quiz:

```shell
quizmd quizzes/python-complexity-patterns-quiz.md
```

If you want to choose a theme:

```bash
quizmd --theme light quizzes/python-complexity-patterns-quiz.md
quizmd --theme dark quizzes/python-complexity-patterns-quiz.md
```

- Use `--theme light` if your terminal has a white/light background.
- Use `--theme dark` if your terminal has a dark background.

> For accessibility use this: `quizmd --no-color quizzes/python-complexity-patterns-quiz.md`
