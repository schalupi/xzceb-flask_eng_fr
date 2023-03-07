from unittest import TestCase
from machinetranslation.translator import english_to_french


class TestEnglishToFrench(TestCase):
    def test_translation(self):
        english_text = "Hello, how are you?"
        expected_french_text = "Bonjour comment ça va?"
        result = english_to_french(english_text)
        self.assertEqual(result, expected_french_text)

    def test_not_equal(self):
        english_text = "I am a robot"
        unexpected_french_text = "Je suis un robot"
        result = english_to_french(english_text)
        self.assertNotEqual(result, unexpected_french_text)


class TestFrenchToEnglish(TestCase):
    def test_translation_equal(self):
        french_text = "Bonjour, comment ça va?"
        expected_english_text = "Hello, how are you?"
        result = french_to_english(french_text)
        self.assertEqual(result, expected_english_text)

    def test_translation_not_equal(self):
        french_text = "Bonjour, comment ça va?"
        unexpected_english_text = "Hi, how are you?"
        result = french_to_english(french_text)
        self.assertNotEqual(result, unexpected_english_text)

