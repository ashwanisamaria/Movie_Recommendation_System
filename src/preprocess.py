import pickle
from pathlib import Path

import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "dataset"
MODEL_DIR = BASE_DIR / "models"

MODEL_DIR.mkdir(exist_ok=True)

movies = pd.read_csv(DATASET_DIR / "movie.csv")
ratings = pd.read_csv(DATASET_DIR / "rating.csv")

merged_data = ratings.merge(
    movies,
    on="movieId"
)

movie_rating_count = (
    merged_data
    .groupby("title")["rating"]
    .count()
    .reset_index()
)

movie_rating_count.rename(
    columns={"rating": "num_ratings"},
    inplace=True
)

merged_data = merged_data.merge(
    movie_rating_count,
    on="title"
)

popular_movies = merged_data[
    merged_data["num_ratings"] >= 100
]

movie_pivot = popular_movies.pivot_table(
    index="title",
    columns="userId",
    values="rating"
)

movie_pivot.fillna(0, inplace=True)

movie_sparse_matrix = csr_matrix(movie_pivot)

model = NearestNeighbors(
    metric="cosine",
    algorithm="brute"
)

model.fit(movie_sparse_matrix)

with open(MODEL_DIR / "model.pkl", "wb") as f:
    pickle.dump(model, f)

with open(MODEL_DIR / "movie_pivot.pkl", "wb") as f:
    pickle.dump(movie_pivot, f)

print("✅ Model Saved Successfully!")