import re

PLAYLIST_ID_REGEX = r'playlist/([a-zA-Z0-9]+)'
ALBUM_ID_REGEX = r'album/([a-zA-Z0-9]+)'

def extractPlaylistID(url: str) -> str:
    """
    Extract playlist ID from Spotify URL.
    :param url: String with Spotify playlist URL
    :return: String with playlist ID
    """
    match = re.search(PLAYLIST_ID_REGEX, url)
    if not match:
        raise ValueError(f"The URL {url} does not match the expected playlist format.")
    else:
        return match.group(1)

def extractAlbumID(url: str) -> str:
    """
    Extract album ID from Spotify URL.
    :param url: String with Spotify album URL
    :return: String with album ID
    """
    match = re.search(ALBUM_ID_REGEX, url)
    if not match:
        raise ValueError(f"The URL {url} does not match the expected album format.")
    else:
        return match.group(1)
