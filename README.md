# Introduction
A python language library for language detection and translation


# Language Detection
## Prerequisites:
1. Install FastApi & Uvicorn (as root)
    - pip install fastapi
    - pip install uvicorn
    
2. Install Polyglot
    - For MacOS:
    <br/><br/>
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
        - pip3.7 --no-cache-dir install pyicu
    3. Polyglot
        - git clone https://github.com/aboSamoor/polyglot
        - python setup.py install
    <br/><br/>
    - For Centos (requires numpy and libicu-dev if not already installed):
        - pip install polyglot
        
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


# Translation
## Prerequisites:
1. pip install googletrans
2. pip install translate

## Running:
- Run server:
    - uvicorn translate_cv:app --reload
- Hit browser: http://127.0.0.1:8000/docs
