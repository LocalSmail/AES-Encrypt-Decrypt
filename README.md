# AES-Encrypt-Decrypt
Python script to Encrypt or Decrypt your input using a password to encrypt

# Join the community

[Discord](https://discord.gg/Rj7u8Qmvsa)
[Guilded](https://www.guilded.gg/i/kXov5bl2?cid=ea9fc898-6fdd-42b6-8377-5f6f8768b077&intent=chat)


# Usage

```python
import './AES' # Put the path to the AES.py file here.

Encrypted_String, iv, key = AES.encrypt('Message', 'Supper Secure Pasword', 100, 32)

# Fun fact
# You dont need to parse ANYTHING apart for a message for this to work!
# Encrypted_String, iv, key = AES.encrypt("Message') # You can just do this!
                                        
Decrypted_String = AES.decrypt(Encrypted_String, iv, key)

print(f'Encrypted String: {Encrypted_String}\nDecrypted String: {Decrypted_String}\nVery Easy!')
```
