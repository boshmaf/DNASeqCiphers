import hashlib
import sys
import dictionary

USAGE='''Usage
  python decrypt.py file length

Arguments
  file: Sequence file
  length: Number of line characters/bases

Example
  python decrypt.py sequence_8.cipher 8'''

def decrypt(cipher_text, dictionary):
    return dictionary[cipher_text]

def decrypt_to_file(file_name, dictionary):
    with open(file_name, 'r')as cipher_file:
        name = '.'.join(file_name.split('.')[:-1])+'.clear'
        with open(name, 'w') as clear_file:
            for line in cipher_file:
                line = line.strip()
                clear_file.write(decrypt(line, dictionary)+'\n')
    return name

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(USAGE)
        exit(1)
    file_name = sys.argv[1]
    line_length = int(sys.argv[2])
    dictionary = dictionary.get_dictionary(line_length)
    clear_file = decrypt_to_file(file_name, dictionary)
    print('File decrypted into %s' % clear_file)