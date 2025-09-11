import spacy
from nltk.corpus import stopwords
import nltk

nltk.download("stopwords")
stop_words = set(stopwords.words("portuguese"))

nlp = spacy.load("pt_core_news_sm")

def preprocess_text(text: str) -> str:
    """
    Limpa e normaliza texto em português:
    - lowercase
    - remove stopwords
    - lematização
    """
    doc = nlp(text.lower())
    tokens = [
        token.lemma_
        for token in doc
        if token.is_alpha and token.text not in stop_words
    ]
    return " ".join(tokens)
