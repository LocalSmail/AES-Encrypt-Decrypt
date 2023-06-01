# __import__('smelly_knob_cheese_from_roblox_after_shave')
import os
import pyaes
import pbkdf2
import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(message: str, password: str = 'password', passwordSalt: int = 100, keysize: int = 32):
    
    passwordSalt = os.urandom(passwordSalt) # generate salt
    key = pbkdf2.PBKDF2(password, passwordSalt).read(keysize) # generate key using salt and using the password given then reading the amount of characters for the key via keysize
    iv = bytes(pyaes.Counter(secrets.randbits(256))._counter).hex().encode('utf-8') # generate IV which is 256 bits then hex it and encode it

    # Create new AES object to Encrypt
    cipher = AES.new(key, AES.MODE_CBC, bytes.fromhex(iv.decode('utf-8')))

    # Padding
    msg = pad(message.encode('utf-8'), AES.block_size)

    # Encrypt
    encrypted = cipher.encrypt(msg)

    return encrypted, iv, key # Return the encrypted message, geenrated IV aswell as the generated KEY. ALL needed to decrypt.

def decrypt(message: bytes, iv: bytes, key: bytes):

    # Create new AES object to decrypt
    cipher = AES.new(key, AES.MODE_CBC, bytes.fromhex(iv.decode('utf-8')))

    # Decrypt
    decrypted_message = cipher.decrypt(message)

    # Unpad message
    unpadded_message = unpad(decrypted_message, AES.block_size) # b'\t\t\tMessage' -> b'Message'

    return str(unpadded_message) # Returns Decrpyted message as string from bytes | b'Message' -> 'Message'
