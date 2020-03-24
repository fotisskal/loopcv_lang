FROM python:3-buster

WORKDIR /usr/src/app

COPY src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY LanguageDetection .
COPY Translation .

EXPOSE 8000