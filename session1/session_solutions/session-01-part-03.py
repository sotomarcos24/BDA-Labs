import csv
import os
import shutil
import subprocess
import tempfile

FILE_PATH = "movies.csv"
INCOMPLETE_FILE_PATH = "movies_incomplete.csv"


def ensure_dataset_file(path, repo_id, repo_filename="movies.csv"):
    if os.path.exists(path):
        return True
    try:
        subprocess.run(
            [
                "hf",
                "download",
                repo_id,
                repo_filename,
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
        return False

    # If the local target filename differs, keep both files by copying.
    if path != repo_filename and os.path.exists(repo_filename):
        try:
            shutil.copyfile(repo_filename, path)
        except Exception:
            return False

    return os.path.exists(path)


def ensure_incomplete_movies_file(path):
    if os.path.exists(path):
        return True
    try:
        # Download to a temporary directory first so we never overwrite root movies.csv.
        with tempfile.TemporaryDirectory() as temp_dir:
            subprocess.run(
                [
                    "hf",
                    "download",
                    "Birkbeck/movies_incomplete",
                    "movies.csv",
                    "--repo-type",
                    "dataset",
                    "--local-dir",
                    temp_dir,
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            source_path = os.path.join(temp_dir, "movies.csv")
            if not os.path.exists(source_path):
                return False
            shutil.copyfile(source_path, path)
    except Exception:
        return False
    return os.path.exists(path)


if not ensure_dataset_file(FILE_PATH, "Birkbeck/movies") and os.path.exists("movies_complete.csv"):
    FILE_PATH = "movies_complete.csv"

if not os.path.exists(FILE_PATH):
    raise SystemExit(
        "movies.csv not found. Run: "
        "hf download Birkbeck/movies movies.csv --repo-type dataset --local-dir ."
    )


# Task 1: Print header only
with open(FILE_PATH, "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Task 1 - Header:")
    print(header)

# Task 2: Print first 5 rows only (including header)
with open(FILE_PATH, "r") as file:
    reader = csv.reader(file)
    print("\nTask 2 - First 5 rows:")
    for i, row in enumerate(reader):
        if i == 5:
            break
        print(row)

# Task 3: Find first Action movie and stop
with open(FILE_PATH, "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    print("\nTask 3 - First Action movie:")
    for row in reader:
        if row[4] == "Action":
            print(row)
            break

print("\nTask 4 - Notes:")
print("Benefit: Built-in, simple, and lightweight for line-by-line processing.")
print("Limitation: All values are strings, so numeric conversion and validation are manual.")

print("\nTask 5 - Complexity answers:")
print("Header only: time O(1), space O(1)")
print("First 5 rows only: time O(1), space O(1)")
print("First Action search: time O(n), space O(1)")

# Exercise 2: Find missing record in incomplete dataset
if ensure_incomplete_movies_file(INCOMPLETE_FILE_PATH):
    with open(INCOMPLETE_FILE_PATH, "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        print("\nExercise 2 - Missing record location:")
        found_missing = False

        for row_number, row in enumerate(reader, start=2):
            for col_number, value in enumerate(row, start=1):
                if value == "":
                    print(
                        f"Missing cell at row {row_number}, column {col_number} ({header[col_number - 1]})"
                    )
                    found_missing = True
                    break
            if found_missing:
                break
        if not found_missing:
            print("No missing cell found.")
else:
    print("\nExercise 2 - movies_incomplete.csv not available.")
    print("Run: hf download Birkbeck/movies_incomplete movies.csv --repo-type dataset --local-dir tmp_incomplete")
    print("Then copy/rename tmp_incomplete/movies.csv to movies_incomplete.csv")

# Mini project: average rating_imdb
with open(FILE_PATH, "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    total = 0.0
    count = 0

    for row in reader:
        try:
            rating = float(row[5])
        except (ValueError, IndexError):
            continue
        total += rating
        count += 1

    print("\nMini Project - Average rating_imdb:")
    if count > 0:
        print(total / count)
    else:
        print("No valid rating values found.")

print("Mini project complexity: time O(n), space O(1)")
