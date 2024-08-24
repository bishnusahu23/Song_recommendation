#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# Load the dataset
df = pd.read_excel("final_tracks.xlsx")

# Ensure all song names are non-null and lowercase
df['Name'] = df['Name'].fillna("").str.lower()

# Function to recommend songs from the same cluster
def recommend_songs(song_name, data, num_recommendations):
    song_name = song_name.lower()
    
    if song_name in data['Name'].values:
        cluster = data.loc[data['Name'] == song_name, 'Cluster_id'].values[0]
        recommendations = data[(data['Cluster_id'] == cluster) & (data['Name'] != song_name)]
        
        # Check if there are enough songs to sample
        if len(recommendations) < num_recommendations:
            return recommendations  # Return all available recommendations
        else:
            return recommendations.sample(num_recommendations)
    else:
        return pd.DataFrame(columns=['Name', 'Artist', 'Genre', 'Popularity'])  # Return an empty DataFrame if the song is not found

# App title with custom styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Music Recommendation System</h1>", unsafe_allow_html=True)

# Select a song
song = st.selectbox('Select a Song:', df['Name'].str.title().values)

# Select the number of recommendations
number_of_songs = st.slider('Select number of recommended songs:', 1, 10, 5)

# Button to trigger recommendation
if st.button('Recommend'):
    # Get recommendations
    recommendations = recommend_songs(song, df, number_of_songs)

    if not recommendations.empty:
        st.success(f"Recommended songs similar to **{song}**:")
        
        # Display the recommended songs with more details
        for index, row in recommendations.iterrows():
            st.markdown(f"""
                <div style="background-color: #f9f9f9; padding: 10px; border-radius: 10px; margin-bottom: 10px;">
                    <h3 style="color: #4CAF50;">🎶 {row['Name'].title()}</h3>
                    <p><strong>Artist:</strong> {row['Artist']}</p>
                    <p><strong>Genre:</strong> {row['Genre']}</p>
                    
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error(f"No recommendations found for **{song}**. Please try another song.")






















# In[ ]:




