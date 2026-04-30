# movies = [
#     {
#         "title": "Howl's Moving Castle",
#         "year": "2004",
#         "director": "Hayao Miyazaki",
#         "music_by": "",
#     },
#     {
#         "title": "Kiki's Delivery Service",
#         "year": "",
#         "director": "Hayao Miyazaki",
#         "music_by": "Joe Hisaishi",
#     },
# ]

# for i, movie in enumerate(movies, start=1):
#     for key, value in movie.items():
#         if value.strip() == "":
#             print(f"Record {i} missing field: {key}")

# for i, movie in enumerate(movies, start=1):
#     if movie["music_by"].strip() == "":
#         print(f"Record {i} missing field: music_by")
#     if movie["year"].strip() == "":
#         print(f"Record {i} missing field: year")

# if movies[0]["music_by"].strip() == "":
#     movies[0]["music_by"] = "Joe Hisaishi"

# if movies[1]["year"].strip() == "":
#     movies[1]["year"] = "1989"

# print(movies)

# original_movies = [movie.copy() for movie in movies]
# cleaned_movies = [movie.copy() for movie in movies]

# if cleaned_movies[0]["music_by"].strip() == "":
#     cleaned_movies[0]["music_by"] = "Joe Hisaishi"

# if cleaned_movies[1]["year"].strip() == "":
#     cleaned_movies[1]["year"] = "1989"

# print("Original:", original_movies)
# print("Cleaned:", cleaned_movies)

# import json

# with open("movies_clean.json", "w", encoding="utf-8") as file:
#     json.dump(cleaned_movies, file, ensure_ascii=False, indent=2)

# print("Saved: movies_clean.json")

import csv
import json

with open("studio_ghibli_movies.csv", "r") as file:
    reader = csv.DictReader(file)
    year_count = 0
    movie_count = 0
    miyazaki_count = 0
    missing_index = {}
    movies = []

    for i, movie in enumerate(reader, start=1):
        movies.append(movie)
        movie_count += 1

        for key, value in movie.items():
            if value.strip() == "":
                print(f"Record {i} missing field: {key}")
                missing_index[i] = key
                if key == "year":
                    movie[key] = "2001"
                elif key == "music_by":
                    movie[key] = "El fary"
                print(f"New {key} = {movie[key]}")

        if "Miyazaki" in movie["director"]:
            miyazaki_count += 1

        year_count += float(movie["year"].strip())
    
    print(f"The average year is {year_count/movie_count}")
    print(f"Miyazaki appears {miyazaki_count} times")

    still_missing = 0
    for index, key in missing_index.items():
        if movies[index - 1][key].strip() == "":
            still_missing += 1

    with open("studio_ghibli_movies_clean.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(movies)

    print("Saved: studio_ghibli_movies_clean.csv")

    print(f"Still missing: {still_missing}")
    print("Time complexity is O(n) and space complexity is O(n)")