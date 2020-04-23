# Introduction
A python language library for language detection and translation


# Language Detection

## API:
Currently 3 different language detection APIs are used:
1. Polyglot (SUGGESTED) :
    - Supports 80+ languages
    - Mixed language detection
    - Most performant method
    - Most accurate method
    - Extremely fast (1000 times faster than other methods)
2. LangDetect:
    - Supports 55 languages out of the box
    - Fast
3. Spacy:
    - Supports 80+ languages
    - Mixed language detection
    - Wrapper of PYCLD2 detector
    - Does not return name of language, only ISO code

# Translation

## API:
Currently 2 different translation APIs are implemented:
1. Py Google Trans API (SUGGESTED) :
    - Implements Google Translate API
    - Project: https://pypi.org/project/googletrans/
    - MAX character limit on a single text translation ~ 15k text length
    - MAX 100 requests per one hour period. 
    - Text given as input must be JSON escaped.
    - If exceeded, returns 429 ERROR (Too many requests). You have to change your public IP address.
    - Translation time ~ 800 msec
2. Translate API:
    - 	Implements Microsoft Translation API(not free) and Translated MyMemory API(free).
    -  	Project: https://pypi.org/project/translate/
    -  	MyMemory provider which is free allows translation of max 10000 words/day.
    - 	MyMemory Issue: QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
      	

# Running:
- Inside loopcv_lang:
    - docker build -f Dockerfile.LanguageDetection --tag LanguageDetection:1.0 .
    
    - docker build -f Dockerfile.LanguageMentionsExtraction --tag LanguageMentionsExtraction:1.0 .
    
    - docker build -f Dockerfile.Translation --tag Translation:1.0 .
    
    - docker run --publish 8000:8000 --detach --name ld LanguageDetection:1.0
    
    - docker run --publish 8000:8000 --detach --name lme LanguageMentionsExtraction:1.0
    
    - docker run --publish 8000:8000 --detach --name trans Translation:1.0
    
 - Hit browser: http://127.0.0.1:8000/docs