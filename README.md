# SpotifyTools
Collection of tools used to play around with Spotify data


In Use:

    trainFavPrediction.py - generate SVM to determine 'likeability' of a song based on Spotify audio features

    spotifyRecs.py - generate Spotify recommendations based on select seeds from 'favorites.csv'

    graphActivity.py - graph relevant data from 'favorites.csv'

    logFavorites.py - pull songs from "Liked Songs" collection and save to 'favorites.csv'

    filteredRecs.py - filter results from spotifyRecs with 'favSVM' and save to playlist




You need to set API credentials as environment variables

SPOTIPY_CLIENT_ID=''

SPOTIPY_CLIENT_SECRET='' 

SPOTIPY_REDIRECT_URI=''