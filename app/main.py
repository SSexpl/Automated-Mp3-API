from fastapi import FastAPI
from classifier import classifier
from Image import GetAlbumArt

app = FastAPI()

@app.get('/', status_code=200)
async def root():
    return {"status": 200, 'log': 'Mp3 Automated Tag Editor up and running!!!'}

@app.get('/api/metadata/{fileName}')
async def getMetadata(fileName: str):
    data = await classifier(fileName)
    #Format return of data accordingly
    return data

@app.get('/api/album/{albumName}')
async def getAlbumArt(albumName: str, artistName: str, res: int):
    data = await GetAlbumArt.getAlbumArt(albumName, artistName, res)
    return data