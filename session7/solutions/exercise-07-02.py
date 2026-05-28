import pandas as pd

movies = pd.read_json("datasets/Movies.json")

# Print missing values per column.
print(movies.isnull().sum())

# Count the total number of missing cells in the DataFrame.
print(movies.isnull().sum().sum())

# Print rows where Major Genre is missing.
print(movies[movies["Major Genre"].isnull()])

# Create a copy of the DataFrame called clean_movies.
clean_movies = movies.copy()

# Fill missing Major Genre and Distributor values with missing.
movies["Distributor"] = movies["Distributor"].fillna("missing")
movies["Major Genre"] = movies["Major Genre"].fillna("missing")

# Fill missing IMDB Rating values with the mean rating in a copy.
IMDB_mean = movies["IMDB Rating values"].mean()
movies["IMDB Rating values"] = movies["IMDB Rating values"].fillna(IMDB_mean)

# Create a small scores DataFrame, use interpolation to fill missing scores, and add comments explaining one risk of mean filling and when interpolation is useful.
scores = pd.DataFrame({
    "week": [1, 2, 3, 4, 5, 6, 7],
    "score": [50, None, 70, None, 90, None, 110],
})

scores["score_interpolated"] = scores["score"].interpolate()

print(scores)