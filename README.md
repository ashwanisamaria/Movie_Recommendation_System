# 🎬 AI Movie Recommendation System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-KNN-orange?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-black?style=for-the-badge&logo=pandas)
![TMDB](https://img.shields.io/badge/TMDB-API-green?style=for-the-badge)

</p>

---

## 📖 Overview

An AI-powered Movie Recommendation System built using **Collaborative Filtering** and **K-Nearest Neighbors (KNN)**. The application recommends movies similar to a user's selected movie based on user rating patterns.

To enhance the user experience, the system integrates the **TMDB API** to fetch movie posters, ratings, release dates, and descriptions in real time.

---

## ✨ Features

- 🎬 Movie Recommendation using Machine Learning
- 🤖 K-Nearest Neighbors (KNN) Algorithm
- ⭐ Real-time Movie Ratings
- 🖼 Movie Posters
- 📅 Release Year
- 📝 Movie Overview
- 🌐 TMDB API Integration
- 🎨 Modern Streamlit UI
- ⚡ Fast Recommendations
- 📱 Responsive Interface

---

## 🧠 Machine Learning Workflow

```
Movie Dataset
        │
        ▼
Ratings Dataset
        │
        ▼
Merge Datasets
        │
        ▼
Popularity Filtering
        │
        ▼
Pivot Table
        │
        ▼
Sparse Matrix
        │
        ▼
KNN Model Training
        │
        ▼
Movie Recommendation
```

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| Pandas | Data Processing |
| Scikit-Learn | Machine Learning |
| SciPy | Sparse Matrix |
| TMDB API | Movie Information |
| Requests | API Calls |

---

## 📂 Project Structure

```
Movie_Recommendation_System/
│
├── assets/
│   └── style.css
│
├── dataset/
│   ├── movie.csv
│   └── link.csv
│
├── src/
│   ├── model.py
│   ├── preprocess.py
│   └── tmdb.py
│
├── app.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/ashwanisamaria/Movie_Recommendation_System.git
```

### Open Project

```bash
cd Movie_Recommendation_System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Streamlit Secrets

Create the following file:

```
.streamlit/secrets.toml
```

Add your TMDB API key:

```toml
TMDB_API_KEY = "YOUR_API_KEY"
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Home Page

> *(Add screenshot here)*

---

### Recommendations

> *(Add screenshot here)*

---

### Movie Details

> *(Add screenshot here)*

---

## 📊 Dataset

This project uses the **MovieLens Dataset**.

Due to GitHub's file size limit, the large **rating.csv** file is not included in this repository.

Download the dataset from:

https://grouplens.org/datasets/movielens/

---

## 🔮 Future Improvements

- Deep Learning Recommendation Model
- Content-Based Filtering
- Hybrid Recommendation System
- User Login System
- Watchlist Feature
- Search Suggestions
- Genre Filtering
- Trailer Integration
- User Rating System

---

## 👨‍💻 Author

**Ashwani Samaria**

- GitHub: https://github.com/ashwanisamaria

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

## 📄 License

This project is intended for educational and learning purposes.
