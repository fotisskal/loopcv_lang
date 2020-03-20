# loopcv_lang
A python language library for language detection and translation


# LANGUAGE DETECTION
## PREREQUISITES:
1. Install FastApi & Uvicorn
    - sudo pip3.7 install fastapi
    - sudo pip3.7 install uvicorn
    
2. Install Polyglot
    1. Install Icu4c
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
    2. Install Pyicu
        - pip3.7 --no-cache-dir install pyicu
    3. Install Polyglot
        - git clone https://github.com/aboSamoor/polyglot
        - python3.7 setup.py install
        
3. Install Langdetect (Optional) <br />
    - pip3 install langdetect
   
4. Install Spacy (Optional) <br />
    - pip3 install -U spacy
    - pip3 install spacy-langdetect
    - python -m spacy download en
    - pip install spacy_cld
    
## RUNNING TRANSLATION LIB:
- Run server:
    - uvicorn detect_language:app --reload
- Hit browser: http://127.0.0.1:8000/docs


# TRANSLATION
##PREREQUISITES:
1. pip3.7 install googletrans
2. pip3.7 install translate

## RUNNING:
- Run server:
    - uvicorn translate_cv:app --reload
- Hit browser: http://127.0.0.1:8000/docs
