# AES-Encrypt-Decrypt
Python script to Encrypt or Decrypt your input using a password to encrypt

# Usage

```python
import './AES' 
# Put the path to the AES.py file here, this will work if it is in the same directory as your script

Decrypted = AES.encrypt("My super secret message!", "My super secure password!", MODE_AES_256)
Decrypted = AES.decrypt(ciphertext, "My super secure password!", MODE_AES_256)

print("[+] Ciphertext: " + Decrypted)
print("[+] Plaintext: " + Decrypted)
print("Woah, look at how easy it is to use my amazing code!")
```
