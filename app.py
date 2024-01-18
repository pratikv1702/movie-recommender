import pandas as pd
import pickle
import streamlit as st


movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
    'select movie',
    (movies['title'].values)
)

if st.button('Recommend'):

    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

