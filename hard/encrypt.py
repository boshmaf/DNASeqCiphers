import base64
import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

USAGE='''Password-based AES encryption in CBC mode with PKCS#7 padding.
The key is a SHA256 hash of an 'average user' password.
The cipher text is stored in base64 encoding.

Usage
  python encrypt.py file password

Arguments
  file: Sequence file
  password: Password to derive AES key

Example
  python encrypt.py sequence.txt p@ssw0rd'''

def encrypt(password, clear_text, encode=True):
    key = SHA256.new(password.encode('utf8')).digest()
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(clear_text) % AES.block_size
    clear_text += bytes([padding]) * padding
    data = IV + encryptor.encrypt(clear_text)
    return base64.b64encode(data).decode('latin-1') if encode else data

def encrpyt_to_file(file_name, password):
    with open(file_name, 'rb')as clear_file:
        name = '.'.join(file_name.split('.')[:-1])+'.cipher'
        with open(name, 'w') as cipher_file:
            clear_text = clear_file.read()
            cipher_file.write(encrypt(password, clear_text))
    return name

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(USAGE)
        exit(1)
    file_name = sys.argv[1]
    password = sys.argv[2]
    cipher_file = encrpyt_to_file(file_name, password)
    print('File encrypted into %s' % cipher_file)