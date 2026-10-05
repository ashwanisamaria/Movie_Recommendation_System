import pickle
import importlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

MOVIES_PATH = MODEL_DIR / "hindi_movies.pkl"
SIMILARITY_PATH = MODEL_DIR / "similarity.pkl"


def load_models():
    """
    Load trained models. If they do not exist, train them automatically.
    """
    if not MOVIES_PATH.exists() or not SIMILARITY_PATH.exists():
        print("Models not found. Training model...")
        preprocess_module = importlib.import_module("src.preprocess")
        preprocess_module.train_content_based_model()

    with open(MOVIES_PATH, "rb") as f:
        movies_df = pickle.load(f)

    with open(SIMILARITY_PATH, "rb") as f:
        similarity = pickle.load(f)

    return movies_df, similarity


movies_df, similarity = load_models()


def recommend_movies(movie_name, n_recommendations=20):
    """
    Recommend similar movies using Cosine Similarity on content tags.
    """
    if movie_name not in movies_df["title"].values:
        return []

    movie_index = movies_df[movies_df["title"] == movie_name].index[0]
    distances = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []
    # Skip index 0 because it's the movie itself
    for i in distances[1:n_recommendations + 1]:
        rec_title = movies_df.iloc[i[0]]["title"]
        recommendations.append(rec_title)

    return recommendations


def get_local_movie_details(movie_name):
    """
    Get movie details directly from local dataset.
    """
    matches = movies_df[movies_df["title"] == movie_name]
    if matches.empty:
        return None

    row = matches.iloc[0]
    return {
        "title": row["title"],
        "poster": row.get("poster_url"),
        "rating": row.get("rating"),
        "release_date": str(row.get("release_year")),
        "overview": row.get("overview"),
        "genre": row.get("genre"),
        "director": row.get("director"),
        "cast": row.get("cast"),
        "tmdb_id": row.get("movie_id"),
    }