import google.generativeai as palm
from dotenv import load_dotenv
import os

async def getArtistandTitle(query: str):
    load_dotenv()
    clientSe = os.getenv("PALM")
    palm.configure(api_key=clientSe)

    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    prompt = "Extract the artist name and song name from this piece of text: "+query

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )
    result: str = (completion.result).split(",")

    return result

    #return [0].strip(),result[1].strip()
