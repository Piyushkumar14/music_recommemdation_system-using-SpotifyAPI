import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_features(audio_features):
    features_df = pd.DataFrame(audio_features)
    required_features = ['danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features_df[required_features])
    features_df[required_features] = features_scaled
    return features_df, scaler