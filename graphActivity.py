import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
import math



def favoritesOverTime(df):
    plt.figure()
    df['visdata'] = matplotlib.dates.date2num(df.loc[:,"Date"].loc[::-1])
    plt.plot_date(df['visdata'], list(range(df.shape[0])))
    plt.title("Length of Favorites Playlist Over Time")
    plt.xlabel("Date")
    plt.ylabel("# Of Songs")

def favoritesOverDuration(df):
    plt.figure()
    df['roundedDuration'] = round(df.loc[:,"duration"]/10000)*10
    durationFreq = df.loc[:,'roundedDuration'].value_counts()
    plt.scatter(durationFreq.keys(), durationFreq[:])
    plt.title("Frequency to Song Length (rounded to 10s of seconds)")
    plt.xlabel("Song length in seconds")
    plt.ylabel("Frequency in Favorites")
    plt.figtext(0.99, 0, "mean duration: " + str(df.loc[:,'roundedDuration'].mean()), horizontalalignment='right')
    
def favoritesTenpo(df):
    plt.figure()
    df['roundedTempo'] = (round(df.loc[:,'tempo']/8)*8)
    tempoFreq = df.loc[:,'roundedTempo'].value_counts()
    plt.scatter(tempoFreq.keys(),tempoFreq[:])
    plt.title("Frequency to Tempo (divided by 8)")
    plt.xlabel("Tempo")
    plt.ylabel("# of Songs")
    plt.figtext(0.99, 0.01, "mean tempo: " + str(df.loc[:,'roundedTempo'].mean()), horizontalalignment='right')
    
    


favDF = pd.read_csv('localdata/favorites.csv')

favoritesOverTime(favDF)

favoritesOverDuration(favDF)

favoritesTenpo(favDF)

plt.show()
