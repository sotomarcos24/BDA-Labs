### Session 2 | part 1

> In Session 2, we start working with CSV files using dictionary-style rows. This is quite different from arrays, because we can use column names as keys to access data (not indexes anymore).

#### 1. Goal

First, you will practice core CSV dictionary logic using:

- `csv.DictReader`
- key-based access (for example `row["title"]`)
- counters
- `for` loops
- `break` for first-match search

#### 2. Prerequisites

Before starting:

1. Open the `session2` folder in Visual Studio Code.
2. Create and activate your virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows (VS Code terminal):

- Create venv (recommended): `python -m venv .venv`
- Alternative on some installs: `py -m venv .venv`
- PowerShell: `.venv\Scripts\Activate.ps1` (may be blocked by execution policy on some machines)
- Command Prompt: `.venv\Scripts\activate.bat`
- If activation is blocked, run scripts directly with: `.venv\Scripts\python.exe your_script.py`
- Optional temporary PowerShell bypass (current session only):
  `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
  Then run: `.venv\Scripts\Activate.ps1`

3. Create (or open) your solution file:

```txt
session2/session_solutions/session-02-part-01.py
```

If `session_solutions/` does not exist yet, create it first.

#### 3. Basics you should know

- `csv.DictReader(file)`: reads each CSV row as a `dict` (dictionary).
- Keys come from the header row (column names).
- Values are still strings, so numeric conversion is manual when needed.
- Dictionary access is clearer than index access when column names are meaningful.

#### 4. Example 1: Read CSV rows as dictionaries

To run this tutorial, first download `movies.csv` from [Birkbeck/movies](https://huggingface.co/datasets/Birkbeck/movies):

```bash
hf download Birkbeck/movies movies.csv --repo-type dataset --local-dir .
```

On Windows PowerShell:

```powershell
hf download Birkbeck/movies movies.csv --repo-type dataset --local-dir .
```

Expected result: `movies.csv` appears in your current folder.

#### 4.1. Safe download for `movies_incomplete.csv`

Warning: `Birkbeck/movies_incomplete` can expose a file named `movies.csv`. If you download it into the same folder, you can overwrite your original `movies.csv`.

Safe flow:

1. Download incomplete data into a temporary folder:

```bash
mkdir -p tmp_incomplete
hf download Birkbeck/movies_incomplete movies.csv --repo-type dataset --local-dir tmp_incomplete
```

2. Copy/rename into your working folder:

```bash
cp tmp_incomplete/movies.csv movies_incomplete.csv
```

On Windows PowerShell:

```powershell
mkdir tmp_incomplete
hf download Birkbeck/movies_incomplete movies.csv --repo-type dataset --local-dir tmp_incomplete
Copy-Item .\tmp_incomplete\movies.csv .\movies_incomplete.csv
```

Make sure the files are in your current folder. Then run the following script.

File: `session2/session_solutions/session-02-part-01.py`

```python
import csv

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

Expected output shape:

```txt
{'movie_id': '1', 'title': 'Movie 1', 'year': '2020', ...}
{'movie_id': '2', 'title': 'Movie 2', 'year': '1994', ...}
```

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
>   <summary>Show answer</summary>
>
> Time: O(n)
>
> Space: O(1)
>
> </details>

#### 5. Example 2: Print one named column

File: `session2/session_solutions/session-02-part-01.py`

```python
import csv

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["genres"])
```

Expected output shape:

```txt
Romance
Action, Animation, Thriller
Thriller
...
```

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
>   <summary>Show answer</summary>
>
> Time: O(n)
>
> Space: O(1)
>
> </details>

#### 6. Example 3: Count rows using a counter

Count how many rows have `year == "2020"`:

File: `session2/session_solutions/session-02-part-01.py`

```python
import csv

count = 0

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["year"] == "2020":
            count += 1

print(count)
```

> [!TIP]
>
> Why do we still use a counter even with dictionaries?
>
> <details>
>   <summary>Show answer</summary>
>
> Dictionaries change how we access columns (by name), but counting logic is still loop + condition + counter.
>
> </details>

#### 7. Example 4: Find first match with `break`

Find the first row where `genres` contains `Action`:

File: `session2/session_solutions/session-02-part-01.py`

```python
import csv

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if "Action" in row["genres"]:
            print(row)
            break
```

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
>   <summary>Show answer</summary>
>
> Time: O(n) worst case
>
> Space: O(1)
>
> </details>

#### 8. Exercise

Add your answers to:

```txt
session2/session_solutions/session-02-part-01.py
```

Tasks for `Birkbeck/movies`:

1. Print the field names from `reader.fieldnames`.
2. Print only the first 5 data rows.
3. Count how many movies are from the `USA`.
4. Find and print the first movie where `genres` is exactly `Action`.
5. Find and print the first movie where `Action` appears inside `genres`.
6. In one short comment, explain one benefit of `DictReader` over `csv.reader`.
7. What are the time and space complexities of your script(s)?

Tasks for `Birkbeck/movies_incomplete`:

1. Find the missing data point and print row and column.
2. Find the average of `votes` from `movies_incomplete.csv`. Why does the naive script fail? How can you fix it?

#### 9. Quiz

Complete the following quiz.

```shell
quizmd quizzes/python-csv-dictreader-quiz.md
```

If you want to choose a theme:

```bash
quizmd --theme light quizzes/python-csv-dictreader-quiz.md
quizmd --theme dark quizzes/python-csv-dictreader-quiz.md
```

- Use `--theme light` if your terminal has a white/light background.
- Use `--theme dark` if your terminal has a dark background.

> For accessibility use this: `quizmd --no-color quizzes/python-csv-dictreader-quiz.md`

#### 10. Call Stelios

Call Stelios to challenge you with a question.

#### 11. Suggested structure and README update

Keep your session structure consistent:

```txt
session2/
  README.md
  session_solutions/
    session-02-part-01.py
    session-02-part-02.py
```

Update `README.md` after completing this tutorial.

Example update:

```md
## Files
- `session_solutions/session-02-part-01.py`
  - Goal: practice DictReader, key access, and first-match search
  - Status: completed

## Notes
- Learned to access CSV columns by name with DictReader.
- Learned to combine dictionary access with counters and break.
```
