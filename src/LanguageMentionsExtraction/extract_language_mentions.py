from fastapi import FastAPI
from pydantic import BaseModel
import spacy
nlp = spacy.load('en_core_web_sm')

import collections

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Language Mention Extraction Api"}


class LanguageMentionsRequest(BaseModel):
    english_text: str

@app.post("/language_mentions_request")
async def find_languages(request: LanguageMentionsRequest):
    doc = nlp(request.english_text.title()) # now 'english', not only 'English' is recognized

    with open('list_of_languages.txt', 'rt') as f:
        official_language_names = [line.strip('"\n ') for line in f.readlines()]

    detected_languages = [ent.text for ent in doc.ents 
        if ent.label_ in ['LANGUAGE','GPE','NORP']] # fairly lenient
    print(detected_languages)

    def official_name(original): # fuzzy search in official names
        
        Result = collections.namedtuple('Result', 'name score')

        def distance_from_original(name):
            counter = 0
            for letter in name.lower():
                if letter in original.lower():
                    counter+=1
            return Result(name=name, score=counter / len(name))

        results = list(map(distance_from_original, official_language_names))
        return max(results, key=lambda x: x.score).name

    unique_langs = {official_name(lang) for lang in detected_languages}
    return list(unique_langs)