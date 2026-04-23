import csv
from io import StringIO

import requests

url = "https://huggingface.co/datasets/Birkbeck/movies/resolve/main/movies.csv"
response = requests.get(url, timeout=30)
response.raise_for_status()

reader = csv.reader(StringIO(response.text))
for i, row in enumerate(reader):
    if i == 5:
        break
    print(row)
