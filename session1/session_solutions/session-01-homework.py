import csv
import os
import subprocess

FILE_PATH = "movies.csv"


def ensure_movies_file():
    if os.path.exists(FILE_PATH):
        return FILE_PATH
    try:
        subprocess.run(
            [
                "hf",
                "download",
                "Birkbeck/movies",
                "movies.csv",
                "--repo-type",
                "dataset",
                "--local-dir",
                ".",
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        pass

    if os.path.exists(FILE_PATH):
        return FILE_PATH
    raise FileNotFoundError(
        "movies.csv not found. Download it first with: "
        "hf download Birkbeck/movies movies.csv --repo-type dataset --local-dir ."
    )


def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def main():
    path = ensure_movies_file()

    with open(path, "r") as file:
        rows = list(csv.reader(file))

    header = rows[0]
    data_rows = rows[1:]

    genres_i = header.index("genres")
    rating_i = header.index("rating_imdb")
    runtime_i = header.index("runtime_min")

    # Task 2: number of rows (excluding header) and number of columns.
    print("Task 2")
    print("Rows (excluding header):", len(data_rows))
    print("Columns:", len(header))
    print()

    # Task 3: first 3 rows (including header).
    print("Task 3 - First 3 rows (including header):")
    for row in rows[:3]:
        print(row)
    print()

    # Task 4: first movie where genres contains Action.
    print("Task 4 - First movie where genres contains 'Action':")
    found_action = None
    for row in data_rows:
        if "Action" in row[genres_i]:
            found_action = row
            break
    print(found_action if found_action else "No matching movie found.")
    print()

    # Task 5: average rating_imdb.
    print("Task 5 - Average rating_imdb:")
    total_rating = 0.0
    count_rating = 0
    for row in data_rows:
        value = safe_float(row[rating_i])
        if value is None:
            continue
        total_rating += value
        count_rating += 1
    print(total_rating / count_rating if count_rating else "No valid values")
    print()

    # Task 6: average of one more numeric column (runtime_min).
    print("Task 6 - Average runtime_min:")
    total_runtime = 0.0
    count_runtime = 0
    for row in data_rows:
        value = safe_float(row[runtime_i])
        if value is None:
            continue
        total_runtime += value
        count_runtime += 1
    print(total_runtime / count_runtime if count_runtime else "No valid values")
    print()

    # Task 7: count movies with rating_imdb >= 8.0.
    print("Task 7 - Count rating_imdb >= 8.0:")
    high_rating_count = 0
    for row in data_rows:
        value = safe_float(row[rating_i])
        if value is not None and value >= 8.0:
            high_rating_count += 1
    print(high_rating_count)
    print()

    # Task 8: complexity notes.
    print("Task 8 - Complexity notes:")
    print("First-match search (Action): time O(n), space O(1)")
    print("Average computation: time O(n), space O(1)")


if __name__ == "__main__":
    main()
