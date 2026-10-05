# 🎬 Bollywood Movie Recommendation System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Cosine_Similarity-orange?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-black?style=for-the-badge&logo=pandas)
![TMDB](https://img.shields.io/badge/TMDB-API-green?style=for-the-badge)

</p>

---

## 📖 Overview

An AI-powered **Bollywood Movie Recommendation System** built using **Content-Based Filtering**, **Natural Language Processing (NLP)**, and **Cosine Similarity**. The application recommends Hindi movies based on similarity in **Genre, Cast, Director, and Plot Summary**.

The system features real-time movie posters, ratings, release years, cast/director information, and comprehensive plot overviews with built-in resilience and fallback support.

---

## ✨ Features

- 🎬 Hindi / Bollywood Movie Recommendations using Machine Learning
- 🧠 NLP Feature Extraction via `CountVectorizer`
- 📐 Cosine Similarity Metric for high-accuracy recommendations
- 🎯 Prominent **Selected Movie Card** showing full details before recommendations
- ⭐ Real-time Movie Ratings & Release Years
- 🖼 High-Quality Movie Posters (TMDB + Curated Dataset fallback)
- 📝 Movie Plot Overviews, Director & Cast Details
- 🎨 Modern Streamlit Dark-Themed UI
- ⚡ Ultra-fast In-Memory Inferences

---

## 🧠 Machine Learning Workflow

```
Hindi Movies Dataset (hindi_movies.csv)
                  │
                  ▼
Feature Extraction (Overview + Genre + Director + Cast)
                  │
                  ▼
Tags Generation & Text Normalization
                  │
                  ▼
CountVectorizer (Bag of Words / 5000 Features)
                  │
                  ▼
Cosine Similarity Matrix Computation
                  │
                  ▼
Model Serialization (hindi_movies.pkl & similarity.pkl)
                  │
                  ▼
Streamlit Web Application & Interactive UI (app.py)
```

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Streamlit | Web Application & UI |
| Pandas & NumPy | Data Processing & Matrix Operations |
| Scikit-Learn | Vectorization (`CountVectorizer`) & `cosine_similarity` |
| TMDB API | Live Movie Information |
| Requests | REST API Calls |

---

## 📂 Project Structure

```
Movie_Recommendation_System/
│
├── assets/
│   ├── style.css
│   ├── homepage.png
│   └── recommendation.png
│
├── dataset/
│   ├── hindi_movies.csv
│   └── create_hindi_dataset.py
│
├── models/
│   ├── hindi_movies.pkl
│   └── similarity.pkl
│
├── src/
│   ├── model.py
│   ├── preprocess.py
│   └── tmdb.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
streamlit run app.py
```

---

## 👨‍💻 Author

**Ashwani Samaria**
