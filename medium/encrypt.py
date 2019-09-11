import hashlib
import sys

USAGE='''Scheme: A line-by-line SHA1 hash cipher.
Each line in the cipher text is an unsalted SHA1 hash
of the corresponding 16 character line in the clear text.

Usage
  python encrypt.py file

Arguments
  file: Sequence file

Example
  python encrypt.py sequence_8.txt'''

def encrpyt(clear_text):
    hasher = hashlib.sha1(clear_text.encode())
    return hasher.hexdigest()

def encrpyt_to_file(file_name):
    with open(file_name, 'r') as clear_file:
        name = '.'.join(file_name.split('.')[:-1])+'.cipher'
        with open(name, 'w') as cipher_file:
            for line in clear_file:
                line = line.strip()
                cipher_file.write(encrpyt(line)+'\n')
    return name

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(USAGE)
        exit(1)
    file_name = sys.argv[1]
    cipher_file = encrpyt_to_file(file_name)
    print('File encrypted into %s' % cipher_file)