from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_email

app = FastAPI(title="Email Classifier API")

class EmailRequest(BaseModel):
    text: str

@app.post("/predict/")
def predict(request: EmailRequest):
    category = predict_email(request.text)
    return {"category": category}
