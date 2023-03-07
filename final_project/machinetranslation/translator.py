import json
import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def english_to_french(english_text):
    """
    Translates English text to French.
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='001',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English.
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='001',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    print(json.dumps(translation, indent=2, ensure_ascii=False))

    return english_text
