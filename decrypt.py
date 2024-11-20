import base64

def decrypt_data(data: str, key: str) -> bytes:
    
    key: bytes = base64.b64decode(key)

    data: bytes = base64.b64decode(data)

    IV: bytes = data[:16]

    data = data[16:]

    decrypted_data: bytes = b""
    new_iv: bytes = IV

    for i in range(int(len(data) / 16)):
        
        decrypted_bloc: bytes = b""
        tmp: bytes = b""

        for j in range(16):
            tmp += (data[i * 16 + j] ^ key[j]).to_bytes()

        for j in range(16):
            decrypted_bloc += (tmp[j] ^ new_iv[j]).to_bytes()

        decrypted_data += decrypted_bloc
        new_iv = data[i * 16:(i + 1) * 16]

    padding_size: int = int.from_bytes(data[-1:])
    
    decrypted_data = decrypted_data[:0 - 1 - padding_size]

    return decrypted_data