# Song Recommendation System
This repository features the implementation of a Song Recommendation System built using a Spotify dataset, scraped via the Spotify Web API. The system utilizes Machine Learning techniques to recommend songs based on various factors such as genre, artist, popularity, and audio features

## Objective:
The main goal of this system is to recommend songs similar to the one selected by the user. By analyzing the audio properties and metadata of the chosen song, the system generates a list of tracks that closely match the user's preferences.

## How It Works:
### Analysis:
The system analyzes various features of the song selected by the user, such as genre, artist, and audio characteristics.
### Recommendation:
Using these features, it recommends a list of similar tracks from the Spotify dataset. The recommendations align with the musical characteristics of the input song to provide relevant suggestions.
## Machine Learning Techniques Used:
### Natural Language Processing (NLP):
Preprocessing the textual data (e.g., song titles, artist names, and genres) to prepare it for similarity calculations.
### Cosine Similarity:
This method computes the similarity score between songs based on their feature vectors, identifying songs that are most similar to the selected one.
## Experimental Insights:
I initially experimented with clustering techniques, achieving a silhouette score of around 5. However, I opted for cosine similarity in the final implementation, as it is more efficient and provides better results for song recommendation by accurately calculating the similarity score between each pair of songs.
## Conclusion:
The use of cosine similarity improved the recommendation engine by providing more relevant and personalized song suggestions. This significantly enhanced the user experience by tailoring the recommendations to the user's preferences.
## Deployment using streamlit: 
https://songrecommendation-wckxeqit7s3ynb8xkcyunh.streamlit.app/
