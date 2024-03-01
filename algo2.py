import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class Encryption:
    def __init__(self, data):
        self.data = data
        self.block_size = AES.block_size

    # Function to generate a key from the data
    def generate_key(self):
        key = hashlib.sha256(self.data).digest()
        return key

    # Function to create a new AES cipher object with the key
    def create_cipher(self, key):
        cipher = AES.new(key, AES.MODE_CBC)
        return cipher

    # Function to encrypt the data
    def encrypt_data(self, cipher):
        encrypted_data = cipher.encrypt(pad(self.data, self.block_size))
        return encrypted_data

    # Function for Convergent Encryption
    def convergent_encryption(self):
        key = self.generate_key()
        cipher = self.create_cipher(key)
        encrypted_data = self.encrypt_data(cipher)
        return encrypted_data, cipher.iv

    # Function for AES Encryption
    def aes_encryption(self, key):
        cipher = self.create_cipher(key)
        encrypted_data = self.encrypt_data(cipher)
        return encrypted_data, cipher.iv

# Test the class and functions
def main():
    data = b"This is some test data"
    key = os.urandom(32)

    encryption = Encryption(data)

    # Convergent Encryption
    ce_encrypted_data, ce_iv = encryption.convergent_encryption()
    print("CE Encrypted Data:", ce_encrypted_data)

    # AES Encryption
    aes_encrypted_data, aes_iv = encryption.aes_encryption(key)
    print("AES Encrypted Data:", aes_encrypted_data)

if __name__ == "__main__":
    main()
