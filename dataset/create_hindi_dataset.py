import csv
from pathlib import Path

BASE_DIR = Path("d:/Movie_Recommendation_System")
DATASET_DIR = BASE_DIR / "dataset"
DATASET_DIR.mkdir(exist_ok=True)

movies = [
    {
        "movie_id": 1,
        "title": "3 Idiots",
        "genre": "Comedy Drama Romance",
        "director": "Rajkumar Hirani",
        "cast": "Aamir Khan Kareena Kapoor R. Madhavan Sharman Joshi Boman Irani",
        "overview": "Two friends embark on a quest for a lost buddy while revisiting college days and recalling the memories of their friend who inspired them to think differently.",
        "rating": 8.4,
        "release_year": 2009,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNTkyOGVjMGEtNmQzZi00NzFlLTlhOWQtODYyMDc2ZGJmYzFhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 2,
        "title": "Dangal",
        "genre": "Biography Drama Sport",
        "director": "Nitesh Tiwari",
        "cast": "Aamir Khan Fatima Sana Shaikh Sanya Malhotra Sakshi Tanwar",
        "overview": "Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games in the face of societal oppression.",
        "rating": 8.3,
        "release_year": 2016,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTQ4MzQzMzM2Nl5BMl5BanBnXkFtZTgwMTQ1NzU3MDI@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 3,
        "title": "Sholay",
        "genre": "Action Adventure Drama",
        "director": "Ramesh Sippy",
        "cast": "Amitabh Bachchan Dharmendra Hema Malini Jaya Bachchan Sanjeev Kumar Amjad Khan",
        "overview": "After his family is murdered by a notorious and ruthless bandit, a former police officer enlists the services of two outlaws to capture him.",
        "rating": 8.2,
        "release_year": 1975,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMjA5NzkxNTg2MV5BMl5BanBnXkFtZTgwMDU3OTUzMDE@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 4,
        "title": "Dilwale Dulhania Le Jayenge",
        "genre": "Drama Romance Musical",
        "director": "Aditya Chopra",
        "cast": "Shah Rukh Khan Kajol Amrish Puri Anupam Kher Farida Jalal",
        "overview": "When Raj meets Simran in Europe, it isn't love at first sight but when Simran moves to India for an arranged marriage, love takes over.",
        "rating": 8.0,
        "release_year": 1995,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMDQyMmE4MDUtYTFhYy00MDkxLThhMjEtZWEwMmU2ZTgyMzJjXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 5,
        "title": "Taare Zameen Par",
        "genre": "Drama Family",
        "director": "Aamir Khan Amole Gupte",
        "cast": "Aamir Khan Darsheel Safary Tisca Chopra Vipin Sharma",
        "overview": "An eight-year-old boy is thought to be a lazy trouble-maker, until the new art teacher has the patience and compassion to discover the real problem behind his struggles in school.",
        "rating": 8.3,
        "release_year": 2007,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTY4MTUxMjQ5OV5BMl5BanBnXkFtZTcwNTUyMzg5Ng@@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 6,
        "title": "Lagaan",
        "genre": "Drama Musical Sport",
        "director": "Ashutosh Gowariker",
        "cast": "Aamir Khan Gracy Singh Rachel Shelley Paul Blackthorne",
        "overview": "The people of a small village in Victorian India stake their future on a game of cricket against their ruthless British rulers.",
        "rating": 8.1,
        "release_year": 2001,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNDYxNWUzZmYtBhY3Ny00NmVkLWI5YmUtMjcwZTk0MmRhYjQ2XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 7,
        "title": "PK",
        "genre": "Comedy Drama Sci-Fi",
        "director": "Rajkumar Hirani",
        "cast": "Aamir Khan Anushka Sharma Sushant Singh Rajput Boman Irani Saurabh Shukla",
        "overview": "An alien on Earth loses the only device he can use to communicate with his spaceship. His innocent nature and child-like questions force the country to evaluate religious dogmas.",
        "rating": 8.1,
        "release_year": 2014,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTYzOTE2NjkxN15BMl5BanBnXkFtZTgwMDgzMTg0MzE@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 8,
        "title": "Swades",
        "genre": "Drama Musical",
        "director": "Ashutosh Gowariker",
        "cast": "Shah Rukh Khan Gayatri Joshi Kishori Ballal Rajesh Vivek",
        "overview": "A successful Indian scientist who works for NASA returns to an Indian village to find his childhood nanny and rediscovers his roots.",
        "rating": 8.2,
        "release_year": 2004,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYzExOTcwNjYtOY2YyYi00YmE2LWI3NmEtMTY3NmU4YWU4YzVkXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 9,
        "title": "Chak De! India",
        "genre": "Drama Sport",
        "director": "Shimit Amin",
        "cast": "Shah Rukh Khan Vidya Malvade Sagarika Ghatge Shilpa Shukla",
        "overview": "Kabir Khan, a former hockey star accused of betraying his country, tries to redeem himself by coaching the Indian women's national hockey team to victory.",
        "rating": 8.1,
        "release_year": 2007,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMjA5MjAzOTgyN15BMl5BanBnXkFtZTcwNTI5MzkxMQ@@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 10,
        "title": "Hera Pheri",
        "genre": "Action Comedy Crime",
        "director": "Priyadarshan",
        "cast": "Akshay Kumar Suniel Shetty Paresh Rawal Tabu Om Puri",
        "overview": "Three unemployed men look for answers to all their financial problems, but when they get involved in a kidnapping cross-connection, chaos ensues.",
        "rating": 8.2,
        "release_year": 2000,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNDExMTBlZTYtZRFhYi00PRlLTgyMWUtZWI5MzY1M2ZkYjM1XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 11,
        "title": "Phir Hera Pheri",
        "genre": "Comedy Crime",
        "director": "Neeraj Vora",
        "cast": "Akshay Kumar Suniel Shetty Paresh Rawal Bipasha Basu Rimi Sen Johnny Lever",
        "overview": "Babu Bhaiya, Raju and Shyam lose all their fortune to a cunning scam artist and now must find a way to pay off a gangster.",
        "rating": 7.3,
        "release_year": 2006,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNTIwMmQwYmEtOGU4NS00MTBkLTlhMDItYTAwYWY1ODlhMWZkXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 12,
        "title": "Bhool Bhulaiyaa",
        "genre": "Comedy Horror Mystery",
        "director": "Priyadarshan",
        "cast": "Akshay Kumar Vidya Balan Ameesha Patel Shiney Ahuja Paresh Rawal",
        "overview": "An NRI and his wife decide to stay in his ancestral home, paying no heed to the warnings about ghosts. Soon, inexplicable occurrences cause him to call a psychiatrist friend to solve the mystery.",
        "rating": 7.4,
        "release_year": 2007,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNzllMmY5NWItOTkyOC00YTY3LWIwYWEtNzA3NDc1MWU5ZGU4XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 13,
        "title": "Welcome",
        "genre": "Comedy Crime Romance",
        "director": "Anees Bazmee",
        "cast": "Akshay Kumar Katrina Kaif Nana Patekar Anil Kapoor Paresh Rawal Feroz Khan",
        "overview": "A man falls in love with a beautiful woman, but later discovers that her brothers are notorious underworld gangsters who want an honest husband for their sister.",
        "rating": 7.0,
        "release_year": 2007,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTY3MjgyNTY2M15BMl5BanBnXkFtZTcwNTg5MDYyMQ@@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 14,
        "title": "Zindagi Na Milegi Dobara",
        "genre": "Adventure Comedy Drama",
        "director": "Zoya Akhtar",
        "cast": "Hrithik Roshan Farhan Akhtar Abhay Deol Katrina Kaif Kalki Koechlin",
        "overview": "Three friends decide to turn their fantasy bachelor road trip across Spain into reality, facing their inner fears and learning to embrace life.",
        "rating": 8.2,
        "release_year": 2011,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BZGFmMjM5OWMtZTRiNC00ODhlLThlYTItZDVjODMzNWVkMmRmXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 15,
        "title": "Yeh Jawaani Hai Deewani",
        "genre": "Comedy Drama Musical Romance",
        "director": "Ayan Mukerji",
        "cast": "Ranbir Kapoor Deepika Padukone Aditya Roy Kapur Kalki Koechlin",
        "overview": "Kabir and Naina bond during a trekking trip in Manali. Before Naina can express her feelings, Kabir leaves to pursue his dream career of travel journalism.",
        "rating": 7.3,
        "release_year": 2013,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNjQ5NjA4YTUtNmU1NC00M2I0LWI2NmYtNWU0OTI4NmY5MzZlXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 16,
        "title": "Barfi!",
        "genre": "Comedy Drama Romance",
        "director": "Anurag Basu",
        "cast": "Ranbir Kapoor Priyanka Chopra Ileana D'Cruz Saurabh Shukla",
        "overview": "Set in the 1970s, the story of three young people who learn that love can neither be defined nor contained by society's norms of normal and abnormal.",
        "rating": 8.1,
        "release_year": 2012,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTY5MjY0NDEyMl5BMl5BanBnXkFtZTcwMzc4MTM2OA@@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 17,
        "title": "Rockstar",
        "genre": "Drama Music Musical Romance",
        "director": "Imtiaz Ali",
        "cast": "Ranbir Kapoor Nargis Fakhri Shammi Kapoor Kumud Mishra",
        "overview": "Janardhan Jakhar chases his dream of becoming a rock star. During his journey, falling in love and heartbreak lead him to stardom and musical genius.",
        "rating": 7.7,
        "release_year": 2011,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BOTc3NzAxMjg4M15BMl5BanBnXkFtZTcwMDc2ODQwNw@@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 18,
        "title": "Kabir Singh",
        "genre": "Action Drama Romance",
        "director": "Sandeep Reddy Vanga",
        "cast": "Shahid Kapoor Kiara Advani Arjan Bajwa Suresh Oberoi",
        "overview": "Kabir Singh, a senior medical student with extreme anger management issues, goes on a self-destructive path after the love of his life is forced to marry another man.",
        "rating": 7.0,
        "release_year": 2019,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYmVkMzkwNGQtMGY2Zi00YWVhLWE0MmQtODk1ZmMwNWU0ZjQ3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 19,
        "title": "Animal",
        "genre": "Action Crime Drama",
        "director": "Sandeep Reddy Vanga",
        "cast": "Ranbir Kapoor Anil Kapoor Bobby Deol Rashmika Mandanna Triptii Dimri",
        "overview": "A son's obsessive love for his distant father leads him down a violent path of bloodshed, vengeance, and extreme brutality.",
        "rating": 6.2,
        "release_year": 2023,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMjg4YmNjOTEtYmMxOS00MTQxLTljNDQtY2VlZTU5ODljOGQ3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 20,
        "title": "Gangs of Wasseypur",
        "genre": "Action Comedy Crime Drama",
        "director": "Anurag Kashyap",
        "cast": "Manoj Bajpayee Nawazuddin Siddiqui Richa Chadha Huma Qureshi Tigmanshu Dhulia",
        "overview": "A clash between Sultan and Shahid Khan leads to the expulsion of Khan from Wasseypur, and ignites a deadly blood feud spanning three generations of coal mafia.",
        "rating": 8.2,
        "release_year": 2012,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTc5NjY4MjUwNF5BMl5BanBnXkFtZTgwODM3NzM5MzE@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 21,
        "title": "Andhadhun",
        "genre": "Comedy Crime Drama Music Mystery Thriller",
        "director": "Sriram Raghavan",
        "cast": "Ayushmann Khurrana Tabu Radhika Apte Anil Dhawan",
        "overview": "A series of mysterious events change the life of a blind pianist, who now must report a murder that he never actually saw, or did he?",
        "rating": 8.2,
        "release_year": 2018,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMWI5YjFmOGItYTMzYS00M2VmLTkwZDMtZGI4MDYyM2E0YmM4XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 22,
        "title": "Drishyam",
        "genre": "Crime Drama Mystery Thriller",
        "director": "Nishikant Kamat",
        "cast": "Ajay Devgn Tabu Shriya Saran Ishita Dutta Rajat Kapoor",
        "overview": "Desperate measures are taken by a man who tries to save his family from the dark side of the law, after they commit an unexpected crime.",
        "rating": 8.2,
        "release_year": 2015,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYmJhZmJlYTItZmZlNy00MGY0LTg0ZGMtNWFkYWU5NTA1YTNhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 23,
        "title": "Drishyam 2",
        "genre": "Crime Drama Mystery Thriller",
        "director": "Abhishek Pathak",
        "cast": "Ajay Devgn Tabu Akshaye Khanna Shriya Saran Ishita Dutta",
        "overview": "7 years after the case related to Vijay Salgaonkar and his family was closed, a series of unexpected events brings the truth to light.",
        "rating": 8.1,
        "release_year": 2022,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMjA5ZjM5OWQtYzMxNS00NzJjLWE2NjMtYTQyMWRmOTg1OTFmXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 24,
        "title": "A Wednesday",
        "genre": "Action Crime Drama Mystery Thriller",
        "director": "Neeraj Pandey",
        "cast": "Naseeruddin Shah Anupam Kher Jimmy Sheirgill Aamir Bashir",
        "overview": "A retiring police commissioner reminisces about the most astounding day of his career, when an ordinary common man held the Mumbai police hostage with a bomb threat.",
        "rating": 8.1,
        "release_year": 2008,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMjA4Nzg5Nzc5Ml5BMl5BanBnXkFtZTcwNjgyMTQ2MQ@@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 25,
        "title": "Special 26",
        "genre": "Action Crime Drama Mystery Thriller",
        "director": "Neeraj Pandey",
        "cast": "Akshay Kumar Anupam Kher Manoj Bajpayee Jimmy Sheirgill Kajal Aggarwal",
        "overview": "A team of con artists conduct fake raids to loot politicians and businessmen of their black money, posing as CBI officers.",
        "rating": 8.0,
        "release_year": 2013,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTY3NTY0MzcyMV5BMl5BanBnXkFtZTcwNTI1OTQ0OA@@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 26,
        "title": "Kahaani",
        "genre": "Mystery Thriller",
        "director": "Sujoy Ghosh",
        "cast": "Vidya Balan Parambrata Chatterjee Nawazuddin Siddiqui Saswata Chatterjee",
        "overview": "A pregnant woman's search for her missing husband brings her from London to Kolkata, but everyone she questions denies having ever met him.",
        "rating": 8.1,
        "release_year": 2012,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYzA4ZjVjMGQtYTVmOC00NzZlLWEzODQtYTFmMGY2NGNmY2Y5XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 27,
        "title": "Tumbbad",
        "genre": "Drama Fantasy Horror Mystery",
        "director": "Rahi Anil Barve Anand Gandhi",
        "cast": "Sohum Shah Jyoti Malshe Anita Date Ronjini Chakraborty",
        "overview": "A mythological story about a goddess who created the entire universe. The plot revolves around the consequences when humans build a temple for her first-born, Hastar, greed consumes all.",
        "rating": 8.2,
        "release_year": 2018,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYmQxNmU4AC00OTQ2LWE1YzgtODlhMWM5ODgxYTE1XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 28,
        "title": "Stree",
        "genre": "Comedy Horror",
        "director": "Amar Kaushik",
        "cast": "Rajkummar Rao Shraddha Kapoor Pankaj Tripathi Aparshakti Khurana Abhishek Banerjee",
        "overview": "In the small town of Chanderi, men live in fear of an evil spirit named Stree who abducts men in the night during festivals.",
        "rating": 7.5,
        "release_year": 2018,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYTY4ODgyOTMtMDVlYS00MDk5LThjYmMtZDRkYTRlMDM1ZjA5XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 29,
        "title": "Stree 2",
        "genre": "Comedy Horror",
        "director": "Amar Kaushik",
        "cast": "Rajkummar Rao Shraddha Kapoor Pankaj Tripathi Aparshakti Khurana Abhishek Banerjee",
        "overview": "After the events of Stree, the town of Chanderi is being haunted again, this time by a headless entity named Sarkata who targets progressive women.",
        "rating": 7.2,
        "release_year": 2024,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMDY3MGUwOGEtNTc4Ny00OTlhLWEyYzEtMTU0MGIzM2Q1ODFmXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 30,
        "title": "Bhediya",
        "genre": "Comedy Horror",
        "director": "Amar Kaushik",
        "cast": "Varun Dhawan Kriti Sanon Abhishek Banerjee Deepak Dobriyal",
        "overview": "Set in the forests of Arunachal, Bhaskar gets bitten by a mythical wolf and begins to transform into the shape-shifting creature.",
        "rating": 6.8,
        "release_year": 2022,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BY2FmZWY5OGMtZDFkNi00MGI0LWEzYWYtNzY5MzE3MDExZTZhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 31,
        "title": "Bajrangi Bhaijaan",
        "genre": "Action Adventure Comedy Drama",
        "director": "Kabir Khan",
        "cast": "Salman Khan Kareena Kapoor Nawazuddin Siddiqui Harshaali Malhotra",
        "overview": "An Indian man with a magnanimous heart takes a mute six-year-old Pakistani girl back to her hometown to reunite her with her family.",
        "rating": 8.1,
        "release_year": 2015,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYjJkOWRjNTYtM2IyMS00NGYwLWJkMzEtNWE5YjMyMWRjMGZhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 32,
        "title": "Sultan",
        "genre": "Action Drama Sport",
        "director": "Ali Abbas Zafar",
        "cast": "Salman Khan Anushka Sharma Randeep Hooda Amit Sadh",
        "overview": "Sultan is a classic underdog tale about a wrestler's journey, looking for a comeback by defeating all odds staked up against him.",
        "rating": 7.0,
        "release_year": 2016,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTY0ODg5NDU0OV5BMl5BanBnXkFtZTgwNjkyOTQ2ODE@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 33,
        "title": "Ek Tha Tiger",
        "genre": "Action Romance Thriller",
        "director": "Kabir Khan",
        "cast": "Salman Khan Katrina Kaif Ranvir Shorey Girish Karnad",
        "overview": "India's top spy Tiger falls in love with a Pakistani spy Zoya during an investigation in Dublin, leading to an international chase.",
        "rating": 7.1,
        "release_year": 2012,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTc3ODc4NTQ3OF5BMl5BanBnXkFtZTcwODY2ODQwNw@@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 34,
        "title": "Tiger Zinda Hai",
        "genre": "Action Adventure Thriller",
        "director": "Ali Abbas Zafar",
        "cast": "Salman Khan Katrina Kaif Sajjad Delafrooz Angad Bedi Kumud Mishra",
        "overview": "When a group of Indian and Pakistani nurses are held hostage in Iraq by a terrorist organization, secret agent Tiger reunites with Zoya on a rescue mission.",
        "rating": 6.9,
        "release_year": 2017,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYmY1NmExNmQtMGVhNS00MmJjLWI5ZWMtNGMwYmU2YmFkMjFhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 35,
        "title": "Pathaan",
        "genre": "Action Adventure Thriller",
        "director": "Siddharth Anand",
        "cast": "Shah Rukh Khan Deepika Padukone John Abraham Dimple Kapadia Ashutosh Rana",
        "overview": "An Indian RAW agent teams up with an exiled spy to stop a renegade private terrorist organisation from launching a deadly biological weapon on India.",
        "rating": 5.9,
        "release_year": 2023,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BM2QzM2UxNzktZWVlNC00OTFkLTljZmMtNmFkMzgzOTgxZTVlXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 36,
        "title": "Jawan",
        "genre": "Action Thriller",
        "director": "Atlee",
        "cast": "Shah Rukh Khan Nayanthara Vijay Sethupathi Deepika Padukone Priyamani",
        "overview": "A high-octane action thriller outlining the emotional journey of a prison warden who is set to rectify the wrongs in the society, driven by a personal vendetta.",
        "rating": 7.0,
        "release_year": 2023,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNDBhMGUwOWMtYjg3Yy00ZGZhLWEzYTAtYjI0OGZlNmVjNzRjXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 37,
        "title": "War",
        "genre": "Action Adventure Thriller",
        "director": "Siddharth Anand",
        "cast": "Hrithik Roshan Tiger Shroff Vaani Kapoor Ashutosh Rana",
        "overview": "An Indian soldier is assigned to eliminate his former mentor and boss, who has gone rogue after assassinating several top agents.",
        "rating": 6.5,
        "release_year": 2019,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNTlmNDMzOWQtYzg4Ny00OWQ0LWFhN2MtNmQ2MDczZGZhNTU5XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 38,
        "title": "Dhoom 2",
        "genre": "Action Crime Thriller",
        "director": "Sanjay Gadhvi",
        "cast": "Hrithik Roshan Abhishek Bachchan Aishwarya Rai Bachchan Uday Chopra Bipasha Basu",
        "overview": "ACP Jai Dixit and his partner Ali are called back into action to catch an elusive master of disguise thief known as Mr. A.",
        "rating": 6.6,
        "release_year": 2006,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BZmJjZTVmOTgtMmRlOS00ZWE3LWEyY2UtMGVmODU4M2E3MjE3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 39,
        "title": "Krrish",
        "genre": "Action Sci-Fi",
        "director": "Rakesh Roshan",
        "cast": "Hrithik Roshan Priyanka Chopra Naseeruddin Shah Rekha",
        "overview": "Krishna, inherits superhuman abilities from his father who was visited by an alien. He falls in love and travels to Singapore, discovering a dark conspiracy.",
        "rating": 6.4,
        "release_year": 2006,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTEwNWZhZWItZTM0MC00YWE0LWJlMTQtYmNmNTljMjE5ZTZhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 40,
        "title": "Koi... Mil Gaya",
        "genre": "Action Drama Fantasy Sci-Fi",
        "director": "Rakesh Roshan",
        "cast": "Hrithik Roshan Preity Zinta Rekha Rajat Bedi",
        "overview": "A developmentally disabled young man uses his late father's computer equipment to summon an alien spacecraft, gaining superpowers from an alien named Jadoo.",
        "rating": 7.1,
        "release_year": 2003,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BZDU1ODcyNjItMTI2Ny00ZTQ4LWE1NjItYzFmMDA4MDYwMzE3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 41,
        "title": "Queen",
        "genre": "Adventure Comedy Drama",
        "director": "Vikas Bahl",
        "cast": "Kangana Ranaut Rajkummar Rao Lisa Haydon Mish Boyko",
        "overview": "A shy, small-town Indian woman decides to go on her honeymoon to Paris and Amsterdam all by herself after her fiancé dumps her a day before the wedding.",
        "rating": 8.1,
        "release_year": 2013,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYzA4ZDQ4NjEtZmVlYS00MmMxLTk1MDYtMjU4MGI4MWQ1ZTdkXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 42,
        "title": "Jab We Met",
        "genre": "Comedy Drama Romance Musical",
        "director": "Imtiaz Ali",
        "cast": "Shahid Kapoor Kareena Kapoor Tarun Arora Dara Singh",
        "overview": "A depressed wealthy businessman's life turns around after meeting a chirpy, carefree Punjabi girl on an overnight train.",
        "rating": 7.9,
        "release_year": 2007,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYTY2NzMzMDMtYzhkYi00MWZhLWI1ODItZDI4M2U4YjQ4NDQyXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 43,
        "title": "Raazi",
        "genre": "Action Drama Thriller",
        "director": "Meghna Gulzar",
        "cast": "Alia Bhatt Vicky Kaushal Rajit Kapoor Shishir Sharma",
        "overview": "A Kashmiri woman is trained as an undercover spy and married into a Pakistani military family during the Indo-Pakistani War of 1971.",
        "rating": 7.7,
        "release_year": 2018,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BZGQ1ZWFmOGEtMDlhMy00NmE5LWI0MzktNzA0YWYzZTI1YmE3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 44,
        "title": "Uri: The Surgical Strike",
        "genre": "Action Drama War",
        "director": "Aditya Dhar",
        "cast": "Vicky Kaushal Paresh Rawal Yami Gautam Mohit Raina Kirti Kulhari",
        "overview": "Indian army special forces execute a covert strike against militant operational bases across the border to avenge a terrorist attack.",
        "rating": 8.2,
        "release_year": 2019,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMWU4ZjNlNTQtOGE2MS00NTA0LWE3NWItYWNmWNTAyZjE5N2NmXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 45,
        "title": "Sanju",
        "genre": "Biography Drama",
        "director": "Rajkumar Hirani",
        "cast": "Ranbir Kapoor Paresh Rawal Manisha Koirala Vicky Kaushal Anushka Sharma",
        "overview": "A biopic of controversial Bollywood actor Sanjay Dutt, his battle with drug addiction, his arrest, and his bond with his legendary father Sunil Dutt.",
        "rating": 7.6,
        "release_year": 2018,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMjMwMjgwMzYyNF5BMl5BanBnXkFtZTgwNTExMjE2NTM@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 46,
        "title": "Munna Bhai M.B.B.S.",
        "genre": "Comedy Drama Musical",
        "director": "Rajkumar Hirani",
        "cast": "Sanjay Dutt Arshad Warsi Gracy Singh Boman Irani Sunil Dutt",
        "overview": "A lovable gangster sets out to fulfill his father's dream of becoming a doctor, with the help of his trusty sidekick Circuit.",
        "rating": 8.1,
        "release_year": 2003,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BOGZmNWRhYWEtNmQzNy00OWVlLWExODUtNTY3YWRkZDI5YWM1XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 47,
        "title": "Lage Raho Munna Bhai",
        "genre": "Comedy Drama Musical",
        "director": "Rajkumar Hirani",
        "cast": "Sanjay Dutt Arshad Warsi Vidya Balan Boman Irani Dilip Prabhavalkar",
        "overview": "Munna Bhai encounters the spirit of Mahatma Gandhi. Through his interactions with Gandhi, he begins to practice 'Gandhigiri' to help ordinary people solve their problems.",
        "rating": 8.0,
        "release_year": 2006,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMWI5NjY0NGYtZTVlOC00MjE4LWFiNmItODk4Y2QxODNmMGM5XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 48,
        "title": "Bajirao Mastani",
        "genre": "Action Drama History Romance",
        "director": "Sanjay Leela Bhansali",
        "cast": "Ranveer Singh Deepika Padukone Priyanka Chopra Tanvi Azmi",
        "overview": "An epic romance between the Maratha general Peshwa Bajirao I and Mastani, the warrior princess of Bundelkhand.",
        "rating": 7.2,
        "release_year": 2015,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMjEzMTYyOTUzMF5BMl5BanBnXkFtZTgwOTkyOTU1NzE@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 49,
        "title": "Padmaavat",
        "genre": "Drama History Romance War",
        "director": "Sanjay Leela Bhansali",
        "cast": "Deepika Padukone Ranveer Singh Shahid Kapoor Aditi Rao Hydari",
        "overview": "Queen Padmavati is married to Rajput ruler Maharawal Ratan Singh. When the tyrannical Sultan Alauddin Khilji hears of her immense beauty, he attacks Chittor to capture her.",
        "rating": 7.1,
        "release_year": 2018,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BOGZmNTE2MWEtYmQ2NC00NjgxLWEyMjgtM2QxMzcxNmE2YmE3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 50,
        "title": "Goliyon Ki Raasleela Ram-Leela",
        "genre": "Drama Musical Romance",
        "director": "Sanjay Leela Bhansali",
        "cast": "Ranveer Singh Deepika Padukone Supriya Pathak Richa Chadha",
        "overview": "Ram and Leela love each other but cannot be together as their families have been at war for the last 500 years.",
        "rating": 6.9,
        "release_year": 2013,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNTI2MmE0OGItNzg3OS00MjY5LWE5NzktNGE5NDdlZmY2ODhmXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 51,
        "title": "Baahubali: The Beginning",
        "genre": "Action Drama Fantasy",
        "director": "S.S. Rajamouli",
        "cast": "Prabhas Rana Daggubati Anushka Shetty Tamannaah Bhatia Ramya Krishnan Sathyaraj",
        "overview": "A young man raised by tribal villagers learns of his royal heritage and embarks on a dangerous journey to rescue the queen mother of Mahishmati.",
        "rating": 8.0,
        "release_year": 2015,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYWVlMjVhZWYtNWViNC00ODFkLTk1MmItYjU1MDY5ZDdhMTU3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 52,
        "title": "Baahubali 2: The Conclusion",
        "genre": "Action Drama Fantasy",
        "director": "S.S. Rajamouli",
        "cast": "Prabhas Rana Daggubati Anushka Shetty Tamannaah Bhatia Ramya Krishnan Sathyaraj",
        "overview": "The epic conclusion revealing why Katappa killed Baahubali, and the final war between Mahendra Baahubali and the ruthless tyrant Bhallaladeva.",
        "rating": 8.2,
        "release_year": 2017,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMmMwNTA1MmUtNTc1Mi00ODljLWEzOWEtNTRhOWRkZTVhYjg3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 53,
        "title": "RRR",
        "genre": "Action Drama",
        "director": "S.S. Rajamouli",
        "cast": "N.T. Rama Rao Jr. Ram Charan Ajay Devgn Alia Bhatt Shriya Saran",
        "overview": "A tale of two legendary revolutionaries and their journey away from home before they began fighting for their country in the 1920s.",
        "rating": 7.8,
        "release_year": 2022,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BODUwNDNjYzctODUxNy00ZTA2LWIyYTEtMDc5Y2E5ZjBmNTMzXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 54,
        "title": "K.G.F: Chapter 1",
        "genre": "Action Crime Drama",
        "director": "Prashanth Neel",
        "cast": "Yash Srinidhi Shetty Ramachandra Raju Anant Nag",
        "overview": "Rocky, a fierce young man rising through the Mumbai underworld, travels to the Kolar Gold Fields disguised as a slave to assassinate a brutal tyrant.",
        "rating": 8.2,
        "release_year": 2018,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BZDNlNzBjMGUtYTA0Yy00OTI2LWJmZjMtZDYzY2VhOGIyMTE1XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 55,
        "title": "K.G.F: Chapter 2",
        "genre": "Action Crime Drama",
        "director": "Prashanth Neel",
        "cast": "Yash Sanjay Dutt Raveena Tandon Srinidhi Shetty Prakash Raj",
        "overview": "Now the king of Kolar Gold Fields, Rocky must defend his empire against deadly foes, including the bloodthirsty Adheera and the prime minister of India.",
        "rating": 8.3,
        "release_year": 2022,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNWRlNDk5NTMtMDNkOC00YWQ4LWFiMDUtODhiNTYzYWI4MGMyXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 56,
        "title": "Kantara",
        "genre": "Action Adventure Drama Mystery Thriller",
        "director": "Rishab Shetty",
        "cast": "Rishab Shetty Sapthami Gowda Kishore Achyuth Kumar",
        "overview": "When greed paves the way for betrayal and murder, a young tribal man invoking the local deity Bhoota Kola fights to protect his people's sacred forest.",
        "rating": 8.2,
        "release_year": 2022,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNjQyMDBjYjktNGQyMy00NzQ2LTk0ZjktYTkzNmNmOGVmNWNjXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 57,
        "title": "Pushpa: The Rise",
        "genre": "Action Crime Drama",
        "director": "Sukumar",
        "cast": "Allu Arjun Rashmika Mandanna Fahadh Faasil Sunil Ajay Ghosh",
        "overview": "A coolie rises through the ranks of a red sandalwood smuggling syndicate, making dangerous enemies including a ruthless police officer.",
        "rating": 7.6,
        "release_year": 2021,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMmQ4YmM3NjgtNTExNC00ZTZhLWEwZTctYjdhOWI4ZWFlMDk2XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 58,
        "title": "Kalki 2898 AD",
        "genre": "Action Adventure Sci-Fi",
        "director": "Nag Ashwin",
        "cast": "Prabhas Amitabh Bachchan Kamal Haasan Deepika Padukone Disha Patani",
        "overview": "In a post-apocalyptic world in the year 2898 AD, the immortal warrior Ashwatthama rises to protect the mother of the prophesied tenth avatar of Vishnu.",
        "rating": 7.5,
        "release_year": 2024,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNjdhZTY1NjItYmMyNy00M2VkLWI4YzEtMzk4YThmYzA5ODQ0XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 59,
        "title": "Karan Arjun",
        "genre": "Action Drama Fantasy",
        "director": "Rakesh Roshan",
        "cast": "Salman Khan Shah Rukh Khan Rakhee Gulzar Kajol Mamta Kulkarni Amrish Puri",
        "overview": "Two brothers murdered by their greedy uncle are reincarnated after their grieving mother prays to Goddess Kali for justice and revenge.",
        "rating": 6.8,
        "release_year": 1995,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BN2E2YmM2YTYtNDEzNC00MDJkLTg3ZGEtY2U4OWU4NGY5ODdhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 60,
        "title": "Kuch Kuch Hota Hai",
        "genre": "Comedy Drama Musical Romance",
        "director": "Karan Johar",
        "cast": "Shah Rukh Khan Kajol Rani Mukerji Salman Khan Sana Saeed",
        "overview": "Before dying, a mother leaves eight letters for her young daughter, instructing her to reunite her father Rahul with his college best friend Anjali.",
        "rating": 7.5,
        "release_year": 1998,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNjUyY2Q5MDktZWIzZS00NWVmLTkxOWEtNzdmYThkMGFiODljXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 61,
        "title": "Kabhi Khushi Kabhie Gham",
        "genre": "Drama Musical Romance",
        "director": "Karan Johar",
        "cast": "Shah Rukh Khan Kajol Amitabh Bachchan Jaya Bachchan Hrithik Roshan Kareena Kapoor",
        "overview": "After marrying a poor woman against his father's wishes, an adopted son is disowned and leaves for London. Years later, his younger brother sets out on a mission to bring him home.",
        "rating": 7.4,
        "release_year": 2001,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BZGQwMjg1ZjEtZTc5OC00N2MwLTg1NTYtM2ZmMmEyMDFjZGFhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 62,
        "title": "Kal Ho Naa Ho",
        "genre": "Comedy Drama Romance Musical",
        "director": "Nikkhil Advani",
        "cast": "Shah Rukh Khan Preity Zinta Saif Ali Khan Jaya Bachchan",
        "overview": "Naina, an introverted MBA student living in New York, falls in love with Aman, a charming neighbor who hides a heartbreaking secret that changes their lives forever.",
        "rating": 7.9,
        "release_year": 2003,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTQ4NTQ5MjMzN15BMl5BanBnXkFtZTcwNDQ1NzMzMQ@@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 63,
        "title": "Chup Chup Ke",
        "genre": "Comedy Drama Romance",
        "director": "Priyadarshan",
        "cast": "Shahid Kapoor Kareena Kapoor Paresh Rawal Rajpal Yadav Suniel Shetty",
        "overview": "A debt-ridden young man attempts suicide by jumping into the sea, but is rescued by fishermen. To escape moneylenders, he pretends to be deaf and mute in a wealthy Gujarati household.",
        "rating": 7.1,
        "release_year": 2006,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNmU0MGNiMTMtM2MwYS00YTMxLWEzYTAtMDQ4ZGM4OWRkYTcwXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 64,
        "title": "Dhamaal",
        "genre": "Action Adventure Comedy",
        "director": "Indra Kumar",
        "cast": "Sanjay Dutt Riteish Deshmukh Arshad Warsi Aashish Chaudhary Javed Jaffrey",
        "overview": "Four lazy friends stumble upon a dying criminal who tells them about a hidden treasure of 10 crore buried in Goa under a big W, sparking a hilarious race against a determined police inspector.",
        "rating": 7.4,
        "release_year": 2007,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTkxNTI4NzA4MF5BMl5BanBnXkFtZTcwOTY4MDcyMQ@@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 65,
        "title": "Golmaal: Fun Unlimited",
        "genre": "Action Comedy Drama",
        "director": "Rohit Shetty",
        "cast": "Ajay Devgn Arshad Warsi Sharman Joshi Tusshar Kapoor Paresh Rawal",
        "overview": "Four runaway scoundrels seek shelter in the bungalow of a blind elderly couple, pretending to be their long-lost grandson while hiding from a relentless gangster.",
        "rating": 7.5,
        "release_year": 2006,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYzA0OGMyMTUtZTZmZi00MGQ2LWFiZTUtMzk4ZTgyOTI1Y2M0XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 66,
        "title": "Article 15",
        "genre": "Crime Drama Mystery",
        "director": "Anubhav Sinha",
        "cast": "Ayushmann Khurrana Nassar Manoj Pahwa Kumud Mishra Isha Talwar Sayani Gupta",
        "overview": "A newly appointed upright IPS officer is sent to a rural district where he investigates the disappearance and brutal murder of three teenage girls belonging to an oppressed caste.",
        "rating": 8.1,
        "release_year": 2019,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BZWYzOGEwNTgtNWU3NS00OWEzLTg2ZGMtMzNlYTk2NTdhYjRiXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 67,
        "title": "Badhaai Ho",
        "genre": "Comedy Drama",
        "director": "Amit Ravindernath Sharma",
        "cast": "Ayushmann Khurrana Sanya Malhotra Neena Gupta Gajraj Rao Surekha Sikri",
        "overview": "A 25-year-old man faces immense embarrassment in front of his friends and girlfriend when he discovers that his middle-aged mother has become pregnant.",
        "rating": 7.9,
        "release_year": 2018,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BZmJhZWRhMjEtMjc2OS00ZWEzLTkzM2EtNzMzYTVlZTA3NjMyXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 68,
        "title": "Bala",
        "genre": "Comedy Drama",
        "director": "Amar Kaushik",
        "cast": "Ayushmann Khurrana Bhumi Pednekar Yami Gautam Saurabh Shukla",
        "overview": "A young man living in Kanpur suffers from premature baldness, coping with the social stigma, lack of confidence, and societal pressures of physical beauty standards.",
        "rating": 7.3,
        "release_year": 2019,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BYTY5OWM0NDAtODdhNS00YWQ1LTg5NWEtOGVlNGExNjcwYjMyXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 69,
        "title": "Bareilly Ki Barfi",
        "genre": "Comedy Romance",
        "director": "Ashwiny Iyer Tiwari",
        "cast": "Ayushmann Khurrana Kriti Sanon Rajkummar Rao Pankaj Tripathi",
        "overview": "Bitti, a free-spirited girl from Bareilly, falls in love with the author of a progressive novel. When she searches for him, a local printing press owner creates a hilarious web of lies.",
        "rating": 7.5,
        "release_year": 2017,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMjA4MDk5MDcyOF5BMl5BanBnXkFtZTgwNTcyNDgzMzI@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "movie_id": 70,
        "title": "Gangs of Wasseypur 2",
        "genre": "Action Comedy Crime Drama",
        "director": "Anurag Kashyap",
        "cast": "Nawazuddin Siddiqui Richa Chadha Huma Qureshi Zeishan Quadri Rajkummar Rao Pankaj Tripathi",
        "overview": "Faizal Khan takes over his father Sardar Khan's legacy and vows to avenge the deaths of his family members, leading to bloody battles for coal trade dominance.",
        "rating": 8.2,
        "release_year": 2012,
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNWE3OGJlZmMtMzIzNy00YmNlLWJhMGEtZDYyOTM0ZDcxNDMwXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    }
]

csv_file = DATASET_DIR / "hindi_movies.csv"

fieldnames = ["movie_id", "title", "genre", "director", "cast", "overview", "rating", "release_year", "poster_url"]

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for m in movies:
        writer.writerow(m)

print(f"Created {csv_file} with {len(movies)} Hindi movies successfully!")
