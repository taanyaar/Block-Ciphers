import os
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

BLOCKSIZE = 16

def byteLen(s):
    return len(s.decode('utf-8'))


def encrypt_ecb(file, key):
    # Read plaintext
    with open(file, 'rb') as f:
        plaintext = f.read()

    # Create a new AES cipher 
    cipher = AES.new(key, AES.MODE_CBC)

    #pad data
    paddedText = pad(plaintext, BLOCKSIZE)


    # Encrypt the plaintext and write it to a new file
    for i in range(0, len(paddedText), BLOCKSIZE):
        ciphertext = cipher.encrypt(paddedText[i:i+BLOCKSIZE])
        #print("cipher, ", paddedText[i:i+BLOCKSIZE], ciphertext)
        with open("ciphertext.bmp", 'wb') as f:
            f.write(ciphertext)


key = get_random_bytes(16)

iv=b'nCz\xd2\xd5\xafF\x89\x00\xdfS\x9a\xae#\x047'
encrypt_ecb("cp-logo.bmp", key)
