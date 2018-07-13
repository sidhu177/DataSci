# -*- coding: utf-8 -*-
"""
This program is to encrypt passwords
"""
import base64
print("Welcome to the Encrypt Decrypt utility")
print("Please select 1 to enrypt and 2 to decrypt")
option = raw_input("1 or 2")
if option==1:
   word = raw_input("Please input the word to be Encrypted\n")
   data = base64.b64encode(word)
   print(data)
elif option==2:    
   key = raw_input("Please input the key to be Decrypter\n")
   data = base64.b64decode(key)
   print(data)