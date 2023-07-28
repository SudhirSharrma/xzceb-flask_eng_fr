"""This module contains two functions:
1. english_to_french: translates english text input to french.
2. french_to_english: translates french text input to englsih.

for translation we are using MyMemoryTranslator from deep_translator.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function takes input of English text and returns its French translation.
    """
    french_text = MyMemoryTranslator(source='en-US', target = 'fr-FR').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """
    This function takes input of French text and returns its English translation.
    """
    english_text = MyMemoryTranslator(source='fr-FR', target ='en-US').translate(french_text)
    print(english_text)
    return english_text
