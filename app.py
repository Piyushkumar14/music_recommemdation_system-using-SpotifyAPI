import streamlit as st
from src.data_collection import get_spotify_client
import pandas as pd

def run_app(recommendations, scaler):
    st.title('Spotify Music Recommendation System')
    st.write('Enter a song or artist you like, and we will recommend similar tracks!')

    track_name = st.text_input('Enter a track name:')
    if st.button('Recommend'):
        sp = get_spotify_client()
        result = sp.search(track_name, limit=1)
        track_id = result['tracks']['items'][0]['id']
        features = sp.audio_features([track_id])[0]

        feature_df = pd.DataFrame(features, index=[0])

        scaled_features = scaler.transform(feature_df[[['danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]])
        distances, indices = recommendations.kneighbors(scaled_features)

        for index in indices[0]:
            track = sp.track(track_id)
            st.write(f"Recommended Track: {track['name']} by {track['artists'][0]['name']}")