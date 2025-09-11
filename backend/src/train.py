import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import joblib
from preprocess import preprocess_text
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "emails_dataset.csv")

df = pd.read_csv(CSV_PATH)

df["cleaned"] = df["email"].apply(preprocess_text)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["cleaned"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = MultinomialNB()
clf.fit(X_train, y_train)

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(clf, os.path.join(MODEL_DIR, "naive_bayes.pkl"))
joblib.dump(vectorizer, os.path.join(MODEL_DIR, "vectorizer.pkl"))

print("Modelo treinado e salvo em /models/")
