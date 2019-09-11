import common
import sys

USAGE='''Scheme: A simple binary fixed-length right-rotate cipher.

Usage
  python encrypt.py file rotations

Arguments
  file: Sequence file
  rotations: Number of 4-bit rotations

Example
  python encrypt.py sequence.txt 1'''

def encrpyt(clear_text, rotations=1):
    binary_text = common.text_to_bits(clear_text)
    for _ in range(rotations*4):
        binary_text = binary_text[-1:] + binary_text[:-1]
    return common.text_from_bits(binary_text)

def encrpyt_to_file(file_name, rotations):
    with open(file_name, 'r')as clear_file:
        name = '.'.join(file_name.split('.')[:-1])+'.cipher'
        with open(name, 'w') as cipher_file:
            for line in clear_file:
                line = line.strip()
                cipher_file.write(encrpyt(line, rotations)+'\n')
    return name

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(USAGE)
        exit(1)
    file_name = sys.argv[1]
    rotations = int(sys.argv[2])
    cipher_file = encrpyt_to_file(file_name, rotations)
    print('File encrypted into %s' % cipher_file)
