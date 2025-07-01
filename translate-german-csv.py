import pandas as pd
from deep_translator import GoogleTranslator

df = pd.read_csv("unique_german_words.csv")
df['english'] = df['wort'].apply(lambda x: GoogleTranslator(source='de', target='en').translate(x))
df.to_csv("german_words_with_english.csv", index=False)
print("Fertig! Datei: german_words_with_english.csv")
