#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


df=pd.read_excel(r"final_tracks.xlsx.xlsx")

# Function to recommend songs from the same cluster
def recommend_songs(song_name, data, num_recommendations):
    song_name=song_name.lower()
    if song_name in data['Name'].values:
        cluster = data.loc[data['Name'] == song_name, 'Cluster_id'].values[0]
    recommendations = data[data['Cluster_id'] == cluster].sample(num_recommendations)
    return recommendations['Name']


st.title('Music Recommendation System')
song=st.selectbox('Select a Song:',df['Name'].values)
number_of_songs=st.selectbox('Select number of recommended songs:',list(range(1,10,1)))

if st.button('recommend'):
    names=recommend_songs(song,df,number_of_songs)






















# In[ ]:




