from Regex.Regex import getArtistandTitle
import asyncio
from Controllers import Deezer
from Controllers import Discogs
from Controllers import Ganna
from Controllers import GooglePage
from Controllers import MusicApi
from Controllers import MusicBrainz
from Controllers import MusicStory
from Controllers import OpenAi
from Controllers import Shazam
from Controllers import Spotify
from Controllers import TheAudioData
from Controllers import TheAudioDB
from Controllers import Wikipedia
from Controllers import Palm
from Controllers import YoutubeMusic
from pprint import pprint

# Total Number of possible Subqueries = 14 mechanisms * 10 fields = 80
# TOTAL_FIELDS: int = 10
# TOTAL_MECHANISMS: int = len(os.listdir(os.getcwd()+ r"\Controllers")) - 1
# TOTAL_MECHANISMS = 14
# TOTAL_QUERIES: int = TOTAL_MECHANISMS * TOTAL_FIELDS


async def classifier(query: str):
    # First use regex to retreieve values from Regex folder's OpenAi.py
    data = await getArtistandTitle(query=query)

    if len(data) == 1:
        return "Error: Unable to parse artist and title from file name"

    artist: str = data[0].strip()
    title: str = data[1].strip()

    # Call each mechanism and store fields into array
    # Return type is as follows:
    #  [artist, title, album, year, track, genre, comments, albumArtist, composer, discno, successfulFieldCalls

    # deezer:         str = await Deezer.getFields(artist, title)
    # discogs:        str = await Discogs.getFields(artist, title)
    # ganna:          str = await Ganna.getFields(artist, title)
    # googleSPage:    str = await GooglePage.getFields(artist, title)
    # musicApi:       str = await MusicApi.getFields(artist, title)
    # musicBrainz:    str = await MusicBrainz.getFields(artist, title)
    # musicStory:     str = await MusicStory.getFields(artist, title)
    # oneMusic:       str = await OneMusicApi.getFields(artist, title)
    # openAi:         str = await OpenAi.getFields(artist, title)
    # shazam:         str = await Shazam.getFields(artist, title)
    # audioData:      str = await TheAudioData.getFields(artist, title)
    # audioDb:        str = await TheAudioDB.getFields(artist, title)
    # wikipedia:      str = await Wikipedia.getFields(artist, title)

    # async multi-call
    results = await asyncio.gather(
        Spotify.getFields(artist, title),
        Palm.getFields(artist, title),
        YoutubeMusic.getFields(artist, title),
    )

    # #Classify each value for most probable solution
    # album:          str = classify([deezer[2], discogs[2], ganna[2], googleSPage[2], musicApi[2], musicBrainz[2], musicStory[2], oneMusic[2], openAi[2], palm[2] shazam[2], spotify[2], audioData[2], audioDb[2], wikipedia[2]])
    # year:           str = classify([deezer[3], discogs[3], ganna[3], googleSPage[3], musicApi[3], musicBrainz[3], musicStory[3], oneMusic[3], openAi[3], palm[3] shazam[3], spotify[3], audioData[3], audioDb[3], wikipedia[3]])
    # track:          str = classify([deezer[4], discogs[4], ganna[4], googleSPage[4], musicApi[4], musicBrainz[4], musicStory[4], oneMusic[4], openAi[4], palm[4] shazam[4], spotify[4], audioData[4], audioDb[4], wikipedia[4]])
    # genre:          str = classify([deezer[5], discogs[5], ganna[5], googleSPage[5], musicApi[5], musicBrainz[5], musicStory[5], oneMusic[5], openAi[5], palm[5] shazam[5], spotify[5], audioData[5], audioDb[5], wikipedia[5]])
    # comments:       str = classify([deezer[6], discogs[6], ganna[6], googleSPage[6], musicApi[6], musicBrainz[6], musicStory[6], oneMusic[6], openAi[6], palm[6] shazam[6], spotify[6], audioData[6], audioDb[6], wikipedia[6]])
    # albumArtist:    str = classify([deezer[7], discogs[7], ganna[7], googleSPage[7], musicApi[7], musicBrainz[7], musicStory[7], oneMusic[7], openAi[7], palm[7] shazam[7], spotify[7], audioData[7], audioDb[7], wikipedia[7]])
    # composer:       str = classify([deezer[8], discogs[8], ganna[8], googleSPage[8], musicApi[8], musicBrainz[8], musicStory[8], oneMusic[8], openAi[8], palm[8] shazam[8], spotify[8], audioData[8], audioDb[8], wikipedia[8]])
    # discno:         int = classify([deezer[9], discogs[9], ganna[9], googleSPage[9], musicApi[9], musicBrainz[9], musicStory[9], oneMusic[9], openAi[9], palm[9] shazam[9], spotify[9], audioData[9], audioDb[9], wikipedia[9]])
    classifiedResults = await classify(results)

    calls: int = {}
    # calls["successfulFieldCalls"] = palm.get("successfulCalls")
    calls["successfulMechanismCalls"] = 0
    calls["successfulQueries"] = 0

    # totalCalls = {} # App Side
    # totalCalls["totalFieldCalls"] = 0
    # totalCalls["totalMechanismCalls"] = 0
    # totalCalls["totalSuccessfulCalls"] = 0

    # successfulFieldCalls: int = [deezer[10], discogs[10], ganna[10], googleSPage[10], musicApi[10], musicBrainz[10], musicStory[10], oneMusic[10], openAi[10], shazam[10], spotify[10], audioData[10], audioDb[10], wikipedia[10]]
    # successfulMechanismCalls: int = 14 # Add 1 for every controller that returns atleast 1 successful sub-field
    # successfulQueries: int = 140 # successful mechanism calls for each controller added up

    # return {"artist": artist,"title": title, "palm":palm, "spotify": spotify}

    # return artist, title, album, year, track, genre, comments, albumArtist, composer, discno,successfulFieldCalls, successfulMechanismCalls, successfulQueries
    return {
        "artist": artist,
        "title": title,
        "data": classifiedResults,
        "successfulCalls": calls,
        # "totalCalls": totalCalls,
    }


