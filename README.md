# Song Recommendation System
This repository contains the implementation of a Song Recommendation System using the Spotify dataset which have been fetched. The system is built with Machine Learning techniques to recommend songs based on the genre, artist, popularity and song features.
## Objective:
The Song Recommendation System is designed to recommend songs similar to the one selected by the user. By analyzing the properties of the chosen song, the system generates a list of tracks that closely match the user's preferences.
### How It Works:
Analysis: The system analyzes the features of the user-selected song.  
Recommendation: Based on this analysis, it recommends a list of similar tracks from the Spotify dataset, ensuring that the recommendations align with the characteristics of the input song.
## ML Techniques used:
NLP techniques to preprocess the text data   
Cosine similarity   

## Conclusion:
I experimented with clustering and obtained a silhouette score of around 5. However, I opted for cosine similarity for the song recommendation system, as it is more efficient and effectively calculates the similarity score between each pair of songs.