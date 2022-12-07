import pickle
from spotifyRecs import pullRecs
from utility import *
import uuid
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', help="Number of songs to pull and filter",default=100, type=int) 
    args = parser.parse_args()

    rawData = pullRecs(args.count)
    songs = [rawData[key][1] for key in rawData.keys()]
    recs = filterSongs(songs)
    createPlaylist("Generated Recommendations "+ str(uuid.uuid4()), recs)

def filterSongs(songs):
    with open('models/favSVM.pkl', 'rb') as f:
        clf = pickle.load(f)
        
    chunks = list(divide_chunks(songs, 100))
    audioFeatures = []
    for chunk in chunks:
        audioFeatures.append(sp.audio_features(tracks=chunk))
    formattedData = []
    for mm in audioFeatures:
        for s in mm:
            try:
                formattedData.append([s['danceability'], s['energy'], s['key'], 
                            s['loudness'], s['speechiness'], s['acousticness'], 
                            s['instrumentalness'], s['liveness'], s['valence'], 
                            s['tempo'], s['duration_ms']])
            except Exception:
                formattedData.append([0,0,0,0,0,0,0,0,0,0,0])
                continue
    inferences = clf.predict(formattedData)
    zipped = {songs[i]: inferences[i] for i in range(len(songs))}
    recs = {k:zipped[k] for k in zipped.keys() if zipped[k] == 1}
    return recs.keys()

if __name__ =="__main__":
    main()