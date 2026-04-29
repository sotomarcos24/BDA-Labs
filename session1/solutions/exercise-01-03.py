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

#Print only the first row (header)
with open(FILE_PATH, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        break
#O(1) time, O(1) space

#Print the first 5 rows only.
with open(FILE_PATH, "r") as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        print(row)
        count += 1
        if count == 5:
            break
#O(n) time, O(1) space

#Find and print the first movie where `genres` contains `Action`, then stop.
with open(FILE_PATH, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if "Action" in row[4]: 
            print(row)
            break
#O(n) time, O(1) space

if ensure_incomplete_movies_file(INCOMPLETE_FILE_PATH):
    with open(INCOMPLETE_FILE_PATH, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        expected_columns = len(header)

        for i, row in enumerate(reader, start=1):
            if len(row) != expected_columns:
                print(f"Issue at row {i}: Missing value")
            elif "" in row:
                print(f"Missing cell at row {i}: {row}")
