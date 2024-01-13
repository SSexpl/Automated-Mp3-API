import requests
import os
from pprint import pprint 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
key=os.environ.get('Genius Token')
async def getFields(artist, title):
    base_url ="https://api.genius.com/search?q="+title+"+"+artist
    headers = {
        "Authorization": "Bearer AXAstvuuSIYEwyM_Ja6OdMeFkZHNGzgtMm6AQL57zz3VPFBDPTwvkZY0E0cCnmXO"
    }
    successfields=2
    response=  requests.get(base_url,headers=headers)
    dict = {}
    # Check if the request was successful (status code 200)
    try:
        # Parse and return the JSON response
         
         
         res=response.json()
         trial=res['response']['hits'][0]['result']
         if(trial['full_title']):
             dict['song_title']=trial['full_title']
             successfields+=1
         if(trial['artist_names']):
             dict['album-artist']=trial['artist_names']
             successfields+=1
         if(trial["release_date_components"]['year']):
             dict['year']=trial["release_date_components"]['year']
             successfields+=1
       
    
       

       
    except:
        # Print an error message if the request was not successful
        print("Error Occured: Data nulled")
        dict['artist'] = dict['song_title'] = dict['album'] = dict['year'] = dict['track'] = dict['genre'] = dict['comments'] = dict['albumArtist'] = dict['composer'] = dict['disc_number'] = None
        successfulFieldCalls = 0
        
    dict['successfulCalls'] =  successfields
    print(dict)
    return dict
# Example usage:


# Print the result
#print(result)
