import spotipy
from spotipy.oauth2 import SpotifyOAuth
import math
import csv

import os

os.environ['SPOTIPY_CLIENT_ID'] = '1d2a39cf5b71423596472455d622fea3'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'caaaa9882763499899c5704aa801d365'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:9090'

playlist_id = "5S8SJdl1BDc0ugpkEvFsIL"
playlist_name = "longplaylist"

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

length = 10000

data = [["Artist", "Name", "Date","ID", "danceability", "energy", "key", "loudness", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo", "duration"]]

for i in range(math.ceil(length/100)):
    results = sp.playlist_items(playlist_id, offset=i*100)
    for idx, item in enumerate(results['items']):
        idx = i*100 + idx
        track = item['track']
        trackID = track['id']
        artist = track['artists'][0]['name']
        features = sp.audio_features(trackID)[0]
        
        #Janky add-in to trim disliked songs data
        if artist in ["Taylor Swift", "Bruno Mars"]:
            continue
        
        data.append([artist, 
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
    print("Pass " + str(i))

        
print("Writing to CSV")

print(len(data))

with open("localdata/" + playlist_name + ".csv", "w",encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerows(data)