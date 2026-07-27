import streamlit as st
import requests
import re
from functools import lru_cache

# ============================================
# TMDB API
# ============================================

API_KEY = st.secrets["TMDB_API_KEY"]

SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# ============================================
# Clean Movie Title
# ============================================

def clean_title(title):

    # Remove year
    title = re.sub(r"\s*\(\d{4}\)$", "", title)

    title = title.strip()

    # Batman, The -> The Batman
    if title.endswith(", The"):
        title = "The " + title[:-5]

    elif title.endswith(", A"):
        title = "A " + title[:-3]

    elif title.endswith(", An"):
        title = "An " + title[:-4]

    # Remove apostrophes
    title = title.replace("'", "")

    # Remove extra spaces
    title = re.sub(r"\s+", " ", title)

    return title


# ============================================
# Search Function
# ============================================

def search_movie(title):

    response = requests.get(

        SEARCH_URL,

        params={
            "api_key": API_KEY,
            "query": title,
            "include_adult": False,
        },

        headers={
            "User-Agent": "Mozilla/5.0"
        },

        timeout=15,
    )

    response.raise_for_status()

    return response.json().get("results", [])


# ============================================
# Movie Details
# ============================================

@lru_cache(maxsize=1000)
def get_movie_details(movie_name):

    movie_name = clean_title(movie_name)

    try:

        # First Search
        results = search_movie(movie_name)

        # Second Search (remove punctuation)
        if not results:

            simple_name = re.sub(
                r"[^\w\s]",
                "",
                movie_name
            )

            results = search_movie(simple_name)

        # Third Search (first 3 words)

        if not results:

            words = movie_name.split()

            if len(words) >= 3:

                short_name = " ".join(words[:3])

                results = search_movie(short_name)

        if not results:

            return None

        movie = results[0]

        poster = None

        if movie.get("poster_path"):

            poster = IMAGE_URL + movie["poster_path"]

        return {

            "title": movie.get("title", movie_name),

            "poster": poster,

            "rating": movie.get("vote_average"),

            "release_date": movie.get("release_date"),

            "overview": movie.get("overview"),

            "tmdb_id": movie.get("id"),

        }

    except requests.exceptions.RequestException as e:

        print("TMDB Error:", e)

        return None