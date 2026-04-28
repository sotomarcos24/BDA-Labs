def count_between_1_and_10(data):
    count = 0
    for item in data:
        if 1 <= item <= 10:
            count += 1
    return count

def sum_even_numbers(data):
    total = 0
    for item in data:
        if item % 2 == 0: 
            total += item
    return total

def find_value_for_key_12(data):
    if 12 in data:
        return data.index(12)
    return -1

def find_row_and_column_for_25(matrix):
    for i in matrix:
        if 25 in i:
            row = matrix.index(i)
            column = matrix[row].index(25)
            return [row + 1, column + 1]
    return None

if __name__ == "__main__":
    data = [30, 6, 9, 12, 15, 8]
    matrix = [
        [5, 10, 15],
        [20, 25, 30],
    ]

    print("Count between 1 and 10:", count_between_1_and_10(data))
    print("Sum of even numbers:", sum_even_numbers(data))
    print("Position of first 12:", find_value_for_key_12(data))
    print("Coordinates of 25 (1-based):", find_row_and_column_for_25(matrix))

    print("\nComplexity answers:")
    print("Task 1 (count in range): time O(n), space O(1)")
    print("Task 2 (sum even): time O(n), space O(1)")
    print("Task 3 (find first 12): time O(n), space O(1)")
    print("Task 4 (find 25 in matrix): time O(n*m), space O(1)")