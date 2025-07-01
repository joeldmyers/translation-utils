import csv
from deep_translator import GoogleTranslator

with open('unique_german_words.csv', newline='', encoding='utf-8') as infile, \
     open('output.csv', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer.writerow(['German', 'English'])  # Header

    for row in reader:
        german_word = row[0]
        english_word = GoogleTranslator(source='de', target='en').translate(german_word)
        writer.writerow([german_word, english_word])
