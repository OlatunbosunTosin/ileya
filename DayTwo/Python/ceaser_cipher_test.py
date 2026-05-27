import unittest

import ceaser_cipher

class TestThatMessageIsEncryptedAndDEcryptedCorrectly(unittest.TestCase):
        
        
    def test_that_message_is_encrypted(self):
    
       expected_message = (ceaser_cipher.ceaser_cipher_encryption("Help meeee!!!",7))
       self.assertEqual(expected_message, "Olsw tllll!!!")
       
       expected_message = (ceaser_cipher.ceaser_cipher_encryption("I will win",2))
       self.assertEqual(expected_message, "K yknn ykp")
       
       
    def test_that_message_is_decrypted(self):
    
       expected_message = (ceaser_cipher.ceaser_cipher_decryption("Olsw tllll!!!",7))
       self.assertEqual(expected_message, "Help meeee!!!")
       
       expected_message = (ceaser_cipher.ceaser_cipher_decryption("K yknn ykp",2))
       self.assertEqual(expected_message, "I will win")

       

    
