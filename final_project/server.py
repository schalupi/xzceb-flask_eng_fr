from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation.translator import english_to_french
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    english_text = request.args.get('textToTranslate')
    french_text = english_to_french(english_text)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    french_text = request.args.get('textToTranslate')
    english_text = french_to_english(french_text)
    return french_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
