from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import dotenv
import json
import os
import re

PLAYLIST_ID_REGEX = r'playlist/([a-zA-Z0-9]+)'

def extractPlaylistID(playlistUrl: str) -> str:
    """
    Extracts the playlist ID from a Spotify playlist URL. We assume the URL is in the format:
    https://open.spotify.com/playlist/{playlistID}
    :param playlistUrl:
    :return: A string representing the playlist ID.
    :raises ValueError: If the URL does not match the expected format.
    """
    match = re.search(PLAYLIST_ID_REGEX, playlistUrl)
    if not match:
        raise ValueError(f"The URL {playlistUrl} does not match the expected format.")
    else:
        return match.group(1)


def getPlaylistTracks(playlistID: str, authManager) -> dict:
    """
    Fetches the tracks from a Spotify playlist using the provided client ID and secret.
    :param playlistID: The ID of the Spotify playlist.
    :param authManager: An instance of SpotifyClientCredentials for authentication.
    :return: A dictionary containing the playlist name, ID, and a list of tracks with
    """
    sp = spotipy.Spotify(auth_manager=authManager)
    playlist = sp.playlist(playlistID)

    output = {"PlaylistName": playlist["name"], "PlaylistID": playlistID, "Tracks": []}

    playlistItems = sp.playlist_items(playlistID, additional_types="track")
    tracks = playlistItems['items']
    while playlistItems['next']:
        playlistItems = sp.next(playlistItems)
        tracks.extend(playlistItems['items'])

    for item in tracks:
        track = item['track']
        output["Tracks"].append({
            "Name": track['name'],
            "Artists": [artist['name'] for artist in track['artists']],
            "Release": track['album']['release_date'],
            "CoverURL": track['album']['images'][0]['url'] if track['album']['images'] else None
        })

    return output


def savePlaylistToJSON(data: dict, filename: str) -> None:
    """
    Saves the playlist data to a JSON file.
    :param data: Dictionary containing playlist data.
    :param filename: Name of the file to save the data to.
    :return: None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main(url: str):
    dotenv.load_dotenv()
    CLIENT_ID, CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_ID"), os.getenv("SPOTIFY_CLIENT_SECRET")

    if not CLIENT_ID or not CLIENT_SECRET:
        raise ValueError("Please set the SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET environment variables.")
    else:
        try:
            authManager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
            playlistID = extractPlaylistID(url)

            playlistContent = getPlaylistTracks(playlistID, authManager)
            savePlaylistToJSON(playlistContent, f'Playlist_{playlistID}.json')

        except Exception as e:
            raise RuntimeError(f"An error occurred while fetching the playlist: {e}")
        else:
            return playlistContent


if __name__ == "__main__":
    PLAYLIST_URL = "https://open.spotify.com/playlist/0xGEyZLiKyKpV5wp5C94vT"
    main(PLAYLIST_URL)
