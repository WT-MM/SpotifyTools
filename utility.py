import spotipy
from spotipy.oauth2 import SpotifyOAuth
import setVars

setVars.setVars()

scope = "user-library-read playlist-modify-private playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

userID = sp.me()['id']

def createPlaylist(name, tracks):
    sp.user_playlist_create(userID, name, public=False)
    playlists = sp.current_user_playlists()
    for i in playlists['items']:
        if i['name'] == name:
            playlist=i['id']
            break
    trackChunks = divide_chunks(list(tracks), 100)
    for i in trackChunks:  
        sp.playlist_add_items(playlist, i)
    
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]