import pandas as pd

movies = pd.read_json("datasets/Movies.json")

# Print the first 5 rows, the last 3 rows, and the number of rows and columns.
print(movies.head())
print(movies.tail(3))

# Print the data type of each column and summary statistics for numeric columns.
print(movies.describe())
print(movies.info)

# Print only the Title, Release Date, and IMDB Rating columns.
print(movies[["Title", "Release Date", "IMDB Rating"]])

# Filter and print movies with IMDB Rating greater than or equal to 8.
rating_filter = movies[movies["IMDB Rating"] >= 8]
print(rating_filter)

# Create a new column called Long Movie that is True when Running Time min is greater than or equal to 120.
movies["Long Movie"] = movies["Running Time min"] >= 120
print(movies["Long Movie"])

# Count the number of movies per Major Genre.
print(movies.groupby("Major Genre").count())

# Sort by IMDB Rating, print the top 10 rows, and add a short comment explaining why inspecting the schema is useful before cleaning data.
rating_sort = movies["IMDB Rating"].sort_values(ascending=False)
print(rating_sort.head(10))