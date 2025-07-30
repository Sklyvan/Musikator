from spotipy.oauth2 import SpotifyClientCredentials
import dotenv
import os

PLAYLIST_NAME, ALBUM_NAME = "Playlist_{playlistID}.json", "Album_{albumID}.json"

def loadEnvironmentCredentials() -> SpotifyClientCredentials:
    """
    Load Spotify API credentials from environment variables.
    :return: SpotifyClientCredentials instance
    :raises ValueError: If SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET is
    """
    dotenv.load_dotenv()
    clientID, clientSecret = os.getenv("SPOTIFY_CLIENT_ID"), os.getenv("SPOTIFY_CLIENT_SECRET")

    if not clientID or not clientSecret:
        raise ValueError("Please set the SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET environment variables.")
    else:
     return SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
