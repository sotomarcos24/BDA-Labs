# Tutorial 2 - Exercise solutions


def count_between_1_and_10(data):
    count = 0
    for value in data:
        if 1 <= value <= 10:
            count += 1
    return count


def sum_even_numbers(data):
    total = 0
    for value in data:
        if value % 2 == 0:
            total += value
    return total


def first_position_of_12(data):
    for i, value in enumerate(data):
        if value == 12:
            return i
    return -1


def find_25_coordinates_user_friendly(matrix):
    for row_i, row in enumerate(matrix, start=1):
        for col_i, value in enumerate(row, start=1):
            if value == 25:
                return [row_i, col_i]
    return None


if __name__ == "__main__":
    data = [30, 6, 9, 12, 15, 8]
    matrix = [
        [5, 10, 15],
        [20, 25, 30],
    ]

    print("Count between 1 and 10:", count_between_1_and_10(data))
    print("Sum of even numbers:", sum_even_numbers(data))
    print("Position of first 12:", first_position_of_12(data))
    print("Coordinates of 25 (1-based):", find_25_coordinates_user_friendly(matrix))

    # Resetting column index is important so each new row starts from column 1.

    print("\nComplexity answers:")
    print("Task 1 (count in range): time O(n), space O(1)")
    print("Task 2 (sum even): time O(n), space O(1)")
    print("Task 3 (find first 12): time O(n), space O(1)")
    print("Task 4 (find 25 in matrix): time O(r * c), space O(1)")
