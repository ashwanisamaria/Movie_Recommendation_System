import pickle
import importlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

MODEL_PATH = MODEL_DIR / "model.pkl"
PIVOT_PATH = MODEL_DIR / "movie_pivot.pkl"


def load_models():
    """
    Load existing models.
    If they don't exist, automatically generate them.
    """

    if not MODEL_PATH.exists() or not PIVOT_PATH.exists():
        print("Models not found. Training model...")
        importlib.import_module("src.preprocess")

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(PIVOT_PATH, "rb") as f:
        movie_pivot = pickle.load(f)

    return model, movie_pivot


model, movie_pivot = load_models()


def recommend_movies(movie_name):

    if movie_name not in movie_pivot.index:
        return []

    movie_index = movie_pivot.index.get_loc(movie_name)

    distances, suggestions = model.kneighbors(
        movie_pivot.iloc[movie_index].values.reshape(1, -1),
        n_neighbors=21
    )

    recommendations = []

    for i in range(1, len(suggestions[0])):
        recommendations.append(movie_pivot.index[suggestions[0][i]])

    return recommendations