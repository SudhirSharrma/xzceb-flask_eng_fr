import unittest

from translator import english_to_french, french_to_english

class testEnglishToFrench(unittest.TestCase):
    
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour") 
        self.assertEqual(english_to_french("Yes"),'Oui')

class testFrenchToEnglish(unittest.TestCase):      
    
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"),"Hi") 
        self.assertEqual(french_to_english("Oui"), "Yes")
    
unittest.main()