# Session 02 imposter quiz

## Question 1

What does `csv.DictReader(file)` return for each row?

- A dictionary keyed by column names
- A list of values only
- A tuple of typed values
- A single string per row

Answer: 1
Imposters: 2
Type: single
Time: 30
Explanation: `DictReader` maps header names to row values.

## Question 2

What is the difference between `genres == "Action"` and `"Action" in genres`?

- `==` is exact match, while `in` also matches multi-genre strings
- They always return the same result
- `in` works only for lists, not strings
- `==` is only for numbers

Answer: 1
Imposters: 2
Type: single
Time: 30
Explanation: Exact match and substring containment are different checks.

## Question 3

In `movies_incomplete.csv`, why can this fail: `int(row["votes"])`?

- Some `votes` values can be empty strings
- `DictReader` already returns integers, so casting fails
- `votes` is always a float with commas
- `int()` cannot be used inside loops

Answer: 1
Imposters: 2
Type: single
Time: 30
Explanation: Missing values are often empty strings and raise `ValueError`.

## Question 4

What should you use to write cleaned dictionary rows back to CSV?

- `csv.DictWriter`
- `csv.reader`
- `hf download`
- `quizmd`

Answer: 1
Imposters: 2
Type: single
Time: 30
Explanation: `DictWriter` writes rows using explicit field names.

## Question 5

What must be true before using binary search (`O(log n)`)?

- The data must be sorted
- The data must have unique values only
- The data must be in CSV format
- The loop must be recursive

Answer: 1
Imposters: 2
Type: single
Time: 30
Explanation: Binary search requires sorted input.
