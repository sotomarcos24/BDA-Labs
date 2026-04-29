import csv

# with open("movies.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

# with open("movies.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["genres"])

#count = 0

# with open("movies.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row["year"] == "2020":
#             count += 1

# print(count)

# with open("movies.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if "Action" in row["genres"]:
#             print(row)
#             break

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    
    # Print the fieldnames
    print(f"Feild names: {reader.fieldnames}")
    
    # Print the first 5 rows
    print("First 5 data rows:")
    for i, row in enumerate(reader):
        print(row)
        if i == 4:
            break
   
    # Number of movies that are form USA
    count1 = 0
    for row in reader:
        if row["country"] == "USA":
            count1 += 1
    print(f"Number of movies from USA: {count1}")
   
    # First Action movie
    for row in reader:
        if row["genres"] == "Action":
            print(f"First Action movie is: {row}")
            break
    # Its easier to acces the column values
    # Time complexity: O(n)
    # Space complexity: O(1)

# Find the missing data
with open("movies_incomplete.csv", "r") as file:
    incomplete_reader = csv.DictReader(file)
    for i, row in enumerate(incomplete_reader):
        for key, value in row.items():
            if value == "":
                print(f"There is a missing value in the row {i} and column {key}")

# The average of votes
with open("movies_incomplete.csv", "r") as file:
    incomplete_reader = csv.DictReader(file)
    row_count = 0
    votes_sum = 0
    for row in incomplete_reader:
        try:
            votes_sum += float(row["votes"])
            row_count += 1
        except:
            continue
    print(f"The average of votes is: {votes_sum/row_count}")


