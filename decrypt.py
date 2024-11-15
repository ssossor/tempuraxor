import base64

def decrypt_data(data: str, key: str) -> bytes:
    
    key: bytes = base64.b64decode(key)

    data: bytes = base64.b64decode(data)

    IV: bytes = data[:16]

    padding_size: int = int.from_bytes(data[-1:])

    data = data[16:-1]

    decrypted_data: bytes = b""
    new_iv: bytes = IV

    for i in range(int((len(data) / 16) - 1)):
        
        decrypted_bloc: bytes = b""
        tmp: bytes = b""

        for j in range(16):
            tmp += (data[i * 16 + j] ^ key[j]).to_bytes()

        for j in range(16):
            decrypted_bloc += (tmp[j] ^ new_iv[j]).to_bytes()

        decrypted_data += decrypted_bloc
    
    for i in range(padding_size):
        decrypted_data = decrypted_data[:-1]

    return decrypted_data