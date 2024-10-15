from src.data_collection import get_user_top_tracks, get_audio_features
from src.preprocessing import preprocess_features
from src.recommendation import recommend_tracks
from app import run_app


def main():
    # Step 1: Data Collection
    top_tracks = get_user_top_tracks()
    audio_features = get_audio_features(top_tracks)

    # Step 2: Data Preprocessing
    processed_features, scaler = preprocess_features(audio_features)

    # Step 3: Recommendation
    recommendations = recommend_tracks(processed_features)

    # Step 4: Run Web Application
    run_app(recommendations, scaler)

if __name__ == '__main__':
    main()
