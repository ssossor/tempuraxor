import base64

def decrypt_data(data, key):
    
    key = base64.b64decode(key).decode("latin-1")

    data = base64.b64decode(data).decode("latin-1")

    IV = data[:16]

    decrypted_data = ""
    new_iv = IV

    for i in range(int((len(data) / 16)) - 1):
        
        decrypted_bloc = ""
        tmp = ""

        for j in range(16):
            tmp += chr(ord(data[(i + 1) * 16 + j]) ^ ord(key[j]))

        for j in range(16):
            decrypted_bloc += chr(ord(tmp[j]) ^ ord(new_iv[j]))

        decrypted_data += decrypted_bloc
    
    while ord(decrypted_data[-1]) == 0:
        decrypted_data = decrypted_data[:-1]

    return decrypted_data