FROM python:3-buster

WORKDIR /usr/src/app

COPY src/requirements.txt ./
COPY commands.sh ./

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY src/LanguageDetection .
COPY src/Translation .
COPY src/LanguageMentionsExtraction .

EXPOSE 8002 8003 8004

CMD ["./commands.sh"]