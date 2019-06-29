import os
import pyAesCrypt
from Crypto.PublicKey import RSA
from cryptography.fernet import Fernet

def generate_rsa_key():
    #Generate a public/ private key pair using 4096 bits key length (512 bytes)
    new_key = RSA.generate(4096, e=65537)
    #The private key in PEM format
    private_key = new_key.exportKey("PEM")
    #The public key in PEM Format
    public_key = new_key.publickey().exportKey("PEM")
    print(len(private_key))
    print(private_key)
    print("\n")
    print(len(public_key))
    print(public_key)
    return private_key, public_key

def encrypt_AES(password):
    pyAesCrypt.encryptFile("./testfolder/encrypt.txt", "encrypt.txt.aes", password, bufferSize)
    return

def encrypt(symmetric_key_password,content):
    f = Fernet(symmetric_key_password)
    encrypted_content = f.encrypt(content.encode())
    print("1")
    print(encrypted_content)
    return encrypted_content

def decrypt_AES(password):
    pyAesCrypt.decryptFile("./encrypt.txt.aes", "encrypt.txt", password, bufferSize)
    return

def decrypt(symmetric_key_password, encrypted_content):
    f = Fernet(symmetric_key_password)
    decrypted_content = f.decrypt(encrypted_content)
    return decrypted_content

def remove_original_file(file):
    os.remove(file)
    return

def store_key(key):
    f = open("store_key.txt", "a")
    f.write(str(key))
    f.close()
    return

def encrypted_file(encrypted_content):
    f = open("encrypted.txt", "a")
    f.write(str(encrypted_content))
    f.close()
    return

def decrypted_file(decrypted_content):
    f = open("decrypted.txt", "a")
    f.write(str(decrypted_content))
    f.close()
    return

if __name__ == "__main__":
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024
    #Slice the keys to get rid of the binary string representation prefix
    rsa_password = str(generate_rsa_key()[1][32:-30])
    symmetric_key_password = Fernet.generate_key()
    print(type(symmetric_key_password))
    store_key(symmetric_key_password)
    for file in os.listdir("./testfolder"):
        if file.endswith(".html"):
            print(os.path.join("./testfolder", file))
    encrypt_AES(rsa_password)
    decrypt_AES(rsa_password)
    with open('./testfolder/encrypt.txt', 'r') as plaintext_file:
        content = plaintext_file.read()
    encrypted_content = encrypt(symmetric_key_password,content)
    encrypted_file(encrypted_content)
    print("2")
    print(encrypted_content)
    decrypted_content = decrypt(symmetric_key_password,encrypted_content)
    decrypted_file(decrypted_content)
    # remove_original_file("./encrypt.txt")

# or if you want to traverse directory, use os.walk:
#
# import os
# for root, dirs, files in os.walk("/mydir"):
#     for file in files:
#         if file.endswith(".txt"):
#              print(os.path.join(root, file))
