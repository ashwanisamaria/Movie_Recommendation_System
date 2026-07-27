import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

with open(MODEL_DIR / "model.pkl", "rb") as f:
    model = pickle.load(f)

with open(MODEL_DIR / "movie_pivot.pkl", "rb") as f:
    movie_pivot = pickle.load(f)


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
        recommendations.append(
            movie_pivot.index[suggestions[0][i]]
        )

    return recommendations