import joblib
from .preprocess import preprocess_text
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "naive_bayes.pkl")
clf = joblib.load(MODEL_PATH)

VECTOR_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "vectorizer.pkl")
vectorizer = joblib.load(VECTOR_PATH)

def predict_email(text: str) -> str:
    processed = preprocess_text(text)
    vectorized = vectorizer.transform([processed])
    prediction = clf.predict(vectorized)[0]
    return prediction

if __name__ == "__main__":
    email = "Olá, gostaria de ajuda para atualizar meu cadastro."
    print(predict_email(email)) 
