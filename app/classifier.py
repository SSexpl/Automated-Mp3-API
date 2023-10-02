from Regex.OpenAi import getArtistandTitle
import os
from Controllers import Deezer
from Controllers import Discogs
from Controllers import Ganna
from Controllers import GooglePage
from Controllers import MusicApi
from Controllers import MusicBrainz
from Controllers import MusicStory
from Controllers import OneMusicApi
from Controllers import OpenAi
from Controllers import Shazam
from Controllers import Spotify
from Controllers import TheAudioData
from Controllers import TheAudioDB
from Controllers import Wikipedia

# Total Number of possible Subqueries = 14 mechanisms * 10 fields = 80
TOTAL_FIELDS: int = 10
TOTAL_MECHANISMS: int = len(os.listdir(os.getcwd()+ r"\Controllers")) - 1
#TOTAL_MECHANISMS = 14
TOTAL_QUERIES: int = 140

async def classifier(query: str):

    #First use regex to retreieve values from Regex folder's OpenAi.py
    artist, title = await getArtistandTitle(query=query)

    # Call each mechanism and store fields into array
    # Return type is as follows:
    #  [artist, title, album, year, track, genre, comments, albumArtist, composer, discno, successfulFieldCalls
    
    deezer:         str = await Deezer.getFields(artist, title)
    discogs:        str = await Discogs.getFields(artist, title)
    ganna:          str = await Ganna.getFields(artist, title)
    googleSPage:    str = await GooglePage.getFields(artist, title)
    musicApi:       str = await MusicApi.getFields(artist, title)
    musicBrainz:    str = await MusicBrainz.getFields(artist, title)
    musicStory:     str = await MusicStory.getFields(artist, title)
    oneMusic:       str = await OneMusicApi.getFields(artist, title)
    openAi:         str = await OpenAi.getFields(artist, title)
    shazam:         str = await Shazam.getFields(artist, title)
    spotify:        str = await Spotify.getFields(artist, title)
    audioData:      str = await TheAudioData.getFields(artist, title)
    audioDb:        str = await TheAudioDB.getFields(artist, title)
    wikipedia:      str = await Wikipedia.getFields(artist, title)

    #Classify each value for most probable solution
    album:          str = classify([deezer[2], discogs[2], ganna[2], googleSPage[2], musicApi[2], musicBrainz[2], musicStory[2], oneMusic[2], openAi[2], shazam[2], spotify[2], audioData[2], audioDb[2], wikipedia[2]]) 
    year:           str = classify([deezer[3], discogs[3], ganna[3], googleSPage[3], musicApi[3], musicBrainz[3], musicStory[3], oneMusic[3], openAi[3], shazam[3], spotify[3], audioData[3], audioDb[3], wikipedia[3]]) 
    track:          str = classify([deezer[4], discogs[4], ganna[4], googleSPage[4], musicApi[4], musicBrainz[4], musicStory[4], oneMusic[4], openAi[4], shazam[4], spotify[4], audioData[4], audioDb[4], wikipedia[4]]) 
    genre:          str = classify([deezer[5], discogs[5], ganna[5], googleSPage[5], musicApi[5], musicBrainz[5], musicStory[5], oneMusic[5], openAi[5], shazam[5], spotify[5], audioData[5], audioDb[5], wikipedia[5]]) 
    comments:       str = classify([deezer[6], discogs[6], ganna[6], googleSPage[6], musicApi[6], musicBrainz[6], musicStory[6], oneMusic[6], openAi[6], shazam[6], spotify[6], audioData[6], audioDb[6], wikipedia[6]]) 
    albumArtist:    str = classify([deezer[7], discogs[7], ganna[7], googleSPage[7], musicApi[7], musicBrainz[7], musicStory[7], oneMusic[7], openAi[7], shazam[7], spotify[7], audioData[7], audioDb[7], wikipedia[7]]) 
    composer:       str = classify([deezer[8], discogs[8], ganna[8], googleSPage[8], musicApi[8], musicBrainz[8], musicStory[8], oneMusic[8], openAi[8], shazam[8], spotify[8], audioData[8], audioDb[8], wikipedia[8]]) 
    discno:         int = classify([deezer[9], discogs[9], ganna[9], googleSPage[9], musicApi[9], musicBrainz[9], musicStory[9], oneMusic[9], openAi[9], shazam[9], spotify[9], audioData[9], audioDb[9], wikipedia[9]]) 

    successfulFieldCalls: int = [deezer[10], discogs[10], ganna[10], googleSPage[10], musicApi[10], musicBrainz[10], musicStory[10], oneMusic[10], openAi[10], shazam[10], spotify[10], audioData[10], audioDb[10], wikipedia[10]]

    successfulMechanismCalls: int = 14 # Add 1 for every controller that returns atleast 1 successful sub-field
    successfulQueries: int = 140 # successful mechanism calls for each controller added up

    return artist, title, album, year, track, genre, comments, albumArtist, composer, discno,successfulFieldCalls, successfulMechanismCalls, successfulQueries

def classify(arr):
    # Use fuzzy string searching or vector string similarity matching
    finClassifiedValue = 0
    return finClassifiedValue