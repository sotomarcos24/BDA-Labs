import numpy as np
import pandas as pd

# Create an array called scores with at least 8 numeric values.
scores = np.array([10,20,30,40,50,60,70,80,90,100])

# Print the array, shape, and data type.
print(scores)
print(scores.shape)
print(scores.dtype)

# Print the mean, minimum, maximum, and standard deviation.
print(np.mean(scores))
print(np.min(scores))
print(np.max(scores))
print(np.std(scores))

# Create a new array called scores_plus_10, then filter and print only scores greater than or equal to 80.
scores_plus_10 = scores + 10
scores_80 = scores[scores >= 80]
print(scores_80)

# Create an array with numbers from 1 to 20, then print only the even numbers.
scores_to_20 = np.arange(1, 21)
print(scores_to_20)

# Create a 3 by 3 matrix, print its shape, print the first row, and print the second column.
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
print(matrix.shape)
print(matrix[0])
print(matrix[:, 1])

# Load Pokemon.csv with pandas, convert the Attack column to a NumPy array, print the average attack, 
pokemon = pd.read_csv("datasets/Pokemon.csv", encoding="cp1252")
attack_values = pokemon["Attack"].to_numpy()
print(np.mean(attack_values))

# print attack values greater than or equal to 120, and add a short comment explaining one difference between a Python list and a NumPy array.
attack_120 = attack_values[attack_values >= 120]
print(attack_120)