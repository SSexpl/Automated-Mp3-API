import google.generativeai as palm
from dotenv import load_dotenv
import re
import os

async def getFields(artist, title):
    load_dotenv()
    clientSe = os.getenv("PALM")
    palm.configure(api_key=clientSe)

    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    prompt = "Find the album, year, track, genre, album artist, composer, disc-number and comments for given song "+title+" by "+artist+". Return format example: #album: albumname, #year: year, #track: track, #genre: genre, #album-artist: album-artist(s), #composer: composer(s), #disc-number: disc-number, #comments: comments"

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=1200, # The maximum length of the response
    )

    #  [artist, title, album, year, track, genre, comments, albumArtist, composer, discno, successfulFieldCalls

    result: str = (completion.result).split("#")
    dict = {}
    successfulFieldCalls = 0

    for i, s in enumerate(result):
        str = re.sub(',', '', result[i])
        str = str.strip()
        idx = str.rfind(":")
        if idx == -1: continue
        key = str[:idx]
        value = str[idx+2:]
        dict[key]=value
        if(value=='None' or value=='' or value=='NaN'): continue
        successfulFieldCalls += 1

    dict["successfulCalls"]=successfulFieldCalls+2 #add artist name and title

    return dict
