import os
import shutil
from fastapi import FastAPI, File, UploadFile
from fastapi import FastAPI, Request, Query
import freeGPT
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/api/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save the file to a temporary location
        file_path = os.path.join("./temp_files", file.filename)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Perform any additional processing if required
        # Your code here...

        return {"message": "File uploaded successfully"}
    except Exception as e:
        return {"error": str(e)}


@app.post("/api/gpt")
async def gpt(info : Request):
    
    req_info = await info.json()
    req_info = dict(req_info)

    resp = await getattr(freeGPT, "gpt4").Completion.create(req_info['text'])

    return {"result" : resp}