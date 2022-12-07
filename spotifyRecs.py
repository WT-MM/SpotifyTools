import random
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import math
import json
import setVars

setVars.setVars()

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


numSongs = 300
songRecs ={}

favDF = pd.read_csv('localdata/favorites.csv')

#seems like URL length limits track seeds to ~5 songs long
seedTracks = random.choices(favDF.loc[:,'ID'], k=5)

if numSongs < 100:
    results = sp.recommendations(seed_tracks=list(seedTracks),limit=numSongs)
    for song in results['tracks']:
        songRecs[[song['name']]] = song['external_urls']['spotify']
else:
    for i in range(math.ceil(numSongs/100)):
        results = sp.recommendations(seed_tracks=list(seedTracks),limit=100)
        for song in results['tracks']:
            if song['id'] not in list(favDF.loc[:,'ID']):
                songRecs[song['name']] = [song['external_urls']['spotify'], song['id']]
            else:
                print("Skipped " + song['name'])
        seedTracks = random.choices(favDF.loc[:,'ID'], k=5)
        
with open("localdata/spotifyrecommendations.json", "w") as outfile:
    json.dump(songRecs, outfile)


