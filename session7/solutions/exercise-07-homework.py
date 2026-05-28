import pandas as pd

pokemon = pd.read_csv("datasets/Pokemon.csv", encoding="cp1252")

# Print the first 10 rows and the last 5 rows.
print(pokemon.head(10))
print(pokemon.tail(5))

# Print the number of rows and columns.
print(pokemon.shape)

# Print the column names and data types.
print(pokemon.columns)

# Rename the columns so they are easier to use in Python
pokemon = pokemon.rename(columns={"#" : "pokemon_id", "Name" : "name", "Type 1" : "type_1", "Type 2" : "type_2", "Total" : "total", "HP" : "hp", "Attack" : "attack", "Defense" : "defense", "Sp. Atk" : "sp_atk", "Sp. Def" : "sp_def", "Speed" : "speed", "Stage" : "stage", "Legendary" : "legendary"})
print(pokemon.columns)

# Check missing values in every column. Fill missing type_2 values with "None".
print(pokemon.isnull().sum())
pokemon["type_2"] = pokemon["type_2"].fillna("None")

# Print summary statistics for the numeric columns.
print(pokemon.describe())

# Find and print:
    # the Pokemon with the highest attack
print(pokemon.loc[pokemon["attack"].idxmax()])
    # the Pokemon with the highest defense
print(pokemon.loc[pokemon["defense"].idxmax()])
    # the Pokemon with the highest speed
print(pokemon.loc[pokemon["speed"].idxmax()])


# Group by type_1 and print:
    # the number of Pokemon per type
print(pokemon.groupby("type_1").count())
    # the average total score per type, sorted from highest to lowest
    # print(pokemon["total"].groupby("type_1").mean(ascending=False))
average_total_by_type = pokemon.groupby("type_1")["total"].mean().sort_values(ascending=False)
print(average_total_by_type)

# Create a new column called power_score using this formula:
pokemon["power_score"] = pokemon["attack"] + pokemon["defense"] + pokemon["speed"]
print(pokemon[["power_score","attack","defense","speed"]])

# Then print the top 10 Pokemon by power_score
top_power = pokemon.sort_values(by="power_score", ascending=False).head(10)
print(top_power)

# save the cleaned DataFrame
pokemon.to_csv("solutions/pokemon_clean.csv", index=False)