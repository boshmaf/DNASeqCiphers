import encrypt
import decrypt
import hashlib
import sys

USAGE='''Usage
  python test.py file password

Arguments
  file: Sequence file
  password: Password to derive AES key

Example
  python test.py sequence.txt p@ssw0rd'''

def convert_dos_file(file_name):
    with open(file_name, 'r') as file_handler:
        text = file_handler.read()
    with open(file_name, 'w') as file_handler:
        file_handler.write(text)

def get_sha1_hash(file_name):
    hasher = hashlib.sha1()
    with open(file_name, 'rb') as file_handler:
        buf = file_handler.read()
        hasher.update(buf)
    return hasher.hexdigest()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(USAGE)
        exit(1)
    file_name = sys.argv[1]
    password = sys.argv[2]
    convert_dos_file(file_name)
    orginal_hash = get_sha1_hash(file_name)
    print('File SHA-1 hash = %s' % orginal_hash)
    cipher_name = encrypt.encrpyt_to_file(file_name, password)
    clear_name = decrypt.decrypt_to_file(cipher_name, password)
    decrypted_hash = get_sha1_hash(clear_name)
    assert orginal_hash == decrypted_hash, 'Test failed!'
    print('Test passed!')
