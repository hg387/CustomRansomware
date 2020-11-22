import string

def encrypt_line(line, key):
    new_line = ""
    for i in line:
        new_line += chr((ord(i) + key) % 128)

    return new_line

def encrypt_line_v2(line, key):
    new_line = ""
    for i in line:
        if i.isalpha() and i.isupper():
            new_line += chr((((ord(i) - ord('A')) + key) % 26) + ord('A'))
        elif i.isalpha() and i.islower():
            new_line += chr((((ord(i) - ord('a')) + key) % 26) + ord('a'))
        elif i.isdigit():
            new_line += chr((((ord(i) - ord('0')) + key) % 10) + ord('0'))
        elif i in string.punctuation and (32 <= ord(i) <= 47):
            new_line += chr((((ord(i) - ord(' ')) + key) % 16) + ord(' '))
        elif i in string.punctuation and (58 <= ord(i) <= 64):
            new_line += chr((((ord(i) - ord(':')) + key) % 7) + ord(':'))
        elif i in string.punctuation and (91 <= ord(i) <= 96):
            new_line += chr((((ord(i) - ord('[')) + key) % 6) + ord('['))
        elif i in string.punctuation and (123 <= ord(i) <= 126):
            new_line += chr((((ord(i) - ord('{')) + key) % 4) + ord('{'))


    return new_line

def save_key(key):
    try:
        with open(".key", "wb") as f:
            f.write(key.to_bytes(256, byteorder='little'))
    except IOError as e:
        print("Exception raised: \n" + e)