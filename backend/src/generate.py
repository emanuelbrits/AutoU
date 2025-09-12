import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "emails_respostas_dataset.csv")
df = pd.read_csv(CSV_PATH)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["email"])

def generate_reply(email_text: str) -> str:
    email_vec = vectorizer.transform([email_text])

    sim_scores = cosine_similarity(email_vec, X).flatten()

    idx_max = sim_scores.argmax()

    return df.iloc[idx_max]["resposta"]

