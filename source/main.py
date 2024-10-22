#!/bin/python3

alphabet='abcdefghijklmnopqrstuvwxyz'
key=''
newMessage=''
encryptOrDecrypt=''
keyKnown=''
decryptCount=1

while encryptOrDecrypt not in ['e','d']:
  encryptOrDecrypt=input('Do you want to encrypt or decrypt a message? Please enter e or d: ')

if encryptOrDecrypt=='e':
  message=input('Please enter a message to encrypt')
  print('You want to encrypt message: ' + message)
  key=int(input('Please enter the number you want to use as a key for encryption: '))
  print('You want to encrypt using key: ' + str(key))
  
  for character in message:
    if character in alphabet:
      position=alphabet.find(character)
      encryptedPosition=(key + position) % 26
      encryptedCharacter=alphabet[encryptedPosition]
      print('Our encrypted character is: ' + encryptedCharacter)
      newMessage += encryptedCharacter
    else:
      newMessage += character
  print('Our encrypted message is ' + newMessage)
  
if encryptOrDecrypt=='d':
  message=input('Please enter a message to decrypt: ')
  while keyKnown not in ['y','n']:
    keyKnown=input('Do you know the encryption key, y or n: ')
    
  if keyKnown == 'y':
    key=int(input('Please enter the number you want to use as a key to decrypt: '))
    
    for character in message:
      if character in alphabet:
        position=alphabet.find(character)
        decryptedPosition=((position+26) - key) % 26
        decryptedCharacter=alphabet[decryptedPosition]
        print('Our decrypted character is: ' + decryptedCharacter)
        newMessage += decryptedCharacter
      else:
        newMessage += character
        
    print('Our decrypted message is: ' + newMessage)
    
  else:
    while decryptCount < 26:
      for character in message:
        if character in alphabet:
          position=alphabet.find(character)
          decryptedPosition=((position+26) - decryptCount) % 26
          decryptedCharacter=alphabet[decryptedPosition]
          newMessage += decryptedCharacter
        else:
          newMessage += character
        
      decryptCount = decryptCount + 1
        
      print('Brute force decrypted message: ' + newMessage)
      newMessage =''