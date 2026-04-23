import csv
import os
import shutil
import subprocess
import tempfile

FILE_PATH = "movies.csv"
INCOMPLETE_FILE_PATH = "movies_incomplete.csv"


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
    raise SystemExit(
        "movies.csv not found. Download it first with: "
        "hf download Birkbeck/movies movies.csv --repo-type dataset --local-dir ."
    )


def ensure_movies_incomplete_file():
    if os.path.exists(INCOMPLETE_FILE_PATH):
        return INCOMPLETE_FILE_PATH

    try:
        # Download incomplete dataset in a temporary folder to avoid overwriting movies.csv.
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
            source = os.path.join(temp_dir, "movies.csv")
            if os.path.exists(source):
                shutil.copyfile(source, INCOMPLETE_FILE_PATH)
    except Exception:
        pass

    if os.path.exists(INCOMPLETE_FILE_PATH):
        return INCOMPLETE_FILE_PATH

    raise SystemExit(
        "movies_incomplete.csv not found. Use safe flow:\n"
        "1) hf download Birkbeck/movies_incomplete movies.csv --repo-type dataset --local-dir tmp_incomplete\n"
        "2) copy/rename tmp_incomplete/movies.csv to movies_incomplete.csv"
    )


movies_file = ensure_movies_file()


# Example 1: Print rows as dictionaries.
with open(movies_file, "r") as file:
    reader = csv.DictReader(file)
    print("Example 1 - First 2 rows as dict:")
    for i, row in enumerate(reader):
        if i == 2:
            break
        print(row)

# Example 2: Print one named column.
with open(movies_file, "r") as file:
    reader = csv.DictReader(file)
    print("\nExample 2 - genres column (first 5):")
    for i, row in enumerate(reader):
        if i == 5:
            break
        print(row["genres"])

# Example 3: Counter by condition.
count_2020 = 0
with open(movies_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["year"] == "2020":
            count_2020 += 1

print("\nExample 3 - Count year == 2020:", count_2020)

# Example 4: First-match with break.
with open(movies_file, "r") as file:
    reader = csv.DictReader(file)
    print("\nExample 4 - First row containing Action:")
    for row in reader:
        if "Action" in row["genres"]:
            print(row)
            break

# Exercise tasks.
with open(movies_file, "r") as file:
    reader = csv.DictReader(file)
    print("\nTask 1 - Field names:")
    print(reader.fieldnames)

with open(movies_file, "r") as file:
    reader = csv.DictReader(file)
    print("\nTask 2 - First 5 data rows:")
    for i, row in enumerate(reader):
        if i == 5:
            break
        print(row)

usa_count = 0
with open(movies_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["country"] == "USA":
            usa_count += 1
print("\nTask 3 - country == USA count:", usa_count)

with open(movies_file, "r") as file:
    reader = csv.DictReader(file)
    print("\nTask 4 - First row where genres == Action:")
    for row in reader:
        if row["genres"] == "Action":
            print(row)
            break

with open(movies_file, "r") as file:
    reader = csv.DictReader(file)
    print("\nTask 5 - First row where Action appears in genres:")
    for row in reader:
        if "Action" in row["genres"]:
            print(row)
            break

print("\nTask 6 - Note:")
print("Benefit: clearer column access by name. Limitation: values are still strings.")

print("\nTask 7 - Complexity notes:")
print("Full scan/count task: time O(n), space O(1)")
print("First-match search: time O(n), space O(1)")

# Incomplete dataset tasks.
incomplete_file = ensure_movies_incomplete_file()

with open(incomplete_file, "r") as file:
    reader = csv.DictReader(file)
    print("\nIncomplete Task 1 - First missing cell (row/column):")
    missing_found = False
    for row_number, row in enumerate(reader, start=2):
        for col_index, (col_name, value) in enumerate(row.items(), start=1):
            if value == "":
                print(f"row {row_number}, column {col_index} ({col_name})")
                missing_found = True
                break
        if missing_found:
            break
    if not missing_found:
        print("No missing value found.")

print("\nIncomplete Task 2 - Naive average attempt for votes:")
try:
    total_votes = 0
    count_votes = 0
    with open(incomplete_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # This fails on empty values and demonstrates the bug.
            total_votes += int(row["votes"])
            count_votes += 1
    print("Naive average:", total_votes / count_votes)
except Exception as error:
    print(f"Naive conversion failed: {type(error).__name__}: {error}")
    print("Reason: some rows have empty or invalid votes values.")

print("\nIncomplete Task 2 - Fixed average of votes:")
total_votes = 0
count_votes = 0
with open(incomplete_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        value = row.get("votes", "")
        if value is None or value.strip() == "":
            continue
        try:
            total_votes += int(value)
            count_votes += 1
        except ValueError:
            continue

if count_votes:
    print(total_votes / count_votes)
else:
    print("No valid votes values found.")
