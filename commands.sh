uvicorn LanguageDetection/detect_language:app --port 8002 --reload &
uvicorn Translation/translate_cv:app --port 8003 --reload &
uvicorn LanguageMentionsExtraction/extract_language_mentions:app --port 8004 --reload &
