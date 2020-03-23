import time

import googletrans
from fastapi import FastAPI
from pydantic import BaseModel
from translate import translate

# 106 languages supported
languages_dict = googletrans.LANGUAGES
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to CV Translation Api"}


# CV string value needs to be escaped
class CV(BaseModel):
    language: str
    cv: str


# "QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS"
@app.post("/translate")
async def translate(request: CV):
    return translate_api(request.language, request.cv)


# 0.7678499221801758
@app.post("/googletrans")
async def pygoogletrans(request: CV):
    return py_google_trans_api(request.language, request.cv)


def translate_api(language, cv):
    start_time = time.time()
    iso_code = list(languages_dict.keys())[list(languages_dict.values()).index(language.lower())]
    print("Text size: %s" % cv.__len__())
    translator = translate.Translator(to_lang=iso_code)
    translated_text = translator.translate(cv)
    print(time.time() - start_time)
    return translated_text


def py_google_trans_api(language, cv):
    start_time = time.time()
    translator = googletrans.Translator()
    iso_code = list(languages_dict.keys())[list(languages_dict.values()).index(language.lower())]
    print("Text size: %s" % cv.__len__())
    translated_text = translator.translate(cv, dest=iso_code).text
    print(time.time() - start_time)
    return "r'%s'" % translated_text
