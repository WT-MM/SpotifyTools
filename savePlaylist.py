import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import math
import csv

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
        try:
            features = sp.audio_features(trackID)[0]
        except:
            print(sys.exc_info()[0])
            continue
        
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