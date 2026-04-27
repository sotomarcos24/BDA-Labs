### Session 1 | Homework

> Use only pure Python and the built-in `csv` module.

#### 1. Goal

Practice dataset loading, filtering, aggregation, and complexity analysis.

#### 2. File to submit

Write your code in:

```txt
session1/solutions/exercise-01-homework.py
```

Use the same `solutions/` folder created in Part 1.

#### 3. Dataset

Use: `movies.csv` from [Birkbeck/movies](https://huggingface.co/datasets/Birkbeck/movies)

#### 4. Tasks

1. Load the dataset with `csv.reader`.
2. Print:
   - the number of data rows (excluding header)
   - the number of columns
3. Print the first 3 rows (including header).
4. Find and print the first movie where the `genres` column contains `Action`.
5. Compute and print the average of `rating_imdb` (ignore missing or invalid values).
6. Compute and print the average of one more numeric column (for example `runtime_min` or `metascore`, ignoring missing values).
7. Count how many movies have `rating_imdb >= 8.0`.
8. Report the time and space complexity for:
   - first-match search task
   - average computation task

> [!TIP]
>
> <details>
> <summary>You may find the following tips useful.</summary>
>
> - Skip the header row using `next(reader)` before processing the data.
> - Convert numeric values using `float()` or `int()` before calculations.
> - Use a counter and a running total to compute averages (`total / count`).
> - Use `break` to stop the loop once the first matching row is found.
> </details>

#### 5. Rules

- Do not use `pandas`.
- Handle invalid/missing numeric values safely.
- Keep your code readable with clear variable names.

#### 6. Suggested README update

```md
## Homework (Session 1)
- File: `solutions/exercise-01-homework.py`
- Status: completed
- Notes:
  - computed averages for rating and one additional numeric column
  - handled missing or invalid values safely during computations
```

#### 7. Share your work

Create a public GitHub repository for your homework. It is recommended to use one repository for all weekly submissions, for example: `bda-homeworks`.

Submit your work by sharing your repository link in the MS Teams channel 

(Discussion forum for this class): [MS Teams discussion forum](https://teams.microsoft.com/l/team/19%3AQLvZizpid98i6iNwF9_ee7RuoAUPC9YsOVoB3Yrq5YY1%40thread.tacv2/conversations?groupId=8b3672d8-2c38-4134-9725-3b779f03c2b0&tenantId=89d07f47-d258-463c-8700-635ffaeca38e).

This allows Stelios and the rest of the class to view and discuss your work 𐦂𖨆𐀪𖠋𐀪𐀪.
