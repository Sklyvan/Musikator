import spotipy

class SpotifyClient:
    def __init__(self, authManager):
        self.sp = spotipy.Spotify(auth_manager=authManager)

    def getPlaylistTracks(self, playlistID: str) -> dict:
        """
        Fetch tracks from a Spotify playlist.
        :param playlistID: A string representing the Spotify playlist ID.
        :return: A dictionary containing the playlist name, ID, and a list of tracks with their details.
        """
        playlist = self.sp.playlist(playlistID)
        output = {"PlaylistName": playlist["name"], "PlaylistID": playlistID, "Tracks": []}

        items = self.sp.playlist_items(playlistID, additional_types="track")
        tracks = items['items']

        while items['next']:
            items = self.sp.next(items)
            tracks.extend(items['items'])

        for item in tracks:
            track = item['track']
            output["Tracks"].append({
                "Name": track['name'],
                "Artists": [artist['name'] for artist in track['artists']],
                "Release": track['album']['release_date'],
                "CoverURL": track['album']['images'][0]['url'] if track['album']['images'] else None
            })

        return output

    def getAlbumTracks(self, albumID: str) -> dict:
        """
        Fetch tracks from a Spotify album.
        :param albumID: A string representing the Spotify album ID.
        :return: A dictionary containing the album name, ID, and a list of tracks with their details.
        """
        album = self.sp.album(albumID)
        output = {"AlbumName": album["name"], "AlbumID": albumID, "Tracks": []}

        for track in album['tracks']['items']:
            output["Tracks"].append({
                "Name": track['name'],
                "Artists": [artist['name'] for artist in track['artists']],
                "Release": album['release_date'],
                "CoverURL": album['images'][0]['url'] if album['images'] else None
            })

        return output
