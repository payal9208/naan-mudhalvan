from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load movies data
movies_path = "movies.csv"

try:
    movies = pd.read_csv(movies_path)
    print("Movies data loaded successfully!")
except Exception as e:
    print(f"Error loading movies data: {e}")
    movies = pd.DataFrame()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        genres = request.form["genres"].strip()

        if not genres:
            return "Please enter a genre."

        # Filter movies based on selected genre
        filtered_movies = movies[
            movies["genres"].str.contains(
                genres,
                case=False,
                na=False
            )
        ]

        # Take first 5 matching movies
        recommendations = filtered_movies[
            ["title", "genres"]
        ].head(5).values.tolist()

        return render_template(
            "recommend.html",
            recommendations=recommendations
        )

    except Exception as e:
        return f"Error generating recommendations: {e}"

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
