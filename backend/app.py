from http.client import HTTPException
import os
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.extractText import extract_text_from_file
from src.predict import predict_email
from src.generate import generate_reply

app = FastAPI(title="Email Classifier API")

origins = [
    "http://localhost:5173", 
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],         
    allow_headers=["*"],        
)

class EmailRequest(BaseModel):
    text: str

@app.post("/predict/")
def predict(request: EmailRequest):
    category = predict_email(request.text)
    response = generate_reply(request.text)
    return {"category": category, "response": response}

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    try:
        temp_file = f"temp_{file.filename}"
        with open(temp_file, "wb") as f:
            f.write(await file.read())

        text = extract_text_from_file(temp_file)

        os.remove(temp_file)

        return {"filename": file.filename, "text": text}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
