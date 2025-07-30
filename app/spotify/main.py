from url import extractPlaylistID, extractAlbumID
from configuration import loadEnvironmentCredentials
from client import SpotifyClient
import json

def saveToJSON(data: dict, filename: str) -> None:
    """
    Save data to a JSON file.
    :param data: A dictionary containing the data to be saved.
    :param filename: The name of the file where the data will be saved.
    :return: None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def savePlaylist(url: str) -> dict:
    """
    Save playlist tracks to JSON file.
    :param url: String with Spotify playlist URL
    :return: A dictionary with playlist details and tracks.
    :raises RuntimeError: If an error occurs while fetching the playlist.
    """
    try:
        authManager = loadEnvironmentCredentials()
        playlistID = extractPlaylistID(url)

        client = SpotifyClient(authManager)
        content = client.getPlaylistTracks(playlistID)

        saveToJSON(content, f'Playlist_{playlistID}.json')
        return content

    except Exception as e:
        raise RuntimeError(f"An error occurred while fetching the playlist: {e}")

def saveAlbum(url: str) -> dict:
    """
    Save album tracks to JSON file.
    :param url: String with Spotify album URL
    :return: A dictionary with album details and tracks.
    :raises RuntimeError: If an error occurs while fetching the album.
    """
    try:
        authManager = loadEnvironmentCredentials()
        albumID = extractAlbumID(url)

        client = SpotifyClient(authManager)
        content = client.getAlbumTracks(albumID)

        saveToJSON(content, f'Album_{albumID}.json')
        return content

    except Exception as e:
        raise RuntimeError(f"An error occurred while fetching the album: {e}")

if __name__ == "__main__":
    ALBUM_URL = "https://open.spotify.com/album/0edbVzfXfKVIAcIRuQ0MMo"
    saveAlbum(ALBUM_URL)
