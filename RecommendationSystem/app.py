import streamlit as sl
import pickle
import requests
def fetch_poster(id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4477c8b9dd6f7ef02a3ca3be5abfa767&language=en-US'.format(id))
    data=response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/original/'+data['poster_path']

def recommend(movie):
    c=0
    for i in movies_list:
        if(movie==i):
            index=c
            break
        c+=1
    distances = similarity[index]
    recommendations=[]
    posters=[]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies:
        movie_id=movie_ids[i[0]]
        recommendations.append(movies_list[i[0]])
        posters.append(fetch_poster(movie_id))
    return recommendations,posters


similarity=pickle.load(open('similarity.pkl','rb'))
movies_list=pickle.load(open('movies.pkl', 'rb'))
movie_ids=movies_list['movie_id'].values
movies_list=movies_list['title'].values
sl.title('Movie Recommendation System')
selected_movie=sl.selectbox('Give us a movie',movies_list)
if sl.button('Recommend'):
    recommendations,posters=recommend(selected_movie)
    col1, col2, col3 = sl.columns(3)
    with col1:
            sl.text(recommendations[0])
            sl.image(posters[0])
    with col2:
            sl.text(recommendations[1])
            sl.image(posters[1])
    with col3:
            sl.text(recommendations[2])
            sl.image(posters[2])
    col4, col5,col6=sl.columns(3)
    with col4:
            sl.text(recommendations[3])
            sl.image(posters[3])
    with col5:
            sl.text(recommendations[4])
            sl.image(posters[4])
