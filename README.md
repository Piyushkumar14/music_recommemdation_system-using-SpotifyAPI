# 🎵 Spotify Music Recommendation System

A simple yet powerful **Music Recommendation System** built using the **Spotify Web API**, **Scikit-learn**, and **Streamlit**.  
This project recommends similar songs based on audio features such as _danceability, energy, valence, tempo_, etc.

I built it while learning about recommendation systems and how Spotify handles audio analysis behind the scenes. It’s not perfect (like me 😅), but it’s a cool project that shows how ML + APIs can come together to create something real.

* * *

## 🚀 Features

-   🎧 Fetches real-time track data from **Spotify API**
    
-   🔍 Extracts audio features (like energy, valence, danceability)
    
-   🤖 Uses **KNN (Nearest Neighbors)** for similarity-based recommendations
    
-   🧠 Scales and normalizes features using **StandardScaler**
    
-   💻 Clean, interactive **Streamlit UI**
    
-   🌐 Supports live track search by name or artist
    

* * *

## 🧩 Tech Stack

| Tool | Purpose |
| --- | --- |
| **Python 3.10+** | Core programming language |
| **Spotify Web API** | Fetching song details and audio features |
| **Spotipy** | Python wrapper for Spotify API |
| **Scikit-learn** | Machine Learning (KNN, StandardScaler) |
| **Pandas** | Data handling |
| **Streamlit** | Frontend web app |
| **dotenv** | Managing environment variables |

* * *

## ⚙️ Project Structure

Here’s how I divided the project into files — to keep things clean and modular.

`music-recommender/ │ ├── src/ │   ├── data_collection.py      # Spotify API client setup and data fetching │   ├── feature_engineering.py  # Feature processing and scaling │   └── model_training.py       # KNN model training and saving │ ├── app.py                      # Streamlit frontend (main app) ├── requirements.txt            # Python dependencies ├── .env                        # API credentials (not shared) └── README.md                   # You're reading it :)`

* * *

## 🔑 Setting up Spotify API Credentials

1.  Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
    
2.  Create a new app
    
    -   App Name: `Music Recommender`
        
    -   Description: `For learning purpose`
        
3.  Set the **Redirect URI** to:
    
    `http://localhost:8888/callback`
    
4.  Copy your **Client ID** and **Client Secret**
    
5.  Create a `.env` file in the project root:
    
    `SPOTIFY_CLIENT_ID="your_client_id_here" SPOTIFY_CLIENT_SECRET="your_client_secret_here" SPOTIFY_REDIRECT_URI="http://localhost:8888/callback"`
    

* * *

## 💻 Installation and Setup

1.  Clone the repository
    
    `git clone https://github.com/yourusername/music-recommender.git cd music-recommender`
    
2.  Create a virtual environment
    
    `python -m venv venv source venv/bin/activate   # for Linux/Mac venv\Scripts\activate      # for Windows`
    
3.  Install dependencies
    
    `pip install -r requirements.txt`
    
4.  Run the app
    
    `streamlit run app.py`
    
5.  Open in your browser at  
    👉 `http://localhost:8501`
    

* * *

## 🧠 How It Works

### Step 1: Collecting Data

-   The user enters a **track name**.
    
-   The Spotify API fetches the track’s **ID** and its **audio features**.
    

### Step 2: Feature Scaling

-   Features like `danceability`, `energy`, `tempo`, etc. are standardized using `StandardScaler`.
    

### Step 3: Finding Similar Songs

-   The app uses a **KNN (Nearest Neighbors)** model trained on example Spotify track features.
    
-   The model finds the closest songs (in feature space).
    

### Step 4: Display Recommendations

-   The recommended songs are fetched from Spotify using their track IDs.
    
-   Their names and artists are displayed on the Streamlit UI.
    

* * *

## 🧪 Example Code (simplified)

`from sklearn.neighbors import NearestNeighbors from sklearn.preprocessing import StandardScaler import pandas as pd  # Example data example_features = pd.DataFrame({     'danceability': [0.5],     'energy': [0.5],     'key': [5],     'loudness': [-5.0],     'speechiness': [0.05],     'acousticness': [0.1],     'instrumentalness': [0.0],     'liveness': [0.1],     'valence': [0.5],     'tempo': [120.0] })  scaler = StandardScaler() scaled_data = scaler.fit_transform(example_features)  knn = NearestNeighbors(n_neighbors=5) knn.fit(scaled_data)`

* * *

## 🧰 Troubleshooting

| Error | Possible Cause | Fix |
| --- | --- | --- |
| `Insufficient client scope` | Scopes missing in Spotify OAuth | Add proper scopes in your `SpotifyOAuth()` |
| `NoneType object is not subscriptable` | Track not found | Check spelling or increase search limit |
| `'list' object has no attribute 'kneighbors'` | Passed list instead of trained model | Make sure to pass the trained `NearestNeighbors` model |
| `invalid redirect URI` | Redirect not matching in Spotify app | Set it to `http://localhost:8888/callback` |

* * *

## 🌱 Future Improvements

-   Add **content-based + collaborative filtering hybrid model**
    
-   Cache user’s listening history
    
-   Include **playlist-based recommendations**
    
-   Deploy on **Streamlit Cloud / Render / Hugging Face Spaces**
    
-   Add **Spotify OAuth login** so users get personalized recs
    

* * *

## 🙋‍♂️ About Me

Hey! I’m **Piyush Kumar**, a data enthusiast exploring how AI and real-world APIs can be combined to make something creative and useful.  
I’m constantly learning, experimenting, and occasionally breaking stuff in the process 😅.

If you liked this project, connect with me on [LinkedIn](https://linkedin.com/in/piyush-kumar) or drop a ⭐ on the repo!

* * *

## 📜 License

This project is open-sourced under the MIT License.  
Feel free to use, modify, and share (with proper credit ❤️).

* * *

Would you like me to make this README more **GitHub-styled** (with emojis, collapsible sections, and code snippets formatted for Markdown)? It’ll look even more appealing to recruiters and devs.
