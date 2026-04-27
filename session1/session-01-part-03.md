### Session 1 | part 3

> In this part, we move from setup to real dataset processing with pure Python.

#### 1. Goal

In this tutorial, you will:

- download a dataset
- read CSV data using Python's built-in `csv` module
- practice basic data-processing tasks
- reason about time and space complexity

#### 2. Prerequisites

Before starting:

1. Open the `session1` folder in Visual Studio Code.
2. Activate your virtual environment.

3. Confirm dependencies are installed:

```bash
pip install -r requirements.txt
```

For this tutorial, the `hf` command requires `huggingface_hub`. Make sure your `requirements.txt` includes:

```txt
huggingface_hub
```

4. Create (or open) your exercise file:

```txt
session1/solutions/exercise-01-03.py
```

If `solutions/` does not exist yet, create it first (see Part 1).

#### 3. Basics you should know

- `csv` module: built-in Python module for reading/writing CSV files.
- `csv.reader(file)`: returns an iterator over rows.
- Each row is a `list` of strings.
- Header row: first row with column names.
- `break`: stops search when the first matching row is found.
- `Hugging Face`: a platform for hosting datasets and models.
- `hf` CLI: command-line tool from `huggingface_hub` used to download datasets.
- `hf download`: downloads a specific file from a dataset or model repository.

#### 4. Download the `movies.csv` dataset (public)

Dataset:

- [Dataset: Birkbeck/movies](https://huggingface.co/datasets/Birkbeck/movies)

Download the dataset file using the following command in terminal (Mac or Windows):

```bash
hf download Birkbeck/movies movies.csv --repo-type dataset --local-dir .
```

Expected result: `movies.csv` appears in your current folder.

#### 5. First CSV read example

Let's read the file row by row. This prints each CSV row as a Python list.

Run this script from the `session1` folder (where `movies.csv` was downloaded). If you run from the `bda` root, use `open("session1/movies.csv", "r")`.

File: `session1/solutions/exercise-01-03.py`

```python
import csv

with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Run the script using:
```
python solutions/exercise-01-03.py
```

Example output:

```txt
['movie_id', 'title', 'year', ...]
['1', 'Movie 1', '2020', ...]
['2', 'Movie 2', '1994', '144', ...]
```

> [!TIP]
>
> What are the time and space complexities of this operation?
>
> <details>
>   <summary>Show answer</summary>
>
>
> Time: O(n)
>
> Space: O(1)
>
> </details>

#### 6. Inspect reader and specific columns

Check what `reader` is:

File: `session1/solutions/exercise-01-03.py`

```python
import csv

with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    print(reader)
```

Example output:

```txt
<_csv.reader object at 0x...>
```

Print the `genres` column (index `4`):

File: `session1/solutions/exercise-01-03.py`

```python
import csv

with open("movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[4])
```

This script assumes all rows have at least 5 columns. To avoid errors, add a check such as `if len(row) > 4:` before accessing the column.

> [!TIP]
>
> What are the time and space complexities of the above script?
>
> <details>
>   <summary>Show answer</summary>
>
>
> Time: O(n)
>
> Space: O(1)
>
> </details>

#### 7. Exercise 1

Write all answers in your `solutions/` folder:

```txt
session1/solutions/exercise-01-03.py
```

Tasks:

1. Print only the first row (header).
2. Print the first 5 rows only.
3. Find and print the first movie where `genres` contains `Action`, then stop.
4. State one benefit and one limitation of using raw `csv.reader`.
5. What are the time and space complexities of your script(s)?

#### 8. Exercise 2

Use this file:

```txt
session1/solutions/exercise-01-03.py
```

Use the [dataset here](https://huggingface.co/datasets/Birkbeck/movies_incomplete). You will need to download the data using the appropriate `hf` command. 

There is a data issue (e.g. missing or malformed row). 
Identify:
- which row is problematic
- which column is affected
- what the issue is

This dataset may also contain a file named `movies.csv`. If you download it into the same folder, you can overwrite your original `movies.csv`.

> [!NOTE]
>
> Use `enumerate(reader)` to track row numbers and detect malformed rows.
>
> <details>
>   <summary>Show code</summary>
> 
> ```python
> for i, row in enumerate(reader):
>     if len(row) != expected_columns:
>         print(f"Issue at row {i}: {row}")
> ```
> Set `expected_columns` based on the header length.
> </details>

#### 9. Quizzes

Complete the following quiz.

```bash
quizmd quizzes/python-loops-and-indexing-quiz.md
```

Now complete the imposter quiz:

> [!NOTE]
> 
> The next quiz is an imposter quiz 🤥.
> 
> You need to identify:
> - the correct answer and
> - the answer that *looks correct but is actually wrong*.
> Read the quiz instructions before you start.
>
> Example:
>
> What is the index of `20` in `[10, 20, 30]`?
>
> Correct answer: `1`
> Imposter answer: `2` (common mistake due to misunderstanding 0-based indexing)

```bash
quizmd quizzes/python-session-01-imposter-quiz.md
```
