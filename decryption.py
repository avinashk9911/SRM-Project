import os
import hashlib
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
        return encrypted_data, cipher.iv

class Decryption:
    def __init__(self, encrypted_data, iv):
        self.encrypted_data = encrypted_data
        self.iv = iv
        self.block_size = AES.block_size

    # Function to generate a key from the data
    def generate_key(self, data):
        key = hashlib.sha256(data).digest()
        return key

    # Function to create a new AES cipher object with the key
    def create_cipher(self, key):
        cipher = AES.new(key, AES.MODE_CBC, iv=self.iv)
        return cipher

    # Function to decrypt the data
    def decrypt_data(self, cipher):
        decrypted_data = unpad(cipher.decrypt(self.encrypted_data), self.block_size)
        return decrypted_data

    # Function for Convergent Decryption
    def convergent_decryption(self, data):
        key = self.generate_key(data)
        cipher = self.create_cipher(key)
        decrypted_data = self.decrypt_data(cipher)
        return decrypted_data

    # Function for AES Decryption
    def aes_decryption(self, key):
        cipher = self.create_cipher(key)
        decrypted_data = self.decrypt_data(cipher)
        return decrypted_data

# Test the class and functions
def main():
    data = b"This is some test data"
    key = os.urandom(32)

    encryption = Encryption(data)

    # Convergent Encryption
    ce_key = encryption.generate_key()
    ce_cipher = encryption.create_cipher(ce_key)
    ce_encrypted_data, ce_iv = encryption.encrypt_data(ce_cipher)

    # AES Encryption
    aes_cipher = encryption.create_cipher(key)
    aes_encrypted_data, aes_iv = encryption.encrypt_data(aes_cipher)

    decryption = Decryption(ce_encrypted_data, ce_iv)

    # Convergent Decryption
    ce_decrypted_data = decryption.convergent_decryption(data)
    print("CE Decrypted Data:", ce_decrypted_data)

    decryption = Decryption(aes_encrypted_data, aes_iv)

    # AES Decryption
    aes_decrypted_data = decryption.aes_decryption(key)
    print("AES Decrypted Data:", aes_decrypted_data)

if __name__ == "__main__":
    main()
