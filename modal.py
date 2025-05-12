import pickle
import pandas as pd

# Load the model
try:
    with open("models/recommender_model.pkl", "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading the model:", e)

# Load the movies data
try:
    movies = pd.read_csv("movies.csv")
    print("Movies data loaded successfully!")
except Exception as e:
    print("Error loading movies data:", e)

# Function to get movie recommendations based on genres
def recommend_movies_by_genre(user_id, selected_genres, num_recommendations=5):
    try:
        # Filter movies based on genres
        filtered_movies = movies[movies['genres'].str.contains('|'.join(selected_genres), case=False, na=False)]
        
        predictions = []
        for _, row in filtered_movies.iterrows():
            movie_id = row['movieId']
            title = row['title']
            pred = model.predict(uid=user_id, iid=movie_id)
            predictions.append((title, pred.est))

        # Sort the predictions by estimated rating in descending order
        top_recommendations = sorted(predictions, key=lambda x: x[1], reverse=True)[:num_recommendations]

        print(f"\nTop {num_recommendations} recommendations for User {user_id} based on genres {selected_genres}:")
        for title, rating in top_recommendations:
            print(f"Movie: {title}, Predicted Rating: {rating:.2f}")

    except Exception as e:
        print("Error generating recommendations:", e)

# Get user input for genres
print("\nEnter your preferred genres (comma-separated, e.g., Comedy,Action): ")
user_genres = input("Genres: ").split(',')

# Example usage
recommend_movies_by_genre(user_id=1, selected_genres=user_genres, num_recommendations=5)
