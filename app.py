from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
model_path = 'models/recommender_model.pkl'
movies_path = 'movies.csv'

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print('Model loaded successfully!')
except Exception as e:
    print(f'Error loading model: {e}')

# Load movies data
try:
    movies = pd.read_csv(movies_path)
    print('Movies data loaded successfully!')
except Exception as e:
    print(f'Error loading movies data: {e}')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        genres = request.form['genres'].split(',')
        user_id = 1  # Default user ID for testing

        # Filter movies by genres
        filtered_movies = movies[movies['genres'].str.contains('|'.join(genres), case=False, na=False)]
        recommendations = []

        # Get predictions
        for _, movie in filtered_movies.iterrows():
            try:
                prediction = model.predict(user_id, movie['movieId']).est
                recommendations.append((movie['title'], prediction))
            except Exception:
                continue

        # Sort by predicted rating
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return render_template('recommend.html', recommendations=recommendations[:5])
    except Exception as e:
        return f'Error generating recommendations: {e}'

if __name__ == '__main__':
    app.run(debug=True)
