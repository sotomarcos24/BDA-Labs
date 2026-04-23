# Complexity intuition quiz (real-life patterns)

## Question 1

Looking for a word in a book page by page:

Hint: you may need to inspect each page in order.

- O(1)
- O(log n)
- O(n)
- O(n^2)

Answer: 3
Type: single
Time: 25
Explanation: Page-by-page scanning is linear in the number of pages.

## Question 2

Finding one student in an unsorted attendance list:

Hint: no sorted structure to skip ahead.

- O(1)
- O(n)
- O(n log n)
- O(2^n)

Answer: 2
Type: single
Time: 25
Explanation: In the worst case, you scan the full list once.

## Question 3

Comparing each candidate resume with every other candidate:

Hint: think nested comparisons.

- O(log n)
- O(n)
- O(n^2)
- O(n!)

Answer: 3
Type: single
Time: 25
Explanation: Pairwise comparisons across candidates are quadratic.

## Question 4

Matching socks from a mixed pile by checking each sock against others:

Hint: for each sock, scan the rest.

- O(n)
- O(n^2)
- O(n log n)
- O(2^n)

Answer: 2
Type: single
Time: 25
Explanation: This is the classic double-loop pattern.

## Question 5

Sorting files efficiently by splitting, sorting subparts, and merging:

Hint: divide and conquer.

- O(n)
- O(n^2)
- O(n log n)
- O(n!)

Answer: 3
Type: single
Time: 25
Explanation: Efficient comparison sorts with divide-and-conquer are typically O(n log n).

## Question 6

Checking whether a card exists in a sorted deck by repeatedly halving the search range:

Hint: discard half each step.

- O(log n)
- O(n)
- O(n^2)
- O(2^n)

Answer: 1
Type: single
Time: 25
Explanation: Halving the remaining search space gives logarithmic growth.

## Question 7

Trying every possible password combination in brute force:

Hint: branching possibilities grow very fast.

- O(log n)
- O(n)
- O(2^n) or worse
- O(n log n)

Answer: 3
Type: single
Time: 25
Explanation: Brute force over combinations is exponential in input length (or worse with larger alphabets/rules).

## Question 8

Naive recursive feature selection where each feature is either included or excluded:

Hint: two branches per item.

- O(n)
- O(n log n)
- O(n^2)
- O(2^n)

Answer: 4
Type: single
Time: 25
Explanation: Binary branching per feature produces an exponential search tree.

## Question 9

Trying all possible orders of n tasks:

Hint: permutations.

- O(n^2)
- O(n log n)
- O(2^n)
- O(n!)

Answer: 4
Type: single
Time: 25
Explanation: Number of orderings is n!, so exhaustive search is factorial.

## Question 10

Finding the best route by checking every possible city order:

Hint: route permutations.

- O(n)
- O(n!)
- O(n log n)
- O(log n)

Answer: 2
Type: single
Time: 25
Explanation: Checking all route orders is factorial-time brute force.

## Question 11

Rank these growth rates from smallest to largest:

Hint: think scalability for large n.

- O(n^2), O(n), O(log n), O(n log n), O(2^n), O(n!)
- O(log n), O(n), O(n log n), O(n^2), O(2^n), O(n!)
- O(log n), O(n log n), O(n), O(n^2), O(2^n), O(n!)
- O(2^n), O(n!), O(n^2), O(n log n), O(n), O(log n)

Answer: 2
Type: single
Time: 35
Explanation: Standard asymptotic ordering is log n, n, n log n, n^2, 2^n, n!.

## Question 12

Which statements are true?

Hint: focus on asymptotic growth, not small-input constants.

- Binary search requires sorted input.
- Starting inner loop at j = i + 1 always changes O(n^2) to O(n).
- O(n log n) usually scales better than O(n^2) for large inputs.
- O(n!) grows faster than O(2^n) for large n.

Answer: 1,3,4
Type: multiple
Time: 35
Explanation: 1, 3, and 4 are true; reducing duplicate pair checks usually keeps the same O(n^2) class.
