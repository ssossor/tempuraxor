import random
import base64

def encrypt_data(data: bytes, key: str) -> str:

    key: bytes = base64.b64decode(key)

    IV: bytes = random.randbytes(16)
    
    padding_size: bytes = ((16 - (len(data) + 1) % 16) % 16).to_bytes()
    data: bytes = data + (chr(0) * ((16 - (len(data) + 1) % 16) % 16)).encode() + padding_size # padding
    
    encrypted_data: bytes = b""
    new_iv: bytes = IV

    for i in range(int(len(data) / 16)):

        encrypted_bloc: bytes = b""
        tmp: bytes = b""

        for j in range(16):
            tmp += (data[i * 16 + j] ^ new_iv[j]).to_bytes()

        for j in range(16):
            encrypted_bloc += (tmp[j] ^ key[j]).to_bytes()
    
        encrypted_data += encrypted_bloc
        new_iv = encrypted_bloc
    
    encrypted_data = IV + encrypted_data + padding_size

    return base64.b64encode(encrypted_data).decode()