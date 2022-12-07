import pickle
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import math
import setVars

setVars.setVars()


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def makeid(length):
    result = "";
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    charactersLength = len(characters)
    for i in range(length):
        result += characters[math.floor(random.random() * charactersLength)];
    return result;

#To make life easier, you can only have multiples of 50. Also not checking for duplicates
def generateRandomSongs(numSongs=50,queryLength=2):
    if(round(numSongs/50) != numSongs/50):
        raise Exception("Try again (this time with a multiple of 50 for numSongs)")
        
    songs = []
    
    for i in range(math.floor(numSongs/50)):
        query = makeid(queryLength)
        try:
            results = sp.search(query, limit=50, offset=int(random.random()*10))
        except Exception as e:
            continue
        songs.append([song['id'] for song in results['tracks']['items']])
    return songs[0]
        


with open('models/favSVM.pkl', 'rb') as f:
    clf = pickle.load(f)


iter = 0

while True:
    randSongs = generateRandomSongs()
    audioFeatures = sp.audio_features(tracks=randSongs)
    formattedData = []
    for s in audioFeatures:
        try:
            formattedData.append([s['danceability'], s['energy'], s['key'], 
                        s['loudness'], s['speechiness'], s['acousticness'], 
                        s['instrumentalness'], s['liveness'], s['valence'], 
                        s['tempo'], s['duration_ms']])
        except Exception:
            continue
        
    inferences = clf.predict(formattedData)
    print(inferences)
        