import string

def encrypt_line_v2(line, key):
    new_line = ""
    for i in line:
        if 0 <= ord(i) <= 127:
            new_line += chr((ord(i) + key) % 128)
        else:
            new_line += i

    return new_line

def encrypt_line(line, key):
    new_line = ""
    for i in line:

        if i.isalpha() and i.isupper():
            new_line += chr((((ord(i) - ord('A')) + key) % 26) + ord('A'))
        elif i.isalpha() and i.islower():
            new_line += chr((((ord(i) - ord('a')) + key) % 26) + ord('a'))
        elif i.isdigit():
            new_line += chr((((ord(i) - ord('0')) + key) % 10) + ord('0'))
        elif 32 <= ord(i) <= 47:
            new_line += chr((((ord(i) - ord(' ')) + key) % 16) + ord(' '))
        elif 58 <= ord(i) <= 64:
            new_line += chr((((ord(i) - ord(':')) + key) % 7) + ord(':'))
        elif 91 <= ord(i) <= 96:
            new_line += chr((((ord(i) - ord('[')) + key) % 6) + ord('['))
        elif 123 <= ord(i) <= 126:
            new_line += chr((((ord(i) - ord('{')) + key) % 4) + ord('{'))
        else:
            new_line += i


    return new_line

def save_key(key):
    try:
        with open(".key", "wb") as f:
            f.write(key.to_bytes(256, byteorder='little'))
    except IOError as e:
        print("Exception raised: \n" + e)