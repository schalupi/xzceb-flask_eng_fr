# -*- coding: utf-8 -*-


from unittest import TestCase
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(TestCase):
    def test_translation(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"
        result = englishToFrench(english_text)
        self.assertEqual(result, expected_french_text)

class TestFrenchToEnglish(TestCase):
    def test_translation(self):
        french_text = "Bonjour"
        expected_english_text = "Hello"
        result = frenchToEnglish(french_text)
        self.assertEqual(result, expected_english_text)