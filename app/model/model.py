import pickle
import re
from pathlib import Path

model_in = open("Predict_Language.pkl", "rb")
lb = pickle.load(model_in)

classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]


def predict_pipleine(text):
    text = re.sub(r"[!@$%(), \n" "^&*?\:`0-9]", " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    pred = lb.predict([text])
    return classes[pred[0]]
