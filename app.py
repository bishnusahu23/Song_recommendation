#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize the Spotify client
CLIENT_ID = "4858241d3e1e4897ae23adb111fdb00f"
CLIENT_SECRET = "efebedcd3c1842bea2b9ffe30e1b8a2f"
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(Name,top_n):
    Name=Name.lower()
    music['Name']=music['Name'].str.lower()
    sim_values=similarity[Name].values.tolist()
    # enumerating the values
    sim_values=enumerate(sim_values)
    # Sorting the values in descending order
    sim_values=sorted(sim_values, key=lambda x: x[1], reverse=True)
    recommended_music_names = []
    recommended_music_posters = []
    for i in sim_values[0:top_n+1]:
        artist = music.iloc[i[0]].Artist
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].Name, artist))
        recommended_music_names.append(music.iloc[i[0]].Name)

    return recommended_music_names, recommended_music_posters

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Song Recommendation System</h1>", unsafe_allow_html=True)

music = pickle.load(open('final_tracks.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb' ))


selected_song = st.selectbox("Type or select a song from the dropdown", music['Name'].values)
# Select the number of recommendations
number_of_songs = st.slider('Select number of recommended songs:', 1, 10, 5)

if st.button('Show Recommendation'):
    recommended_music_names, recommended_music_posters = recommend(selected_song,number_of_songs)
    st.subheader('Recommended Songs for You')
    
    
    for name, poster in zip(recommended_music_names, recommended_music_posters):
        with st.container():
            col1, col2 = st.columns([1, 4])  
            with col1:
                st.image(poster, width=80)   
            with col2:
                st.write(name)                
                st.markdown('---')     
# In[ ]:




