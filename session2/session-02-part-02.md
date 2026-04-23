### Session 2 | part 2

> In this part, we go deeper with `csv.DictReader` and compare it directly with `csv.reader`.

#### 1. Goal

In this tutorial, you will:

- compare `csv.reader` and `csv.DictReader`
- read CSV files and access values by index vs by column name
- clean missing values in a real dataset
- write cleaned data back to disk
- practice complexity analysis on data-cleaning workflows

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

3. Confirm dependencies are installed:

```bash
pip install -r requirements.txt
```

4. Create (or open) your solution file:

```txt
session2/session_solutions/session-02-part-02.py
```

If `session_solutions/` does not exist yet, create it first.

#### 3. Download dataset

Dataset:

- [Birkbeck/studio_ghibli_movies](https://huggingface.co/datasets/Birkbeck/studio_ghibli_movies)

Download:

```bash
hf download Birkbeck/studio_ghibli_movies studio_ghibli_movies.csv \
  --repo-type dataset \
  --local-dir .
```

On Windows PowerShell (one line):

```powershell
hf download Birkbeck/studio_ghibli_movies studio_ghibli_movies.csv --repo-type dataset --local-dir .
```

Expected result: `studio_ghibli_movies.csv` appears in your current folder.

#### 4. Basics you should know

- `csv.reader(file)`: each row is a list, so columns are accessed by index.
- `csv.DictReader(file)`: each row is a dictionary, so columns are accessed by name.
- `csv.DictWriter(file, fieldnames=...)`: writes rows as dictionaries with explicit column names.
- Missing data often appears as `""` (empty string).

#### 5. Example 1: `csv.reader` vs `csv.DictReader`

Using `csv.reader` (index-based):

```python
import csv

with open("studio_ghibli_movies.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    first_row = next(reader)
    print("Header:", header)
    print("First title (index 1):", first_row[1])
```

Using `csv.DictReader` (name-based):

```python
import csv

with open("studio_ghibli_movies.csv", "r") as file:
    reader = csv.DictReader(file)
    first_row = next(reader)
    print("Columns:", reader.fieldnames)
    print("First title (key):", first_row["title"])
```

#### 6. Example 2: Save, reopen, clean, and resave

Start with a simple in-memory list:

```python
students = [
    {"name": "Ana", "score": "85", "email": "ana@mail.com"},
    {"name": "Ben", "score": "", "email": "ben@mail.com"},
    {"name": "Cara", "score": "91", "email": ""},
]
```

Save raw data:

```python
import csv

with open("students_raw.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score", "email"])
    writer.writeheader()
    writer.writerows(students)
```

Reopen, fix missing `email`, and save again:

```python
import csv

with open("students_raw.csv", "r") as in_file:
    reader = csv.DictReader(in_file)
    fixed_rows = []

    for row in reader:
        if row["email"] == "":
            row["email"] = "unknown@mail.com"
        fixed_rows.append(row)

with open("students_fixed.csv", "w", newline="") as out_file:
    writer = csv.DictWriter(out_file, fieldnames=["name", "score", "email"])
    writer.writeheader()
    writer.writerows(fixed_rows)
```

#### 7. Exercise (data cleaning)

Add your answers to:

```txt
session2/session_solutions/session-02-part-02.py
```

Use `studio_ghibli_movies.csv`.

#### 8. Optional focus music

While you do this task, you can listen here:

- [Joe Hisaishi - Merry-Go-Round of Life](https://www.youtube.com/watch?v=2pQKqQ9sG50&list=RD2pQKqQ9sG50&start_radio=1)

Tasks:

1. Load the file with `csv.DictReader`.
2. Print all rows where `year` is missing.
3. Replace missing `year` values with the correct year (you should research and complete the correct data).
4. Find the row where `music_by` is missing (`Howl's Moving Castle`).
5. Find the composer on Wikipedia and complete `music_by` with the correct name.
6. Save the cleaned dataset as `studio_ghibli_movies_clean.csv`.
7. In a short note, compare `csv.reader` vs `csv.DictReader` for readability and maintenance.
8. Report time and space complexity of your cleaning script.

Note: the research step is intentional. The missing years/composer are not fully inferable from the CSV alone, so you are expected to use an external source (for example Wikipedia or an official filmography source).

#### 9. Quiz

Complete the following quiz.

```shell
quizmd quizzes/python-csv-cleaning-and-reader-comparison-quiz.md
```

If you want to choose a theme:

```bash
quizmd --theme light quizzes/python-csv-cleaning-and-reader-comparison-quiz.md
quizmd --theme dark quizzes/python-csv-cleaning-and-reader-comparison-quiz.md
```

- Use `--theme light` if your terminal has a white/light background.
- Use `--theme dark` if your terminal has a dark background.

> For accessibility use this: `quizmd --no-color quizzes/python-csv-cleaning-and-reader-comparison-quiz.md`

#### 10. Call Stelios

Call Stelios to challenge you with a data-cleaning edge case before moving to homework.

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
- `session_solutions/session-02-part-02.py`
  - Goal: compare reader vs DictReader and clean/write CSV data
  - Status: completed

## Notes
- Learned to use DictReader/DictWriter for clearer code.
- Learned to clean missing values and save cleaned outputs.
- Complexity summary:
  - single-pass cleaning: time O(n), space O(n)
```
