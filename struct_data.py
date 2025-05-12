import pandas as pd
from sklearn.model_selection import train_test_split

# Load cleaned data
df = pd.read_csv("data/cleaned_data.csv")

# Aggregate duplicate user-movie pairs by taking the mean rating
df = df.groupby(['userId', 'title'], as_index=False)['rating'].mean()

# Create user-item matrix
user_movie_ratings = df.pivot(index='userId', columns='title', values='rating').fillna(0)

# Split into train/test
train, test = train_test_split(user_movie_ratings, test_size=0.2, random_state=42)

train.to_csv("data/train_matrix.csv")
test.to_csv("data/test_matrix.csv")
print("Data structured for training/testing.")
