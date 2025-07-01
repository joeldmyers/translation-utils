import spacy
import pandas as pd

# Laden Sie das deutsche Sprachmodell
nlp = spacy.load("de_core_news_sm")

# Laden Sie den Text
with open("transcript_combined.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Verarbeiten des Textes
doc = nlp(text)

# Lemmatisieren und filtern (nur alphabetische Tokens)
lemmata = set()
for token in doc:
    if token.is_alpha:
        lemmata.add(token.lemma_.lower())

# In DataFrame umwandeln und als CSV speichern
df = pd.DataFrame(sorted(lemmata), columns=["wort"])
df.to_csv("unique_german_words.csv", index=False)
