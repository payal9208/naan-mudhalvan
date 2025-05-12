import os
import pandas as pd
import numpy as np
import pickle
from surprise import SVD, Dataset, Reader, accuracy
from surprise.model_selection import train_test_split

# Specify the path to save the trained model
model_path = "models/recommender_model.pkl"

# Ensure the 'models' directory exists
os.makedirs(os.path.dirname(model_path), exist_ok=True)

# Load the dataset
print("Loading the dataset...")
try:
    # Replace with your actual data file paths
    ratings_path = "ratings.csv"
    movies_path = "movies.csv"

    ratings = pd.read_csv(ratings_path)
    movies = pd.read_csv(movies_path)

    # Merge datasets on movieId
    data = pd.merge(ratings, movies, on='movieId')
    print("Data loaded successfully!")
    print("Number of rows:", len(data))
    print(data.head())
except Exception as e:
    print("Error loading data:", e)
    exit()

# Prepare the data for the Surprise library
print("Preparing data for training...")
try:
    reader = Reader(rating_scale=(0.5, 5.0))
    surprise_data = Dataset.load_from_df(data[['userId', 'movieId', 'rating']], reader)
    trainset, testset = train_test_split(surprise_data, test_size=0.2)
    print("Data preparation completed!")
except Exception as e:
    print("Error during data preparation:", e)
    exit()

# Train the SVD model
print("Training the model...")
try:
    model = SVD()
    model.fit(trainset)
    print("Model training completed!")
except Exception as e:
    print("Error during model training:", e)
    exit()

# Evaluate the model
print("Evaluating the model...")
try:
    predictions = model.test(testset)
    rmse = accuracy.rmse(predictions)
    mae = accuracy.mae(predictions)
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE:  {mae:.4f}")
except Exception as e:
    print("Error during evaluation:", e)
    exit()

# Save the model
print("Saving the trained model...")
try:
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved successfully at: {model_path}")
except Exception as e:
    print("Error saving the model:", e)
