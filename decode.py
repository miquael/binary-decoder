# decode file contents (binary)
# in terminal, run to decode file (key0):
# > python3 decode.py key0

import sys

file = sys.argv[1]

with open(file, 'r') as f:
    encoded = f.read()
print(file + ' encoded content: ')
print(encoded)

# split content string 
enc = encoded.split(" ")

# dec will hold the decoded string
dec = ""

# decode
print('decoded content: ')
for i in range(len(enc)):
  dec += chr(int(enc[i], 2))
print(dec)

# decode lenth (chars)
length = len(enc)
print('length: ' + str(length))