import pickle
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "dataset"
MODEL_DIR = BASE_DIR / "models"

MODEL_DIR.mkdir(exist_ok=True)

CSV_PATH = DATASET_DIR / "hindi_movies.csv"


def train_content_based_model():
    print("Loading Hindi Movies Dataset...")
    df = pd.read_csv(CSV_PATH)

    # Fill NA values with empty string
    df["genre"] = df["genre"].fillna("")
    df["director"] = df["director"].fillna("")
    df["cast"] = df["cast"].fillna("")
    df["overview"] = df["overview"].fillna("")

    # Feature Engineering: Combine tags
    df["tags"] = (
        df["overview"]
        + " "
        + df["genre"]
        + " "
        + df["director"]
        + " "
        + df["cast"]
    ).apply(lambda x: x.lower())

    print("Vectorizing tags using CountVectorizer...")
    cv = CountVectorizer(max_features=5000, stop_words="english")
    vectors = cv.fit_transform(df["tags"]).toarray()

    print("Computing Cosine Similarity Matrix...")
    similarity = cosine_similarity(vectors)

    print("Saving models to models/ directory...")
    with open(MODEL_DIR / "hindi_movies.pkl", "wb") as f:
        pickle.dump(df, f)

    with open(MODEL_DIR / "similarity.pkl", "wb") as f:
        pickle.dump(similarity, f)

    print("SUCCESS: Hindi Content-Based Model Saved Successfully!")


if __name__ == "__main__":
    train_content_based_model()