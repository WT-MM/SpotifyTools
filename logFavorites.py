import spotipy
from spotipy.oauth2 import SpotifyOAuth
import math
import csv




scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

favNum = 289

data = []

for i in range(math.ceil(289/20)):
    results = sp.current_user_saved_tracks(offset=i*20)
    for idx, item in enumerate(results['items']):
        idx = i*20 + idx
        track = item['track']
        data.append([idx, track['artists'][0]['name'], track['name'],item['added_at']])
        #print(idx, track['artists'][0]['name'], " – ", track['name'])

    
with open("localdata/out.csv", "w",encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerows(data)