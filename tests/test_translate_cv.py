from unittest import TestCase

import googletrans

from Translation.translate_cv import translate_api


class Test(TestCase):
    def test_translate_api(self):
        language = "French"
        cv = "Read the following text very carefully and see what you can understand without looking at the English translation"
        print(translate_api(language, cv))


class TestB(TestCase):
    def test_languages(self):
        print(googletrans.LANGUAGES.__len__())
