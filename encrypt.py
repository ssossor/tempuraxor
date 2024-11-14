import random
import base64

def encrypt_data(data, key):

    key = base64.b64decode(key).decode("latin-1")

    IV = random.randbytes(16).decode("latin-1")
    
    data = data + chr(0) * (16 - len(data) % 16) # padding
    
    encrypted_data = ""
    new_iv = IV

    for i in range(int(len(data) / 16)):

        encrypted_bloc = ""
        tmp = ""

        for j in range(16):
            tmp += chr(ord(data[i * 16 + j]) ^ ord(new_iv[j]))

        for j in range(16):
            encrypted_bloc += chr(ord(tmp[j]) ^ ord(key[j]))
    
        encrypted_data += encrypted_bloc
    
    encrypted_data = IV + encrypted_data

    return base64.b64encode(encrypted_data.encode("latin-1")).decode("latin-1")