import common
import sys

USAGE='''Usage
  python decrypt.py file rotations

Arguments
  file: Sequence file
  rotations: Number of 4-bit rotations

Example
  python decrypt.py sequence.cipher 1'''

def decrypt(cipher_text, rotations=1):
    binary_text = common.text_to_bits(cipher_text)
    for _ in range(rotations*4):
        binary_text = binary_text[1:] + binary_text[:1]
    return common.text_from_bits(binary_text)

def decrypt_to_file(file_name, rotations):
    with open(file_name, 'r')as cipher_file:
        name = '.'.join(file_name.split('.')[:-1])+'.clear'
        with open(name, 'w') as clear_file:
            for line in cipher_file:
                line = line.strip()
                clear_file.write(decrypt(line, rotations)+'\n')
    return name

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(USAGE)
        exit(1)
    file_name = sys.argv[1]
    rotations = int(sys.argv[2])
    clear_name = decrypt_to_file(file_name, rotations)
    print('File decrypted into %s' % clear_name)