# Introduction
A python language library for language detection and translation


# Language Detection
## Prerequisites:
1. Install FastApi & Uvicorn (as root)
    - pip install fastapi
    - pip install uvicorn
    
2. Install Polyglot

    - For Linux
        - Requires numpy, libicu-dev, pycld2, pyicu and morfessor if not already installed,
         but would 1st check running command below as standalone.
        - pip install polyglot
        
    - For MacOS:
        1. Icu4c
            - brew uninstall --force icu4c
            - brew cleanup -s icu4c
            - brew cleanup --prune-prefix
            - brew install icu4c
            - curl -LO http://download.icu-project.org/files/icu4c/64.2/icu4c-64_2-src.tgz
            - tar xzvf icu4c-64_2-src.tgz
            - cd icu/source
            - chmod +x runConfigureICU configure install-sh
            - ./runConfigureICU MacOSX
            - make
            - sudo make install
        2. Pyicu
            - pip --no-cache-dir install pyicu
        3. Polyglot
            - git clone https://github.com/aboSamoor/polyglot
            - python setup.py install

        
3. Install Langdetect (Optional) <br />
    - pip install langdetect
   
4. Install Spacy (Optional) <br />
    - pip install -U spacy
    - pip install spacy-langdetect
    - python -m spacy download en
    - pip install spacy_cld
    
## Running:
- Run server:
    - uvicorn detect_language:app --reload
- Hit browser: http://127.0.0.1:8000/docs

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
## Prerequisites:
1. Install FastApi & Uvicorn (as root)
    - pip install fastapi
    - pip install uvicorn
2. pip install googletrans
3. pip install translate

## Running:
- Run server:
    - uvicorn translate_cv:app --reload
- Hit browser: http://127.0.0.1:8000/docs

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
      	
