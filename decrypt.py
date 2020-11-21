from pathlib import *
def decrypt_line(line, key):
    new_line = ""

    for i in line:
        new_ord = ord(i) - key

        if new_ord < 0:
            new_ord = 128 + new_ord

        new_line += chr(new_ord)

    return new_line

def find_key(input_path):
    p = Path(input_path)
    for file in p.rglob('*.key'):
        if file.name == ".key":
            with open(file, "rb") as f:
                key = int.from_bytes(f.read(), byteorder='little')
                return key
        else:
            print("No key found\n")