import replicate
from dotenv import load_dotenv
import os
from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import pprint
import google.generativeai as palm
import uvicorn

load_dotenv()


palm.configure(api_key=os.environ.get("PALM_API_KEY"))

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/getResponse")
async def getResponse(info : Request):

    print(await info.body())
    infoDict = await info.json()
    infoDict = dict(infoDict)
    

    prompt_input =  infoDict['text']

    completion = palm.generate_text(
        model=model,
        prompt=prompt_input,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )
            
    return {"response" : completion.result}

