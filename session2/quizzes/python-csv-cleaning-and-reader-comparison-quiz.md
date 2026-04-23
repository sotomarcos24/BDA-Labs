# Python CSV Data Cleaning and Reader Comparison Quiz

## Question 1

What is the main difference between `csv.reader` and `csv.DictReader`?

- `csv.reader` returns dictionaries and `csv.DictReader` returns lists
- `csv.reader` uses indexes, while `csv.DictReader` uses column names
- `csv.reader` only works on Windows
- `csv.DictReader` automatically fixes missing values

Answer: 2
Type: single
Time: 45
Explanation: `csv.reader` returns rows as lists accessed by index, while `csv.DictReader` returns rows as dictionaries accessed by column name.

## Question 2

What does `csv.DictWriter(file, fieldnames=...)` do?

- Reads rows as dictionaries
- Writes rows as dictionaries using explicit column names
- Finds missing values automatically
- Converts CSV files to JSON

Answer: 2
Type: single
Time: 45
Explanation: `csv.DictWriter` is used to write rows as dictionaries with named columns.

## Question 3

How does missing data often appear in CSV files?

- As `0`
- As `None`
- As `""` (empty string)
- As `False`

Answer: 3
Type: single
Time: 45
Explanation: In this session, missing values are treated as empty strings.

## Question 4

Which of the following actions are part of the cleaning workflow in this session?

- Load data with `csv.DictReader`
- Replace missing values
- Save cleaned data back to disk
- Train a machine learning model

Answer: 1,2,3
Type: multiple
Time: 45
Explanation: The focus is on reading, cleaning, and writing CSV data, not training models.

## Question 5

Why is `DictReader` often better for readability and maintenance?

- Because it removes the need for loops
- Because column names are clearer than remembering numeric indexes
- Because it automatically validates all data
- Because it always uses less memory

Answer: 2
Type: single
Time: 45
Explanation: Using column names makes the code easier to read and maintain.

## Question 6

Why does the cleaning example first save raw data, then reopen it, and save a fixed version?

- To practice a realistic read-clean-write workflow
- To make the file larger
- To avoid using dictionaries
- To convert CSV into binary

Answer: 1
Type: single
Time: 45
Explanation: This mirrors a common workflow where raw data is loaded, cleaned, and then written back out.

## Question 7

Which dataset is used in this session?

- `Birkbeck/movies`
- `Birkbeck/movies_incomplete`
- `Birkbeck/studio_ghibli_movies`
- `Birkbeck/netflix_titles`

Answer: 3
Type: single
Time: 45
Explanation: Part 2 uses the `Birkbeck/studio_ghibli_movies` dataset.

## Question 8

Which missing field is specifically mentioned in the session tasks?

- `title` for Spirited Away
- `music_by` for Howl's Moving Castle
- `country` for Ponyo
- `director` for Totoro

Answer: 2
Type: single
Time: 45
Explanation: The task asks students to find the missing `music_by` value for `Howl's Moving Castle`.

## Question 9

What is the time and space complexity of a single-pass cleaning script that stores cleaned rows before writing?

- Time O(1), Space O(1)
- Time O(log n), Space O(1)
- Time O(n), Space O(1)
- Time O(n), Space O(n)

Answer: 4
Type: single
Time: 45
Explanation: The script scans all rows once and stores cleaned rows in memory before writing them, so time is O(n) and space is O(n).

## Question 10

Which of the following are good outputs of this session?

- A cleaned `studio_ghibli_movies_clean.csv`
- A short comparison of `csv.reader` vs `csv.DictReader`
- A report of time and space complexity
- A Hugging Face model card

Answer: 1,2,3
Type: multiple
Time: 45
Explanation: The session asks students to clean and save the dataset, compare reader styles, and report complexity.
