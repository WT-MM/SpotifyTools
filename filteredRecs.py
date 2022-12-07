import pickle
from spotifyRecs import pullRecs
from utility import *
import uuid




with open('models/favSVM.pkl', 'rb') as f:
    clf = pickle.load(f)


iter = 0


rawData = pullRecs(100)
songs = [rawData[key][1] for key in rawData.keys()]
audioFeatures = sp.audio_features(tracks=songs)
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
zipped = {songs[i]: inferences[i] for i in range(len(songs))}
recs = {k:zipped[k] for k in zipped.keys() if zipped[k] == 1}

createPlaylist("Generated Recommendations "+ str(uuid.uuid4()), recs.keys())