async def classify(dict):
    arrays = {
        "artist": [],
        "title": [],
        "album": [],
        "year": [],
        "track": [],
        "genre": [],
        "comments": [],
        "albumArtist": [],
        "composer": [],
        "discno": [],
    }
    finClassifiedResult = {}
    totalSuccesfulCalls = 0

    for x in dict:
        if x.get("artist") != None:
            totalSuccesfulCalls += 1
            arrays["artist"].append(x.get("artist"))

        if x.get("title") != None:
            totalSuccesfulCalls += 1
            arrays["title"].append(x.get("title"))

        if x.get("album") != None:
            totalSuccesfulCalls += 1
            arrays["album"].append(x.get("album"))

        if x.get("year") != None:
            totalSuccesfulCalls += 1
            arrays["year"].append(int(x.get("year")))

        if x.get("track") != None:
            totalSuccesfulCalls += 1
            arrays["track"].append(int(x.get("track")))

        if x.get("comments") != None:
            totalSuccesfulCalls += 1
            arrays["comments"].append(x.get("comments"))

        if x.get("album-artist") != None:
            totalSuccesfulCalls += 1
            arrays["albumArtist"].append(x.get("album-artist"))

        if x.get("composer") != None:
            totalSuccesfulCalls += 1
            arrays["composer"].append(x.get("composer"))

        if x.get("disc-number") != None:
            totalSuccesfulCalls += 1
            arrays["discno"].append(int(x.get("disc-number")))

        if x.get("genre") != None:
            if type(x.get("genre")) == list:
                for vals in x.get("genre"):
                    arrays["genre"].append(vals)
                totalSuccesfulCalls += 1
            else:
                arrays["genre"].append(x.get("genre"))
                totalSuccesfulCalls += 1

        if x.get("successfulCalls") == 10:
            finClassifiedResult["successfulMechanismCalls"] += 1

    # test1 = await classifyArray(arrays.get('artist'), "str"),
    # test1 = await classifyArray(arrays.get('title'), "str"),
    # test1 = await classifyArray(arrays.get('album'), "str"),
    # test1 = await classifyArray(arrays.get('year'), "num"),
    # test1 = await classifyArray(arrays.get('track'), "num"),
    # test1 = await classifyArray(arrays.get('comments'), "str"),
    # test1 = await classifyArray(arrays.get('album-artist'), "str"),
    # test1 = await classifyArray(arrays.get('composer'), "str"),
    # test1 = await classifyArray(arrays.get('disc-number'), "num"),
    # test1 = await classifyArray(arrays.get('genre'), "str")

    data = await asyncio.gather(
        classifyArray(arrays.get("artist"), "str", "artist"),
        classifyArray(arrays.get("title"), "str", "title"),
        classifyArray(arrays.get("album"), "str", "album"),
        classifyArray(arrays.get("year"), "num", "year"),
        classifyArray(arrays.get("track"), "num", "track"),
        classifyArray(arrays.get("comments"), "str", "comments"),
        classifyArray(arrays.get("albumArtist"), "str", "albumArtist"),
        classifyArray(arrays.get("composer"), "str", "composer"),
        classifyArray(arrays.get("discno"), "num", "discno"),
        classifyArray(arrays.get("genre"), "str", "genre"),
    )

    finClassifiedResult["totalSuccesfulCalls"] = totalSuccesfulCalls
    finClassifiedResult["data"] = data

    return finClassifiedResult


async def classifyArray(array, type, key):
    # Use fuzzy string searching or vector string similarity matching

    # Iterate thru each value check its ratio with the others. One with highest value wins - use fuzzy search
    # - if succesffuly classified - +1 to succesffuly classified
    # - if cannot be determined (like 4, 5) - return suggested value + error code yellow (medium)
    # - if cannot be classified (NaN) - return no value w/ error code red

    print(array)
    return (array, type)
