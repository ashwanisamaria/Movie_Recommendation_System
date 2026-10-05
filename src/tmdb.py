import streamlit as st
import requests
import re
from functools import lru_cache
from src.model import get_local_movie_details

# ============================================
# TMDB API Configuration
# ============================================

API_KEY = st.secrets.get("TMDB_API_KEY", "")
SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# ============================================
# Clean Movie Title
# ============================================

def clean_title(title):
    title = re.sub(r"\s*\(\d{4}\)$", "", title)
    title = title.strip()
    if title.endswith(", The"):
        title = "The " + title[:-5]
    elif title.endswith(", A"):
        title = "A " + title[:-3]
    elif title.endswith(", An"):
        title = "An " + title[:-4]
    title = title.replace("'", "")
    title = re.sub(r"\s+", " ", title)
    return title


# ============================================
# Live Search Function
# ============================================

def search_movie(title):
    if not API_KEY:
        return []

    try:
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
            timeout=3,
        )
        if response.status_code == 200:
            return response.json().get("results", [])
    except Exception:
        pass
    return []


# ============================================
# Movie Details (Instant Local + Live Dynamic)
# ============================================

@lru_cache(maxsize=1000)
def get_movie_details(movie_name):
    # 1. Primary: Fast & verified local dataset with official TMDB CDN images
    local_info = get_local_movie_details(movie_name)
    if local_info and local_info.get("poster"):
        return local_info

    # 2. Dynamic Fallback: Live TMDB API Search
    cleaned_name = clean_title(movie_name)
    results = search_movie(cleaned_name)

    if not results:
        simple_name = re.sub(r"[^\w\s]", "", cleaned_name)
        results = search_movie(simple_name)

    if not results:
        words = cleaned_name.split()
        if len(words) >= 3:
            short_name = " ".join(words[:3])
            results = search_movie(short_name)

    if results:
        movie = results[0]
        poster = None
        if movie.get("poster_path"):
            poster = IMAGE_URL + movie["poster_path"]

        return {
            "title": movie.get("title", movie_name),
            "poster": poster,
            "rating": movie.get("vote_average", (local_info.get("rating") if local_info else None)),
            "release_date": movie.get("release_date", (local_info.get("release_date") if local_info else None)),
            "overview": movie.get("overview", (local_info.get("overview") if local_info else None)),
            "genre": (local_info.get("genre") if local_info else "Bollywood"),
            "director": (local_info.get("director") if local_info else ""),
            "cast": (local_info.get("cast") if local_info else ""),
            "tmdb_id": movie.get("id"),
        }

    return local_info