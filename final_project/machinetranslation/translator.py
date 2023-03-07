# -*- coding: utf-8 -*-

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(englishText):   
    authenticator = IAMAuthenticator('{apikey}')
    language_translator = LanguageTranslatorV3(
        version='001',
        authenticator=authenticator
)

    language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')

    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    
    return frenchText



def frenchToEnglish(frenchText):
    authenticator = IAMAuthenticator('{apikey}')
    language_translator = LanguageTranslatorV3(
        version='001',
        authenticator=authenticator
)

    language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')

    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    print(json.dumps(translation, indent=2, ensure_ascii=False))

    return englishText