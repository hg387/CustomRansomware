

def encrypt_line(line, key):
    new_line = ""
    for i in line:
        new_line += chr((ord(i) + key) % 128)

    return new_line

def save_key(key):
    with open(".key", "wb") as f:
        f.write(key.to_bytes(256, byteorder='little'))
