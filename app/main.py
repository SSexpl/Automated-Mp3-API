from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/')
async def root():
    return {'testData': 'Mp3 Automated Tag Editor up and running!!!', 'code': '200'}

@app.get('/api/metadata/{fileName}')
async def getMetadata(fileName: str, fileCount: int):
    successfulQueries: int = 8
    unSuccessfulQueries: int = 2
    return {'fileName': fileName, 'fileCount': fileCount, 'successfulQueries': successfulQueries, 'unSuccessfulQueries': unSuccessfulQueries}

@app.get('/api/album/{albumName}')
async def getAlbumArt(albumName: str, artistName: str, res: int):
    return {'albumName': albumName, 'artistName': artistName, 'res': res}