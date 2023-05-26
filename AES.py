# __import__('smelly_knob_cheese_from_roblox_after_shave')
import bson
import pbkdf2
import base64

from Crypto.Cipher import AES
from secrets import token_bytes

MODE_AES_256 = 32
MODE_AES_128 = 16

def encrypt(message: str, password: str, mode:int = MODE_AES_256):
    salt = token_bytes(32)
    key = pbkdf2.PBKDF2(password, salt, iterations=2000).read(mode)

    cipher = AES.new(key, AES.MODE_GCM, nonce=token_bytes(16))
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    nonce = cipher.nonce
    
    return base64.urlsafe_b64encode(bson.dumps({"": [salt, nonce, tag, ciphertext]})).decode()

def decrypt(encrypted_message: str, password:str, mode:int = MODE_AES_256):
    encrypted_message = bson.loads(base64.urlsafe_b64decode(encrypted_message.encode()))[""]
    salt, nonce, tag, ciphertext = encrypted_message

    key = pbkdf2.PBKDF2(password, salt, iterations=2000).read(mode)

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag).decode()

    return plaintext

def perform_test():
    password = base64.urlsafe_b64encode(token_bytes(24)).decode()
    message = base64.urlsafe_b64encode(token_bytes(40)).decode()
    
    if decrypt(encrypt(message, password, MODE_AES_256), password, MODE_AES_256) != message or \
    decrypt(encrypt(message, password, MODE_AES_128), password, MODE_AES_128) != message:
        return False
    
    return True
