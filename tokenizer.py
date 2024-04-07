import spacy
import re
import string
from spacy.lang.en.stop_words import STOP_WORDS
import pickle

with open('en_core_web_md.pickle', 'rb') as file:
    nlp = pickle.load(file)

punctuations = string.punctuation

def tokenizer(text):
    # Remove <br /> tags, emojis
    clean_text = re.sub('<br\s*/?>', '', text)
    clean_text = re.sub(':\S+', '', clean_text)

    doc = nlp(clean_text)
    # lemmatize -> remove stopwords and punctuations
    lemma_tokens = [token.lemma_ for token in doc if token.pos_ !='PRON']
    clean_tokens = ' '.join([token.lower() for token in lemma_tokens if token not in STOP_WORDS and token not in punctuations])

    return clean_tokens

def sentiment(result):
    if result > 0:
        return "Positive"
    else:
        return "Negative"