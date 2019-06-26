import os
import pyAesCrypt
from Crypto.PublicKey import RSA

def generate_key():
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

def encrypt():
    pyAesCrypt.encryptFile("./testfolder/encrypt.txt", "encrypt.txt.aes", password, bufferSize)
    return

def decrypt():
    pyAesCrypt.decryptFile("./encrypt.txt.aes", "encrypt.txt", password, bufferSize)
    return

if __name__ == "__main__":
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024
    password = str(generate_key()[1][32:-30])
    for file in os.listdir("./testfolder"):
        if file.endswith(".html"):
            print(os.path.join("./testfolder", file))
    encrypt()
    decrypt()
# or if you want to traverse directory, use os.walk:
#
# import os
# for root, dirs, files in os.walk("/mydir"):
#     for file in files:
#         if file.endswith(".txt"):
#              print(os.path.join(root, file))
