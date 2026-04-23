# Python CSV Reader and Dataset Processing Quiz

## Question 1

What does `csv.reader(file)` return?

- A dictionary for each row
- A list of strings for each row
- A single string
- A DataFrame

Answer: 2
Type: single
Time: 45
Explanation: `csv.reader` returns each row as a list of strings.

## Question 2

What is the header row in a CSV file?

- The last row of data
- A row with numeric values
- The first row containing column names
- A row used for sorting

Answer: 3
Type: single
Time: 45
Explanation: The header row is the first row and contains column names.

## Question 3

Which of the following are true about `csv.reader`?

- It returns rows as lists
- It automatically converts values to integers
- It requires manual indexing to access columns
- It skips the header automatically

Answer: 1,3
Type: multiple
Time: 45
Explanation: `csv.reader` returns lists and requires index-based access. It does not convert types or skip headers automatically.

## Question 4

How do you access the `genres` column when using `csv.reader`?

- row["genres"]
- row.genres
- row[4]
- reader["genres"]

Answer: 3
Type: single
Time: 45
Explanation: With `csv.reader`, columns are accessed by index, e.g. `row[4]`.

## Question 5

Why is using `break` useful when searching for the first match?

- It skips invalid rows
- It stops the loop after finding the first match
- It converts data types
- It removes duplicates

Answer: 2
Type: single
Time: 45
Explanation: `break` stops the loop early once the target condition is met.

## Question 6

What is the time complexity of scanning all rows in a CSV file?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 3
Type: single
Time: 45
Explanation: Each row is processed once, so the time complexity is O(n).

## Question 7

What is a limitation of using raw `csv.reader`?

- It cannot read files
- It requires index-based access instead of named columns
- It uses too much memory
- It only works on Windows

Answer: 2
Type: single
Time: 45
Explanation: `csv.reader` uses indexes, which makes code less readable compared to named access.

## Question 8

Which of the following are valid tasks in this session?

- Print the first row
- Print the first 5 rows
- Find the first movie with genre "Action"
- Train a machine learning model

Answer: 1,2,3
Type: multiple
Time: 45
Explanation: The session focuses on CSV reading, searching, and basic processing tasks.

## Question 9

What is the space complexity of reading and printing rows one by one?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 1
Type: single
Time: 45
Explanation: Rows are processed one at a time without storing them, so space is O(1).

## Question 10

What is the purpose of the `hf download` command?

- To run Python scripts
- To install packages
- To download datasets from Hugging Face
- To convert CSV to JSON

Answer: 3
Type: single
Time: 45
Explanation: `hf download` retrieves dataset files from Hugging Face repositories.
