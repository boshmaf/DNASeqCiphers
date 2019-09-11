# DNASeqCrypto
DNA sequence encryption schemes for [Qatar International Cybersecurity Competition - Genomics](https://www.hbku.edu.qa/en/qicc):

- [Easy](https://github.com/qcri/DNASeqCrypto#easy): A simple fixed-length binary rotate cipher.
- [Medium](https://github.com/qcri/DNASeqCrypto#medium): A line-by-line SHA1 hash cipher.
- [Hard](https://github.com/qcri/DNASeqCrypto#hard): Password-based AES/CBC/PKCS#7 cipher.

Install Python3 dependencies before you start:
```
pip3 install -r requirements.txt
```

## Easy

A simple fixed-length binary rotate cipher.

The clear-text sequence file is assumed to consist of multiple lines with a trailing empty line. Each non-empty line has a fixed length, which is similar to all lines, and consists of a DNA sequence representing a combination of the 4-bases (i.e., A, C, G, T).

To encrypt:
```
cd easy/
python encrypt.py sequence.txt 1
```
This will encrypt `sequence.txt` using a 4-bit rorate cipher and store the result to `sequence.cipher`. 

To decrypt:
```
python decrypt.py sequence.cipher 1
```
This will decrypt `sequence.cipher` using a 4-bit rorate cipher and store the result to `sequence.clear`. This file must be an exact copy of `sequence.txt`, which means they have the same hash.

To run an end-to-end test:
```
python test.py sequence.txt 1
```

## Medium

A line-by-line SHA1 hash cipher. Each line in the cipher text is an unsalted SHA1 hash
of the corresponding 16 character line in the clear text. The longer the line in the clear text, the harder this scheme gets to crack. It requires a dictionary attack of precomputed hashes of all possible combinations. The space is relatively small, however.

The clear-text sequence file is assumed to consist of multiple lines with a trailing empty line. Each non-empty line has a fixed length of 16 characters, which is similar to all lines, and consists of a DNA sequence representing a combination of the 4-bases (i.e., A, C, G, T).

To encrypt:
```
cd medium/
python encrypt.py sequence_16.txt
```
This will encrypt `sequence_16.txt` using a a line-by-line SHA1 hash cipher and store the result to `sequence_16.cipher`. 

To decrypt:
```
python decrypt.py sequence_16.cipher
```
This will decrypt `sequence_16.cipher` using a hash dictionary of all possible 4^16 base combinations and store the result to `sequence_16.clear`. This file must be an exact copy of `sequence_16.txt`, which means they have the same hash.

To run an end-to-end test:
```
python test.py sequence_16.txt
```

## Hard

Password-based AES encryption in CBC mode with PKCS#7 padding. The key is a SHA256 hash of an 'average user' password. The cipher text is stored in base64 encoding. Cracking this shceme requires a dictionary attack of precomputed hashes of passwords. The space is massive, but users tend to choose "guessable" passwords.

The clear-text sequence file is assumed to consist of a DNA sequence of any length representing a combination of the 4-bases (i.e., A, C, G, T).

To encrypt:
```
cd hard/
python encrypt.py sequence.txt p@ssw0rd
```
This will encrypt `sequence.txt` using a password-based encryption scheme and store the result to `sequence.cipher`. 

To decrypt:
```
python decrypt.py sequence.cipher p@ssw0rd
```
This will decrypt `sequence.cipher` using a password-based decryption scheme and store the result to `sequence.clear`. This file must be an exact copy of `sequence.txt`, which means they have the same hash.

To run an end-to-end test:
```
python test.py sequence.txt p@ssw0rd
```
