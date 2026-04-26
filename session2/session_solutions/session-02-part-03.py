def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_with_iterations(data, target):
    left = 0
    right = len(data) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if data[mid] == target:
            return mid, iterations
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, iterations


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


def count_pairs(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                count += 1
    return count


def count_pairs_no_duplicates(data):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            count += 1
    return count


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def permute_count(data):
    if len(data) <= 1:
        return 1

    total = 0
    for i in range(len(data)):
        rest = data[:i] + data[i + 1 :]
        total += permute_count(rest)
    return total


if __name__ == "__main__":
    nums = [2, 5, 8, 12, 16, 23, 38, 56, 72]
    sample = [10, 20, 30, 40]

    print("Example outputs:")
    print("binary_search:", binary_search(nums, 23))
    print("merge_sort:", merge_sort([7, 2, 9, 1, 5, 3]))
    print("count_pairs:", count_pairs(sample))
    print("fib(6):", fib(6))
    print("permute_count([1, 2, 3, 4]):", permute_count([1, 2, 3, 4]))

    print("\nComplexity one-liners:")
    print("binary_search is O(log n) because each loop halves the remaining search range.")
    print("merge_sort is O(n log n) because it splits by depth log n and merges n work per level.")
    print("count_pairs is O(n^2) because nested loops scale with n * n.")
    print("fib recursion is O(2^n) due to two recursive branches at most levels.")
    print("permute_count is O(n!) conceptually; this version is closer to O(n * n!) due to slicing.")

    index, loops = binary_search_with_iterations(nums, 23)
    print("\nTask 3 - binary_search with iteration count:")
    print("index:", index, "iterations:", loops)

    original_pairs = count_pairs(sample)
    unique_pairs = count_pairs_no_duplicates(sample)
    print("\nTask 4 - count_pairs with inner loop from i + 1:")
    print("original count_pairs:", original_pairs)
    print("count_pairs_no_duplicates:", unique_pairs)
    print("Effect: avoids mirrored duplicates and self-pairs, so constant work decreases.")

    print("\nTask 5 - Growth ranking (smallest to largest):")
    print("O(log n) < O(n log n) < O(n^2) < O(2^n) < O(n!)")
