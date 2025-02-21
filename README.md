# Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on the selected movie's content (plot, genres, keywords, cast, and crew).

## 🚀 Features
- Interactive web interface using Streamlit
- Movie recommendations with movie posters
- Content-based filtering using text similarity
- Integration with TMDB API for movie posters

## 🛠️ Technical Concepts Used

### 1. Data Processing & Text Mining
- **Text Preprocessing**: Converting text to lowercase, tokenization, and stemming using NLTK's PorterStemmer
- **Feature Extraction**: Using CountVectorizer to convert text data into numerical vectors
- **Cosine Similarity**: Measuring similarity between movies based on their feature vectors

### 2. Machine Learning
- **Content-Based Filtering**: Recommendations based on movie features rather than user interactions
- **Vector Space Model**: Representing movies as numerical vectors in high-dimensional space

### 3. Web Technologies
- **Streamlit**: Frontend web framework for creating the interactive interface
- **TMDB API Integration**: Fetching movie posters using the TMDB (The Movie Database) API

## 📝 Project Steps

### 1. Data Collection and Preprocessing
- Loaded movie data from TMDB dataset (5000 movies)
- Merged movies and credits dataframes
- Extracted relevant features: genres, keywords, cast, crew, and overview
- Cleaned and preprocessed text data:
  - Removed spaces from names
  - Converted text to lowercase
  - Applied stemming to reduce words to their root form

### 2. Feature Engineering
- Combined all text features (overview, genres, keywords, cast, crew) into a single 'tags' column
- Created a bag-of-words representation using CountVectorizer
- Generated similarity matrix using cosine similarity

### 3. Recommendation Engine
- Built a recommendation function that:
  - Finds the index of the selected movie
  - Calculates similarity scores with all other movies
  - Returns top 5 most similar movies

### 4. Web Application
- Created an interactive interface using Streamlit
- Implemented movie selection dropdown
- Displayed recommended movies with their posters
- Integrated TMDB API for fetching movie posters

## 🔧 Technologies Used
- Python 3.x
- Pandas for data manipulation
- NLTK for text processing
- Scikit-learn for feature extraction and similarity calculation
- Streamlit for web interface
- TMDB API for movie data

## 📊 Dataset
The project uses the TMDB 5000 Movie Dataset containing:
- Movie metadata (budget, genres, keywords, etc.)
- Cast and crew information
- Movie overviews and titles

## 🎯 Future Improvements
- Add user authentication
- Implement collaborative filtering
- Include movie ratings and reviews
- Add more movie details in the interface
- Optimize recommendation algorithm for larger datasets
