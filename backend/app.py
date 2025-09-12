from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
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
