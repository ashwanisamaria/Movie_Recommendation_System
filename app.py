import streamlit as st
from pathlib import Path

from src.model import recommend_movies, movie_pivot
from src.tmdb import get_movie_details

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
)

# ==========================================
# Load CSS
# ==========================================

def load_css():
    css_path = Path("assets/style.css")

    if css_path.exists():
        with open(css_path) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )

load_css()

# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg",
        width=180,
    )

    st.title("⚙️ Settings")

    number_of_recommendations = st.slider(
        "Recommendations",
        min_value=5,
        max_value=20,
        value=5,
    )

    st.markdown("---")

    st.markdown(
        """
### 📌 Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- TMDB API
"""
    )

    st.markdown("---")

    st.success("✅ AI Powered")

# ==========================================
# Header
# ==========================================

st.markdown(
    """
<div class="main-title">
🎬 <span>AI Movie Recommendation</span> System
</div>

<div class="subtitle">
Discover movies you'll love using Machine Learning ❤️
</div>
""",
    unsafe_allow_html=True,
)

st.divider()

st.info(
    "🎯 Get personalized movie recommendations using collaborative filtering and Machine Learning."
)

# ==========================================
# Movie Selection
# ==========================================

movie_list = sorted(movie_pivot.index.tolist())

selected_movie = st.selectbox(
    "Choose a Movie",
    movie_list,
)

# ==========================================
# Recommendation Button
# ==========================================

if st.button("🎬 Recommend Movies"):

    recommendations = recommend_movies(selected_movie)
    recommendations = recommendations[:number_of_recommendations]

    st.markdown(
        "<div class='section-title'>🎥 Recommended Movies</div>",
        unsafe_allow_html=True,
    )

    cols_per_row = 5

    for row_start in range(0, len(recommendations), cols_per_row):

        cols = st.columns(cols_per_row)

        for col, movie in zip(
            cols,
            recommendations[row_start:row_start + cols_per_row],
        ):

            with col:
                print(type(movie))
                print(movie)

                details = get_movie_details(movie)
                if details:

                    if details.get("poster"):
                        st.image(
                            details["poster"],
                            use_container_width=True,
                        )

                    st.markdown(
                        f"### {details['title']}"
                    )

                    if details.get("rating"):
                        st.write(
                            f"⭐ **Rating:** {details['rating']}/10"
                        )

                    if details.get("release_date"):
                        st.write(
                            f"📅 **Year:** {details['release_date'][:4]}"
                        )

                    if details.get("overview"):

                        overview = details["overview"]

                        if len(overview) > 120:
                            overview = overview[:120] + "..."

                        st.caption(overview)

                    st.link_button(
                        "🎬 View on TMDB",
                        f"https://www.themoviedb.org/movie/{details['tmdb_id']}",
                        use_container_width=True,
                    )

                else:

                    st.error("Movie details not found.")