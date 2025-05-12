import pandas as pd

# Load data
movies = pd.read_csv("data/ml-latest-small/movies.csv")
ratings = pd.read_csv("data/ml-latest-small/ratings.csv")

# Merge datasets
df = pd.merge(ratings, movies, on="movieId")

# Drop unnecessary columns
df = df.drop(columns=["timestamp"])

df.to_csv("data/cleaned_data.csv", index=False)
print("Data cleaned and saved.")
