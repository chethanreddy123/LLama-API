import replicate
from dotenv import load_dotenv
import os
from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


load_dotenv()


os.environ['REPLICATE_API_TOKEN'] = os.environ.get("LLAMA_API_KEY")


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

    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', 
                               input={"prompt": f"{prompt_input}: ",
                                      "temperature":0.1, "top_p":0.9, "max_length":512, "repetition_penalty":1})

    full_response = ''
    for item in output:
        full_response += item
        
    return {"response" : full_response}