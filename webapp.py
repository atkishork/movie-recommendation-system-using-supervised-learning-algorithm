import numpy as np # type: ignore
import streamlit as st # type: ignore
from streamlit_option_menu import option_menu # type: ignore
from streamlit_lottie import st_lottie # type: ignore
import streamlit.components.v1 as html # type: ignore
from PIL import Image
import numpy as np # type: ignore
import pandas as pd # type: ignore
from st_aggrid import AgGrid # type: ignore
import plotly.express as px # type: ignore
import pickle
import requests

#---Configuring the web apps's title name and its favicon
st.set_page_config(page_title =" Movie Recommendation System",page_icon =":computer:",layout="wide")

#----Making the navigation menu
with st.sidebar:
    choose =option_menu(
        "MR System",["Home","About us","Contact us"],
        icons = ["house","cpu","people","envelope"],
        menu_icon = "app-indicator",
        default_index = 0,
        styles={
        "container": {"padding": "5!important","background-color": "#040C6D"},
        "icon": {"color": "#FFFFFF ", "font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left","color": "#FFFFFF ", "margin":"0px", "--hover-color": "#373A5B "},
        "nav-link-selected": {"background-color": "#010318"},
    }
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#---Loading all the iamges used here
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_cbemdbsc.json")
lottie_coding2 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_knvn3kk2.json")
logo = Image.open(r'./img/logo2.png')

if choose == "Home":
    def fetch_poster(movie_id): #--- Function made to fetch the poster of movies 

        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path


    movies = pd.read_pickle('./dictonary/movie_dict.pkl') #--- loading the pickle format data from jupyter notebook
    similarity = pd.read_pickle('./dictonary/Similarity.pkl')


    def recommend(movie):   #--- Function that implements KNN using cosine similarity.
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(
            list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        movie_list = sorted(list(enumerate(distances)),
                            reverse=True, key=lambda x: x[1])[1:16]
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:16]:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters



    movie_list = movies['title'].values
    


    #--- Designing the header part of our function    
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               #---To display the header text using css style
            st.markdown("""  <style> .font { font-size:45px ; font-family: 'Cooper Black'; color: #009edc;} </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">Movie Recommendation System</p>', unsafe_allow_html=True)    
    with col2:               #---To display brand logo
        st.image(logo, width=90 )


    apps = ['--Select--', 'Movie based']
    app_options = st.selectbox('Select application:', apps)

    if app_options == 'Movie based':
        selected_movie =st.selectbox('Select movie:', movie_list)

    #--- Recommending top 15 movies:
    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(recommended_movie_posters[0])
            st.text(recommended_movie_names[0])

        with col2:
            st.image(recommended_movie_posters[1])
            st.text(recommended_movie_names[1])

        with col3:
            st.image(recommended_movie_posters[2])
            st.text(recommended_movie_names[2])
        with col4:
            st.image(recommended_movie_posters[3])
            st.text(recommended_movie_names[3])

        with col5:
            st.image(recommended_movie_posters[4])
            st.text(recommended_movie_names[4])

        col6, col7, col8, col9, col10 = st.columns(5)
        with col6:
            st.image(recommended_movie_posters[5])
            st.text(recommended_movie_names[5])

        with col7:
            st.image(recommended_movie_posters[6])
            st.text(recommended_movie_names[6])

        with col8:
            st.image(recommended_movie_posters[7])
            st.text(recommended_movie_names[7])
        with col9:
            st.image(recommended_movie_posters[8])
            st.text(recommended_movie_names[8])

        with col10:
            st.image(recommended_movie_posters[9])
            st.text(recommended_movie_names[9])
        col10, col11, col12, col13, col14 = st.columns(5)
        with col10:
            st.image(recommended_movie_posters[10])
            st.text(recommended_movie_names[10])

        with col11:
            st.image(recommended_movie_posters[11])
            st.text(recommended_movie_names[11])

        with col12:
            st.image(recommended_movie_posters[12])
            st.text(recommended_movie_names[12])
        with col13:
            st.image(recommended_movie_posters[13])
            st.text(recommended_movie_names[13])

        with col14:
            st.image(recommended_movie_posters[14])
            st.text(recommended_movie_names[14])


elif choose == "About us":
    with st.container():
        st.markdown(""" <style> .font { font-size:45px ; font-family: 'Cooper Black'; color: #009edc;} </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Project</p>', unsafe_allow_html=True)  
        st.write("##")
        col1, col2 = st.columns([0.7,0.3])
        with col1:
            st.write("This is a **Movie Recommendation System**, an AI-powered application built using **Machine Learning** techniques. The system is designed to suggest movies to users based on their preferences by analyzing various features like genre, cast, director, and IMDb ratings.")
            st.write("#")
            st.write("### Project Details:")
            st.write("**NAME**: Movie Recommendation System")
            st.write("**TECHNOLOGY**: Machine Learning")
            st.write("**ALGORITHM USED**: Supervised Learning - Cosine Similarity & Apriori Algorithm")
            st.write("**LANGUAGE USED**: Python, HTML, CSS")
            st.write("**TOOLS & IDEs**: Jupyter Notebook, VS Code")
            st.write("**FRAMEWORK**: Streamlit (for Web App)")
            st.write("##")
        with col2:
            st_lottie(lottie_coding2, height=300, key="coding")
        st.write("---")

        st.subheader("How It Works")
        st.write("---")
        st.write("Our system takes **three recently watched movies** as input and analyzes their attributes to recommend the top 5 similar movies.")
        st.write("The recommendation is based on:")
        st.write("- **Cosine Similarity**: Measures the similarity between movies by comparing their feature vectors.")
        st.write("- **Apriori Algorithm**: Finds patterns in user preferences and provides more personalized recommendations.")
        st.write("---")

        st.subheader("Algorithms Used")
        st.write("---")

        st.write("### 1. Cosine Similarity")
        st.write("This algorithm computes the similarity between two movies based on their feature vectors. It determines how closely related they are by calculating the angle between their vectors in high-dimensional space.")
        st.write("**Example:** If two movies have similar genres, cast, and directors, the cosine similarity score will be high, meaning they are closely related.")
        st.write("---")

        st.write("### 2. Apriori Algorithm")
        st.write("Apriori is used for association rule learning. It helps in finding relationships between different movies watched by users. If many users who watch a certain set of movies also like another specific movie, our system will suggest it.")
        st.write("**Example:** If many users who watched 'Interstellar' and 'Inception' also liked 'Tenet,' our system will recommend 'Tenet' to a user who watched the first two movies.")
        st.write("---")

        st.subheader("Future Expansions")
        st.write("---")
        st.write("We aim to improve this recommendation system by:")
        st.write("- **Integrating Deep Learning Models** (e.g., Neural Networks for better feature extraction)")
        st.write("- **User Behavior Analysis** (tracking watch history and preferences for better personalization)")
        st.write("- **Real-time Recommendations** (using APIs to fetch live data and improve accuracy)")
        st.write("- **Multi-platform Support** (deploying as a full-fledged web and mobile application)")
        st.write("#")
        st.write("---")

#---If "Contact us" selected, it will redirect to contact form page.
elif choose == "Contact us":
    st.markdown(""" 
    <style> 
        .font { font-size:35px ; font-family: 'Cooper Black'; color: #009edc; text-align: center;} 
    </style> 
""", unsafe_allow_html=True)

st.markdown('<p class="font">Contact Us</p>', unsafe_allow_html=True)

st.write("📩 **For any queries, suggestions, or feedback, please email us at:** [kishorkumar83076@gmail.com](mailto:kishorkumar83076@gmail.com)")