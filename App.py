from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load movies data
movies = pd.read_csv("movies.csv")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    genres = request.form.get("genres", "").strip()

    if not genres:
        return "Please enter a genre."

    # Filter movies based on genre
    filtered_movies = movies[
        movies["genres"].str.contains(genres, case=False, na=False)
    ]

    # Get first 5 matching movies
    recommendations = filtered_movies["title"].head(5).tolist()

    return render_template(
        "recommend.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)
  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
