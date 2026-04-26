import csv
import os
import shutil
import subprocess

GHIBLI_FILE = "studio_ghibli_movies.csv"
GHIBLI_FALLBACK_FILE = os.path.join("data", "studio_ghibli_movies.csv")


def ensure_dataset_file(path, repo_id, repo_filename):
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

    if path != repo_filename and os.path.exists(repo_filename):
        try:
            shutil.copyfile(repo_filename, path)
        except Exception:
            return False

    return os.path.exists(path)


def resolve_ghibli_file():
    if os.path.exists(GHIBLI_FILE):
        return GHIBLI_FILE

    if ensure_dataset_file(
        GHIBLI_FILE,
        "Birkbeck/studio_ghibli_movies",
        "studio_ghibli_movies.csv",
    ):
        return GHIBLI_FILE

    if os.path.exists(GHIBLI_FALLBACK_FILE):
        return GHIBLI_FALLBACK_FILE

    raise FileNotFoundError("studio_ghibli_movies.csv not available")


def compare_reader_and_dictreader(path):
    print("Example 1 - csv.reader")
    with open(path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        first_row = next(reader)
        print("Header:", header)
        print("First title (index 1):", first_row[1])

    print("\nExample 1 - csv.DictReader")
    with open(path, "r") as file:
        reader = csv.DictReader(file)
        first_row = next(reader)
        print("Columns:", reader.fieldnames)
        print("First title (key):", first_row["title"])


def clean_ghibli_dataset(input_path, output_path):
    with open(input_path, "r") as in_file:
        reader = csv.DictReader(in_file)
        fieldnames = reader.fieldnames
        cleaned_rows = []
        missing_year_rows = []

        first_missing = None
        for row_number, row in enumerate(reader, start=2):
            for col_name, value in row.items():
                if value == "" and first_missing is None:
                    first_missing = (row_number, col_name)

            title = row.get("title", "")
            if row.get("year", "") == "":
                missing_year_rows.append({"row": row_number, "title": title})
                if title == "Kiki's Delivery Service":
                    row["year"] = "1989"
                elif title == "Ponyo":
                    row["year"] = "2008"

            if row.get("music_by", "") == "" and title == "Howl's Moving Castle":
                row["music_by"] = "Joe Hisaishi"

            cleaned_rows.append(row)

    with open(output_path, "w", newline="") as out_file:
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    print("\nExercise - Missing cell and cleaned output")
    if first_missing:
        print(f"First missing cell: row {first_missing[0]}, column '{first_missing[1]}'")
    else:
        print("No missing cells found.")
    print("Rows where year was missing:")
    for item in missing_year_rows:
        print(f"- row {item['row']}: {item['title']}")
    print(f"Saved cleaned file: {output_path}")


def save_raw_and_fix_students():
    students = [
        {"name": "Ana", "score": "85", "email": "ana@mail.com"},
        {"name": "Ben", "score": "", "email": "ben@mail.com"},
        {"name": "Cara", "score": "91", "email": ""},
    ]

    # Step 1: save raw data.
    with open("students_raw.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score", "email"])
        writer.writeheader()
        writer.writerows(students)

    # Step 2: reopen, fix missing email, save again.
    with open("students_raw.csv", "r") as in_file:
        reader = csv.DictReader(in_file)
        fixed_rows = []
        for row in reader:
            if row["email"] == "":
                row["email"] = "unknown@mail.com"
            fixed_rows.append(row)

    with open("students_fixed.csv", "w", newline="") as out_file:
        writer = csv.DictWriter(out_file, fieldnames=["name", "score", "email"])
        writer.writeheader()
        writer.writerows(fixed_rows)

    print("Saved students_raw.csv")
    print("Saved students_fixed.csv")


def main():
    try:
        ghibli_path = resolve_ghibli_file()
    except FileNotFoundError as error:
        raise SystemExit(
            f"{error}. Run: hf download Birkbeck/studio_ghibli_movies "
            "studio_ghibli_movies.csv --repo-type dataset --local-dir ."
        ) from error

    compare_reader_and_dictreader(ghibli_path)
    clean_ghibli_dataset(ghibli_path, "studio_ghibli_movies_clean.csv")

    save_raw_and_fix_students()

    print("\nComplexity notes:")
    print("- Reader/DictReader scans: time O(n), space O(1)")
    print("- Cleaning + storing rows then writing: time O(n), space O(n)")


if __name__ == "__main__":
    main()
