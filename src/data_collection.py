import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI


def get_spotify_client():
    sp_oauth = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='user-read-private user-library-read user-top-read'
    )

    token_info = sp_oauth.get_cached_token()
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        print(f'Please navigate to the following URL to authorize the application: {auth_url}')
        response = input('Enter the URL you were redirected to: ')
        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)

    sp = spotipy.Spotify(auth=token_info['access_token'])
    return sp


def get_user_top_tracks():
    sp = get_spotify_client()
    top_tracks = sp.current_user_top_tracks(limit=50)
    return [track['id'] for track in top_tracks['items']]


def get_audio_features(track_ids):
    sp = get_spotify_client()
    features = sp.audio_features(track_ids)
    feature_names = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']
    # print([{name: feature[name] for name in feature_names} for feature in features if feature])
    return [{name: feature[name] for name in feature_names} for feature in features if feature]