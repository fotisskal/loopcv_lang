FROM python:3-buster

WORKDIR /usr/src/app

COPY src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY LanguageDetection .
COPY Translation .
COPY LanguageMentionsExtraction .

EXPOSE 8000
