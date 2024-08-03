import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests
movies_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
last = movies_list
movies_list = movies_list['title']
st.title('Movie Recommendation System')
selected_moviename = st.selectbox('Pickone',movies_list)

def fetch_poster(movie_ids):
    api_key = '8265bd1679663a7ea12ac168da84d2e8'
    response =  requests.get(f'https://api.themoviedb.org/3/movie/{movie_ids}?api_key={api_key}&language=en-US')
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
    
def recommend(movie):
    movie = movie.lower()
    movie_index = last[last['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_ids = last.iloc[i[0]].movie_id
        recommended_movies.append((last.iloc[i[0]].title).title())
        recommended_movies_posters.append(fetch_poster(movie_ids))
    return recommended_movies,recommended_movies_posters

if st.button('Recommend'):
    name,posters = recommend(selected_moviename)
    cols = st.columns(5)
    for col, name, poster in zip(cols, name, posters):
        with col:
            st.text(name)
            st.image(poster)
        