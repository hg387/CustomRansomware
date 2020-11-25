from pathlib import *
import string
def decrypt_line_v2(line, key):
    new_line = ""

    for i in line:
        new_line += chr((ord(i) - key) % 128)

    return new_line

def decrypt_line(line, key):
    new_line = ""
    for i in line:
        if i.isalpha() and i.isupper():
            new_line += chr((((ord(i) - ord('A')) - key) % 26) + ord('A'))
        elif i.isalpha() and i.islower():
            new_line += chr((((ord(i) - ord('a')) - key) % 26) + ord('a'))
        elif i.isdigit():
            new_line += chr((((ord(i) - ord('0')) - key) % 10) + ord('0'))
        elif 32 <= ord(i) <= 47:
            new_line += chr((((ord(i) - ord(' ')) - key) % 16) + ord(' '))
        elif 58 <= ord(i) <= 64:
            new_line += chr((((ord(i) - ord(':')) - key) % 7) + ord(':'))
        elif 91 <= ord(i) <= 96:
            new_line += chr((((ord(i) - ord('[')) - key) % 6) + ord('['))
        elif 123 <= ord(i) <= 126:
            new_line += chr((((ord(i) - ord('{')) - key) % 4) + ord('{'))
        else:
            new_line += i


    return new_line

def find_key(input_path):
    p = Path(input_path)
    try:
        for file in p.rglob('*.key'):
            if file.name == ".key":
                with open(file, "rb") as f:
                    key = int.from_bytes(f.read(), byteorder='little')
                    return key
            else:
                print("No key found\n")
                return None
    except IOError as e:
        print("Exception Raised: \n" + e)