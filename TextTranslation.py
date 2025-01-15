from deep_translator import GoogleTranslator
from gtts import gTTS
import os
def translate_text(text, source_language, target_language):
    try:
        translated_text = GoogleTranslator(source=source_language, target=target_language).translate(text)
        return translated_text
    except Exception as e:
        print(f"An error occurred during translation")
        return None
def main():
    text = input("Enter the text to translate: ")
    source_language = input("Enter the source language : ")
    target_language = input("Enter the target language : ")
    translated_text = translate_text(text, source_language, target_language)
    #engine = pyttsx3.init()
    
    if translated_text:
        #print("Translated Text: ", translated_text)
        #engine.say(translated_text)
        #engine.runAndWait()
        print(translated_text)
        tts = gTTS(translated_text, lang=target_language)
        tts.save("output.mp3")
        os.system("start output.mp3")

if __name__ == "__main__":
    main()
