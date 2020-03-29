import pycountry
import spacy
from fastapi import FastAPI
from pydantic import BaseModel
from spacy_langdetect import LanguageDetector
from langdetect import DetectorFactory, detect_langs
from polyglot.detect import Detector

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Language Detection Api"}


class JobPost(BaseModel):
    text: str


@app.post("/polyglot")
async def polyglot(request: JobPost):
    return polyglot_detect(request.text)


@app.post("/langdetect")
async def langdetect(request: JobPost):
    return lang_detect(request.text)


@app.post("/spacy")
async def langdetect(request: JobPost):
    return spacy_detect(request.text)


def lang_detect(text_to_detect):
    DetectorFactory.seed = 0
    top_iso_codes = detect_langs(text_to_detect)
    iso_code = top_iso_codes[0].lang
    confidence = top_iso_codes[0].prob
    language = pycountry.languages.get(alpha_2=iso_code)
    language_info = {
        "name": language.name,
        "code": iso_code,
        "confidence": confidence
    }
    return language_info


def spacy_detect(text_to_detect):
    nlp = spacy.load('en')
    nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)
    doc = nlp(text_to_detect)
    language_info = {
        "code": doc["language"],
        "confidence": doc["score"]
    }
    return language_info


def polyglot_detect(text_to_detect):
    polyglot_info = Detector(text_to_detect).languages[0]
    lang_name = polyglot_info.name
    lang_code = polyglot_info.code
    lang_confidence = polyglot_info.confidence
    language_info = {
        "name": lang_name,
        "code": lang_code,
        "confidence": lang_confidence
    }
    return language_info
