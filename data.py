import pandas as pd
import zipfile
import urllib.request
import os

# Download MovieLens dataset
url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
filename = "ml-latest-small.zip"

urllib.request.urlretrieve(url, filename)

# Extract it
with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall("data")

print("Dataset downloaded and extracted.")
