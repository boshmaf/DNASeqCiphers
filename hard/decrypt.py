import base64
import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

USAGE='''Usage
  python decrypt.py file length

Arguments
  file: Sequence file
  password: Password to derive AES key

Example
  python decrypt.py sequence.cipher p@ssw0rd'''

def decrypt(password, cipher_text, decode=True):
    if decode:
        cipher_text = base64.b64decode(cipher_text.encode('latin-1'))
    key = SHA256.new(password.encode('utf8')).digest()
    IV = cipher_text[:AES.block_size]
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(cipher_text[AES.block_size:])
    padding = data[-1]
    if data[-padding:] != bytes([padding]) * padding:
        raise ValueError('Invalid padding!')
    return data[:-padding]

def decrypt_to_file(file_name, password):
    with open(file_name, 'r')as cipher_file:
        name = '.'.join(file_name.split('.')[:-1])+'.clear'
        with open(name, 'wb') as clear_file:
            cipher_text = cipher_file.read()
            clear_file.write(decrypt(password, cipher_text))
    return name

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(USAGE)
        exit(1)
    file_name = sys.argv[1]
    password = sys.argv[2]
    clear_file = decrypt_to_file(file_name, password)
    print('File decrypted into %s' % clear_file)