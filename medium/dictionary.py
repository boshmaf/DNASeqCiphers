import hashlib
import itertools

def get_combinations(line_length=4):
    return list(map(list, itertools.product(['A', 'C', 'G', 'T'], repeat=line_length)))

def hash(combinations):
    hashes = {}
    for combination in combinations:
        line = ''.join(combination)
        hasher = hashlib.sha1(line.encode())
        hashes[hasher.hexdigest()] = line
    return hashes

def get_dictionary(line_length=4):
    return hash(get_combinations(line_length=line_length))

if __name__ == '__main__':
    print(get_dictionary(line_length=4))