# Python loops and indexing quiz

## Question 1

What is the purpose of a counter in Python loops?

- To keep the current element value for printing only
- To immediately exit the loop after one condition
- To collect all loop results into a new list
- To count how many times an event/condition occurs

Answer: 4
Type: single
Time: 45
Explanation: A counter increases or decreases to track quantity.

## Question 2

What does an index represent in a list?

- The value of the element
- The memory location
- The position of the element
- The length of the list

Answer: 3
Type: single
Time: 45
Explanation: Index refers to the position of an element in a list, starting at 0.

## Question 3

You need both the index and value while iterating through a list. Which pattern is most appropriate?

- `for item in data:`
- `if i < len(data):`
- `for i in range(len(data))`: then use `data[i]`
- `while True:` without updating an index

Answer: 3
Type: single
Time: 45
Explanation: `range(len(data))` gives valid indexes, and data[i] gives the corresponding values.

## Question 4

What does break do inside a loop?

- Skips one iteration
- Stops the loop immediately
- Restarts the loop
- Prints a value

Answer: 2
Type: single
Time: 30
Explanation: break exits the loop immediately when triggered.

## Question 5

What does range(len(data)) allow you to do?

- Modify the list
- Delete elements
- Sort the list
- Iterate over indexes of a list

Answer: 4
Type: single
Time: 45
Explanation: It lets you loop over indexes instead of values.

## Question 6

What is a nested loop?

- A loop that runs once
- A loop with a condition
- A loop inside another loop
- A loop that uses break

Answer: 3
Type: single
Time: 35
Explanation: A nested loop is a loop inside another loop.

## Question 7

Why do we reset col_index = 0 after each row in a matrix?

- To stop the program on last row
- To restart counting columns for the new row
- To delete values
- To reduce memory usage

Answer: 2
Type: single
Time: 45
Explanation: Each row starts from column 0, so the index must reset.

## Question 8

What is the time complexity of counting elements in a list using a loop?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 3
Type: single
Time: 45
Explanation: You visit each element once -> O(n).

## Question 9

What is the time complexity of traversing a matrix with nested loops?

- O(n)
- O(n²)
- O(r * c)
- O(1)

Answer: 3
Type: single
Time: 45
Explanation: You visit each row and column -> O(r * c).

## Question 10

Which of the following are good practices from the tutorial?

- Use functions for reusable logic
- Write everything in one file only
- Use counters and indexes correctly
- Reset inner loop variables when needed

Answer: 1,3,4
Type: multiple
Time: 45
Explanation: Good practice includes reusable functions, correct indexing, and resetting loop variables.
