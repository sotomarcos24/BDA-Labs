import csv
FILE_PATH = "movies.csv"

with open(FILE_PATH, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    rows = list(reader)
    
    # Number of rows in the file (excluding the header)
    print(f"Number of rows (excluding header): {len(rows)}")
    
    #Number of columns in the file
    print(f"Number of columns: {len(header)}")
    
    # 3 first rows of the file (including the header)
    print("First 3 rows (including header):")
    print(header)
    for row in rows[:3]:
        print(row)
    
    # Find and print the first movie where `genres` contains `Action`, then stop.
    for row in rows:
        if "Action" in row[4]:
            print("First movie with Action genre:")
            print(row)
            break
    
    # Calculate and print the average rating of all movies in the file.
    sum1 = 0
    count1 = 0
    for row in rows:
        try:
            sum1 += float(row[5])
            count1 += 1
        except (ValueError, IndexError):
            pass
    print(f"Average rating: {sum1/count1}")
    
    # Calculate and print the average of the rating + metascore for all movies in the file.
    sum2 = 0
    count2 = 0
    for row in rows:
        try:
            sum2 += float(row[13])
            count2 += 1
        except (ValueError, IndexError):
            pass
    print(f"Average metascore: {sum2/count2}")

    # Count and print the number of movies with a rating greater than or equal to 0.8.
    count = 0
    for row in rows:
        try:
            if float(row[5]) >= 8.0:
                count += 1
        except (ValueError, IndexError):
            pass
    print(f"Number of movies with rating >= 8.0: {count}")


    print("First-match search time complexity: O(n) and space complexity: O(1)")
    print("Average computation time complexity: O(n) and space complexity: O(1)")