import random
import base64

def generate_key():
    key = base64.b64encode(random.randbytes(16)).decode("latin-1") # 16 * 8 = 128 = key / block size
    return key