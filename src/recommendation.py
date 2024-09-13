# recommendation.py

from sklearn.neighbors import NearestNeighbors


def recommend_tracks(features_scaled, track_ids):
    model = NearestNeighbors(n_neighbors=5, algorithm='auto')
    model.fit(features_scaled)
    distances, indices = model.kneighbors(features_scaled)

    # Recommend tracks for the first track in the list
    recommended_indices = indices[0]
    recommended_tracks = [track_ids[i] for i in recommended_indices]

    return recommended_tracks
