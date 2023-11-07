from ytmusicapi import YTMusic
from pprint import pprint 

async def getFields(artist, title):
    yt = YTMusic()
    successfulFieldCalls = 0
    dict = {}
    query = title + " " + artist

    try:
        search_results = yt.search(query, filter="songs", ignore_spelling=False)

        if search_results[0].get('album').get('name'):
            dict['album'] = search_results[0].get('album').get('name')
            successfulFieldCalls += 1

        if search_results[0].get('artists'):
            dict['artist'] = search_results[0].get('artists')[0].get('name')
            if(len(search_results[0].get('artists'))>1):
                listOfartists = []
                for x in search_results[0].get('artists'):
                    listOfartists.append(x.get('name'))
                dict['album-artist'] = dict['composer'] = listOfartists
            else:
                dict['album-artist'] = dict['composer'] = dict.get('artist')
            successfulFieldCalls += 3

        if search_results[0].get('year'):
            dict['year'] = search_results[0].get('year')
            successfulFieldCalls += 1
        elif search_results[0].get('year') == None:
            dict['year'] = None

        if search_results[0].get('title'):
            dict['title'] = search_results[0].get('title')
        else:
            dict['title'] = title
        successfulFieldCalls += 1

        dict['track'] = dict['genre'] = dict['comments'] = dict['disc_number'] = None
        
    except:
        print("Err")
        dict['artist'] = dict['song_title'] = dict['album'] = dict['year'] = dict['track'] = dict['genre'] = dict['comments'] = dict['albumArtist'] = dict['composer'] = dict['disc_number'] = None
        successfulFieldCalls = 0
    
    dict['successfulCalls'] = successfulFieldCalls

    return dict