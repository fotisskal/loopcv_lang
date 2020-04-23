FROM python:3-buster

WORKDIR /usr/src/app

COPY src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY src/LanguageDetection .

EXPOSE 8000

CMD ["uvicorn", "LanguageDetection/detect_language:app", "--port", "8000", "--reload"]