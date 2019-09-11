import encrypt
import decrypt
import hashlib
import sys

USAGE='''Usage
  python test.py file rotations

Arguments
  file: Sequence file
  rotations: Number of 4-bit rotations

Example
  python test.py sequence.txt 1'''

def test():
    clear_text = 'AGCCAGCCTTCT'
    cipher_text = encrypt.encrpyt(clear_text)
    assert clear_text == decrypt.decrypt(cipher_text), 'Simple test faild!'
    print('Simple test passed!')

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
    if len(sys.argv) == 1:
        test()
        print()
    if len(sys.argv) != 3:
        print(USAGE)
        exit(1)
    file_name = sys.argv[1]
    rotations = int(sys.argv[2])
    convert_dos_file(file_name)
    orginal_hash = get_sha1_hash(file_name)
    print('File SHA-1 hash = %s' % orginal_hash)
    cipher_name = encrypt.encrpyt_to_file(file_name, rotations)
    clear_name = decrypt.decrypt_to_file(cipher_name, rotations)
    decrypted_hash = get_sha1_hash(clear_name)
    assert orginal_hash == decrypted_hash, 'Test failed!'
    print('Test passed!')
