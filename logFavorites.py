import spotipy
from spotipy.oauth2 import SpotifyOAuth
import math
import csv
import setVars

setVars.setVars()


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

favNum = 289

data = [["Artist", "Name", "Date","ID", "danceability", "energy", "key", "loudness", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo", "duration"]]

for i in range(math.ceil(289/20)):
    results = sp.current_user_saved_tracks(offset=i*20)
    for idx, item in enumerate(results['items']):
        idx = i*20 + idx
        track = item['track']
        trackID = track['id']
        features = sp.audio_features(trackID)[0]
        data.append([track['artists'][0]['name'], 
                     track['name'],
                     item['added_at'].split("T")[0],
                     trackID,
                     features['danceability'],
                     features['energy'],
                     features['key'],
                     features['loudness'],
                     features['speechiness'],
                     features['acousticness'],
                     features['instrumentalness'],
                     features['liveness'],
                     features['valence'],
                     features['tempo'],
                     features['duration_ms']])
        #print(idx, track['artists'][0]['name'], " – ", track['name'])
    
with open("localdata/favorites.csv", "w",encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerows(data)