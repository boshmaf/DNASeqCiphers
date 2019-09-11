import encrypt
import decrypt
import dictionary
import hashlib
import sys

USAGE='''Usage
  python test.py file

Arguments
  file: Sequence file

Example
  python test.py sequence_8.txt'''

def test():
    clear_text = 'AGCCAGCC'
    hash_dictionary = dictionary.get_dictionary(len(clear_text))
    cipher_text = encrypt.encrpyt(clear_text)
    assert clear_text == decrypt.decrypt(cipher_text, hash_dictionary), 'Simple test faild!'
    print('Simple test passed!')

def convert_dos_file(file_name):
    with open(file_name, 'r') as file_handler:
        text = file_handler.read()
    with open(file_name, 'w') as file_handler:
        file_handler.write(text)

def get_line_length(file_name):
    line_length = 0
    with open(file_name, 'r') as file_handler:
        for line in file_handler:
            line = line.strip()
            line_length = len(line)
            break
    with open(file_name, 'r') as file_handler:
        for line in file_handler:
            line = line.strip()
            if len(line) != line_length:
                raise Exception('Inconsistent line length!')
    return line_length

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
    if len(sys.argv) != 2:
        print(USAGE)
        exit(1)
    file_name = sys.argv[1]
    convert_dos_file(file_name)
    orginal_hash = get_sha1_hash(file_name)
    line_length = get_line_length(file_name)
    print('File with line length = %i and SHA-1 hash = %s' % (line_length, orginal_hash))
    dictionary = dictionary.get_dictionary(line_length)
    cipher_name = encrypt.encrpyt_to_file(file_name)
    clear_name = decrypt.decrypt_to_file(cipher_name, dictionary)
    decrypted_hash = get_sha1_hash(clear_name)
    assert orginal_hash == decrypted_hash, 'Test failed!'
    print('Test passed!')
