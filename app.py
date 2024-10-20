import streamlit as st
from sklearn.preprocessing import StandardScaler
from src.data_collection import get_spotify_client, get_audio_features, get_user_top_tracks
import pandas as pd
from sklearn.neighbors import NearestNeighbors

def run_app(recommendations, scaler, track_ids):
    st.title('Spotify Music Recommendation System')
    st.write('Enter a song or artist you like, and we will recommend similar tracks!')

    track_name = st.text_input('Enter a track name:')
    if st.button('Recommend'):
        sp = get_spotify_client()
        result = sp.search(track_name, limit=1)

        # Ensure search returned results
        if len(result['tracks']['items']) == 0:
            st.write("No track found with the given name.")
            return

        track_id = result['tracks']['items'][0]['id']
        features = get_audio_features([track_id])[0]  # Ensure this returns a dictionary-like object

        # Ensure features are correctly transformed to a DataFrame
        feature_df = pd.DataFrame([features])

        # Select only the required features
        required_features = ['danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness',
                             'instrumentalness', 'liveness', 'valence', 'tempo']
        feature_df = feature_df[required_features]

        # Scale the features
        scaled_features = scaler.transform(feature_df)

        # Get recommendations using the KNN model
        distances, indices = recommendations.kneighbors(scaled_features)

        for index in indices[0]:
            recommended_track_id = track_ids[index]  # Use the recommended track ID
            track = sp.track(recommended_track_id)
            st.write(f"Recommended Track: {track['name']} by {track['artists'][0]['name']}")

if __name__ == "__main__":
    # Example of how to fit the model and scaler outside the function
    track_ids = get_user_top_tracks()
    features = get_audio_features(track_ids)
    example_features = pd.DataFrame(features)

    required_features = ['danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness',
                         'instrumentalness', 'liveness', 'valence', 'tempo']
    example_features = example_features[required_features]
     # Replace with actual track IDs
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(example_features)
    recommendations = NearestNeighbors(n_neighbors=5, algorithm='auto')
    recommendations.fit(features_scaled)

    run_app(recommendations, scaler, track_ids)