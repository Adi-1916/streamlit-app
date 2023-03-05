import streamlit as st
from googletrans import Translator
import random

# Initialize the translator
translator = Translator()
def generate_random_language():
    # Define a list of languages
    languages = [
        'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs',
        'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'co', 'hr', 'cs', 'da', 'nl',
        'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el',
        'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id',
        'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky',
        'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi',
        'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa',
        'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl',
        'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'tr',
        'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
    ]
    # Choose a random language from the list
    language_code = random.choice(languages)
    return language_code
def main():
    # Set app title
    st.title('English Translator')

    # Get user input
    input_text = st.text_input('Enter text in English')

    # Check if input is not empty
    if input_text:
        # Generate a random language code
        lang_code = generate_random_language()

        # Translate the input text to the random language
        translated_text = translator.translate(input_text, dest=lang_code).text

        # Display the translated text
        st.success(f'Translated text: {translated_text}')

if __name__ == '__main__':
    main()
