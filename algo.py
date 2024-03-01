import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Convergent Encryption
def convergent_encryption(data):
    # Generate a key from the data
    key = hashlib.sha256(data).digest()
    
    # Create a new AES cipher object with the key
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Encrypt the data
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    
    return encrypted_data, cipher.iv

# AES Encryption
def aes_encryption(data, key):
    # Create a new AES cipher object with the key
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Encrypt the data
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    
    return encrypted_data, cipher.iv

# Test the functions
data = b"This is some test data"
key = os.urandom(32)

# Convergent Encryption
ce_encrypted_data, ce_iv = convergent_encryption(data)
print("CE Encrypted Data:", ce_encrypted_data)

# AES Encryption
aes_encrypted_data, aes_iv = aes_encryption(data, key)
print("AES Encrypted Data:", aes_encrypted_data)
