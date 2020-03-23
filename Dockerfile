FROM python:3-buster

COPY src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY LanguageDetection .
COPY Translation .

EXPOSE 8000