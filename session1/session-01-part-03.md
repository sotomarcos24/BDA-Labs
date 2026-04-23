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

3. Confirm dependencies are installed:

```bash
pip install -r requirements.txt
```

For this tutorial, the `hf` command requires `huggingface_hub`.
Make sure your `requirements.txt` includes:

```txt
huggingface_hub
```

4. Create (or open) your solution file:

```txt
session1/session_solutions/session-01-part-03.py
```

If `session_solutions/` does not exist yet, create it first (see Part 1).

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

Download the dataset file:

```bash
hf download Birkbeck/movies movies.csv \
  --repo-type dataset \
  --local-dir .
```

On Windows PowerShell, run the same command in one line:

```powershell
hf download Birkbeck/movies movies.csv --repo-type dataset --local-dir .
```

Optional: if the download fails due to environment/access limits, run `hf auth login` and try again.

Expected result: `movies.csv` appears in your current folder.

#### 5. First CSV read example

Let's load the file in the computer memory. This prints each CSV row as a Python list.

```python
import csv

with open("movies.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Example output shape:

```txt
['movie_id', 'title', 'year', ...]
['1', 'Movie 1', '2020', ...]
['2', 'Movie 2', '1994', '144', ...]
```

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

#### 6. Inspect reader and specific columns

Check what `reader` is:

```python
import csv

with open("movies.csv", "r") as file:
    reader = csv.reader(file)
    print(reader)
```

Example output:

```txt
<_csv.reader object at 0x...>
```

Print the `genres` column (index `4`):

```python
import csv

with open("movies.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[4])
```

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

Write all answers in:

```txt
session1/session_solutions/session-01-part-03.py
```

Tasks:

1. Print the first row only (header).
2. Print the first 5 rows only.
3. Find and print the first movie where `genres == 'Action'`, then stop.
4. Note one benefit and one limitation of using raw `csv.reader`.
5. What are the time and space complexities of your script(s)?

#### 8. Exercise 2

Use the [dataset here](https://huggingface.co/datasets/Birkbeck/movies_incomplete). There is a small issue with a missing record, can you find it? Where is it (row/column).

> [!IMPORTANT]
>
> This dataset can also expose a file named `movies.csv`. If you download it into the same folder, you can overwrite your original `movies.csv`.

Safe download flow:

1. Download incomplete data into a temporary folder:

```bash
mkdir -p tmp_incomplete
hf download Birkbeck/movies_incomplete movies.csv --repo-type dataset --local-dir tmp_incomplete
```

2. Copy/rename it into your working folder:

```bash
cp tmp_incomplete/movies.csv movies_incomplete.csv
```

On Windows PowerShell:

```powershell
mkdir tmp_incomplete
hf download Birkbeck/movies_incomplete movies.csv --repo-type dataset --local-dir tmp_incomplete
Copy-Item .\tmp_incomplete\movies.csv .\movies_incomplete.csv
```

