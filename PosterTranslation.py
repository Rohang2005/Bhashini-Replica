import pytesseract
from PIL import Image
from deep_translator import GoogleTranslator

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def image_extraction(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return str(e)
    
def translated_text(text,source_lang,target_lang):
    try:
        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated_text
    except:
        print("An error occurred while translating the text")
        return None

def main():
    image_path = 'test2.jpg'
    extracted_text = image_extraction(image_path)
    print("The extracted text from the image")
    print("***************************************************************************************************")
    print(extracted_text)
    print("***************************************************************************************************")
    lang1=input("Enter the source language")
    lang2=input("Enter the target language")
    translate_text=translated_text(extracted_text,lang1,lang2)
    print("The translated text which was present in the entered image")
    print("***************************************************************************************************")
    print(translate_text)
    print("***************************************************************************************************")
if __name__ == "__main__":
    main()
