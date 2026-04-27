# Python CSV Reader and Dataset Processing Quiz

## Question 1

What does `csv.reader(file)` return?

- A list of strings for each row
- A dictionary for each row
- A single string
- A DataFrame

Answer: 1
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
- reader["genres"]
- row[4]

Answer: 4
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
- It uses too much memory
- It only works on Windows
- It requires index-based access

Answer: 4
Type: single
Time: 45
Explanation: `csv.reader` uses indexes, which makes code less readable compared to named access.

## Question 8

What is the space complexity when loading the entire CSV file into a list?

- O(1)
- O(log n)
- O(n)
- O(n²)
  
Answer: 3
Type: single
Time: 45
Explanation: All rows are stored in memory, so space grows linearly with input size.

## Question 9

What is the space complexity when reading sequentially without storing rows?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 1
Type: single
Time: 45
Explanation: Rows are processed one at a time without storing them, so space is O(1).

## Question 10

What is the space complexity when counting rows without storing them?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 1
Type: single
Time: 45
Explanation: Only a counter variable is used, no extra storage is required.

## Question 11

What is the time complexity when filtering rows based on a condition (e.g. age > 30)?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 3
Type: single
Time: 45
Explanation: Every row must be checked against the condition.

## Question 12

What is the time complexity when removing duplicate rows using a nested loop approach?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 4
Type: single
Time: 45
Explanation: Each row is compared with every other row to detect duplicates.

## Question 13

What is the space complexity when storing all pairwise combinations of rows from a CSV file?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 4
Type: single
Time: 45
Explanation: All pairs of rows are stored, leading to n² combinations.

## Question 14

What is the time complexity of reading only the first row of a CSV file?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 1
Type: single
Time: 45
Explanation: Only one row is read, so the operation takes constant time.

## Question 15

What is the time complexity when checking if a CSV file is empty?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 1
Type: single
Time: 45
Explanation: Only the first read attempt is needed to determine if the file has any rows 😄.

## Question 16

What is the purpose of the `hf download` command?

- To run Python scripts
- To install packages
- To download datasets from anywhere
- To download datasets from Hugging Face

Answer: 4
Type: single
Time: 45
Explanation: `hf download` retrieves dataset files from Hugging Face repositories.
